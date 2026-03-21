#!/usr/bin/env python3
"""Refresh canon README metadata, including current canon sha256."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Refresh canon README metadata.")
    parser.add_argument("episode_id", help="Episode id such as ep002")
    parser.add_argument(
        "--set-current-text-canon",
        help="Optionally replace current_text_canon before recomputing hash.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=repo_root,
        help="Repository root path.",
    )
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canon_payload_files(canon_dir: Path) -> list[Path]:
    return sorted(
        path for path in canon_dir.iterdir() if path.is_file() and path.name != "README.md"
    )


def replace_or_insert(lines: list[str], key: str, value: str, after_key: str | None = None) -> list[str]:
    target_prefix = f"- {key}:"
    new_line = f"- {key}: {value}"
    for index, line in enumerate(lines):
        if line.startswith(target_prefix):
            lines[index] = new_line
            return lines
    if after_key is not None:
        after_prefix = f"- {after_key}:"
        for index, line in enumerate(lines):
            if line.startswith(after_prefix):
                lines.insert(index + 1, new_line)
                return lines
    insert_at = 0
    for index, line in enumerate(lines):
        if line.startswith("## "):
            insert_at = index
            break
    lines.insert(insert_at, new_line)
    return lines


def main() -> int:
    args = parse_args()
    canon_readme = args.repo_root / "artifacts" / "writing" / "episodes" / args.episode_id / "canon" / "README.md"
    if not canon_readme.exists():
        raise SystemExit(f"missing canon README: {canon_readme}")

    lines = canon_readme.read_text(encoding="utf-8").splitlines()
    metadata: dict[str, str] = {}
    for line in lines:
        if line.startswith("- ") and ":" in line:
            key, value = line[2:].split(":", 1)
            metadata[key.strip()] = value.strip()

    if args.set_current_text_canon is not None:
        metadata["current_text_canon"] = args.set_current_text_canon
        lines = replace_or_insert(lines, "current_text_canon", args.set_current_text_canon)

    current_text_canon = metadata.get("current_text_canon", "none")
    current_word_canon = metadata.get("current_word_canon", "none")
    canon_files = canon_payload_files(canon_readme.parent)

    if current_word_canon not in ("", "none"):
        raise SystemExit(
            "single-file canon policy violation: current_word_canon must remain none"
        )

    if current_text_canon == "none":
        if canon_files:
            listed = ", ".join(path.name for path in canon_files)
            raise SystemExit(
                "single-file canon policy violation: current_text_canon is none but "
                f"canon/ contains files: {listed}"
            )
        canon_hash = "none"
    else:
        canon_path = canon_readme.parent / current_text_canon
        if not canon_path.exists():
            raise SystemExit(f"current_text_canon does not exist: {canon_path}")
        if len(canon_files) != 1 or canon_files[0].name != current_text_canon:
            listed = ", ".join(path.name for path in canon_files) or "(none)"
            raise SystemExit(
                "single-file canon policy violation: canon/ must contain exactly one "
                f"non-README file matching current_text_canon. found: {listed}"
            )
        canon_hash = sha256_file(canon_path)

    lines = replace_or_insert(
        lines,
        "current_text_canon_sha256",
        canon_hash,
        after_key="current_text_canon",
    )
    canon_readme.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"refreshed canon metadata: {canon_readme}")
    print(f"- current_text_canon: {current_text_canon}")
    print(f"- current_text_canon_sha256: {canon_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
