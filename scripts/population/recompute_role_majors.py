#!/usr/bin/env python3
"""Recompute major field by vocation (기사/사제 major mismatch fix).

Rule summary:
- 마법사: 기존 탑 기반 마법 학파 major 유지
- 기사: 기사 10개 과정으로 재배정
- 사제: 7개 신전과로 재배정

The assignment is deterministic by seed and mana_color-weighted for lore coherence.
Updates both CSV and P-*.yaml.
"""

from __future__ import annotations

import argparse
import csv
import random
import re
import sys
from collections import Counter
from pathlib import Path


KNIGHT_MAJORS = [
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
]

PRIEST_MAJORS = [
    "Valerion 신전과",
    "Silvaria 신전과",
    "Lusenia 신전과",
    "Calision 신전과",
    "Enosian 신전과",
    "Vesperian 신전과",
    "봉인신 신전과",
]

# Tower-weighted assignment for 기사 과정.
KNIGHT_WEIGHTS_BY_TOWER = {
    "적탑":  [0.24, 0.04, 0.18, 0.16, 0.09, 0.07, 0.12, 0.06, 0.02, 0.02],
    "황탑":  [0.18, 0.05, 0.03, 0.16, 0.14, 0.02, 0.13, 0.07, 0.12, 0.10],
    "청탑":  [0.10, 0.24, 0.04, 0.04, 0.05, 0.02, 0.08, 0.16, 0.15, 0.12],
    "녹탑":  [0.10, 0.08, 0.02, 0.18, 0.12, 0.23, 0.07, 0.05, 0.04, 0.11],
    "백탑":  [0.08, 0.22, 0.03, 0.04, 0.10, 0.03, 0.06, 0.20, 0.13, 0.11],
    "자탑": [0.06, 0.08, 0.03, 0.10, 0.14, 0.02, 0.05, 0.18, 0.24, 0.10],
    "흑탑":  [0.10, 0.04, 0.03, 0.25, 0.11, 0.02, 0.16, 0.20, 0.06, 0.03],
}

# Tower-weighted assignment for 사제 신전과.
PRIEST_WEIGHTS_BY_TOWER = {
    "적탑":  [0.50, 0.05, 0.08, 0.10, 0.05, 0.20, 0.02],
    "황탑":  [0.45, 0.05, 0.08, 0.25, 0.05, 0.10, 0.02],
    "청탑":  [0.05, 0.25, 0.10, 0.45, 0.08, 0.05, 0.02],
    "녹탑":  [0.05, 0.45, 0.30, 0.10, 0.05, 0.03, 0.02],
    "백탑":  [0.03, 0.10, 0.45, 0.30, 0.07, 0.03, 0.02],
    "자탑": [0.05, 0.05, 0.08, 0.15, 0.50, 0.15, 0.02],
    "흑탑":  [0.04, 0.03, 0.03, 0.05, 0.15, 0.60, 0.10],
}

COLOR_TO_TOWER = {
    "청": "청탑",
    "황": "황탑",
    "적": "적탑",
    "녹": "녹탑",
    "백": "백탑",
    "자": "자탑",
    "흑": "흑탑",
}

MAGE_MAJOR_SET = {
    "경면수호학파", "빙쇄구속학파", "수류유도학파",
    "황도유성학파", "뇌철견인학파", "결정변성학파",
    "홍련포화학파", "용철무구학파", "화연장막학파",
    "생맥약초학파", "야생교감학파", "포자영토학파",
    "생명고정학파", "정화광휘학파", "서약집행학파",
    "전심공명학파", "환영직조학파", "보존각인학파",
    "침식주술학파", "음영잠행학파", "단절추방학파",
}


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    bundle_root = repo_root / "world/live"
    parser = argparse.ArgumentParser(description="Recompute majors for 기사/사제")
    parser.add_argument(
        "--population-csv",
        type=Path,
        default=bundle_root / "population" / "population_slots.csv",
        help="Input/output population CSV",
    )
    parser.add_argument(
        "--population-dir",
        type=Path,
        default=bundle_root / "population",
        help="Population YAML directory",
    )
    parser.add_argument("--seed", type=int, default=42, help="Deterministic seed")
    return parser.parse_args()


def weighted_pick(rng: random.Random, labels: list[str], weights: list[float]) -> str:
    return rng.choices(labels, weights=weights, k=1)[0]


