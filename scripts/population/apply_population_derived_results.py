#!/usr/bin/env python3
"""Apply Batch derive results (DT/NFC/SM) to population YAML/CSV.

Expected input:
- Batch output JSONL with custom_id like derive-P-0001.
- Supports multiple output shapes from responses/chat-completions wrappers.

Updates:
- world/live/population/P-*.yaml (derived block)
- world/live/population/population_slots.csv (DT/NFC/SM columns)
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import sys
from pathlib import Path


DERIVED_KEYS = ("DT", "NFC", "SM")
ID_PATTERN = re.compile(r"^derive-(P-\d{4})$")


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    default_population_dir = repo_root / "world/live" / "population"
    default_csv = default_population_dir / "population_slots.csv"
    default_failed = repo_root / "artifacts" / "batch" / "population_derive_failed_ids.txt"
    parser = argparse.ArgumentParser(description="Apply population derive batch results")
    parser.add_argument("--batch-output-jsonl", type=Path, required=True, help="Batch output JSONL path")
    parser.add_argument("--population-dir", type=Path, default=default_population_dir, help="Population YAML dir")
    parser.add_argument("--csv-path", type=Path, default=default_csv, help="Population CSV path")
    parser.add_argument(
        "--failed-out",
        type=Path,
        default=default_failed,
        help="Output txt for failed/missing IDs",
    )
    parser.add_argument("--strict", action="store_true", help="Fail if any line cannot be applied")
    return parser.parse_args()


def clip01(value: float) -> float:
    return max(0.01, min(0.99, value))


def q2(value: float) -> float:
    return float(f"{clip01(value):.2f}")


def extract_custom_id(line_obj: dict[str, object]) -> str | None:
    raw = line_obj.get("custom_id")
    if isinstance(raw, str):
        return raw
    return None


def extract_text_candidates(obj: object, out: list[str]) -> None:
    if isinstance(obj, str):
        out.append(obj)
        return
    if isinstance(obj, dict):
        for key in ("output_text", "text", "content"):
            if key in obj:
                extract_text_candidates(obj[key], out)
        for v in obj.values():
            extract_text_candidates(v, out)
        return
    if isinstance(obj, list):
        for item in obj:
            extract_text_candidates(item, out)


def find_json_object(text: str) -> dict[str, object] | None:
    text = text.strip()
    if not text:
        return None
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        candidate = text[start : end + 1]
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            return None
    return None


def extract_payload(line_obj: dict[str, object]) -> dict[str, object] | None:
    # 1) direct object with derived.
    if "derived" in line_obj:
        return line_obj

    # 2) body object in batch output.
    response = line_obj.get("response")
    if isinstance(response, dict):
        body = response.get("body")
        if isinstance(body, dict) and "derived" in body:
            return body

        # Gather candidate text fields recursively, then parse as JSON.
        candidates: list[str] = []
        extract_text_candidates(body, candidates)
        extract_text_candidates(response, candidates)
        for text in candidates:
            parsed = find_json_object(text)
            if parsed and "derived" in parsed:
                return parsed

    # 3) fallback: search entire line object for JSON text that contains derived.
    candidates = []
    extract_text_candidates(line_obj, candidates)
    for text in candidates:
        parsed = find_json_object(text)
        if parsed and "derived" in parsed:
            return parsed
    return None


def parse_pid(custom_id: str, payload: dict[str, object]) -> str | None:
    m = ID_PATTERN.match(custom_id)
    if m:
        return m.group(1)
    raw_id = payload.get("id")
    if isinstance(raw_id, str) and re.match(r"^P-\d{4}$", raw_id):
        return raw_id
    return None


def parse_derived(payload: dict[str, object]) -> dict[str, float] | None:
    raw = payload.get("derived")
    if not isinstance(raw, dict):
        return None
    out: dict[str, float] = {}
    for k in DERIVED_KEYS:
        v = raw.get(k)
        try:
            out[k] = q2(float(v))  # type: ignore[arg-type]
        except (TypeError, ValueError):
            return None
    return out


def update_yaml_slot(path: Path, derived: dict[str, float]) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    replacement = (
        "derived:\n"
        f"  DT: {derived['DT']:.2f}\n"
        f"  NFC: {derived['NFC']:.2f}\n"
        f"  SM: {derived['SM']:.2f}\n"
    )
    pattern = re.compile(r"(?ms)^derived:\n(?:[ \t].*\n)+")
    if pattern.search(text):
        text = pattern.sub(replacement, text, count=1)
    else:
        text += "\n" + replacement
    path.write_text(text, encoding="utf-8")


def update_csv(csv_path: Path, derived_map: dict[str, dict[str, float]]) -> tuple[int, int]:
    if not csv_path.is_file():
        raise FileNotFoundError(csv_path)
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    required_cols = ["id", "DT", "NFC", "SM"]
    for col in required_cols:
        if col not in fieldnames:
            fieldnames.append(col)

    applied = 0
    missing = 0
    for row in rows:
        pid = row.get("id", "")
        d = derived_map.get(pid)
        if d is None:
            missing += 1
            continue
        row["DT"] = f"{d['DT']:.2f}"
        row["NFC"] = f"{d['NFC']:.2f}"
        row["SM"] = f"{d['SM']:.2f}"
        applied += 1

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return applied, missing


def print_stats(derived_map: dict[str, dict[str, float]]) -> None:
    if not derived_map:
        print("No derived values to summarize.")
        return
    print(f"applied_ids={len(derived_map)}")
    for key in DERIVED_KEYS:
        values = [v[key] for v in derived_map.values()]
        print(
            f"{key}: mean={statistics.mean(values):.3f}, std={statistics.pstdev(values):.3f}, "
            f"min={min(values):.2f}, max={max(values):.2f}"
        )


def main() -> int:
    args = parse_args()
    if not args.batch_output_jsonl.is_file():
        print(f"Batch output not found: {args.batch_output_jsonl}", file=sys.stderr)
        return 2

    derived_map: dict[str, dict[str, float]] = {}
    failed: list[str] = []

    with args.batch_output_jsonl.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                failed.append(f"line:{line_no}:invalid_json")
                continue
            if not isinstance(obj, dict):
                failed.append(f"line:{line_no}:not_object")
                continue

            custom_id = extract_custom_id(obj)
            if not custom_id:
                failed.append(f"line:{line_no}:missing_custom_id")
                continue

            payload = extract_payload(obj)
            if payload is None:
                failed.append(f"{custom_id}:payload_not_found")
                continue

            pid = parse_pid(custom_id, payload)
            if not pid:
                failed.append(f"{custom_id}:invalid_pid")
                continue

            derived = parse_derived(payload)
            if derived is None:
                failed.append(f"{custom_id}:invalid_derived")
                continue

            derived_map[pid] = derived

    # Update YAML slots.
    yaml_missing = 0
    for pid, derived in derived_map.items():
        yaml_path = args.population_dir / f"{pid}.yaml"
        if not yaml_path.is_file():
            failed.append(f"{pid}:yaml_missing")
            yaml_missing += 1
            continue
        update_yaml_slot(yaml_path, derived)

    csv_applied, csv_missing = update_csv(args.csv_path, derived_map)

    # Write failed ids/reasons.
    args.failed_out.parent.mkdir(parents=True, exist_ok=True)
    with args.failed_out.open("w", encoding="utf-8") as f:
        for item in failed:
            f.write(item + "\n")

    print(f"parsed_ids={len(derived_map)}")
    print(f"yaml_missing={yaml_missing}")
    print(f"csv_applied={csv_applied}")
    print(f"csv_missing={csv_missing}")
    print(f"failed_count={len(failed)}")
    print(f"failed_out={args.failed_out}")
    print_stats(derived_map)

    if args.strict and failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
