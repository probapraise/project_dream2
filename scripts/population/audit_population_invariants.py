#!/usr/bin/env python3
"""Audit population distribution and conditional-field invariants.

Checks:
- total slots (3600)
- quota distributions (background_type / grade / mana_color / vocation)
- dorm rule invariants (crest_vision_holder priority + vocation-based dorm)
- major validity by vocation
- conditional fields (noble_house / race / origin)
- foreigner origin quota distribution
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

import yaml


EXPECTED_TOTAL = 3600

EXPECTED_BACKGROUND = {
    "signature_noble": 160,
    "common_noble": 2870,
    "commoner": 200,
    "foreigner": 120,
    "nonhuman": 250,
}

EXPECTED_GRADE = {
    "1학년": 900,
    "2학년": 900,
    "3학년": 850,
    "4학년": 800,
    "연구과정": 150,
}

EXPECTED_MANA_COLOR = {
    "청": 900,
    "황": 650,
    "적": 600,
    "녹": 515,
    "백": 450,
    "자": 428,
    "흑": 57,
}

EXPECTED_VOCATION = {
    "마법사": 2220,
    "기사": 1020,
    "사제": 360,
}

EXPECTED_FOREIGNER_ORIGIN = {
    "ARC-인접왕국권": 50,
    "SAH-울카자르권": 18,
    "NOR-스카르벨권": 18,
    "ARC-원거리소국권": 17,
    "출신불명": 17,
}

ALLOWED_RACES = {
    "고블린",
    "하플링",
    "비스트킨",
    "드워프",
    "엘프",
    "아쿠아틱",
    "오크",
    "리자드포크",
}

MAGE_MAJORS = {
    "경면수호학파",
    "빙쇄구속학파",
    "수류유도학파",
    "탄도관성학파",
    "자계유도학파",
    "군진선도학파",
    "홍련포화학파",
    "용철무구학파",
    "화연장막학파",
    "응급약리학파",
    "생태계약학파",
    "균사환경학파",
    "생명고정학파",
    "정화광휘학파",
    "서약집행학파",
    "교신전심학파",
    "허상연출학파",
    "보존각인학파",
    "침식주술학파",
    "음영잠행학파",
    "단절추방학파",
}

KNIGHT_MAJORS = {
    "검창전술과",
    "방패호위과",
    "중장돌격과",
    "기동타격과",
    "궁노사격과",
    "기마·마수운용과",
    "공성·공병과",
    "대마전투과",
    "지휘참모과",
    "병참·군정과",
}

PRIEST_MAJORS = {
    "Valerion 신전과",
    "Silvaria 신전과",
    "Lusenia 신전과",
    "Calision 신전과",
    "Enosian 신전과",
    "Vesperian 신전과",
    "봉인신 신전과",
}

COLOR_DORM = {
    "청": "청탑 기숙사",
    "황": "황탑 기숙사",
    "적": "적탑 기숙사",
    "녹": "녹탑 기숙사",
    "백": "백탑 기숙사",
    "자": "자탑 기숙사",
    "흑": "흑탑 기숙사",
}


def parse_bool(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
    return None


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    default_population = repo_root / "world/live" / "population"
    parser = argparse.ArgumentParser(description="Audit population invariants")
    parser.add_argument(
        "--population-dir",
        type=Path,
        default=default_population,
        help="Population directory containing P-*.yaml",
    )
    return parser.parse_args()


def expected_dorm(row: dict[str, object]) -> str | None:
    holder = parse_bool(row.get("crest_vision_holder", ""))
    vocation = str(row.get("vocation", ""))
    mana_color = str(row.get("mana_color", ""))

    if holder is True:
        return "비전관"
    if holder is None:
        return None
    if vocation == "마법사":
        return COLOR_DORM.get(mana_color)
    if vocation == "기사":
        return "기사동"
    if vocation == "사제":
        return "신전동군"
    return None


def check_counter(
    name: str,
    counter: Counter[str],
    expected: dict[str, int],
    violations: list[str],
) -> None:
    keys = set(counter.keys()) | set(expected.keys())
    bad = []
    for key in sorted(keys):
        actual = counter.get(key, 0)
        target = expected.get(key, 0)
        if actual != target:
            bad.append(f"{key}: actual={actual}, expected={target}")
    if bad:
        violations.append(f"{name} quota mismatch -> " + "; ".join(bad))


def load_slots(population_dir: Path) -> list[dict[str, object]]:
    yaml_files = sorted(population_dir.glob("P-*.yaml"))
    slots: list[dict[str, object]] = []
    for path in yaml_files:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"Invalid YAML object in {path}")
        data["_path"] = str(path)
        slots.append(data)
    return slots


def main() -> int:
    args = parse_args()
    slots = load_slots(args.population_dir)

    violations: list[str] = []

    if len(slots) != EXPECTED_TOTAL:
        violations.append(f"slot count mismatch: actual={len(slots)}, expected={EXPECTED_TOTAL}")

    background_counts = Counter(str(s.get("background_type", "")) for s in slots)
    grade_counts = Counter(str(s.get("grade", "")) for s in slots)
    mana_counts = Counter(str(s.get("mana_color", "")) for s in slots)
    vocation_counts = Counter(str(s.get("vocation", "")) for s in slots)
    dorm_counts = Counter(str(s.get("dorm", "")) for s in slots)
    crest_counts = Counter(str(parse_bool(s.get("crest_vision_holder", ""))) for s in slots)

    check_counter("background_type", background_counts, EXPECTED_BACKGROUND, violations)
    check_counter("grade", grade_counts, EXPECTED_GRADE, violations)
    check_counter("mana_color", mana_counts, EXPECTED_MANA_COLOR, violations)
    check_counter("vocation", vocation_counts, EXPECTED_VOCATION, violations)

    foreigner_origin_counts: Counter[str] = Counter()

    for slot in slots:
        slot_id = str(slot.get("id", ""))
        bg = str(slot.get("background_type", ""))
        crest = parse_bool(slot.get("crest_vision_holder", ""))
        vocation = str(slot.get("vocation", ""))
        major = str(slot.get("major", ""))
        dorm = str(slot.get("dorm", ""))

        if crest is None:
            violations.append(f"{slot_id}: invalid crest_vision_holder={slot.get('crest_vision_holder')!r}")

        expected = expected_dorm(slot)
        if expected is not None and dorm != expected:
            violations.append(f"{slot_id}: dorm={dorm}, expected={expected}")

        if vocation == "마법사" and major not in MAGE_MAJORS:
            violations.append(f"{slot_id}: invalid mage major={major}")
        elif vocation == "기사" and major not in KNIGHT_MAJORS:
            violations.append(f"{slot_id}: invalid knight major={major}")
        elif vocation == "사제" and major not in PRIEST_MAJORS:
            violations.append(f"{slot_id}: invalid priest major={major}")

        noble_house = str(slot.get("noble_house", ""))
        race = str(slot.get("race", ""))
        origin = str(slot.get("origin", ""))

        if bg == "signature_noble":
            if not noble_house:
                violations.append(f"{slot_id}: missing noble_house for signature_noble")
        elif noble_house:
            violations.append(f"{slot_id}: unexpected noble_house for background={bg}")

        if bg == "nonhuman":
            if not race:
                violations.append(f"{slot_id}: missing race for nonhuman")
            elif race not in ALLOWED_RACES:
                violations.append(f"{slot_id}: invalid race={race}")
        elif race:
            violations.append(f"{slot_id}: unexpected race for background={bg}")

        if bg == "foreigner":
            if not origin:
                violations.append(f"{slot_id}: missing origin for foreigner")
            else:
                foreigner_origin_counts[origin] += 1
                if origin not in EXPECTED_FOREIGNER_ORIGIN:
                    violations.append(f"{slot_id}: invalid origin={origin}")
        elif origin:
            violations.append(f"{slot_id}: unexpected origin for background={bg}")

    check_counter(
        "foreigner.origin",
        foreigner_origin_counts,
        EXPECTED_FOREIGNER_ORIGIN,
        violations,
    )

    print(f"slots={len(slots)}")
    print(f"background_counts={dict(background_counts)}")
    print(f"grade_counts={dict(grade_counts)}")
    print(f"mana_color_counts={dict(mana_counts)}")
    print(f"vocation_counts={dict(vocation_counts)}")
    print(f"crest_vision_holder_counts={dict(crest_counts)}")
    print("dorm_counts:")
    for dorm, count in dorm_counts.most_common():
        print(f"  {dorm}: {count}")
    print("foreigner_origin_counts:")
    for origin, count in foreigner_origin_counts.most_common():
        print(f"  {origin}: {count}")

    if violations:
        print(f"violations={len(violations)}", file=sys.stderr)
        for item in violations[:50]:
            print(f"  - {item}", file=sys.stderr)
        if len(violations) > 50:
            print(f"  ... ({len(violations) - 50} more)", file=sys.stderr)
        return 1

    print("violations=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
