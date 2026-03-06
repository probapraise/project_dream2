#!/usr/bin/env python3
"""
NS-* 비학생 모집단 슬롯 생성 스크립트

[방식]
  1. 에르미렌 씨족(25명): 별도 빅5 분포로 생성, org_id=ORG-CLN-ELF-001 고정
  2. 일반 비학생(630명): 공통 빅5 분포로 생성
  3. 전체 655명: DT/NFC/SM 파생 지표 계산 (z-score 정규화, P-*와 동일 방식)
  4. 630명: 직군 적합도 greedy 배정 (정원 제약)
  5. YAML 개별 파일 + CSV 출력

[슬롯 스키마]
  id: NS-XXXX
  job_type: 직군 (교수/감찰단/에르미렌씨족 등)
  role: UNASSIGNED (향후 named 단계에서 세부 역할 기입)
  org_id: ORG-CLN-ELF-001 | null
  b5: {O, C, E, A, N}
  derived: {DT, NFC, SM}
  status: uninstantiated
  ch_id: null

[비학생 빅5 타깃 분포]
  학생(P-*)보다 학술 편향 약함, 직업인 혼합으로 C 약간 낮음
  O: mean=0.55 std=0.18
  C: mean=0.57 std=0.17
  E: mean=0.52 std=0.18
  A: mean=0.55 std=0.17
  N: mean=0.47 std=0.18

[에르미렌 씨족 빅5 타깃 분포]
  성목 수호·의례 특성: O↑ C↑ A↑ E↓ N↓
  O: mean=0.70 std=0.10
  C: mean=0.65 std=0.12
  E: mean=0.45 std=0.14
  A: mean=0.68 std=0.11
  N: mean=0.35 std=0.14

[재현성]
  SEED=42 고정.
"""

import csv
import statistics
import sys
from pathlib import Path

import numpy as np

SEED = 42

# ---------------------------------------------------------------------------
# 분포 파라미터
# ---------------------------------------------------------------------------

NS_TRAITS = [
    ("O", 0.55, 0.18),
    ("C", 0.57, 0.17),
    ("E", 0.52, 0.18),
    ("A", 0.55, 0.17),
    ("N", 0.47, 0.18),
]

ERMIREN_TRAITS = [
    ("O", 0.70, 0.10),
    ("C", 0.65, 0.12),
    ("E", 0.45, 0.14),
    ("A", 0.68, 0.11),
    ("N", 0.35, 0.14),
]

DERIVED_TARGETS = {
    "DT":  {"mean": 0.28, "sd": 0.18, "formula_r": 0.55},
    "NFC": {"mean": 0.54, "sd": 0.16, "formula_r": 0.60},
    "SM":  {"mean": 0.40, "sd": 0.17, "formula_r": 0.55},
}

# ---------------------------------------------------------------------------
# 직군 정원 (에르미렌 제외 합계 = 630)
# ---------------------------------------------------------------------------

JOB_QUOTAS = [
    ("교수",        200),
    ("연구원",       50),
    ("행정직",       50),
    ("왕실파견감독관",  15),
    ("감찰단",       70),
    ("서약원파견관",   15),
    ("시설기숙사관리",  80),
    ("의료진",       20),
    ("장내상인",      60),
    ("룬공학장인",    30),
    ("식당서비스",    40),
]

ERMIREN_JOB = "에르미렌씨족"
ERMIREN_ORG = "ORG-CLN-ELF-001"
ERMIREN_COUNT = 25

assert sum(q for _, q in JOB_QUOTAS) == 630, "일반 직군 정원 합계가 630이 아닙니다."


# ---------------------------------------------------------------------------
# 빅5 샘플링
# ---------------------------------------------------------------------------

def clip01(v: float) -> float:
    return max(0.01, min(0.99, v))


def q2(v: float) -> float:
    return round(clip01(v), 2)


def sample_b5(rng: np.random.Generator, traits: list) -> dict:
    return {name: q2(float(rng.normal(mean, std))) for name, mean, std in traits}


# ---------------------------------------------------------------------------
# 파생 지표 계산 (recompute_derived.py 동일 방식)
# ---------------------------------------------------------------------------

