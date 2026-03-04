#!/usr/bin/env python3
"""Generate P-* population slots for Dream2 bootstrap.

Produces Big5 values sampled from academy-adjusted normal distributions:
- O: mean 0.65, std 0.16
- C: mean 0.62, std 0.16
- E: mean 0.50, std 0.18
- A: mean 0.58, std 0.16
- N: mean 0.50, std 0.18

Also assigns background_type with academy composition priors:
- signature_noble: 160
- common_noble: 2870
- commoner: 200
- foreigner: 120
- nonhuman: 250

Dorm allocation policy (when count=3600):
- 일반동(동관): 1200
- 일반동(서관): 1140
- 장학생동: 620
- 비전관: 160 (signature_noble only)
- 연구·탑동: 280
- 외국·인외동: 200

All numeric values are clipped to [0.01, 0.99] and rounded to 2 decimals.
"""

from __future__ import annotations

import argparse
import csv
import random
import statistics
import sys
from pathlib import Path


TRAITS = (
    ("O", 0.65, 0.16),
    ("C", 0.62, 0.16),
    ("E", 0.50, 0.18),
    ("A", 0.58, 0.16),
    ("N", 0.50, 0.18),
)

BACKGROUND_TARGETS_3600 = (
    ("signature_noble", 160),
    ("common_noble", 2870),
    ("commoner", 200),
    ("foreigner", 120),
    ("nonhuman", 250),
)

DORM_TARGETS_3600 = (
    ("일반동(동관)", 1200),
    ("일반동(서관)", 1140),
    ("장학생동", 620),
    ("비전관", 160),
    ("연구·탑동", 280),
    ("외국·인외동", 200),
)

