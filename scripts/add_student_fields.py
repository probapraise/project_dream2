#!/usr/bin/env python3
"""
P-* 학생 슬롯 추가 필드 배정 스크립트

[추가 필드]
  grade       : 학년 (1학년/2학년/3학년/4학년/연구과정)
  mana_color  : 마나 주색 (청/황/적/녹/백/보라/흑)
  tower       : 탑 소속 (청탑/황탑/적탑/녹탑/백탑/보라탑/흑탑)  ← mana_color와 동일 생성
  major       : 주전공 학파 (탑별 극단 배분, 각인학파=1명)
  vocation    : 직능 (마법사/기사/사제)
  noble_house : signature_noble 160명만 ORG-ARC-HOU-001~024
  race        : nonhuman 250명만 종족명
  origin      : foreigner 120명만 UNASSIGNED

[배분]
  grade:   1학년 900 / 2학년 900 / 3학년 850 / 4학년 800 / 연구과정 150
  tower:   청900 / 황650 / 적600 / 녹515 / 백450 / 보라428 / 흑57
  major:   탑별 학파 극단 배분 (아래 TOWER_MAJORS 참조)
  vocation: 마법사2220 / 기사1020 / 사제360

[재현성]
  SEED=42 고정.
"""

import csv
import sys
from pathlib import Path

import numpy as np
import yaml

SEED = 42

# ---------------------------------------------------------------------------
# 배분 정의
# ---------------------------------------------------------------------------

GRADE_QUOTAS = [
    ("1학년",   900),
    ("2학년",   900),
    ("3학년",   850),
    ("4학년",   800),
    ("연구과정", 150),
]

TOWER_QUOTAS = [
    ("청탑",   900),
    ("황탑",   650),
    ("적탑",   600),
    ("녹탑",   515),
    ("백탑",   450),
    ("보라탑", 428),
    ("흑탑",    57),
]

MANA_COLOR_MAP = {
    "청탑":  "청",
    "황탑":  "황",
    "적탑":  "적",
    "녹탑":  "녹",
    "백탑":  "백",
    "보라탑": "보라",
    "흑탑":  "흑",
}

TOWER_MAJORS = {
    "청탑":  [("방벽수호학파", 520), ("결속조형학파", 200), ("구속연쇄학파", 150), ("공간쇄정학파", 30)],
    "황탑":  [("관성조율학파", 350), ("전자유도학파", 160), ("공성진동학파", 120), ("전장연산학파", 20)],
    "적탑":  [("화염포격학파", 380), ("폭연연성학파", 155), ("연기전술학파",  55), ("적열단조학파",  10)],
    "녹탑":  [("약리전술학파", 330), ("정령계약학파", 150), ("균사전장학파",   35)],
    "백탑":  [("순백응급학파", 360), ("광휘정화학파",  75), ("역서명파쇄학파", 15)],
    "보라탑": [("전심학파",   300), ("심상환영학파",  95), ("몽유침잠학파",   32), ("각인학파",  1)],
    "흑탑":  [("침식주술학파",  40), ("흑영잠행학파",  17)],
}

VOCATION_QUOTAS = [
    ("마법사", 2220),
    ("기사",   1020),
    ("사제",    360),
]

# 16가문 × 7명 + 8가문 × 6명 = 160
NOBLE_HOUSES = [f"ORG-ARC-HOU-{i:03d}" for i in range(1, 25)]
NOBLE_HOUSE_QUOTAS = [(h, 7) for h in NOBLE_HOUSES[:16]] + [(h, 6) for h in NOBLE_HOUSES[16:]]

RACES = [
    ("고블린",    90),
    ("하플링",    45),
    ("비스트킨",  35),
    ("드워프",    25),
    ("엘프",      20),
    ("아쿠아틱",  15),
    ("오크",      10),
    ("리자드포크", 10),
]

# ---------------------------------------------------------------------------
# 검증
# ---------------------------------------------------------------------------

assert sum(q for _, q in GRADE_QUOTAS) == 3600, "grade 합계 != 3600"
assert sum(q for _, q in TOWER_QUOTAS) == 3600, "tower 합계 != 3600"
assert sum(q for _, q in VOCATION_QUOTAS) == 3600, "vocation 합계 != 3600"
assert sum(q for _, q in NOBLE_HOUSE_QUOTAS) == 160, "noble_house 합계 != 160"
assert sum(q for _, q in RACES) == 250, "race 합계 != 250"
for tower, majors in TOWER_MAJORS.items():
    tower_q = dict(TOWER_QUOTAS)[tower]
    assert sum(q for _, q in majors) == tower_q, f"{tower} major 합계 != {tower_q}"