def compute_derived(slots: list[dict], rng: np.random.Generator) -> list[dict]:
    n = len(slots)
    O = np.array([s["b5"]["O"] for s in slots])
    C = np.array([s["b5"]["C"] for s in slots])
    E = np.array([s["b5"]["E"] for s in slots])
    A = np.array([s["b5"]["A"] for s in slots])
    N = np.array([s["b5"]["N"] for s in slots])

    def derive(raw: np.ndarray, key: str) -> np.ndarray:
        cfg = DERIVED_TARGETS[key]
        total_sd   = cfg["sd"]
        formula_sd = total_sd * cfg["formula_r"]
        noise_sd   = float(np.sqrt(max(total_sd ** 2 - formula_sd ** 2, 0)))
        raw_std = float(np.std(raw))
        z = (raw - np.mean(raw)) / raw_std if raw_std > 1e-9 else np.zeros(n)
        base = z * formula_sd + cfg["mean"]
        noise = rng.normal(0, noise_sd, n)
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
# 직군 적합도 함수
# ---------------------------------------------------------------------------

def job_score(job: str, b5: dict, d: dict) -> float:
    O, C, E, A, N = b5["O"], b5["C"], b5["E"], b5["A"], b5["N"]
    DT, NFC, SM = d["DT"], d["NFC"], d["SM"]

    if job == "교수":
        return  0.35*NFC + 0.25*O + 0.15*C - 0.10*N + 0.05*E + 0.05*A
    if job == "연구원":
        return  0.40*NFC + 0.30*O + 0.10*C - 0.05*N
    if job == "행정직":
        return  0.35*C + 0.25*A - 0.20*O + 0.10*E - 0.10*DT + 0.05*SM
    if job == "왕실파견감독관":
        return  0.30*SM + 0.30*C - 0.20*A + 0.10*DT + 0.05*E
    if job == "감찰단":
        return  0.35*C + 0.25*SM - 0.25*A + 0.10*N + 0.05*DT
    if job == "서약원파견관":
        return  0.35*A + 0.30*C - 0.25*DT + 0.10*SM
    if job == "시설기숙사관리":
        return  0.40*C - 0.20*NFC - 0.15*O + 0.15*A
    if job == "의료진":
        return  0.40*A + 0.25*C - 0.20*DT + 0.10*NFC + 0.05*N
    if job == "장내상인":
        return  0.35*E + 0.30*SM + 0.15*A + 0.10*DT - 0.05*C
    if job == "룬공학장인":
        return  0.30*O + 0.30*NFC + 0.25*C - 0.10*E
    if job == "식당서비스":
        return  0.35*E + 0.30*A + 0.20*SM - 0.10*DT
    return 0.0


# ---------------------------------------------------------------------------
# 직군 배정 (greedy)
# ---------------------------------------------------------------------------

def assign_jobs(regular_slots: list[dict]) -> None:
    """regular_slots에 job_type을 in-place로 배정. 점수 내림차순 greedy."""
    jobs = [j for j, _ in JOB_QUOTAS]
    remaining = dict(JOB_QUOTAS)

    # (score, slot_idx, job) 전체 조합 생성 후 점수 내림차순 정렬
    candidates = []
    for i, s in enumerate(regular_slots):
        for job in jobs:
            score = job_score(job, s["b5"], s["derived"])
            candidates.append((score, i, job))
    candidates.sort(key=lambda x: -x[0])

    assigned = [False] * len(regular_slots)
    for score, idx, job in candidates:
        if assigned[idx]:
            continue
        if remaining.get(job, 0) > 0:
            regular_slots[idx]["job_type"] = job
            assigned[idx] = True
            remaining[job] -= 1

    # 안전망: 정원 합계 불일치 시 미배정 표시
    for i, s in enumerate(regular_slots):
        if not assigned[i]:
            s["job_type"] = "미배정"
            print(f"  경고: {s['id']} 미배정", file=sys.stderr)


# ---------------------------------------------------------------------------
# 출력
# ---------------------------------------------------------------------------

