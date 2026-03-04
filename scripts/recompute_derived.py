#!/usr/bin/env python3
"""
P-* 모집단 슬롯 DT/NFC/SM 재계산 스크립트 (Python-only)

[이전 방식의 문제]
  - LLM 배치 산출 시 "if uncertain, use 0.00" 잔차 정책 → eps ≈ 0.00 고정
  - OUTPUT SCHEMA 예시가 전부 0.01 → LLM 앵커링
  - DT_base가 high-A × high-C 학술원 모집단에서 구조적으로 음수 → clip → 0.01 98.4%

[이 스크립트의 접근법]
  1. Big5 선형 결합으로 원시 점수(raw) 계산 (방향성·상대 강도는 문헌 기반)
  2. 전체 모집단 내 z-점수 정규화 (모집단 내 상대 위치 보존)
  3. 타깃 분포(mean, formula_sd)로 스케일 (population 특성과 무관하게 분포 보장)
  4. 가우시안 잔차 노이즈 추가 (Big5로 설명 못 하는 개인차)
  5. [0.01, 0.99] 클리핑

[파라미터 근거]
  DT(다크 트라이어드):
    - mean=0.28: 학술원 입학자는 A·C 높아 일반 모집단보다 낮음
      단 귀족 정치·지위 경쟁 환경으로 스토리 변별력 확보
    - sd=0.18: 0.01~0.99 전 구간 분포 (악역/회색지대/선역 명확히 분리)
    - formula_r=0.55: R²≈0.30, 메타분석 추정치; A·C가 강한 억제 인자
    가중치: -0.50*A - 0.35*C + 0.25*N + 0.20*E - 0.05*O

  NFC(인지 욕구):
    - mean=0.54: 학문 선택 편향 → 일반 모집단(0.50) 대비 상향
    - sd=0.16: 성실한 학생 vs 지적 호기심 중심 학생 구분
    - formula_r=0.60: R²≈0.36; O·C가 핵심 예측 인자
    가중치: 0.45*O + 0.30*C - 0.15*N + 0.05*E + 0.05*A

  SM(자기감시):
    - mean=0.40: 귀족 위계·파벌 환경 → 일반 모집단(~0.35)보다 상향
    - sd=0.17: 사교계 카멜레온 ~ 직설형 캐릭터 폭넓게 분포
    - formula_r=0.55: R²≈0.30; E가 핵심, N이 억제 인자
    가중치: 0.40*E + 0.15*O + 0.10*A - 0.10*C - 0.20*N

[재현성]
  SEED=42 고정. 동일 입력 → 동일 출력 보장.
"""

import csv
import re
import statistics
import sys
from pathlib import Path

import numpy as np
import yaml

SEED = 42

# --- 타깃 분포 파라미터 ---
# mean     : 타깃 평균
# sd       : 타깃 전체 표준편차
# formula_r: 공식-타깃 상관(= sqrt(R²)), Big5가 설명하는 분산 비율의 제곱근
TARGETS = {
    "DT": {"mean": 0.28, "sd": 0.18, "formula_r": 0.55},
    "NFC": {"mean": 0.54, "sd": 0.16, "formula_r": 0.60},
    "SM":  {"mean": 0.40, "sd": 0.17, "formula_r": 0.55},
}


# ---------------------------------------------------------------------------
# 로딩
# ---------------------------------------------------------------------------

def load_slot(yaml_path: Path) -> dict | None:
    """YAML에서 id + b5 로드. 실패 시 None."""
    try:
        with yaml_path.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not data or "b5" not in data:
            return None
        b5 = data["b5"]
        return {
            "id": data.get("id", yaml_path.stem),
            "O": float(b5["O"]),
            "C": float(b5["C"]),
            "E": float(b5["E"]),
            "A": float(b5["A"]),
            "N": float(b5["N"]),
        }
    except Exception:
        return None


# ---------------------------------------------------------------------------
# 계산
# ---------------------------------------------------------------------------

def compute_all_derived(slots: list[dict], rng: np.random.Generator) -> list[dict]:
    """
    slots: load_slot() 결과 리스트
    반환: 각 슬롯에 대한 {"DT": float, "NFC": float, "SM": float} 리스트
    """
    n = len(slots)
    O = np.array([s["O"] for s in slots])
    C = np.array([s["C"] for s in slots])
    E = np.array([s["E"] for s in slots])
    A = np.array([s["A"] for s in slots])
    N = np.array([s["N"] for s in slots])

    def derive(raw: np.ndarray, key: str) -> np.ndarray:
        cfg = TARGETS[key]
        total_sd    = cfg["sd"]
        formula_sd  = total_sd * cfg["formula_r"]           # 공식이 기여하는 SD
        noise_sd    = np.sqrt(max(total_sd**2 - formula_sd**2, 0))  # 잔차 SD

        # 1) z-점수 정규화 (모집단 내 상대 위치)
        raw_std = float(np.std(raw))
        z = (raw - np.mean(raw)) / raw_std if raw_std > 1e-9 else np.zeros(n)

        # 2) 타깃 분포로 스케일
        base = z * formula_sd + cfg["mean"]

        # 3) 잔차 노이즈 (Big5로 설명 안 되는 개인차)
        noise = rng.normal(0, noise_sd, n)

        # 4) 클리핑
        return np.clip(base + noise, 0.01, 0.99)

    DT_raw  = -0.50*A - 0.35*C + 0.25*N + 0.20*E - 0.05*O
    NFC_raw =  0.45*O + 0.30*C - 0.15*N + 0.05*E + 0.05*A
    SM_raw  =  0.40*E + 0.15*O + 0.10*A - 0.10*C - 0.20*N

    DT  = derive(DT_raw,  "DT")
    NFC = derive(NFC_raw, "NFC")
    SM  = derive(SM_raw,  "SM")

    return [
        {
            "DT":  round(float(DT[i]),  2),
            "NFC": round(float(NFC[i]), 2),
            "SM":  round(float(SM[i]),  2),
        }
        for i in range(n)
    ]