BACKGROUND_DORM_TARGETS_3600 = {
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


def clip01(value: float) -> float:
    return max(0.01, min(0.99, value))


def q2(value: float) -> float:
    return float(f"{clip01(value):.2f}")


def slot_id(index: int) -> str:
    return f"P-{index:04d}"


def allocate_background_counts(count: int) -> dict[str, int]:
    total = sum(n for _, n in BACKGROUND_TARGETS_3600)
    if count == total:
        return {k: n for k, n in BACKGROUND_TARGETS_3600}

    raw = []
    floor_counts: dict[str, int] = {}
    for key, base_n in BACKGROUND_TARGETS_3600:
        x = count * (base_n / total)
        n = int(x)
        floor_counts[key] = n
        raw.append((key, x - n))

    remainder = count - sum(floor_counts.values())
    raw.sort(key=lambda item: item[1], reverse=True)
    for i in range(remainder):
        floor_counts[raw[i][0]] += 1
    return floor_counts


def build_background_sequence(count: int, rng: random.Random) -> list[str]:
    counts = allocate_background_counts(count)
    seq: list[str] = []
    for key, _ in BACKGROUND_TARGETS_3600:
        seq.extend([key] * counts[key])
    rng.shuffle(seq)
    return seq


def build_rows(count: int, seed: int) -> list[dict[str, object]]:
    rng = random.Random(seed)
    background_seq = build_background_sequence(count, rng)
    rows: list[dict[str, object]] = []

    for i in range(1, count + 1):
        b5 = {name: q2(rng.gauss(mean, std)) for name, mean, std in TRAITS}
        rows.append(
            {
                "id": slot_id(i),
                "background_type": background_seq[i - 1],
                "dorm": "UNASSIGNED",
                "b5": b5,
                "derived": {"DT": None, "NFC": None, "SM": None},
                "status": "uninstantiated",
                "ch_id": None,
            }
        )
    assign_dorms(rows, seed)
    return rows


def assign_dorms(rows: list[dict[str, object]], seed: int) -> None:
    if len(rows) != 3600:
        # Non-standard count runs keep dorm unassigned.
        return

    bg_counts: dict[str, int] = {}
    for row in rows:
        bg = str(row["background_type"])
        bg_counts[bg] = bg_counts.get(bg, 0) + 1

    for bg, matrix in BACKGROUND_DORM_TARGETS_3600.items():
        required = sum(matrix.values())
        if bg_counts.get(bg, 0) != required:
            raise ValueError(
                f"Background count mismatch for dorm allocation: {bg} have {bg_counts.get(bg, 0)} want {required}"
            )

    ids_by_bg: dict[str, list[str]] = {}
    row_by_id = {str(row["id"]): row for row in rows}
    for bg, _ in BACKGROUND_TARGETS_3600:
        ids = [str(row["id"]) for row in rows if str(row["background_type"]) == bg]
        rng = random.Random(seed + BACKGROUND_SEED_OFFSET[bg])
        rng.shuffle(ids)
        ids_by_bg[bg] = ids

    for bg, matrix in BACKGROUND_DORM_TARGETS_3600.items():
        ids = ids_by_bg[bg]
        cursor = 0
        for dorm, n in matrix.items():
            for pid in ids[cursor : cursor + n]:
                row_by_id[pid]["dorm"] = dorm
            cursor += n

    dorm_counts: dict[str, int] = {}
    for row in rows:
        dorm = str(row["dorm"])
        dorm_counts[dorm] = dorm_counts.get(dorm, 0) + 1
        if dorm == "비전관" and str(row["background_type"]) != "signature_noble":
            raise ValueError(f"Invalid non-signature assignment to 비전관: {row['id']}")

    for dorm, target in DORM_TARGETS_3600:
        if dorm_counts.get(dorm, 0) != target:
            raise ValueError(
                f"Dorm count mismatch: {dorm} have {dorm_counts.get(dorm, 0)} want {target}"
            )


def ensure_writable(path: Path, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(
            f"{path} already exists. Use --force to overwrite existing outputs."
        )


def write_csv(rows: list[dict[str, object]], csv_path: Path, force: bool) -> None:
    ensure_writable(csv_path, force)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["id", "background_type", "dorm", "O", "C", "E", "A", "N", "DT", "NFC", "SM", "status", "ch_id"]
        )
        for row in rows:
            b5 = row["b5"]  # type: ignore[assignment]
            writer.writerow(
                [
                    row["id"],
                    row["background_type"],
                    row["dorm"],
                    f"{b5['O']:.2f}",
                    f"{b5['C']:.2f}",
                    f"{b5['E']:.2f}",
                    f"{b5['A']:.2f}",
                    f"{b5['N']:.2f}",
                    "",
                    "",
                    "",
                    row["status"],
                    "",
                ]
            )


def _yaml_value(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def write_yaml_slots(rows: list[dict[str, object]], out_dir: Path, force: bool) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    existing = list(out_dir.glob("P-*.yaml"))
    if existing and not force:
        raise FileExistsError(
            f"{out_dir} already has {len(existing)} slot files. Use --force to overwrite."
        )

    for row in rows:
        b5 = row["b5"]  # type: ignore[assignment]
        derived = row["derived"]  # type: ignore[assignment]
        content = "\n".join(
            [
                f"id: {row['id']}",
                f"background_type: {row['background_type']}",
                f"dorm: {row['dorm']}",
                "b5:",
                f"  O: {_yaml_value(b5['O'])}",
                f"  C: {_yaml_value(b5['C'])}",
                f"  E: {_yaml_value(b5['E'])}",
                f"  A: {_yaml_value(b5['A'])}",
                f"  N: {_yaml_value(b5['N'])}",
                "derived:",
                f"  DT: {_yaml_value(derived['DT'])}",
                f"  NFC: {_yaml_value(derived['NFC'])}",
                f"  SM: {_yaml_value(derived['SM'])}",
                f"status: {row['status']}",
                "ch_id: null",
                "",
            ]
        )
        (out_dir / f"{row['id']}.yaml").write_text(content, encoding="utf-8")


def print_stats(rows: list[dict[str, object]]) -> None:
    print(f"Generated {len(rows)} slots.")
    bg_counts: dict[str, int] = {}
    for row in rows:
        key = row["background_type"]  # type: ignore[assignment]
        bg_counts[key] = bg_counts.get(key, 0) + 1
    print("Background distribution:")
    for key, _ in BACKGROUND_TARGETS_3600:
        print(f"  {key}: {bg_counts.get(key, 0)}")
    dorm_counts: dict[str, int] = {}
    for row in rows:
        key = row["dorm"]  # type: ignore[assignment]
        dorm_counts[key] = dorm_counts.get(key, 0) + 1
    print("Dorm distribution:")
    for key, _ in DORM_TARGETS_3600:
        print(f"  {key}: {dorm_counts.get(key, 0)}")
    for name, _, _ in TRAITS:
        values = [row["b5"][name] for row in rows]  # type: ignore[index]
        mean = statistics.mean(values)
        pstdev = statistics.pstdev(values)
        print(f"{name}: mean={mean:.3f}, std={pstdev:.3f}, min={min(values):.2f}, max={max(values):.2f}")


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    default_out_dir = repo_root / "worldbible_refined_bundle_20260303" / "population"
    default_csv = default_out_dir / "population_slots.csv"

    parser = argparse.ArgumentParser(description="Generate P-* population slots")
    parser.add_argument("--count", type=int, default=3600, help="Number of slots to generate")
    parser.add_argument("--seed", type=int, default=20260304, help="Random seed for reproducible output")
    parser.add_argument(
        "--format",
        choices=("yaml", "csv", "both"),
        default="both",
        help="Output format",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=default_out_dir,
        help="Output directory for YAML slot files",
    )
    parser.add_argument(
        "--csv-path",
        type=Path,
        default=default_csv,
        help="CSV output path",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing outputs",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.count <= 0:
        print("--count must be > 0", file=sys.stderr)
        return 2

    rows = build_rows(args.count, args.seed)

    if args.format in ("yaml", "both"):
        write_yaml_slots(rows, args.output_dir, args.force)
        print(f"YAML slots written to: {args.output_dir}")
    if args.format in ("csv", "both"):
        write_csv(rows, args.csv_path, args.force)
        print(f"CSV written to: {args.csv_path}")

    print_stats(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
