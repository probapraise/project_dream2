#!/usr/bin/env python3
"""Apply bootstrap population policy to P-slot CSV/YAML.

Policy (current):
1) Background counts:
   - signature_noble: 160
   - common_noble: 2870
   - commoner: 200
   - foreigner: 120
   - nonhuman: 250
2) Dorm assignment:
   - crest_vision_holder=true -> 비전관
   - crest_vision_holder=false + vocation=마법사 -> <mana_color>탑 기숙사
   - crest_vision_holder=false + vocation=기사 -> 기사동
   - crest_vision_holder=false + vocation=사제 -> 신전동군
"""

from __future__ import annotations

import argparse
import csv
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

COLOR_DORM = {
    "청": "청탑 기숙사",
    "황": "황탑 기숙사",
    "적": "적탑 기숙사",
    "녹": "녹탑 기숙사",
    "백": "백탑 기숙사",
    "보라": "보라탑 기숙사",
    "흑": "흑탑 기숙사",
}

DORM_ORDER = (
    "비전관",
    "청탑 기숙사",
    "황탑 기숙사",
    "적탑 기숙사",
    "녹탑 기숙사",
    "백탑 기숙사",
    "보라탑 기숙사",
    "흑탑 기숙사",
    "기사동",
    "신전동군",
)

LEGACY_DORMS = {
    "일반동(동관)",
    "일반동(서관)",
    "장학생동",
    "연구·탑동",
    "외국·인외동",
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
    repo_root = Path(__file__).resolve().parents[1]
    bundle_root = repo_root / "worldbible_refined_bundle_20260303"
    parser = argparse.ArgumentParser(description="Apply bootstrap background+dorm policy (current)")
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
    parser.add_argument("--seed", type=int, default=20260304, help="Reserved compatibility arg (unused)")
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


def ensure_crest_vision_holder(rows: list[dict[str, str]]) -> int:
    backfilled = 0
    for row in rows:
        crest = parse_bool(row.get("crest_vision_holder", ""))
        if crest is None:
            crest = row.get("background_type", "") == "signature_noble"
            backfilled += 1
        row["crest_vision_holder"] = "true" if crest else "false"
    return backfilled


def assign_dorms(rows: list[dict[str, str]], seed: int) -> None:
    _ = seed
    for row in rows:
        holder = parse_bool(row.get("crest_vision_holder", ""))
        if holder is None:
            raise RuntimeError(f"invalid crest_vision_holder: id={row.get('id')} value={row.get('crest_vision_holder')!r}")

        if holder:
            row["dorm"] = "비전관"
            continue

        vocation = row.get("vocation", "")
        if vocation == "마법사":
            mana_color = row.get("mana_color", "")
            dorm = COLOR_DORM.get(mana_color)
            if dorm is None:
                raise RuntimeError(
                    f"Cannot assign mage dorm without valid mana_color: id={row.get('id')} mana_color={mana_color!r}"
                )
            row["dorm"] = dorm
            continue
        if vocation == "기사":
            row["dorm"] = "기사동"
            continue
        if vocation == "사제":
            row["dorm"] = "신전동군"
            continue

        raise RuntimeError(f"Unsupported vocation for dorm assignment: id={row.get('id')} vocation={vocation!r}")

    dorm_counts = Counter(row["dorm"] for row in rows)
    for legacy in LEGACY_DORMS:
        if dorm_counts.get(legacy, 0) > 0:
            raise RuntimeError(f"Legacy dorm label detected after assignment: {legacy}")

    for row in rows:
        holder = parse_bool(row.get("crest_vision_holder", ""))
        if holder is True and row["dorm"] != "비전관":
            raise RuntimeError(f"Invalid crest-holder dorm: {row['id']} -> {row['dorm']}")
        if holder is False and row["dorm"] == "비전관":
            raise RuntimeError(f"Invalid non-holder assignment to 비전관: {row['id']}")


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


def update_yaml(path: Path, background_type: str, crest_vision_holder: str, dorm: str) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)
    lines = path.read_text(encoding="utf-8").splitlines()
    has_dorm = any(line.startswith("dorm:") for line in lines)
    has_crest = any(line.startswith("crest_vision_holder:") for line in lines)

    out: list[str] = []
    replaced_bg = False
    replaced_crest = False
    replaced_dorm = False
    for line in lines:
        if line.startswith("background_type:"):
            out.append(f"background_type: {background_type}")
            replaced_bg = True
            if not has_crest:
                out.append(f"crest_vision_holder: {crest_vision_holder}")
            if not has_dorm:
                out.append(f"dorm: {dorm}")
            continue
        if line.startswith("crest_vision_holder:"):
            out.append(f"crest_vision_holder: {crest_vision_holder}")
            replaced_crest = True
            continue
        if line.startswith("dorm:"):
            out.append(f"dorm: {dorm}")
            replaced_dorm = True
            continue
        out.append(line)

    if not replaced_bg:
        raise RuntimeError(f"background_type not found in {path}")
    if has_crest and not replaced_crest:
        raise RuntimeError(f"crest_vision_holder replacement failed in {path}")
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
    for dorm in DORM_ORDER:
        print(f"  {dorm}: {dorm_counts.get(dorm, 0)}")
    for dorm in sorted(k for k in dorm_counts.keys() if k not in DORM_ORDER):
        print(f"  {dorm}: {dorm_counts[dorm]}")


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
    required = {"id", "background_type", "vocation", "mana_color"}
    if not required.issubset(set(rows[0].keys())):
        print(f"CSV missing required columns: {required}", file=sys.stderr)
        return 2

    rebalance_backgrounds(rows)
    crest_backfilled = ensure_crest_vision_holder(rows)
    assign_dorms(rows, seed=args.seed)
    write_csv(args.csv_path, rows)

    for row in rows:
        yaml_path = args.population_dir / f"{row['id']}.yaml"
        update_yaml(
            yaml_path,
            row["background_type"],
            row["crest_vision_holder"],
            row["dorm"],
        )

    print_summary(rows)
    print(f"crest_backfilled={crest_backfilled}")
    print(f"updated_csv={args.csv_path}")
    print(f"updated_yaml_dir={args.population_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