# ---------------------------------------------------------------------------
# 파일 갱신
# ---------------------------------------------------------------------------

_DERIVED_BLOCK_RE = re.compile(r"(?ms)^derived:\n(?:[ \t].*\n)+")


def update_yaml(path: Path, derived: dict) -> None:
    text = path.read_text(encoding="utf-8")
    block = (
        "derived:\n"
        f"  DT: {derived['DT']:.2f}\n"
        f"  NFC: {derived['NFC']:.2f}\n"
        f"  SM: {derived['SM']:.2f}\n"
    )
    if _DERIVED_BLOCK_RE.search(text):
        text = _DERIVED_BLOCK_RE.sub(block, text, count=1)
    else:
        text = text.rstrip("\n") + "\n" + block
    path.write_text(text, encoding="utf-8")


def update_csv(csv_path: Path, derived_map: dict[str, dict]) -> tuple[int, int]:
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    for col in ("DT", "NFC", "SM"):
        if col not in fieldnames:
            fieldnames.append(col)

    applied = missing = 0
    for row in rows:
        d = derived_map.get(row.get("id", ""))
        if d:
            row["DT"]  = f"{d['DT']:.2f}"
            row["NFC"] = f"{d['NFC']:.2f}"
            row["SM"]  = f"{d['SM']:.2f}"
            applied += 1
        else:
            missing += 1

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return applied, missing


# ---------------------------------------------------------------------------
# 통계 출력
# ---------------------------------------------------------------------------

def print_stats(derived_map: dict[str, dict]) -> None:
    print(f"\n{'지표':5s} {'평균':>7s} {'목표':>7s} {'SD':>7s} {'목표SD':>7s} "
          f"{'min':>5s} {'max':>5s} {'@0.01':>6s} {'@0.99':>6s}")
    print("-" * 60)
    for key in ("DT", "NFC", "SM"):
        vals = [v[key] for v in derived_map.values()]
        t = TARGETS[key]
        print(
            f"{key:5s} "
            f"{statistics.mean(vals):7.3f} "
            f"{t['mean']:7.2f} "
            f"{statistics.pstdev(vals):7.3f} "
            f"{t['sd']:7.2f} "
            f"{min(vals):5.2f} "
            f"{max(vals):5.2f} "
            f"{sum(1 for v in vals if v == 0.01):6d} "
            f"{sum(1 for v in vals if v == 0.99):6d}"
        )


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    pop_dir   = repo_root / "worldbible_refined_bundle_20260303" / "population"
    csv_path  = pop_dir / "population_slots.csv"

    yaml_files = sorted(pop_dir.glob("P-*.yaml"))
    if not yaml_files:
        print("P-*.yaml 파일을 찾을 수 없습니다.", file=sys.stderr)
        return 1

    # --- 로딩 ---
    print(f"슬롯 로딩 중... ({len(yaml_files)}개)")
    slots: list[dict] = []
    failed_load: list[str] = []
    for yf in yaml_files:
        s = load_slot(yf)
        if s is None:
            failed_load.append(yf.stem)
        else:
            slots.append(s)

    if failed_load:
        print(f"  경고: 로드 실패 {len(failed_load)}개 → {failed_load[:5]}")
    print(f"  로드 성공: {len(slots)}개")

    # --- 계산 ---
    print(f"\nDT/NFC/SM 재계산 중... (seed={SEED})")
    rng = np.random.default_rng(SEED)
    derived_list = compute_all_derived(slots, rng)

    derived_map = {s["id"]: d for s, d in zip(slots, derived_list)}

    # --- YAML 갱신 ---
    print("YAML 갱신 중...")
    for pid, derived in derived_map.items():
        update_yaml(pop_dir / f"{pid}.yaml", derived)
    print(f"  완료: {len(derived_map)}개")

    # --- CSV 갱신 ---
    print("CSV 갱신 중...")
    applied, missing = update_csv(csv_path, derived_map)
    print(f"  적용: {applied}개 / 미해당: {missing}개")

    # --- 통계 ---
    print_stats(derived_map)
    print("\n재계산 완료.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