# ---------------------------------------------------------------------------
# 유틸
# ---------------------------------------------------------------------------

def expand_quotas(quotas: list) -> list:
    """[(label, count), ...] → label을 count번 반복한 리스트."""
    result = []
    for label, count in quotas:
        result.extend([label] * count)
    return result


# ---------------------------------------------------------------------------
# YAML 읽기 / 쓰기
# ---------------------------------------------------------------------------

def load_yaml(path: Path) -> dict | None:
    try:
        with path.open(encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"  로드 실패: {path.name} — {e}", file=sys.stderr)
        return None


def write_yaml(path: Path, s: dict) -> None:
    """P-* YAML 슬롯 재작성 (필드 순서 고정, status/ch_id는 CSV 전용)."""
    b5 = s["b5"]
    d  = s["derived"]

    lines = [
        f"id: {s['id']}",
        f"background_type: {s['background_type']}",
        f"dorm: {s['dorm']}",
        f"grade: {s['grade']}",
        f"mana_color: {s['mana_color']}",
        f"tower: {s['tower']}",
        f"major: {s['major']}",
        f"vocation: {s['vocation']}",
    ]

    if "noble_house" in s:
        lines.append(f"noble_house: {s['noble_house']}")
    if "race" in s:
        lines.append(f"race: {s['race']}")
    if "origin" in s:
        lines.append(f"origin: {s['origin']}")

    lines += [
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
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# CSV 갱신
# ---------------------------------------------------------------------------

def update_csv(slots: list[dict], csv_path: Path) -> None:
    """기존 CSV에 새 컬럼 추가."""
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        old_fields = list(reader.fieldnames or [])

    # id → slot 매핑
    slot_map = {s["id"]: s for s in slots}

    new_cols = ["grade", "mana_color", "tower", "major", "vocation",
                "noble_house", "race", "origin"]
    for col in new_cols:
        if col not in old_fields:
            old_fields.append(col)

    for row in rows:
        s = slot_map.get(row.get("id", ""))
        if not s:
            continue
        row["grade"]      = s.get("grade", "")
        row["mana_color"] = s.get("mana_color", "")
        row["tower"]      = s.get("tower", "")
        row["major"]      = s.get("major", "")
        row["vocation"]   = s.get("vocation", "")
        row["noble_house"] = s.get("noble_house", "")
        row["race"]       = s.get("race", "")
        row["origin"]     = s.get("origin", "")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=old_fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"  CSV 갱신 완료: {csv_path.name}")


# ---------------------------------------------------------------------------
# 통계 출력
# ---------------------------------------------------------------------------

