#!/usr/bin/env python3
"""Audit prompt packet freshness and basic readiness for an episode."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


BULLET_RE = re.compile(r"^- ([a-z0-9_]+):\s*(.+?)\s*$")
EPISODE_RE = re.compile(r"^ep(\d+)")
VERSIONED_FILE_RE = re.compile(r"^(?P<stem>.+)_v(?P<version>\d+)\.md$")
INJECTION_LINE_RE = re.compile(r"^\d+\.\s+`?(.+?)`?\s*$")
EMPTY_BULLET_RE = re.compile(r"^\s*-\s*$")
EMPTY_BACKTICK_BULLET_RE = re.compile(r"^\s*-\s*``\s*$")
UNRESOLVED_TOKEN_RE = re.compile(
    r"<(episode_id|recent_canon_[123](?:_sha256)?|anchor_[^>]+)>"
)
MEMORY_TIER_PATHS = (
    "world/live/docs/memory_tiers/recent.md",
    "world/live/docs/memory_tiers/current_arc.md",
    "world/live/docs/memory_tiers/entity_registry.md",
    "world/live/docs/memory_tiers/long_term.md",
)


@dataclass(frozen=True)
class CanonSnapshot:
    episode_id: str
    canon_path: Path
    canon_sha256: str


@dataclass(frozen=True)
class AuditMessage:
    level: str
    label: str
    message: str


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Audit prompt packet freshness.")
    parser.add_argument("episode_id", help="Episode id such as ep003")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=repo_root,
        help="Repository root path.",
    )
    parser.add_argument(
        "--strict-ready",
        action="store_true",
        help="Treat readiness warnings as failures.",
    )
    return parser.parse_args()


def strip_markdown(value: str) -> str:
    value = value.strip()
    if value.startswith("`") and value.endswith("`"):
        return value[1:-1]
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_bullet_metadata(lines: list[str]) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in lines:
        match = BULLET_RE.match(line.strip())
        if not match:
            continue
        key, value = match.groups()
        metadata[key] = strip_markdown(value)
    return metadata


def read_bullet_metadata(path: Path, limit: int = 20) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    return parse_bullet_metadata(lines[:limit])


def episode_sort_key(episode_id: str) -> int:
    match = EPISODE_RE.match(episode_id)
    if not match:
        raise ValueError(f"unsupported episode id format: {episode_id}")
    return int(match.group(1))


def discover_current_canons(repo_root: Path) -> list[CanonSnapshot]:
    snapshots: list[CanonSnapshot] = []
    for readme in sorted((repo_root / "artifacts" / "writing" / "episodes").glob("*/canon/README.md")):
        metadata = read_bullet_metadata(readme, limit=20)
        episode_id = metadata.get("episode_id")
        current_text_canon = metadata.get("current_text_canon")
        if not episode_id or not current_text_canon or current_text_canon == "none":
            continue
        canon_path = readme.parent / current_text_canon
        if not canon_path.exists():
            continue
        snapshots.append(
            CanonSnapshot(
                episode_id=episode_id,
                canon_path=canon_path,
                canon_sha256=sha256_file(canon_path),
            )
        )
    return sorted(snapshots, key=lambda item: episode_sort_key(item.episode_id))


def expected_recent_canons(repo_root: Path, episode_id: str, limit: int = 3) -> list[CanonSnapshot]:
    target_index = episode_sort_key(episode_id)
    candidates = [item for item in discover_current_canons(repo_root) if episode_sort_key(item.episode_id) < target_index]
    return list(reversed(candidates))[:limit]


def find_latest_versioned_file(episode_dir: Path, stem: str) -> Path | None:
    best_path: Path | None = None
    best_version = -1
    for path in episode_dir.glob(f"{stem}_v*.md"):
        match = VERSIONED_FILE_RE.match(path.name)
        if not match or match.group("stem") != stem:
            continue
        version = int(match.group("version"))
        if version > best_version:
            best_version = version
            best_path = path
    return best_path


def extract_section_lines(path: Path, heading: str) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    target = f"## {heading}"
    collecting = False
    collected: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped == target:
            collecting = True
            continue
        if collecting and stripped.startswith("## "):
            break
        if collecting:
            collected.append(line)
    return collected


def extract_injection_items(path: Path) -> list[str]:
    section_lines = extract_section_lines(path, "Injection order")
    items: list[str] = []
    for line in section_lines:
        match = INJECTION_LINE_RE.match(line.strip())
        if not match:
            continue
        raw_item = strip_markdown(match.group(1))
        if raw_item == "none":
            continue
        items.append(raw_item)
    return items


def find_placeholder_lines(path: Path) -> list[int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    flagged: list[int] = []
    for index, line in enumerate(lines, start=1):
        stripped = line.rstrip("\n")
        if EMPTY_BULLET_RE.match(stripped):
            flagged.append(index)
            continue
        if EMPTY_BACKTICK_BULLET_RE.match(stripped):
            flagged.append(index)
            continue
        if UNRESOLVED_TOKEN_RE.search(stripped):
            flagged.append(index)
            continue
        if is_empty_table_row(stripped):
            flagged.append(index)
            continue
    return flagged


def is_empty_table_row(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return False
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    return len(cells) >= 2 and all(not cell for cell in cells)


def audit_packet_metadata(
    repo_root: Path,
    packet_file: Path,
    episode_id: str,
    required_docs: dict[str, Path | None],
) -> list[AuditMessage]:
    messages: list[AuditMessage] = []
    metadata = read_bullet_metadata(packet_file, limit=20)
    expected = expected_recent_canons(repo_root, episode_id)
    expected_paths = [str(item.canon_path.relative_to(repo_root)) for item in expected]
    expected_hashes = [item.canon_sha256 for item in expected]
    while len(expected_paths) < 3:
        expected_paths.append("none")
        expected_hashes.append("none")

    for slot in range(1, 4):
        path_key = f"recent_canon_{slot}_path"
        hash_key = f"recent_canon_{slot}_sha256"
        actual_path = metadata.get(path_key)
        actual_hash = metadata.get(hash_key)
        expected_path = expected_paths[slot - 1]
        expected_hash = expected_hashes[slot - 1]

        if actual_path is None:
            messages.append(AuditMessage("fail", "Prompt Packet", f"missing metadata key: {path_key}"))
            continue
        if actual_hash is None:
            messages.append(AuditMessage("fail", "Prompt Packet", f"missing metadata key: {hash_key}"))
            continue
        if actual_path != expected_path:
            messages.append(
                AuditMessage(
                    "fail",
                    "Prompt Packet",
                    f"{path_key} mismatch: actual={actual_path} expected={expected_path}",
                )
            )
            continue
        if actual_hash != expected_hash:
            messages.append(
                AuditMessage(
                    "fail",
                    "Prompt Packet",
                    f"{hash_key} mismatch: actual={actual_hash} expected={expected_hash}",
                )
            )
            continue
        messages.append(AuditMessage("ok", "Prompt Packet", f"{path_key} synced"))

    for memory_path in MEMORY_TIER_PATHS:
        if not (repo_root / memory_path).exists():
            messages.append(
                AuditMessage("fail", "Prompt Packet", f"missing memory tier doc: {memory_path}")
            )

    style_file = required_docs["Episode Style Constitution"]
    setting_file = required_docs["Setting Brief"]
    long_range_file = required_docs["Long Range Summary"]
    prompt_file = required_docs["Writing Prompt"]

    expected_injection_order: list[str] = []
    if style_file is not None:
        expected_injection_order.append(style_file.name)
    if setting_file is not None:
        expected_injection_order.append(setting_file.name)
    expected_injection_order.extend(path for path in expected_paths if path != "none")
    expected_injection_order.extend(MEMORY_TIER_PATHS)
    if long_range_file is not None:
        expected_injection_order.append(long_range_file.name)
    if prompt_file is not None:
        expected_injection_order.append(prompt_file.name)

    actual_injection_items = extract_injection_items(packet_file)
    if actual_injection_items != expected_injection_order:
        messages.append(
            AuditMessage(
                "fail",
                "Prompt Packet",
                "Injection order does not match expected raw canon + memory tier + local doc sequence",
            )
        )
    else:
        messages.append(AuditMessage("ok", "Prompt Packet", "Injection order synced"))

    return messages


def audit_readiness(label: str, path: Path) -> AuditMessage | None:
    placeholder_lines = find_placeholder_lines(path)
    if not placeholder_lines:
        return None
    preview = ", ".join(str(line) for line in placeholder_lines[:6])
    suffix = "" if len(placeholder_lines) <= 6 else ", ..."
    return AuditMessage("warn", label, f"placeholder content remains at lines: {preview}{suffix}")


def render(messages: list[AuditMessage], strict_ready: bool) -> int:
    order = ("fail", "warn", "ok")
    counts = {key: 0 for key in order}
    for message in messages:
        counts[message.level] += 1
        label = message.level.upper()
        print(f"[{label}] {message.label}: {message.message}")

    print()
    print(f"summary: {counts['ok']} ok, {counts['warn']} warn, {counts['fail']} fail")
    if counts["fail"]:
        return 1
    if strict_ready and counts["warn"]:
        return 1
    return 0


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root
    episode_dir = repo_root / "artifacts" / "writing" / "episodes" / args.episode_id
    if not episode_dir.exists():
        raise SystemExit(f"missing episode directory: {episode_dir}")

    required_docs = {
        "Style Selection": find_latest_versioned_file(episode_dir, "style_selection"),
        "Episode Style Constitution": find_latest_versioned_file(episode_dir, "episode_style_constitution"),
        "Setting Brief": find_latest_versioned_file(episode_dir, "setting_brief"),
        "Long Range Summary": find_latest_versioned_file(episode_dir, "long_range_summary"),
        "Prompt Packet": find_latest_versioned_file(episode_dir, "prompt_packet"),
        "Writing Prompt": find_latest_versioned_file(episode_dir, "prompt"),
    }

    messages: list[AuditMessage] = []
    for label, path in required_docs.items():
        if path is None:
            messages.append(AuditMessage("fail", label, "missing versioned file"))
        else:
            messages.append(AuditMessage("ok", label, f"found {path.name}"))

    prompt_packet = required_docs["Prompt Packet"]
    if prompt_packet is not None:
        messages.extend(audit_packet_metadata(repo_root, prompt_packet, args.episode_id, required_docs))

    for label in ("Episode Style Constitution", "Setting Brief", "Long Range Summary", "Prompt Packet", "Writing Prompt"):
        path = required_docs[label]
        if path is None:
            continue
        readiness_message = audit_readiness(label, path)
        if readiness_message is not None:
            messages.append(readiness_message)

    return render(messages, args.strict_ready)


if __name__ == "__main__":
    sys.exit(main())
