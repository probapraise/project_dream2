#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLE_DIR="${1:-${ROOT_DIR}/worldbible_refined_bundle_20260303}"
INDEX_FILE="${BUNDLE_DIR}/docs/world_bible_index_v2.md"
WB_DIR="${BUNDLE_DIR}/world_bible"

errors=0
warns=0

say() { printf '%s\n' "$*"; }
err() { say "[ERROR] $*"; errors=$((errors + 1)); }
warn() { say "[WARN ] $*"; warns=$((warns + 1)); }

say "== World Bundle Audit =="
say "bundle: ${BUNDLE_DIR}"

[[ -d "$BUNDLE_DIR" ]] || { err "bundle dir missing"; exit 1; }
[[ -f "$INDEX_FILE" ]] || { err "missing docs/world_bible_index_v2.md"; exit 1; }
[[ -d "$WB_DIR" ]] || { err "missing world_bible dir"; exit 1; }

zone_count=$(find "$BUNDLE_DIR" -type f -name '*:Zone.Identifier' | wc -l | tr -d ' ')
if [[ "$zone_count" != "0" ]]; then
  warn "Zone.Identifier 파일 ${zone_count}개 발견 (운영 대상에서 제외 권장)"
fi

mapfile -t section_ids < <(grep -E '^- \[WB-[0-9]{4}\]' "$INDEX_FILE" | sed -E 's/^- \[(WB-[0-9]{4})\].*/\1/')
if [[ ${#section_ids[@]} -eq 0 ]]; then
  err "index_v2에서 WB section id를 찾지 못함"
fi
ids_blob=" $(printf '%s ' "${section_ids[@]:-}")"

while IFS= read -r rel; do
  [[ -z "$rel" ]] && continue
  if [[ ! -f "${BUNDLE_DIR}/${rel}" ]]; then
    err "index file reference missing: ${rel}"
  fi
done < <(grep -E '^  - file:' "$INDEX_FILE" | sed -E 's/^  - file:[[:space:]]*//')

while IFS= read -r dep_line; do
  dep_raw="${dep_line#*depends_on: }"
  dep_raw="$(echo "$dep_raw" | sed 's/[[:space:]]//g')"
  [[ "$dep_raw" == "(없음)" || -z "$dep_raw" ]] && continue
  IFS=',' read -ra deps <<< "$dep_raw"
  for dep in "${deps[@]}"; do
    [[ -z "$dep" ]] && continue
    if [[ "$ids_blob" != *" ${dep} "* ]]; then
      err "unknown depends_on id: ${dep}"
    fi
  done
done < <(grep -E '^  - depends_on:' "$INDEX_FILE")

mapfile -t wb_files < <(find "$WB_DIR" -maxdepth 1 -type f -name 'WB-*.md' | sort)
if [[ ${#wb_files[@]} -eq 0 ]]; then
  err "world_bible/WB-*.md 없음"
fi

actual_ids=()
for file in "${wb_files[@]}"; do
  base="$(basename "$file")"
  expected="$(echo "$base" | sed -E 's/^(WB-[0-9]{4}).*/\1/')"
  actual="$(grep -m1 '^id:' "$file" | sed -E 's/^id:[[:space:]]*//' | tr -d '"' || true)"

  if [[ -z "$actual" ]]; then
    err "frontmatter id 누락: world_bible/${base}"
    continue
  fi

  actual_ids+=("$actual")

  if [[ "$actual" != "$expected" ]]; then
    err "id mismatch: ${base} (expected=${expected}, actual=${actual})"
  fi

  if [[ "$ids_blob" != *" ${expected} "* ]]; then
    warn "index_v2 미등록 섹션: ${expected} (${base})"
  fi
done

if [[ ${#actual_ids[@]} -gt 0 ]]; then
  dup_ids=$(printf '%s\n' "${actual_ids[@]}" | sort | uniq -d || true)
  if [[ -n "$dup_ids" ]]; then
    while IFS= read -r d; do
      [[ -z "$d" ]] && continue
      err "duplicate WB id: ${d}"
    done <<< "$dup_ids"
  fi
fi

say "done: errors=${errors}, warnings=${warns}"
if [[ "$errors" -gt 0 ]]; then
  exit 1
fi
