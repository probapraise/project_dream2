#!/usr/bin/env python3
"""Apply bootstrap population policy to P-slot CSV/YAML.

Policy (v2026-03-04):
1) Background counts:
   - signature_noble: 160
   - common_noble: 2870
   - commoner: 200
   - foreigner: 120
   - nonhuman: 250
2) Dorm assignment:
   - 일반동(동관): 1200
   - 일반동(서관): 1140
   - 장학생동: 620
   - 비전관: 160 (signature_noble only)
   - 연구·탑동: 280
   - 외국·인외동: 200
"""

from __future__ import annotations

import argparse
import csv
import random
import sys
from collections import Counter
from pathlib import Path


BACKGROUND_TARGETS = (
    ("signature_noble", 160),
    ("common_noble", 2870),
    ("commoner", 200),
    ("foreigner", 120),
    ("nonhuman", 250),
)

DORM_TARGETS = (
    ("일반동(동관)", 1200),
    ("일반동(서관)", 1140),
    ("장학생동", 620),
    ("비전관", 160),
    ("연구·탑동", 280),
    ("외국·인외동", 200),
)

# Deterministic operational matrix aligned to WB-0015 13.6.
BACKGROUND_DORM_TARGETS = {
    "signature_noble": {"비전관": 160},
    "common_noble": {"일반동(동관)": 1150, "일반동(서관)": 1100, "장학생동": 370, "연구·탑동": 250},
    "commoner": {"장학생동": 200},
    "foreigner": {"외국·인외동": 120},
    "nonhuman": {"일반동(동관)": 50, "일반동(서관)": 40, "장학생동": 50, "연구·탑동": 30, "외국·인외동": 80},
}

BACKGROUND_SEED_OFFSET = {
    "signature_noble": 11,
    "common_noble": 23,
    "commoner": 37,
    "foreigner": 41,
    "nonhuman": 53,
}


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    bundle_root = repo_root / "worldbible_refined_bundle_20260303"
    parser = argparse.ArgumentParser(description="Apply bootstrap background+dorm policy")
    parser.add_argument(
        "--csv-path",
        type=Path,
        default=bundle_root / "population" / "population_slots.csv",
        help="Population CSV path",
    )
    parser.add_argument(
        "--population-dir",
        type=Path,
        default=bundle_root / "population",
        help="Population YAML directory",
    )
    parser.add_argument("--seed", type=int, default=20260304, help="Random seed for deterministic ID shuffling")
    return parser.parse_args()


def id_sort_key(pid: str) -> int:
    return int(pid.split("-")[1])


def rebalance_backgrounds(rows: list[dict[str, str]]) -> None:
    target_map = dict(BACKGROUND_TARGETS)
    counts = Counter(row["background_type"] for row in rows)
    row_by_id = {row["id"]: row for row in rows}

    # Build donor pools from surplus groups (largest ID first for deterministic churn reduction).
    donor_pools: dict[str, list[str]] = {}
    for bg, _ in BACKGROUND_TARGETS:
        extra = counts.get(bg, 0) - target_map[bg]
        if extra > 0:
            ids = sorted((r["id"] for r in rows if r["background_type"] == bg), key=id_sort_key, reverse=True)
            donor_pools[bg] = ids[:extra]

    deficits = []
    for bg, _ in BACKGROUND_TARGETS:
        need = target_map[bg] - counts.get(bg, 0)
        if need > 0:
            deficits.append((bg, need))

    donor_order = [bg for bg, _ in BACKGROUND_TARGETS if bg in donor_pools]

    for deficit_bg, need in deficits:
        while need > 0:
            donor_bg = next((bg for bg in donor_order if donor_pools.get(bg)), None)
            if donor_bg is None:
                raise RuntimeError(f"Unable to satisfy deficit for {deficit_bg}: remaining {need}")
            pid = donor_pools[donor_bg].pop(0)
            row_by_id[pid]["background_type"] = deficit_bg
            need -= 1

    final_counts = Counter(row["background_type"] for row in rows)
    for bg, target in BACKGROUND_TARGETS:
        if final_counts.get(bg, 0) != target:
            raise RuntimeError(
                f"Background rebalance failed for {bg}: expected {target}, got {final_counts.get(bg, 0)}"
            )


