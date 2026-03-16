#!/usr/bin/env python3
"""
P-* 학생 슬롯 current-term snapshot 필드 배정 스크립트

이 스크립트는 세계관 정본 자체를 생성하지 않는다.
`world/live/population/profiles/current_term_snapshot_v1.yaml`에 적힌
현재 학기 스냅샷 분포를 기준으로 `population/P-*.yaml`과
`population/population_slots.csv`를 재현한다.
current canon frontier가 pre-academy여도 academy snapshot layer는 유지하며,
현재 서사 시점은 `world/live/docs/narrative_state.md`와
`world/live/population/core_cast/*.md`를 먼저 읽어야 한다.
"""

import argparse
import csv
import sys
from pathlib import Path

import numpy as np
import yaml

DEFAULT_SEED = 42


def default_crest_vision_holder(background_type: str) -> bool:
    return background_type == "signature_noble"


def normalize_crest_vision_holder(value: object, background_type: str) -> bool:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
    return default_crest_vision_holder(background_type)

# ---------------------------------------------------------------------------
# 프로필 로드 / 검증
# ---------------------------------------------------------------------------


def normalize_quotas(raw: list) -> list[tuple[str, int]]:
    return [(str(label), int(count)) for label, count in raw]


def load_snapshot_profile(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    required = [
        "seed",
        "expected_slot_count",
        "grade_quotas",
        "tower_quotas",
        "mana_color_map",
        "tower_majors",
        "vocation_quotas",
        "knight_majors",
        "priest_majors",
        "knight_weights_by_tower",
        "priest_weights_by_tower",
        "noble_house_quotas",
        "race_quotas",
    ]
    missing = [key for key in required if key not in data]
    if missing:
        raise ValueError(f"snapshot profile missing keys: {', '.join(missing)}")

    profile = {
        "seed": int(data.get("seed", DEFAULT_SEED)),
        "expected_slot_count": int(data["expected_slot_count"]),
        "grade_quotas": normalize_quotas(data["grade_quotas"]),
        "tower_quotas": normalize_quotas(data["tower_quotas"]),
        "mana_color_map": {str(k): str(v) for k, v in dict(data["mana_color_map"]).items()},
        "tower_majors": {
            str(tower): normalize_quotas(majors)
            for tower, majors in dict(data["tower_majors"]).items()
        },
        "vocation_quotas": normalize_quotas(data["vocation_quotas"]),
        "knight_majors": [str(item) for item in data["knight_majors"]],
        "priest_majors": [str(item) for item in data["priest_majors"]],
        "knight_weights_by_tower": {
            str(tower): [float(value) for value in weights]
            for tower, weights in dict(data["knight_weights_by_tower"]).items()
        },
        "priest_weights_by_tower": {
            str(tower): [float(value) for value in weights]
            for tower, weights in dict(data["priest_weights_by_tower"]).items()
        },
        "noble_house_quotas": normalize_quotas(data["noble_house_quotas"]),
        "race_quotas": normalize_quotas(data["race_quotas"]),
    }
    profile["color_to_tower"] = {v: k for k, v in profile["mana_color_map"].items()}
    validate_snapshot_profile(profile)
    return profile


def validate_snapshot_profile(profile: dict) -> None:
    expected = profile["expected_slot_count"]
    if sum(q for _, q in profile["grade_quotas"]) != expected:
        raise ValueError("grade 합계가 expected_slot_count와 다릅니다.")
    if sum(q for _, q in profile["tower_quotas"]) != expected:
        raise ValueError("tower 합계가 expected_slot_count와 다릅니다.")
    if sum(q for _, q in profile["vocation_quotas"]) != expected:
        raise ValueError("vocation 합계가 expected_slot_count와 다릅니다.")
    if sum(q for _, q in profile["noble_house_quotas"]) != 160:
        raise ValueError("noble_house 합계 != 160")
    if sum(q for _, q in profile["race_quotas"]) != 250:
        raise ValueError("race 합계 != 250")

    tower_quota_map = dict(profile["tower_quotas"])
    for tower, majors in profile["tower_majors"].items():
        tower_q = tower_quota_map.get(tower)
        if tower_q is None:
            raise ValueError(f"tower_majors에 tower_quotas에 없는 탑이 있습니다: {tower}")
        if sum(q for _, q in majors) != tower_q:
            raise ValueError(f"{tower} major 합계 != {tower_q}")

    for tower, weights in profile["knight_weights_by_tower"].items():
        if len(weights) != len(profile["knight_majors"]):
            raise ValueError(f"{tower} knight weight 길이 불일치")
        if abs(sum(weights) - 1.0) >= 1e-9:
            raise ValueError(f"{tower} knight weight 합계 != 1.0")

    for tower, weights in profile["priest_weights_by_tower"].items():
        if len(weights) != len(profile["priest_majors"]):
            raise ValueError(f"{tower} priest weight 길이 불일치")
        if abs(sum(weights) - 1.0) >= 1e-9:
            raise ValueError(f"{tower} priest weight 합계 != 1.0")


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
        "# academy current-term snapshot slot",
        "# current narrative frontier는 별도이며, `world/live/docs/narrative_state.md`를 먼저 본다.",
        f"id: {s['id']}",
        f"background_type: {s['background_type']}",
        f"crest_vision_holder: {'true' if bool(s['crest_vision_holder']) else 'false'}",
        f"dorm: {s['dorm']}",
        f"grade: {s['grade']}",
        f"mana_color: {s['mana_color']}",
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

    new_cols = ["crest_vision_holder", "grade", "mana_color", "major", "vocation",
                "noble_house", "race", "origin"]
    for col in new_cols:
        if col not in old_fields:
            old_fields.append(col)
    if "tower" in old_fields:
        old_fields.remove("tower")

    for row in rows:
        s = slot_map.get(row.get("id", ""))
        if not s:
            continue
        row["crest_vision_holder"] = "true" if bool(s.get("crest_vision_holder", False)) else "false"
        row["grade"]      = s.get("grade", "")
        row["mana_color"] = s.get("mana_color", "")
        row["major"]      = s.get("major", "")
        row["vocation"]   = s.get("vocation", "")
        row["noble_house"] = s.get("noble_house", "")
        row["race"]       = s.get("race", "")
        row["origin"]     = s.get("origin", "")
        row.pop("tower", None)

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=old_fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"  CSV 갱신 완료: {csv_path.name}")