def assign_major(row: dict[str, str], rng: random.Random) -> str:
    vocation = row.get("vocation", "")
    mana_color = row.get("mana_color", "")
    tower = COLOR_TO_TOWER.get(mana_color, "")
    if vocation == "기사":
        weights = KNIGHT_WEIGHTS_BY_TOWER.get(tower)
        if weights is None:
            weights = [1.0] * len(KNIGHT_MAJORS)
        return weighted_pick(rng, KNIGHT_MAJORS, weights)
    if vocation == "사제":
        weights = PRIEST_WEIGHTS_BY_TOWER.get(tower)
        if weights is None:
            weights = [1.0] * len(PRIEST_MAJORS)
        return weighted_pick(rng, PRIEST_MAJORS, weights)
    return row.get("major", "")


def update_csv(csv_path: Path, seed: int) -> dict[str, str]:
    if not csv_path.is_file():
        raise FileNotFoundError(csv_path)

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    if "major" not in fieldnames:
        fieldnames.append("major")

    rng = random.Random(seed)
    # Stable order by numeric P-id for deterministic outputs.
    rows.sort(key=lambda r: int(r["id"].split("-")[1]))

    major_by_id: dict[str, str] = {}
    for row in rows:
        major = assign_major(row, rng)
        row["major"] = major
        major_by_id[row["id"]] = major

    # Restore original file order by id.
    rows.sort(key=lambda r: int(r["id"].split("-")[1]))
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return major_by_id


def update_yaml(population_dir: Path, major_by_id: dict[str, str]) -> tuple[int, int]:
    yaml_files = sorted(population_dir.glob("P-*.yaml"))
    if not yaml_files:
        raise FileNotFoundError(f"No P-*.yaml in {population_dir}")

    replaced = 0
    inserted = 0
    major_re = re.compile(r"(?m)^major:\s*.*$")
    for p in yaml_files:
        pid = p.stem
        major = major_by_id.get(pid)
        if major is None:
            continue
        text = p.read_text(encoding="utf-8")
        if major_re.search(text):
            text = major_re.sub(f"major: {major}", text, count=1)
            replaced += 1
        else:
            new_text = re.sub(
                r"(?m)^(mana_color:\s*.*)$",
                rf"\1\nmajor: {major}",
                text,
                count=1,
            )
            if new_text == text:
                text = text + f"\nmajor: {major}\n"
            else:
                text = new_text
            inserted += 1
        p.write_text(text, encoding="utf-8")
    return replaced, inserted


def validate(csv_path: Path) -> tuple[Counter[str], Counter[str], Counter[str]]:
    with csv_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    wrong_knight = [
        r["id"] for r in rows
        if r.get("vocation") == "기사" and r.get("major") not in KNIGHT_MAJORS
    ]
    wrong_priest = [
        r["id"] for r in rows
        if r.get("vocation") == "사제" and r.get("major") not in PRIEST_MAJORS
    ]
    wrong_mage = [
        r["id"] for r in rows
        if r.get("vocation") == "마법사" and r.get("major") not in MAGE_MAJOR_SET
    ]
    if wrong_knight:
        raise ValueError(f"기사 major 불일치: {wrong_knight[:5]}")
    if wrong_priest:
        raise ValueError(f"사제 major 불일치: {wrong_priest[:5]}")
    if wrong_mage:
        raise ValueError(f"마법사 major 불일치: {wrong_mage[:5]}")

    by_vocation = Counter(r.get("vocation", "") for r in rows)
    knight_major_counts = Counter(r.get("major", "") for r in rows if r.get("vocation") == "기사")
    priest_major_counts = Counter(r.get("major", "") for r in rows if r.get("vocation") == "사제")
    return by_vocation, knight_major_counts, priest_major_counts


def main() -> int:
    args = parse_args()
    major_by_id = update_csv(args.population_csv, args.seed)
    replaced, inserted = update_yaml(args.population_dir, major_by_id)
    by_vocation, knight_major_counts, priest_major_counts = validate(args.population_csv)

    print(f"rows={len(major_by_id)}")
    print(f"yaml_replaced={replaced}")
    print(f"yaml_inserted={inserted}")
    print(f"vocation_counts={dict(by_vocation)}")
    print("knight_major_counts:")
    for k, n in knight_major_counts.most_common():
        print(f"  {k}: {n}")
    print("priest_major_counts:")
    for k, n in priest_major_counts.most_common():
        print(f"  {k}: {n}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        raise