def print_stats(slots: list[dict]) -> None:
    from collections import Counter

    def show(title, counter, quotas):
        print(f"\n[{title}]")
        for label, quota in quotas:
            actual = counter[label]
            flag = "" if actual == quota else " !"
            print(f"  {label:14s}: {actual:4d} / {quota}{flag}")

    print("\n" + "=" * 50)
    show("학년 배정",   Counter(s["grade"]    for s in slots), GRADE_QUOTAS)
    show("탑 배정",     Counter(s["tower"]    for s in slots), TOWER_QUOTAS)
    show("직능 배정",   Counter(s["vocation"] for s in slots), VOCATION_QUOTAS)

    print("\n[학파 배정]")
    major_counter = Counter(s["major"] for s in slots)
    for tower, majors in TOWER_MAJORS.items():
        print(f"  {tower}:")
        for label, quota in majors:
            actual = major_counter[label]
            flag = "" if actual == quota else " !"
            print(f"    {label:16s}: {actual:4d} / {quota}{flag}")

    sig = [s for s in slots if s.get("background_type") == "signature_noble"]
    if sig:
        nh_counter = Counter(s.get("noble_house", "") for s in sig)
        print(f"\n[서명귀족 noble_house] (총 {len(sig)}명)")
        counts = sorted(nh_counter.items())
        for h, c in counts:
            print(f"  {h}: {c}")

    nh = [s for s in slots if s.get("background_type") == "nonhuman"]
    if nh:
        race_counter = Counter(s.get("race", "") for s in nh)
        print(f"\n[비인간 race] (총 {len(nh)}명)")
        for label, quota in RACES:
            actual = race_counter[label]
            flag = "" if actual == quota else " !"
            print(f"  {label:10s}: {actual:3d} / {quota}{flag}")

    # 각인학파 슬롯 확인
    kak = [s for s in slots if s.get("major") == "각인학파"]
    if kak:
        print(f"\n[각인학파 슬롯] → {kak[0]['id']} (background_type={kak[0]['background_type']})")


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    pop_dir   = repo_root / "worldbible_refined_bundle_20260303" / "population"
    csv_path  = pop_dir / "population_slots.csv"

    yaml_files = sorted(pop_dir.glob("P-*.yaml"))
    if not yaml_files:
        print("P-*.yaml 파일 없음.", file=sys.stderr)
        return 1

    # --- 이미 grade 필드가 있으면 경고 후 덮어씀 ---
    sample = load_yaml(yaml_files[0])
    if sample and "grade" in sample:
        print("경고: grade 필드가 이미 존재합니다. 덮어씁니다.")

    print(f"슬롯 로딩 중... ({len(yaml_files)}개)")
    slots: list[dict] = []
    for yf in yaml_files:
        s = load_yaml(yf)
        if s is not None:
            s["_path"] = yf
            slots.append(s)
    print(f"  로드 성공: {len(slots)}개")

    if len(slots) != 3600:
        print(f"경고: 슬롯 수 {len(slots)} (예상 3600)", file=sys.stderr)

    rng = np.random.default_rng(SEED)

    # 전체 인덱스 (각 필드 배정 직전에 독립 셔플)
    idx = list(range(len(slots)))

    # --- grade 배정 (셔플 1) ---
    rng.shuffle(idx)
    grade_seq = expand_quotas(GRADE_QUOTAS)
    for rank, slot_i in enumerate(idx):
        slots[slot_i]["grade"] = grade_seq[rank]

    # --- tower / mana_color 배정 (셔플 2 — grade와 독립) ---
    rng.shuffle(idx)
    tower_seq = expand_quotas(TOWER_QUOTAS)
    tower_by_slot: dict[int, str] = {}
    for rank, slot_i in enumerate(idx):
        tower = tower_seq[rank]
        slots[slot_i]["tower"]      = tower
        slots[slot_i]["mana_color"] = MANA_COLOR_MAP[tower]
        tower_by_slot[slot_i] = tower

    # --- major 배정 (tower별, tower 셔플 순서 내 상대 위치 활용) ---
    tower_indices: dict[str, list[int]] = {t: [] for t, _ in TOWER_QUOTAS}
    for rank, slot_i in enumerate(idx):
        tower_indices[tower_by_slot[slot_i]].append(slot_i)

    for tower, t_idx_list in tower_indices.items():
        major_seq = expand_quotas(TOWER_MAJORS[tower])
        for i, slot_i in enumerate(t_idx_list):
            slots[slot_i]["major"] = major_seq[i]

    # --- vocation 배정 (셔플 3 — tower/grade와 독립) ---
    rng.shuffle(idx)
    voc_seq = expand_quotas(VOCATION_QUOTAS)
    for rank, slot_i in enumerate(idx):
        slots[slot_i]["vocation"] = voc_seq[rank]

    # --- noble_house 배정 (signature_noble만) ---
    sig_indices = [i for i, s in enumerate(slots)
                   if s.get("background_type") == "signature_noble"]
    if len(sig_indices) != 160:
        print(f"  경고: signature_noble {len(sig_indices)}개 (예상 160)", file=sys.stderr)
    sig_arr = np.array(sig_indices, dtype=int)
    rng.shuffle(sig_arr)
    nh_seq = expand_quotas(NOBLE_HOUSE_QUOTAS)
    for i, slot_i in enumerate(sig_arr):
        slots[slot_i]["noble_house"] = nh_seq[i]

    # --- race 배정 (nonhuman만) ---
    nh_indices = [i for i, s in enumerate(slots)
                  if s.get("background_type") == "nonhuman"]
    if len(nh_indices) != 250:
        print(f"  경고: nonhuman {len(nh_indices)}개 (예상 250)", file=sys.stderr)
    nh_arr = np.array(nh_indices, dtype=int)
    rng.shuffle(nh_arr)
    race_seq = expand_quotas(RACES)
    for i, slot_i in enumerate(nh_arr):
        slots[slot_i]["race"] = race_seq[i]

    # --- origin 배정 (foreigner만) ---
    for s in slots:
        if s.get("background_type") == "foreigner":
            s["origin"] = "UNASSIGNED"

    # --- YAML 재작성 ---
    print("YAML 재작성 중...")
    for s in slots:
        write_yaml(s["_path"], s)
    print(f"  완료: {len(slots)}개")

    # --- CSV 갱신 ---
    print("CSV 갱신 중...")
    update_csv(slots, csv_path)

    # --- 통계 ---
    print_stats(slots)
    print("\n완료.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