# ---------------------------------------------------------------------------
# 통계 출력
# ---------------------------------------------------------------------------

def print_stats(slots: list[dict], profile: dict) -> None:
    from collections import Counter

    def show(title, counter, quotas):
        print(f"\n[{title}]")
        for label, quota in quotas:
            actual = counter[label]
            flag = "" if actual == quota else " !"
            print(f"  {label:14s}: {actual:4d} / {quota}{flag}")

    print("\n" + "=" * 50)
    show("학년 배정", Counter(s["grade"] for s in slots), profile["grade_quotas"])
    tower_counter = Counter(profile["color_to_tower"].get(s["mana_color"], "UNASSIGNED") for s in slots)
    show("탑 배정(내부)", tower_counter, profile["tower_quotas"])
    show("직능 배정", Counter(s["vocation"] for s in slots), profile["vocation_quotas"])

    print("\n[마법사 학파 배정]")
    print("  note: actual_mage는 직능 재배정 후 남은 마법사 수, profile_baseline은 snapshot profile의 탑별 초기 배치 기준이다.")
    for tower, majors in profile["tower_majors"].items():
        mage_total_in_tower = sum(
            1
            for s in slots
            if profile["color_to_tower"].get(s["mana_color"]) == tower
            and s["vocation"] == "마법사"
        )
        tower_total = dict(profile["tower_quotas"])[tower]
        print(f"  {tower}: mage_total={mage_total_in_tower} / tower_total={tower_total}")
        for label, quota in majors:
            actual = sum(
                1
                for s in slots
                if profile["color_to_tower"].get(s["mana_color"]) == tower
                and s["vocation"] == "마법사"
                and s["major"] == label
            )
            print(f"    {label:16s}: actual_mage={actual:4d} / profile_baseline={quota}")

    print("\n[기사 과정 배정]")
    knight_counter = Counter(s["major"] for s in slots if s["vocation"] == "기사")
    for label in profile["knight_majors"]:
        print(f"  {label:16s}: {knight_counter[label]:4d}")

    print("\n[사제 신전과 배정]")
    priest_counter = Counter(s["major"] for s in slots if s["vocation"] == "사제")
    for label in profile["priest_majors"]:
        print(f"  {label:16s}: {priest_counter[label]:4d}")

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
        for label, quota in profile["race_quotas"]:
            actual = race_counter[label]
            flag = "" if actual == quota else " !"
            print(f"  {label:10s}: {actual:3d} / {quota}{flag}")

    # 보존각인학파 슬롯 확인
    kak = [s for s in slots if s.get("major") == "보존각인학파"]
    if kak:
        print(f"\n[보존각인학파 슬롯] → {kak[0]['id']} (background_type={kak[0]['background_type']})")


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    default_profile = repo_root / "world/live/population/profiles/current_term_snapshot_v1.yaml"

    parser = argparse.ArgumentParser(
        description="현재 학기 population snapshot profile 기준으로 P-* 슬롯 필드를 재생성한다."
    )
    parser.add_argument(
        "--profile",
        type=Path,
        default=default_profile,
        help="snapshot profile YAML 경로",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="프로필 기본 seed를 덮어쓸 때 사용",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="YAML/CSV를 쓰지 않고 profile 검증과 배정 통계만 출력",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    pop_dir = repo_root / "world/live" / "population"
    csv_path = pop_dir / "population_slots.csv"

    profile = load_snapshot_profile(args.profile)
    seed = profile["seed"] if args.seed is None else args.seed

    print(f"snapshot profile: {args.profile.relative_to(repo_root)}")
    print(f"seed: {seed}")

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
            bg = str(s.get("background_type", ""))
            s["crest_vision_holder"] = normalize_crest_vision_holder(
                s.get("crest_vision_holder"),
                bg,
            )
            s["_path"] = yf
            slots.append(s)
    print(f"  로드 성공: {len(slots)}개")

    expected_slot_count = profile["expected_slot_count"]
    if len(slots) != expected_slot_count:
        print(f"경고: 슬롯 수 {len(slots)} (예상 {expected_slot_count})", file=sys.stderr)

    rng = np.random.default_rng(seed)

    # 전체 인덱스 (각 필드 배정 직전에 독립 셔플)
    idx = list(range(len(slots)))

    # --- grade 배정 (셔플 1) ---
    rng.shuffle(idx)
    grade_seq = expand_quotas(profile["grade_quotas"])
    for rank, slot_i in enumerate(idx):
        slots[slot_i]["grade"] = grade_seq[rank]

    # --- mana_color 배정 (셔플 2 — grade와 독립) ---
    rng.shuffle(idx)
    tower_seq = expand_quotas(profile["tower_quotas"])
    tower_by_slot: dict[int, str] = {}
    for rank, slot_i in enumerate(idx):
        tower = tower_seq[rank]
        slots[slot_i]["mana_color"] = profile["mana_color_map"][tower]
        tower_by_slot[slot_i] = tower

    # --- major 임시 배정 (tower별 전체 슬롯 기준) ---
    # 이후 vocation 배정 후 기사/사제는 직능 전용 major로 재배정한다.
    tower_indices: dict[str, list[int]] = {t: [] for t, _ in profile["tower_quotas"]}
    for rank, slot_i in enumerate(idx):
        tower_indices[tower_by_slot[slot_i]].append(slot_i)
    for tower, t_idx_list in tower_indices.items():
        major_seq = expand_quotas(profile["tower_majors"][tower])
        for i, slot_i in enumerate(t_idx_list):
            slots[slot_i]["major"] = major_seq[i]

    # --- vocation 배정 (셔플 3 — mana_color/grade와 독립) ---
    rng.shuffle(idx)
    voc_seq = expand_quotas(profile["vocation_quotas"])
    for rank, slot_i in enumerate(idx):
        slots[slot_i]["vocation"] = voc_seq[rank]

    # --- 기사/사제 major 재배정 (직능 전용 과정) ---
    for s in slots:
        tower = profile["color_to_tower"].get(s["mana_color"], "")
        if s["vocation"] == "기사":
            weights = np.array(profile["knight_weights_by_tower"][tower], dtype=float)
            choice_idx = int(rng.choice(len(profile["knight_majors"]), p=weights))
            s["major"] = profile["knight_majors"][choice_idx]
        elif s["vocation"] == "사제":
            weights = np.array(profile["priest_weights_by_tower"][tower], dtype=float)
            choice_idx = int(rng.choice(len(profile["priest_majors"]), p=weights))
            s["major"] = profile["priest_majors"][choice_idx]

    # --- noble_house 배정 (signature_noble만) ---
    sig_indices = [i for i, s in enumerate(slots)
                   if s.get("background_type") == "signature_noble"]
    if len(sig_indices) != 160:
        print(f"  경고: signature_noble {len(sig_indices)}개 (예상 160)", file=sys.stderr)
    sig_arr = np.array(sig_indices, dtype=int)
    rng.shuffle(sig_arr)
    nh_seq = expand_quotas(profile["noble_house_quotas"])
    for i, slot_i in enumerate(sig_arr):
        slots[slot_i]["noble_house"] = nh_seq[i]

    # --- race 배정 (nonhuman만) ---
    nh_indices = [i for i, s in enumerate(slots)
                  if s.get("background_type") == "nonhuman"]
    if len(nh_indices) != 250:
        print(f"  경고: nonhuman {len(nh_indices)}개 (예상 250)", file=sys.stderr)
    nh_arr = np.array(nh_indices, dtype=int)
    rng.shuffle(nh_arr)
    race_seq = expand_quotas(profile["race_quotas"])
    for i, slot_i in enumerate(nh_arr):
        slots[slot_i]["race"] = race_seq[i]

    # --- origin 배정 (foreigner만) ---
    for s in slots:
        if s.get("background_type") == "foreigner":
            s["origin"] = "UNASSIGNED"

    # --- 통계 ---
    print_stats(slots, profile)

    if args.dry_run:
        print("\ndry-run: YAML/CSV 쓰기를 생략했습니다.")
        return 0

    # --- YAML 재작성 ---
    print("YAML 재작성 중...")
    for s in slots:
        write_yaml(s["_path"], s)
    print(f"  완료: {len(slots)}개")

    # --- CSV 갱신 ---
    print("CSV 갱신 중...")
    update_csv(slots, csv_path)

    print("\n완료.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
