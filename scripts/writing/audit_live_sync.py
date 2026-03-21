#!/usr/bin/env python3
"""Audit canon-to-live document sync status."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


BULLET_RE = re.compile(r"^- ([a-z0-9_]+):\s*(.+?)\s*$")
EPISODE_RE = re.compile(r"^ep(\d+)")
SYNC_HEADER = "## Sync metadata"
REQUIRED_METADATA_KEYS = (
    "sync_category",
    "last_synced_episode",
    "sync_source",
    "sync_source_sha256",
    "sync_summary",
)


@dataclass(frozen=True)
class CanonSnapshot:
    episode_id: str
    canon_readme: Path
    canon_path: Path
    summary_path: Path
    canon_sha256: str
    readme_declared_sha256: str | None


@dataclass(frozen=True)
class ManifestEntry:
    category: str
    path: Path
    label: str
    description: str
    max_episode_lag: int | None = None


@dataclass(frozen=True)
class AuditResult:
    level: str
    entry: ManifestEntry
    message: str


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Audit canon -> live doc sync metadata.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=repo_root / "artifacts" / "writing" / "live_sync_manifest.json",
        help="Path to live sync manifest JSON.",
    )
    parser.add_argument(
        "--episode-id",
        help="Audit against a specific episode_id instead of the latest current canon.",
    )
    parser.add_argument(
        "--print-targets",
        action="store_true",
        help="Print manifest targets and exit without auditing document freshness.",
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


def episode_sort_key(episode_id: str) -> tuple[int, str]:
    match = EPISODE_RE.match(episode_id)
    if not match:
        raise ValueError(f"Unsupported episode id format: {episode_id}")
    return int(match.group(1)), episode_id


def read_sync_metadata(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    in_sync_section = False
    section_lines: list[str] = []
    for line in lines[:40]:
        stripped = line.strip()
        if stripped == SYNC_HEADER:
            in_sync_section = True
            continue
        if in_sync_section and stripped.startswith("## "):
            break
        if in_sync_section:
            section_lines.append(line)
    return parse_bullet_metadata(section_lines)


def read_canon_metadata(path: Path) -> dict[str, str]:
    return parse_bullet_metadata(path.read_text(encoding="utf-8").splitlines())


def discover_current_canons(repo_root: Path) -> list[CanonSnapshot]:
    episode_root = repo_root / "artifacts" / "writing" / "episodes"
    snapshots: list[CanonSnapshot] = []
    for readme in sorted(episode_root.glob("*/canon/README.md")):
        metadata = read_canon_metadata(readme)
        episode_id = metadata.get("episode_id")
        current_text_canon = metadata.get("current_text_canon")
        if not episode_id or not current_text_canon or current_text_canon == "none":
            continue
        canon_path = readme.parent / current_text_canon
        summary_path = readme.parent.parent / "summary_v1.md"
        canon_sha256 = sha256_file(canon_path) if canon_path.exists() else ""
        snapshots.append(
            CanonSnapshot(
                episode_id=episode_id,
                canon_readme=readme,
                canon_path=canon_path,
                summary_path=summary_path,
                canon_sha256=canon_sha256,
                readme_declared_sha256=metadata.get("current_text_canon_sha256"),
            )
        )
    return sorted(snapshots, key=lambda item: episode_sort_key(item.episode_id))


def load_manifest(path: Path) -> list[ManifestEntry]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    entries: list[ManifestEntry] = []
    for category in ("required", "conditional", "manual"):
        for item in raw.get(category, []):
            entries.append(
                ManifestEntry(
                    category=category,
                    path=Path(item["path"]),
                    label=item["label"],
                    description=item["description"],
                    max_episode_lag=item.get("max_episode_lag"),
                )
            )
    return entries


def resolve_target_snapshot(
    snapshots: list[CanonSnapshot], episode_id: str | None
) -> CanonSnapshot:
    if not snapshots:
        raise ValueError("No current canon snapshots found.")
    if episode_id is None:
        return snapshots[-1]
    for snapshot in snapshots:
        if snapshot.episode_id == episode_id:
            return snapshot
    raise ValueError(f"episode_id not found in current canon snapshots: {episode_id}")


def resolve_repo_path(repo_root: Path, raw_value: str) -> Path | None:
    value = strip_markdown(raw_value)
    if not value or value == "none":
        return None
    return repo_root / value


def classify_result(entry: ManifestEntry, lag: int) -> str:
    if lag < 0:
        return "fail"
    if entry.category == "required":
        return "ok" if lag == 0 else "fail"
    if entry.category == "conditional":
        if lag == 0:
            return "ok"
        if entry.max_episode_lag is not None and lag <= entry.max_episode_lag:
            return "warn"
        return "fail"
    return "ok" if lag == 0 else "info"


def audit_entry(
    repo_root: Path, target: CanonSnapshot, entry: ManifestEntry
) -> AuditResult:
    doc_path = repo_root / entry.path
    if not doc_path.exists():
        return AuditResult("fail", entry, f"missing file: {entry.path}")

    metadata = read_sync_metadata(doc_path)
    missing_keys = [key for key in REQUIRED_METADATA_KEYS if key not in metadata]
    if missing_keys:
        return AuditResult(
            "fail",
            entry,
            f"missing sync metadata keys: {', '.join(missing_keys)}",
        )

    if metadata["sync_category"] != entry.category:
        return AuditResult(
            "fail",
            entry,
            f"sync_category mismatch: doc={metadata['sync_category']} manifest={entry.category}",
        )

    try:
        target_index = episode_sort_key(target.episode_id)[0]
        synced_index = episode_sort_key(metadata["last_synced_episode"])[0]
    except ValueError as exc:
        return AuditResult("fail", entry, str(exc))

    lag = target_index - synced_index
    level = classify_result(entry, lag)

    sync_source = resolve_repo_path(repo_root, metadata["sync_source"])
    sync_summary = resolve_repo_path(repo_root, metadata["sync_summary"])

    if sync_source is None or not sync_source.exists():
        return AuditResult("fail", entry, f"sync_source missing or unreadable: {metadata['sync_source']}")
    if sync_summary is None or not sync_summary.exists():
        return AuditResult("fail", entry, f"sync_summary missing or unreadable: {metadata['sync_summary']}")
    if metadata["sync_source_sha256"] != target.canon_sha256:
        return AuditResult(
            "fail",
            entry,
            "sync_source_sha256 does not match current canon content",
        )

    if metadata["last_synced_episode"] not in metadata["sync_source"]:
        return AuditResult(
            "fail",
            entry,
            "sync_source path does not match last_synced_episode",
        )
    if metadata["last_synced_episode"] not in metadata["sync_summary"]:
        return AuditResult(
            "fail",
            entry,
            "sync_summary path does not match last_synced_episode",
        )

    if level == "ok":
        return AuditResult(
            level,
            entry,
            f"synced at {metadata['last_synced_episode']}",
        )
    if level == "warn":
        return AuditResult(
            level,
            entry,
            f"lag {lag} episode(s): last_synced_episode={metadata['last_synced_episode']}, allowed={entry.max_episode_lag}",
        )
    if level == "info":
        return AuditResult(
            level,
            entry,
            f"manual doc last checked at {metadata['last_synced_episode']}",
        )
    return AuditResult(
        level,
        entry,
        f"stale by {lag} episode(s): last_synced_episode={metadata['last_synced_episode']}, target={target.episode_id}",
    )


def precheck_target_snapshot(target: CanonSnapshot) -> list[str]:
    failures: list[str] = []
    if not target.canon_path.exists():
        failures.append(f"current_text_canon missing: {target.canon_path}")
        return failures
    canon_files = sorted(
        path.name
        for path in target.canon_readme.parent.iterdir()
        if path.is_file() and path.name != "README.md"
    )
    if canon_files != [target.canon_path.name]:
        failures.append(
            "single-file canon policy violation: "
            f"expected only {target.canon_path.name}, found {', '.join(canon_files) or '(none)'}"
        )
    metadata = read_canon_metadata(target.canon_readme)
    current_word_canon = metadata.get("current_word_canon", "none")
    if current_word_canon not in ("", "none"):
        failures.append("single-file canon policy violation: current_word_canon must be none")
    declared = target.readme_declared_sha256
    if not declared or declared == "none":
        failures.append("canon README missing current_text_canon_sha256")
    elif declared != target.canon_sha256:
        failures.append(
            "canon README hash mismatch: "
            f"declared={declared} actual={target.canon_sha256}"
        )
    return failures


def print_targets(entries: list[ManifestEntry]) -> None:
    current_category = None
    for entry in entries:
        if entry.category != current_category:
            current_category = entry.category
            print(f"{current_category}:")
        suffix = ""
        if entry.max_episode_lag is not None:
            suffix = f" (max_episode_lag={entry.max_episode_lag})"
        print(f"- {entry.path}{suffix}")
        print(f"  {entry.description}")


def render_results(target: CanonSnapshot, results: list[AuditResult], precheck_failures: list[str]) -> int:
    print(f"target_episode: {target.episode_id}")
    print(f"target_canon: {target.canon_path.relative_to(target.canon_readme.parents[3])}")
    print(f"target_summary: {target.summary_path.relative_to(target.canon_readme.parents[3])}")
    print(f"target_canon_sha256: {target.canon_sha256}")
    print()

    order = ("fail", "warn", "info", "ok")
    label_map = {"fail": "FAIL", "warn": "WARN", "info": "INFO", "ok": "OK"}
    counts = {key: 0 for key in order}
    for message in precheck_failures:
        counts["fail"] += 1
        print(f"[FAIL] Canon Registry: {message}")
    for result in results:
        counts[result.level] += 1
        print(
            f"[{label_map[result.level]}] {result.entry.label}: "
            f"{result.entry.path} :: {result.message}"
        )

    print()
    print(
        "summary: "
        f"{counts['ok']} ok, {counts['warn']} warn, {counts['info']} info, {counts['fail']} fail"
    )
    return 1 if counts["fail"] else 0


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    manifest_path = args.manifest
    entries = load_manifest(manifest_path)

    if args.print_targets:
        print_targets(entries)
        return 0

    snapshots = discover_current_canons(repo_root)
    target = resolve_target_snapshot(snapshots, args.episode_id)
    precheck_failures = precheck_target_snapshot(target)
    results = [audit_entry(repo_root, target, entry) for entry in entries]
    return render_results(target, results, precheck_failures)


if __name__ == "__main__":
    sys.exit(main())