def write_yaml_slots(slots: list[dict], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for s in slots:
        b5 = s["b5"]
        d  = s["derived"]
        content = "\n".join([
            f"id: {s['id']}",
            f"job_type: {s['job_type']}",
            "role: UNASSIGNED",
            f"org_id: {s.get('org_id') or 'null'}",
            "b5:",
            f"  O: {b5['O']:.2f}",
            f"  C: {b5['C']:.2f}",
            f"  E: {b5['E']:.2f}",
            f"  A: {b5['A']:.2f}",
            f"  N: {b5['N']:.2f}",
            "derived:",
            f"  DT: {d['DT']:.2f}",
            f"  NFC: {d['NFC']:.2f}",
            f"  SM: {d['SM']:.2f}",
            "status: uninstantiated",
            "ch_id: null",
            "",
        ])
        (out_dir / f"{s['id']}.yaml").write_text(content, encoding="utf-8")


def write_csv(slots: list[dict], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id", "job_type", "role", "org_id",
        "O", "C", "E", "A", "N",
        "DT", "NFC", "SM",
        "status", "ch_id",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in slots:
            b5 = s["b5"]
            d  = s["derived"]
            writer.writerow({
                "id":       s["id"],
                "job_type": s["job_type"],
                "role":     "UNASSIGNED",
                "org_id":   s.get("org_id") or "",
                "O":  f"{b5['O']:.2f}",
                "C":  f"{b5['C']:.2f}",
                "E":  f"{b5['E']:.2f}",
                "A":  f"{b5['A']:.2f}",
                "N":  f"{b5['N']:.2f}",
                "DT":  f"{d['DT']:.2f}",
                "NFC": f"{d['NFC']:.2f}",
                "SM":  f"{d['SM']:.2f}",
                "status": "uninstantiated",
                "ch_id":  "",
            })


def print_stats(slots: list[dict]) -> None:
    from collections import Counter
    job_counts = Counter(s["job_type"] for s in slots)

    print("\n[직군 배정 결과]")
    for job, quota in JOB_QUOTAS:
        actual = job_counts[job]
        flag = "" if actual == quota else " !"
        print(f"  {job:12s}: {actual:3d} / {quota}{flag}")
    print(f"  {'에르미렌씨족':12s}: {job_counts[ERMIREN_JOB]:3d} / {ERMIREN_COUNT}")
    total = sum(job_counts.values())
    print(f"  {'합계':12s}: {total:3d} / 655")

    print(f"\n[파생 지표 통계]")
    print(f"{'지표':5s} {'평균':>7s} {'목표':>7s} {'SD':>7s} {'목표SD':>7s} {'min':>5s} {'max':>5s}")
    print("-" * 50)
    for key in ("DT", "NFC", "SM"):
        vals = [s["derived"][key] for s in slots]
        t = DERIVED_TARGETS[key]
        print(
            f"{key:5s} {statistics.mean(vals):7.3f} {t['mean']:7.2f} "
            f"{statistics.pstdev(vals):7.3f} {t['sd']:7.2f} "
            f"{min(vals):5.2f} {max(vals):5.2f}"
        )


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    out_dir   = repo_root / "world/live" / "nonstudent"
    csv_path  = out_dir / "nonstudent_slots.csv"

    if out_dir.exists() and any(out_dir.glob("NS-*.yaml")):
        print(f"경고: {out_dir} 에 이미 NS-*.yaml 파일이 있습니다.", file=sys.stderr)
        print("재생성하려면 기존 파일을 삭제 후 실행하세요.", file=sys.stderr)
        return 1

    rng = np.random.default_rng(SEED)
    slots: list[dict] = []

    # 1. 에르미렌 씨족 25명 (NS-0001 ~ NS-0025)
    print(f"에르미렌 씨족 생성 중... ({ERMIREN_COUNT}명)")
    for i in range(1, ERMIREN_COUNT + 1):
        slots.append({
            "id":       f"NS-{i:04d}",
            "job_type": ERMIREN_JOB,
            "org_id":   ERMIREN_ORG,
            "b5":       sample_b5(rng, ERMIREN_TRAITS),
        })

    # 2. 일반 비학생 630명 (NS-0026 ~ NS-0655)
    print("일반 비학생 생성 중... (630명)")
    for i in range(ERMIREN_COUNT + 1, 656):
        slots.append({
            "id":       f"NS-{i:04d}",
            "job_type": None,
            "org_id":   None,
            "b5":       sample_b5(rng, NS_TRAITS),
        })

    # 3. 파생 지표 계산 (전체 655명 동시)
    print("파생 지표 계산 중... (seed=42)")
    derived_list = compute_derived(slots, rng)
    for s, d in zip(slots, derived_list):
        s["derived"] = d

    # 4. 일반 비학생 직군 배정
    print("직군 배정 중...")
    regular = [s for s in slots if s["job_type"] is None]
    assign_jobs(regular)

    # 5. 출력
    print(f"YAML 출력 중... → {out_dir}")
    write_yaml_slots(slots, out_dir)
    print(f"CSV 출력 중... → {csv_path}")
    write_csv(slots, csv_path)

    print_stats(slots)
    print("\n완료.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
