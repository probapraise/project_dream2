#!/usr/bin/env python3
"""Audit semantic continuity between the latest live semantic layer and next-episode packet docs.

Severity policy:
- fail: explicit contradiction in knowledge/access/state that should block draft generation
- warn: carry loss, handoff omission, open-promise fade, placeholders, or likely drift
- info: scope/context notes only
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


BULLET_RE = re.compile(r"^- ([a-z0-9_]+):\s*(.+?)\s*$")
VERSIONED_FILE_RE = re.compile(r"^(?P<stem>.+)_v(?P<version>\d+)\.md$")
EPISODE_RE = re.compile(r"^ep(\d+)")
EMPTY_BULLET_RE = re.compile(r"^\s*-\s*$")
EMPTY_BACKTICK_BULLET_RE = re.compile(r"^\s*-\s*``\s*$")
UNRESOLVED_TOKEN_RE = re.compile(
    r"<(episode_id|recent_canon_[123](?:_sha256)?|anchor_[^>]+)>"
)
TOP_LEVEL_FIELD_RE = re.compile(r"^- ([^:]+):\s*(.+?)\s*$")
SECTION_HEADING_RE = re.compile(r"^## (.+)$")
META_ANCHOR_RE = re.compile(r"^(?:ep\d+(?:_prologue)?|ARC-\d+|FS-\d+)$")
STOPWORD_TERMS = {
    "type",
    "status",
    "open",
    "window",
    "carry",
    "latest",
    "linked",
    "arcs",
    "narrative",
    "function",
    "immediate",
    "promise",
    "threat",
    "emotional",
    "system",
    "false",
    "relief",
    "long",
    "horizon",
    "current",
    "next",
    "likely",
    "move",
    "있는",
    "하는",
    "이다",
    "지금",
    "현재",
    "단계",
    "구조",
    "장치",
    "기능",
    "상태",
}
TARGET_NEGATION_MARKERS = (
    "안 된다",
    "않는다",
    "않아야",
    "금지",
    "드러나면 안",
    "모르면 안",
    "피해야",
)
TIME_SKIP_PATTERNS = (
    re.compile(r"며칠 뒤"),
    re.compile(r"몇 날 뒤"),
    re.compile(r"몇 주 뒤"),
    re.compile(r"몇 달 뒤"),
    re.compile(r"오랜 시간이 지난"),
    re.compile(r"한참 뒤"),
    re.compile(r"입학 후"),
    re.compile(r"아카데미.*들어간 뒤"),
)


@dataclass(frozen=True)
class CanonSnapshot:
    episode_id: str
    canon_path: Path


@dataclass(frozen=True)
class Evidence:
    path: Path | None
    line_no: int | None
    text: str

    def render(self) -> str:
        if self.path is None:
            return self.text
        return f"{self.path}:{self.line_no}: {self.text}"


@dataclass(frozen=True)
class Finding:
    level: str
    category: str
    subject: str
    summary: str
    evidence_a: Evidence
    evidence_b: Evidence


@dataclass(frozen=True)
class SectionBlock:
    identifier: str
    title: str
    start_line: int
    heading_text: str
    fields: dict[str, tuple[str, int]]
    lines: list[tuple[int, str]]


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Audit semantic continuity.")
    parser.add_argument("episode_id", help="Target next episode id such as ep003")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=repo_root,
        help="Repository root path.",
    )
    parser.add_argument(
        "--strict-warn",
        action="store_true",
        help="Treat warnings as failures. Default mode only fails on hard contradictions.",
    )
    return parser.parse_args()


def strip_markdown(value: str) -> str:
    value = value.strip()
    if value.startswith("`") and value.endswith("`"):
        return value[1:-1]
    return value


def episode_sort_key(episode_id: str) -> int:
    match = EPISODE_RE.match(episode_id)
    if not match:
        raise ValueError(f"unsupported episode id format: {episode_id}")
    return int(match.group(1))


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
        snapshots.append(CanonSnapshot(episode_id=episode_id, canon_path=canon_path))
    return sorted(snapshots, key=lambda item: episode_sort_key(item.episode_id))


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


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def extract_section_lines(path: Path, heading: str) -> list[tuple[int, str]]:
    lines = read_lines(path)
    target = f"## {heading}"
    collecting = False
    collected: list[tuple[int, str]] = []
    for index, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped == target:
            collecting = True
            continue
        if collecting and stripped.startswith("## "):
            break
        if collecting:
            collected.append((index, line))
    return collected


def parse_section_blocks(path: Path, prefix: str) -> list[SectionBlock]:
    lines = read_lines(path)
    blocks: list[SectionBlock] = []
    current_heading: tuple[int, str] | None = None
    current_lines: list[tuple[int, str]] = []

    def flush() -> None:
        nonlocal current_heading, current_lines
        if current_heading is None:
            return
        line_no, heading_text = current_heading
        identifier, _, title = heading_text[4:].partition(" ")
        fields: dict[str, tuple[str, int]] = {}
        for entry_line_no, entry in current_lines:
            match = TOP_LEVEL_FIELD_RE.match(entry.strip())
            if not match:
                continue
            key, value = match.groups()
            fields[key.strip()] = (strip_markdown(value), entry_line_no)
        blocks.append(
            SectionBlock(
                identifier=identifier.strip(),
                title=title.strip(),
                start_line=line_no,
                heading_text=heading_text,
                fields=fields,
                lines=current_lines[:],
            )
        )
        current_heading = None
        current_lines = []

    for index, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith(prefix):
            flush()
            current_heading = (index, stripped)
            continue
        if current_heading is not None:
            if stripped.startswith("### ") or stripped.startswith("## "):
                flush()
                if stripped.startswith(prefix):
                    current_heading = (index, stripped)
                continue
            current_lines.append((index, line))
    flush()
    return blocks


def parse_character_blocks(path: Path) -> dict[str, list[tuple[int, str]]]:
    section_lines = extract_section_lines(path, "Active characters and knowledge states")
    blocks: dict[str, list[tuple[int, str]]] = {}
    current_name: str | None = None
    current_lines: list[tuple[int, str]] = []

    def flush() -> None:
        nonlocal current_name, current_lines
        if current_name is not None:
            blocks[current_name] = current_lines[:]
        current_name = None
        current_lines = []

    for line_no, line in section_lines:
        stripped = line.strip()
        if stripped.startswith("- ") and stripped.endswith(":") and not line.startswith("  "):
            flush()
            current_name = stripped[2:-1].strip()
            continue
        if current_name is not None:
            current_lines.append((line_no, line))
    flush()
    return blocks


def find_placeholder_lines(path: Path) -> list[int]:
    flagged: list[int] = []
    for index, line in enumerate(read_lines(path), start=1):
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


def normalize_anchor(term: str) -> str:
    normalized = term.strip("`'\"[](){}.,:;!?/ ")
    for suffix in ("으로", "에게", "에서", "까지", "부터", "처럼", "이다", "한다", "되는", "되는가", "였다", "한다", "의", "은", "는", "이", "가", "을", "를", "과", "와", "도", "만", "로"):
        if normalized.endswith(suffix) and len(normalized) > len(suffix) + 1:
            normalized = normalized[: -len(suffix)]
            break
    return normalized


def extract_anchor_phrases(text: str) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()
    for phrase in re.findall(r"`([^`]+)`", text):
        cleaned = normalize_anchor(phrase)
        if len(cleaned) >= 2 and cleaned not in seen and not META_ANCHOR_RE.match(cleaned):
            anchors.append(cleaned)
            seen.add(cleaned)
    for term in re.findall(r"[A-Za-z0-9가-힣]{2,}", text):
        cleaned = normalize_anchor(term)
        if len(cleaned) < 2 or cleaned in STOPWORD_TERMS or META_ANCHOR_RE.match(cleaned):
            continue
        if cleaned not in seen:
            anchors.append(cleaned)
            seen.add(cleaned)
    return anchors[:8]


def extract_priority_anchors(text: str, fallback_text: str = "") -> list[str]:
    backtick_only = [normalize_anchor(phrase) for phrase in re.findall(r"`([^`]+)`", text)]
    backtick_only = [
        phrase
        for phrase in backtick_only
        if len(phrase) >= 2 and not META_ANCHOR_RE.match(phrase)
    ]
    if backtick_only:
        deduped: list[str] = []
        seen: set[str] = set()
        for phrase in backtick_only:
            if phrase in seen:
                continue
            deduped.append(phrase)
            seen.add(phrase)
        return deduped[:6]
    return extract_anchor_phrases(fallback_text or text)


def first_match(
    paths: list[Path],
    patterns: list[re.Pattern[str]],
    ignore_markers: tuple[str, ...] = (),
) -> Evidence | None:
    for path in paths:
        for line_no, line in enumerate(read_lines(path), start=1):
            if ignore_markers and any(marker in line for marker in ignore_markers):
                continue
            for pattern in patterns:
                if pattern.search(line):
                    return Evidence(path, line_no, line.strip())
    return None


def presence_in_target_docs(target_docs: list[Path], anchors: list[str]) -> bool:
    text = "\n".join(path.read_text(encoding="utf-8") for path in target_docs)
    return any(anchor in text for anchor in anchors)


def make_absence_evidence(paths: list[Path], message: str) -> Evidence:
    names = ", ".join(path.name for path in paths)
    return Evidence(None, None, f"searched [{names}] -> {message}")


def build_target_docs(episode_dir: Path) -> dict[str, Path | None]:
    return {
        "setting_brief": find_latest_versioned_file(episode_dir, "setting_brief"),
        "prompt": find_latest_versioned_file(episode_dir, "prompt"),
        "long_range_summary": find_latest_versioned_file(episode_dir, "long_range_summary"),
    }


def add_placeholder_warnings(findings: list[Finding], target_docs: dict[str, Path | None]) -> None:
    for label, path in target_docs.items():
        if path is None:
            continue
        placeholder_lines = find_placeholder_lines(path)
        if not placeholder_lines:
            continue
        preview = ", ".join(str(line) for line in placeholder_lines[:6])
        suffix = "" if len(placeholder_lines) <= 6 else ", ..."
        findings.append(
            Finding(
                "warn",
                "Readiness",
                path.name,
                f"placeholder content remains at lines: {preview}{suffix}",
                Evidence(path, placeholder_lines[0], "placeholder or unresolved template token"),
                make_absence_evidence([path], "semantic checks may be incomplete until placeholders are filled"),
            )
        )


def knowledge_guard_findings(
    base_setting_brief: Path | None,
    target_paths: list[Path],
) -> list[Finding]:
    findings: list[Finding] = []
    if base_setting_brief is None or not base_setting_brief.exists():
        return findings

    character_blocks = parse_character_blocks(base_setting_brief)
    hidden_topics = ("정체", "빙의", "전생", "위장", "시험 구조")
    know_terms = ("알고", "안다", "눈치챘", "간파", "확신", "파악")

    for name, lines in character_blocks.items():
        guard_line: tuple[int, str] | None = None
        topics: list[str] = []
        for line_no, line in lines:
            if "모른" in line or "알지 못" in line or "드러나면 안" in line:
                matched_topics = [topic for topic in hidden_topics if topic in line]
                if matched_topics:
                    guard_line = (line_no, line.strip())
                    topics = matched_topics
                    break
        if guard_line is None or not topics:
            continue

        patterns = [
            re.compile(
                rf"{re.escape(name)}.{{0,40}}(?:{'|'.join(re.escape(topic) for topic in topics)}).{{0,20}}(?:{'|'.join(know_terms)})"
            ),
            re.compile(
                rf"(?:{'|'.join(re.escape(topic) for topic in topics)}).{{0,20}}{re.escape(name)}.{{0,20}}(?:{'|'.join(know_terms)})"
            ),
        ]
        target_evidence = first_match(target_paths, patterns, ignore_markers=TARGET_NEGATION_MARKERS)
        if target_evidence is None:
            continue
        findings.append(
            Finding(
                "fail",
                "Knowledge",
                name,
                "target episode docs leak a fact that the base episode marks as still unknown",
                Evidence(base_setting_brief, guard_line[0], guard_line[1]),
                target_evidence,
            )
        )
    return findings


def calion_certainty_findings(entity_registry: Path, target_paths: list[Path]) -> list[Finding]:
    live_evidence = first_match(
        [entity_registry],
        [re.compile(r"칼리온.*의심 중"), re.compile(r"current read on Kirion:.*의심 중")],
    )
    if live_evidence is None:
        return []

    target_evidence = first_match(
        target_paths,
        [
            re.compile(r"칼리온.{0,40}(정체|빙의|전생|위장).{0,20}(알고 있|안다|확신|간파|파악)"),
            re.compile(r"칼리온.{0,30}(이미|벌써).{0,20}(알고 있|안다|확신)"),
            re.compile(r"(정체|빙의|전생).{0,20}칼리온.{0,20}(알고 있|안다|확신|간파|파악)"),
        ],
        ignore_markers=TARGET_NEGATION_MARKERS,
    )
    if target_evidence is None:
        return []
    return [
        Finding(
            "fail",
            "Knowledge",
            "칼리온",
            "target episode docs jump 칼리온 from suspicion to certainty without intervening canon evidence",
            live_evidence,
            target_evidence,
        )
    ]


def access_rights_findings(
    recent_doc: Path,
    entity_registry: Path,
    episode_deltas: Path,
    target_paths: list[Path],
) -> list[Finding]:
    findings: list[Finding] = []
    live_evidence = first_match(
        [recent_doc, entity_registry, episode_deltas],
        [
            re.compile(r"서고 접근권"),
            re.compile(r"자색 표준식 입문서 열람 허가"),
        ],
    )
    if live_evidence is None:
        return findings

    denied_access = first_match(
        target_paths,
        [
            re.compile(r"서고 접근권.{0,20}(없|없는|못|않|금지|차단)"),
            re.compile(r"서고.{0,20}(들어갈 수 없|들어가지 못|허가되지 않)"),
            re.compile(r"자색 표준식 입문서.{0,20}(열람|접근|허가).{0,12}(없|않|못|금지|차단)"),
        ],
        ignore_markers=TARGET_NEGATION_MARKERS,
    )
    if denied_access is not None:
        findings.append(
            Finding(
                "fail",
                "State",
                "서고 접근권",
                "target episode docs deny an access right already granted in the latest canon state",
                live_evidence,
                denied_access,
            )
        )

    flattened_control = first_match(
        target_paths,
        [
            re.compile(r"서고 접근권.{0,20}(자유|안도|안심|드디어)"),
            re.compile(r"열람 허가.{0,20}(자유|안도|안심|드디어)"),
        ],
        ignore_markers=TARGET_NEGATION_MARKERS,
    )
    flattening_evidence = first_match(
        [recent_doc],
        [re.compile(r"접근권 부여형 감시"), re.compile(r"보상형 통제"), re.compile(r"안도나 자유가 아니라")],
    )
    if flattened_control is not None and flattening_evidence is not None:
        findings.append(
            Finding(
                "warn",
                "State",
                "서고 접근권",
                "target episode docs flatten a control-state into simple freedom/relief",
                flattening_evidence,
                flattened_control,
            )
        )
    return findings


def immediate_promise_findings(foreshadow_registry: Path, target_paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    items = parse_section_blocks(foreshadow_registry, "### FS-")
    for item in items:
        status = item.fields.get("status", ("", 0))[0]
        payoff_window = item.fields.get("payoff window", ("", 0))[0]
        if status != "open" or "immediate" not in payoff_window:
            continue
        block_text = "\n".join(text for _, text in item.lines)
        anchors = extract_priority_anchors(block_text, item.title)
        if not anchors:
            continue
        if presence_in_target_docs(target_paths, anchors):
            continue
        findings.append(
            Finding(
                "warn",
                "Promise",
                f"{item.identifier} {item.title}",
                "immediate open promise is not visibly carried into target episode docs",
                Evidence(foreshadow_registry, item.start_line, item.heading_text),
                make_absence_evidence(target_paths, f"no anchor mention for {', '.join(anchors)}"),
            )
        )
    return findings


def recent_bridge_findings(recent_doc: Path, target_paths: list[Path]) -> list[Finding]:
    pressure_lines = extract_section_lines(recent_doc, "Next-scene pressure")
    if not pressure_lines:
        return []
    pressure_text = "\n".join(text for _, text in pressure_lines)
    anchors = extract_priority_anchors(pressure_text)
    if not anchors or presence_in_target_docs(target_paths, anchors):
        return []
    first_line_no, first_line_text = pressure_lines[0]
    return [
        Finding(
            "warn",
            "Temporal",
            "recent bridge",
            "target episode docs do not visibly pick up the immediate handoff pressure from recent memory",
            Evidence(recent_doc, first_line_no, first_line_text.strip()),
            make_absence_evidence(target_paths, f"no bridge anchor mention for {', '.join(anchors)}"),
        )
    ]


def time_skip_findings(
    foreshadow_registry: Path,
    target_paths: list[Path],
) -> list[Finding]:
    items = parse_section_blocks(foreshadow_registry, "### FS-")
    if not any(
        item.fields.get("status", ("", 0))[0] == "open"
        and "immediate" in item.fields.get("payoff window", ("", 0))[0]
        for item in items
    ):
        return []
    skip_evidence = first_match(target_paths, list(TIME_SKIP_PATTERNS))
    if skip_evidence is None:
        return []
    live_evidence = first_match(
        [foreshadow_registry],
        [re.compile(r"payoff window: immediate")],
    )
    if live_evidence is None:
        live_evidence = Evidence(foreshadow_registry, 1, "open immediate promises remain active")
    return [
        Finding(
            "warn",
            "Temporal",
            "immediate payoff window",
            "target episode docs appear to jump time while immediate promises are still open",
            live_evidence,
            skip_evidence,
        )
    ]


def render(findings: list[Finding], strict_warn: bool) -> int:
    level_order = ("fail", "warn", "info")
    counts = {level: 0 for level in level_order}
    for finding in findings:
        counts[finding.level] += 1
        print(f"[{finding.level.upper()}] {finding.category} / {finding.subject}: {finding.summary}")
        print(f"  evidence A: {finding.evidence_a.render()}")
        print(f"  evidence B: {finding.evidence_b.render()}")

    print()
    print(
        f"summary: {counts['fail']} fail, {counts['warn']} warn, {counts['info']} info"
    )
    if strict_warn:
        print("exit rule: fail or warn -> non-zero")
    else:
        print("exit rule: fail only -> non-zero")
    if counts["fail"]:
        return 1
    if strict_warn and counts["warn"]:
        return 1
    return 0


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root
    episode_dir = repo_root / "artifacts" / "writing" / "episodes" / args.episode_id
    if not episode_dir.exists():
        raise SystemExit(f"missing episode directory: {episode_dir}")

    current_canons = discover_current_canons(repo_root)
    if not current_canons:
        raise SystemExit("no current canon snapshots found")

    latest_current = current_canons[-1]
    target_index = episode_sort_key(args.episode_id)
    latest_index = episode_sort_key(latest_current.episode_id)

    findings: list[Finding] = []
    if target_index <= latest_index:
        findings.append(
            Finding(
                "info",
                "Scope",
                args.episode_id,
                "semantic audit is most reliable for the next episode after the latest current canon; current live docs reflect the latest canon state",
                Evidence(latest_current.canon_path, 1, f"latest current canon episode: {latest_current.episode_id}"),
                make_absence_evidence([episode_dir], f"target episode index={target_index}, latest current index={latest_index}"),
            )
        )

    target_docs = build_target_docs(episode_dir)
    required_missing = [name for name, path in target_docs.items() if path is None]
    if required_missing:
        raise SystemExit(f"missing target docs: {', '.join(required_missing)}")

    target_paths = [path for path in target_docs.values() if path is not None]
    add_placeholder_warnings(findings, target_docs)

    live_root = repo_root / "world" / "live" / "docs"
    recent_doc = live_root / "memory_tiers" / "recent.md"
    entity_registry = live_root / "memory_tiers" / "entity_registry.md"
    episode_deltas = live_root / "episode_deltas.md"
    foreshadow_registry = live_root / "foreshadow_registry.md"
    base_episode_dir = repo_root / "artifacts" / "writing" / "episodes" / latest_current.episode_id
    base_setting_brief = find_latest_versioned_file(base_episode_dir, "setting_brief")

    findings.extend(
        access_rights_findings(recent_doc, entity_registry, episode_deltas, target_paths)
    )
    findings.extend(calion_certainty_findings(entity_registry, target_paths))
    findings.extend(knowledge_guard_findings(base_setting_brief, target_paths))
    findings.extend(immediate_promise_findings(foreshadow_registry, target_paths))
    findings.extend(recent_bridge_findings(recent_doc, target_paths))
    findings.extend(time_skip_findings(foreshadow_registry, target_paths))

    return render(findings, args.strict_warn)


if __name__ == "__main__":
    sys.exit(main())
