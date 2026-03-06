#!/usr/bin/env python3
"""
Assign foreigner origins to P-* slots.

Safety model:
- Default execution is read-only.
- Actual writes happen only with `--apply`.
- Existing assigned origins block writes unless `--force` is given.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import yaml


SEED = 42
EXPECTED_FOREIGNER_TOTAL = 120
UNASSIGNED_VALUES = {"", "UNASSIGNED", "null", "None"}

ORIGIN_QUOTAS = [
    ("ARC-인접왕국권", 50),
    ("SAH-울카자르권", 18),
    ("NOR-스카르벨권", 18),
    ("ARC-원거리소국권", 17),
    ("출신불명", 17),
]

assert sum(quota for _, quota in ORIGIN_QUOTAS) == EXPECTED_FOREIGNER_TOTAL, "origin quota sum mismatch"

_ORIGIN_RE = re.compile(r"^origin: .*$", re.MULTILINE)


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    default_population_dir = repo_root / "world/live" / "population"
    default_csv_path = default_population_dir / "population_slots.csv"

    parser = argparse.ArgumentParser(description="Plan or apply foreigner origin assignments")
    parser.add_argument(
        "--population-dir",
        type=Path,
        default=default_population_dir,
        help="Population YAML directory containing P-*.yaml",
    )
    parser.add_argument(
        "--csv-path",
        type=Path,
        default=default_csv_path,
        help="Population CSV path",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=SEED,
        help="Deterministic RNG seed for assignment planning",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply assignments to YAML/CSV. Without this flag, the command is read-only.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow overwrite when origins are already assigned.",
    )
    parser.add_argument(
        "--show-plan",
        action="store_true",
        help="Print per-slot assignment plan in addition to summary output.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Alias for explicit read-only validation mode.",
    )
    return parser.parse_args()


def is_unassigned(value: object) -> bool:
    return str(value).strip() in UNASSIGNED_VALUES


def expand_quotas(quotas: list[tuple[str, int]]) -> list[str]:
    expanded: list[str] = []
    for label, count in quotas:
        expanded.extend([label] * count)
    return expanded


def read_yaml(path: Path) -> dict[str, object] | None:
    with path.open(encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if loaded is None:
        return None
    if not isinstance(loaded, dict):
        raise ValueError(f"invalid yaml object: {path}")
    return loaded


def load_foreigner_slots(population_dir: Path) -> list[dict[str, object]]:
    slots: list[dict[str, object]] = []
    for path in sorted(population_dir.glob("P-*.yaml")):
        data = read_yaml(path)
        if not data:
            continue
        if data.get("background_type") != "foreigner":
            continue
        slot_id = str(data.get("id") or path.stem)
        slots.append(
            {
                "id": slot_id,
                "path": path,
                "origin": str(data.get("origin", "")).strip(),
            }
        )
    return slots


def validate_slot_count(slots: list[dict[str, object]]) -> None:
    if len(slots) != EXPECTED_FOREIGNER_TOTAL:
        raise ValueError(
            f"expected {EXPECTED_FOREIGNER_TOTAL} foreigner slots, found {len(slots)}"
        )


def summarize_current_origins(slots: list[dict[str, object]]) -> tuple[Counter[str], list[str]]:
    assigned = Counter()
    already_assigned_ids: list[str] = []
    for slot in slots:
        origin = str(slot["origin"]).strip()
        if is_unassigned(origin):
            continue
        assigned[origin] += 1
        already_assigned_ids.append(str(slot["id"]))
    return assigned, already_assigned_ids


def plan_assignments(slots: list[dict[str, object]], seed: int) -> list[tuple[str, Path, str]]:
    ids_and_paths = [(str(slot["id"]), Path(slot["path"])) for slot in slots]
    rng = np.random.default_rng(seed)
    indices = list(range(len(ids_and_paths)))
    rng.shuffle(indices)

    origin_seq = expand_quotas(ORIGIN_QUOTAS)
    plan: list[tuple[str, Path, str]] = []
    for rank, index in enumerate(indices):
        slot_id, path = ids_and_paths[index]
        plan.append((slot_id, path, origin_seq[rank]))
    plan.sort(key=lambda item: item[0])
    return plan


def update_yaml_origin(path: Path, origin: str) -> None:
    text = path.read_text(encoding="utf-8")
    new_line = f"origin: {origin}"
    if _ORIGIN_RE.search(text):
        text = _ORIGIN_RE.sub(new_line, text, count=1)
    else:
        text = re.sub(
            r"(^vocation: .+$)",
            r"\1\n" + new_line,
            text,
            count=1,
            flags=re.MULTILINE,
        )
    path.write_text(text, encoding="utf-8")


def update_csv(csv_path: Path, origin_map: dict[str, str]) -> int:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    if "origin" not in fieldnames:
        fieldnames.append("origin")

    updated = 0
    for row in rows:
        slot_id = row.get("id", "")
        if slot_id not in origin_map:
            continue
        row["origin"] = origin_map[slot_id]
        updated += 1

    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return updated


def print_summary(slots: list[dict[str, object]], plan: list[tuple[str, Path, str]], assigned_counts: Counter[str]) -> None:
    plan_counts = Counter(origin for _, _, origin in plan)
    print(f"foreigner_slots={len(slots)}")
    print(f"already_assigned={sum(assigned_counts.values())}")
    print("planned_counts:")
    for label, quota in ORIGIN_QUOTAS:
        print(
            f"  {label}: planned={plan_counts.get(label, 0)} expected={quota} current={assigned_counts.get(label, 0)}"
        )


def print_plan(plan: list[tuple[str, Path, str]]) -> None:
    print("assignment_plan:")
    for slot_id, _, origin in plan:
        print(f"  {slot_id} -> {origin}")


def main() -> int:
    args = parse_args()

    if not args.population_dir.is_dir():
        print(f"[fail] population dir not found: {args.population_dir}", file=sys.stderr)
        return 2
    if not args.csv_path.is_file():
        print(f"[fail] csv not found: {args.csv_path}", file=sys.stderr)
        return 2

    slots = load_foreigner_slots(args.population_dir)
    try:
        validate_slot_count(slots)
    except ValueError as exc:
        print(f"[fail] {exc}", file=sys.stderr)
        return 1

    assigned_counts, already_assigned_ids = summarize_current_origins(slots)
    plan = plan_assignments(slots, args.seed)

    print_summary(slots, plan, assigned_counts)
    if args.show_plan:
        print_plan(plan)

    read_only = not args.apply
    if args.check and args.apply:
        print("[fail] --check and --apply cannot be used together", file=sys.stderr)
        return 2

    if read_only:
        print("mode=read_only")
        if already_assigned_ids:
            print("state=assigned")
        else:
            print("state=unassigned")
        return 0

    if already_assigned_ids and not args.force:
        print(
            "[fail] origins already assigned; rerun with --force to overwrite",
            file=sys.stderr,
        )
        print(
            f"assigned_slot_count={len(already_assigned_ids)} first_slot={already_assigned_ids[0]}",
            file=sys.stderr,
        )
        return 1

    origin_map = {slot_id: origin for slot_id, _, origin in plan}

    print("apply_yaml=yes")
    for slot_id, path, origin in plan:
        update_yaml_origin(path, origin)

    print("apply_csv=yes")
    csv_updated = update_csv(args.csv_path, origin_map)
    print(f"csv_updated={csv_updated}")

    final_counts = Counter(origin_map.values())
    print("final_counts:")
    for label, quota in ORIGIN_QUOTAS:
        actual = final_counts.get(label, 0)
        status = "ok" if actual == quota else "mismatch"
        print(f"  {label}: {actual}/{quota} ({status})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
