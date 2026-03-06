#!/usr/bin/env python3
"""Build Batch JSONL requests for population derive (DT/NFC/SM).

Input:
- population CSV with columns: id, background_type, O, C, E, A, N, ...

Output:
- JSONL file where each line is a batch request payload using /v1/responses.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


DEFAULT_SYSTEM_PROMPT = """You are a deterministic trait-derivation engine.
Task: derive DT, NFC, SM from Big5 values using the provided formulas.
Rules:
1) Keep all outputs in [0.01, 0.99].
2) Return numeric values with 2 decimals.
3) Include intermediate values (base, residual, clipped) for auditability.
4) Preserve the input id exactly.
5) Output JSON only (no prose)."""


USER_PROMPT_TEMPLATE = """[INPUT]
id: {id}
b5:
  O: {O}
  C: {C}
  E: {E}
  A: {A}
  N: {N}

[FORMULAS]
DT_base  = -0.50*A - 0.35*C + 0.25*N + 0.20*E - 0.05*O
NFC_base =  0.45*O + 0.30*C - 0.15*N + 0.05*E + 0.05*A
SM_base  =  0.40*E + 0.15*O + 0.10*A - 0.10*C - 0.20*N

[RESIDUAL POLICY]
- Draw residual-like offsets for diversity, but keep them small:
  eps_DT  in [-0.45, 0.45]  (target sigma ~0.15)
  eps_NFC in [-0.36, 0.36]  (target sigma ~0.12)
  eps_SM  in [-0.39, 0.39]  (target sigma ~0.13)
- If uncertain, use 0.00.

[POST PROCESS]
DT  = clip(DT_base  + eps_DT ,  0.01, 0.99)
NFC = clip(NFC_base + eps_NFC,  0.01, 0.99)
SM  = clip(SM_base  + eps_SM ,  0.01, 0.99)

[OUTPUT SCHEMA]
{{
  "id": "{id}",
  "b5": {{ "O": {O}, "C": {C}, "E": {E}, "A": {A}, "N": {N} }},
  "calc": {{
    "DT_base": 0.00,
    "NFC_base": 0.00,
    "SM_base": 0.00,
    "eps_DT": 0.00,
    "eps_NFC": 0.00,
    "eps_SM": 0.00
  }},
  "derived": {{ "DT": 0.01, "NFC": 0.01, "SM": 0.01 }}
}}"""


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    default_csv = repo_root / "world/live" / "population" / "population_slots.csv"
    default_out = repo_root / "artifacts" / "batch" / "population_derive_requests.jsonl"
    parser = argparse.ArgumentParser(description="Build population derive batch JSONL")
    parser.add_argument("--csv-path", type=Path, default=default_csv, help="Input population CSV path")
    parser.add_argument("--out-jsonl", type=Path, default=default_out, help="Output JSONL path")
    parser.add_argument("--model", default="gpt-5-mini", help="Model name for requests")
    parser.add_argument("--url", default="/v1/responses", help="Batch request URL")
    parser.add_argument("--system-prompt-file", type=Path, help="Optional file to override default system prompt")
    parser.add_argument("--limit", type=int, help="Optional max rows to export")
    parser.add_argument("--force", action="store_true", help="Overwrite output if exists")
    return parser.parse_args()


def load_system_prompt(path: Path | None) -> str:
    if path is None:
        return DEFAULT_SYSTEM_PROMPT
    return path.read_text(encoding="utf-8").strip()


def as_two_decimals(raw: str) -> str:
    # Keep JSON numbers stable and compact for prompts.
    return f"{float(raw):.2f}"


def build_request_line(row: dict[str, str], model: str, url: str, system_prompt: str) -> dict[str, object]:
    user_prompt = USER_PROMPT_TEMPLATE.format(
        id=row["id"],
        O=as_two_decimals(row["O"]),
        C=as_two_decimals(row["C"]),
        E=as_two_decimals(row["E"]),
        A=as_two_decimals(row["A"]),
        N=as_two_decimals(row["N"]),
    )
    return {
        "custom_id": f"derive-{row['id']}",
        "method": "POST",
        "url": url,
        "body": {
            "model": model,
            "input": [
                {"role": "system", "content": [{"type": "input_text", "text": system_prompt}]},
                {"role": "user", "content": [{"type": "input_text", "text": user_prompt}]},
            ],
            "response_format": {"type": "json_object"},
        },
    }


def main() -> int:
    args = parse_args()
    if not args.csv_path.is_file():
        print(f"CSV not found: {args.csv_path}", file=sys.stderr)
        return 2

    if args.out_jsonl.exists() and not args.force:
        print(f"Output exists: {args.out_jsonl} (use --force)", file=sys.stderr)
        return 2

    system_prompt = load_system_prompt(args.system_prompt_file)
    args.out_jsonl.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with args.csv_path.open(newline="", encoding="utf-8") as src, args.out_jsonl.open(
        "w", encoding="utf-8"
    ) as dst:
        reader = csv.DictReader(src)
        required = {"id", "O", "C", "E", "A", "N"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            print(
                f"CSV missing required columns. Need: {sorted(required)}. Got: {reader.fieldnames}",
                file=sys.stderr,
            )
            return 2

        for row in reader:
            if args.limit is not None and count >= args.limit:
                break
            line = build_request_line(row, args.model, args.url, system_prompt)
            dst.write(json.dumps(line, ensure_ascii=False) + "\n")
            count += 1

    print(f"requests_written={count}")
    print(f"out_jsonl={args.out_jsonl}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