def assign_dorms(rows: list[dict[str, str]], seed: int) -> None:
    counts = Counter(row["background_type"] for row in rows)
    for bg, matrix in BACKGROUND_DORM_TARGETS.items():
        required = sum(matrix.values())
        have = counts.get(bg, 0)
        if have != required:
            raise RuntimeError(f"Background {bg} count mismatch: have={have}, required_by_matrix={required}")

    row_by_id = {row["id"]: row for row in rows}
    ids_by_bg: dict[str, list[str]] = {}
    for bg, _ in BACKGROUND_TARGETS:
        ids = [r["id"] for r in rows if r["background_type"] == bg]
        rng = random.Random(seed + BACKGROUND_SEED_OFFSET[bg])
        rng.shuffle(ids)
        ids_by_bg[bg] = ids

    for row in rows:
        row["dorm"] = ""

    for bg, matrix in BACKGROUND_DORM_TARGETS.items():
        ids = ids_by_bg[bg]
        cursor = 0
        for dorm, n in matrix.items():
            for pid in ids[cursor : cursor + n]:
                row_by_id[pid]["dorm"] = dorm
            cursor += n

    dorm_counts = Counter(row["dorm"] for row in rows)
    for dorm, target in DORM_TARGETS:
        if dorm_counts.get(dorm, 0) != target:
            raise RuntimeError(f"Dorm allocation failed for {dorm}: expected {target}, got {dorm_counts.get(dorm, 0)}")

    for row in rows:
        if row["dorm"] == "비전관" and row["background_type"] != "signature_noble":
            raise RuntimeError(f"Invalid non-signature assignment to 비전관: {row['id']}")


def write_csv(csv_path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise RuntimeError("No rows to write")

    fieldnames = list(rows[0].keys())
    if "dorm" not in fieldnames:
        if "background_type" in fieldnames:
            idx = fieldnames.index("background_type") + 1
            fieldnames.insert(idx, "dorm")
        else:
            fieldnames.append("dorm")

    # Keep stable output order by id.
    rows_sorted = sorted(rows, key=lambda r: id_sort_key(r["id"]))
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_sorted)


def update_yaml(path: Path, background_type: str, dorm: str) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    has_dorm = any(line.startswith("dorm:") for line in lines)

    out: list[str] = []
    replaced_bg = False
    replaced_dorm = False
    for line in lines:
        if line.startswith("background_type:"):
            out.append(f"background_type: {background_type}")
            replaced_bg = True
            if not has_dorm:
                out.append(f"dorm: {dorm}")
            continue
        if line.startswith("dorm:"):
            out.append(f"dorm: {dorm}")
            replaced_dorm = True
            continue
        out.append(line)

    if not replaced_bg:
        raise RuntimeError(f"background_type not found in {path}")
    if has_dorm and not replaced_dorm:
        raise RuntimeError(f"dorm replacement failed in {path}")

    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def print_summary(rows: list[dict[str, str]]) -> None:
    bg_counts = Counter(row["background_type"] for row in rows)
    dorm_counts = Counter(row["dorm"] for row in rows)

    print("Background counts:")
    for bg, _ in BACKGROUND_TARGETS:
        print(f"  {bg}: {bg_counts.get(bg, 0)}")
    print("Dorm counts:")
    for dorm, _ in DORM_TARGETS:
        print(f"  {dorm}: {dorm_counts.get(dorm, 0)}")


def main() -> int:
    args = parse_args()
    if not args.csv_path.is_file():
        print(f"CSV not found: {args.csv_path}", file=sys.stderr)
        return 2

    with args.csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if len(rows) != 3600:
        print(f"Unexpected row count: {len(rows)} (expected 3600)", file=sys.stderr)
        return 2
    required = {"id", "background_type"}
    if not required.issubset(set(rows[0].keys())):
        print(f"CSV missing required columns: {required}", file=sys.stderr)
        return 2

    rebalance_backgrounds(rows)
    assign_dorms(rows, seed=args.seed)
    write_csv(args.csv_path, rows)

    for row in rows:
        yaml_path = args.population_dir / f"{row['id']}.yaml"
        update_yaml(yaml_path, row["background_type"], row["dorm"])

    print_summary(rows)
    print(f"updated_csv={args.csv_path}")
    print(f"updated_yaml_dir={args.population_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
