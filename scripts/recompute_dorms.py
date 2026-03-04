#!/usr/bin/env python3
"""Recompute dorm assignments from current agreed rules.

Rules:
1) crest_vision_holder=true -> 비전관 (강제 우선)
2) crest_vision_holder=false:
   - vocation=마법사 -> <mana_color> 기숙사
   - vocation=기사   -> 기사동
   - vocation=사제   -> 신전동군
3) 외국인/인외는 별도 분리동 없이 동일 규칙 적용.

Updates:
- population/population_slots.csv (crest_vision_holder, dorm)
- population/P-*.yaml (crest_vision_holder, dorm)
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path


COLOR_DORM = {
    "청": "청탑 기숙사",
    "황": "황탑 기숙사",
    "적": "적탑 기숙사",
    "녹": "녹탑 기숙사",
    "백": "백탑 기숙사",
    "보라": "보라탑 기숙사",
    "흑": "흑탑 기숙사",
}

VISION_DORM = "비전관"
KNIGHT_DORM = "기사동"
PRIEST_DORM = "신전동군"


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    bundle_root = repo_root / "worldbible_refined_bundle_20260303"
    parser = argparse.ArgumentParser(description="Recompute population dorm assignments")
    parser.add_argument(
        "--population-csv",
        type=Path,
        default=bundle_root / "population" / "population_slots.csv",
        help="Input/output population CSV path",
    )
    parser.add_argument(
        "--population-dir",
        type=Path,
        default=bundle_root / "population",
        help="Population YAML directory (P-*.yaml)",
    )
    return parser.parse_args()


def parse_bool(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
    return None


def compute_dorm(row: dict[str, str]) -> tuple[str, str]:
    holder = parse_bool(row.get("crest_vision_holder", ""))
    if holder is None:
        raise ValueError(f"invalid crest_vision_holder: id={row.get('id')} value={row.get('crest_vision_holder')!r}")
    if holder:
        return VISION_DORM, "vision_priority"

    vocation = row.get("vocation", "")
    if vocation == "마법사":
        mana_color = row.get("mana_color", "")
        dorm = COLOR_DORM.get(mana_color)
        if dorm is None:
            raise ValueError(f"invalid mana_color for mage dorm: id={row.get('id')} mana_color={mana_color!r}")
        return dorm, "mage_track"
    if vocation == "기사":
        return KNIGHT_DORM, "knight_track"
    if vocation == "사제":
        return PRIEST_DORM, "priest_track"

    return (row.get("dorm") or "UNASSIGNED"), "fallback"


def update_csv(csv_path: Path) -> tuple[dict[str, str], Counter[str], Counter[str], int]:
    if not csv_path.is_file():
        raise FileNotFoundError(csv_path)

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    if "dorm" not in fieldnames:
        fieldnames.append("dorm")
    if "crest_vision_holder" not in fieldnames:
        insert_at = fieldnames.index("background_type") + 1 if "background_type" in fieldnames else 1
        fieldnames.insert(insert_at, "crest_vision_holder")
    if "tower" in fieldnames:
        fieldnames.remove("tower")

    dorm_by_id: dict[str, str] = {}
    reason_counter: Counter[str] = Counter()
    dorm_counter: Counter[str] = Counter()
    crest_backfilled = 0

    for row in rows:
        crest = parse_bool(row.get("crest_vision_holder", ""))
        if crest is None:
            # Backfill for legacy rows lacking the explicit field.
            bg = row.get("background_type", "")
            if bg not in {"signature_noble", "common_noble", "commoner", "foreigner", "nonhuman"}:
                raise ValueError(f"unknown background_type for crest backfill: id={row.get('id')} bg={bg!r}")
            crest = bg == "signature_noble"
            crest_backfilled += 1
        row["crest_vision_holder"] = "true" if crest else "false"

        pid = row.get("id", "")
        dorm, reason = compute_dorm(row)  # type: ignore[arg-type]
        row["dorm"] = dorm
        row.pop("tower", None)
        if pid:
            dorm_by_id[pid] = dorm
        reason_counter[reason] += 1
        dorm_counter[dorm] += 1

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return dorm_by_id, reason_counter, dorm_counter, crest_backfilled


def update_yaml_slots(population_dir: Path, dorm_by_id: dict[str, str], crest_by_id: dict[str, str]) -> tuple[int, int, int]:
    yaml_files = sorted(population_dir.glob("P-*.yaml"))
    if not yaml_files:
        raise FileNotFoundError(f"No P-*.yaml files in {population_dir}")

    replaced = 0
    inserted = 0
    crest_inserted = 0
    dorm_line_re = re.compile(r"(?m)^dorm:\s*.*$")
    crest_line_re = re.compile(r"(?m)^crest_vision_holder:\s*.*$")

    for path in yaml_files:
        pid = path.stem
        dorm = dorm_by_id.get(pid)
        crest = crest_by_id.get(pid)
        if dorm is None:
            continue

        text = path.read_text(encoding="utf-8")
        if crest is not None:
            if crest_line_re.search(text):
                text = crest_line_re.sub(f"crest_vision_holder: {crest}", text, count=1)
            else:
                new_text = re.sub(
                    r"(?m)^(background_type:\s*.*)$",
                    rf"\1\ncrest_vision_holder: {crest}",
                    text,
                    count=1,
                )
                if new_text != text:
                    text = new_text
                    crest_inserted += 1
        if dorm_line_re.search(text):
            text = dorm_line_re.sub(f"dorm: {dorm}", text, count=1)
            replaced += 1
        else:
            # Standard slot shape always has background_type line.
            new_text = re.sub(
                r"(?m)^(background_type:\s*.*)$",
                rf"\1\ndorm: {dorm}",
                text,
                count=1,
            )
            if new_text == text:
                text = f"dorm: {dorm}\n{text}"
            else:
                text = new_text
            inserted += 1
        path.write_text(text, encoding="utf-8")

    return replaced, inserted, crest_inserted


def run_validations(dorm_by_id: dict[str, str], csv_path: Path) -> None:
    # Validation by rereading CSV (authoritative for crest/vocation checks).
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    bad_vision = [
        r["id"]
        for r in rows
        if parse_bool(r.get("crest_vision_holder", "")) is True and r.get("dorm") != VISION_DORM
    ]
    if bad_vision:
        raise ValueError(f"crest_vision_holder=true not in 비전관: {bad_vision[:5]}")

    bad_nonvision = [
        r["id"]
        for r in rows
        if parse_bool(r.get("crest_vision_holder", "")) is False and r.get("dorm") == VISION_DORM
    ]
    if bad_nonvision:
        raise ValueError(f"crest_vision_holder=false in 비전관: {bad_nonvision[:5]}")

    bad_split = [r["id"] for r in rows if r.get("dorm") == "외국·인외동"]
    if bad_split:
        raise ValueError(f"외국·인외동 잔존: {bad_split[:5]}")


def main() -> int:
    args = parse_args()

    dorm_by_id, reason_counter, dorm_counter, crest_backfilled = update_csv(args.population_csv)
    crest_by_id: dict[str, str] = {}
    with args.population_csv.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            pid = row.get("id", "")
            if pid:
                crest_by_id[pid] = str(row.get("crest_vision_holder", "false")).strip().lower()

    replaced, inserted, crest_inserted = update_yaml_slots(args.population_dir, dorm_by_id, crest_by_id)
    run_validations(dorm_by_id, args.population_csv)

    print(f"rows={len(dorm_by_id)}")
    print(f"yaml_replaced={replaced}")
    print(f"yaml_inserted={inserted}")
    print(f"yaml_crest_inserted={crest_inserted}")
    print(f"csv_crest_backfilled={crest_backfilled}")
    print("reason_counts:")
    for key, n in reason_counter.items():
        print(f"  {key}: {n}")
    print("dorm_counts:")
    for dorm, n in dorm_counter.most_common():
        print(f"  {dorm}: {n}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        raise
