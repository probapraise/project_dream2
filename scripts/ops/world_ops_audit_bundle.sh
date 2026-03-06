#!/usr/bin/env bash
set -euo pipefail

SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"
BUNDLE_DIR="${1:-${ROOT_DIR}/world/live}"
INDEX_FILE="${BUNDLE_DIR}/docs/world_bible_index_v2.md"
WB_DIR="${BUNDLE_DIR}/world_bible"
POP_CSV="${BUNDLE_DIR}/population/population_slots.csv"

errors=0
warns=0

say() { printf '%s\n' "$*"; }
err() { say "[ERROR] $*"; errors=$((errors + 1)); }
warn() { say "[WARN ] $*"; warns=$((warns + 1)); }

check_forbidden_literal() {
  local literal="$1"
  local reason="$2"
  shift 2
  local matches
  matches="$(rg -n -F -- "$literal" "$@" 2>/dev/null || true)"
  if [[ -n "$matches" ]]; then
    err "legacy term detected: '${literal}' (${reason})"
    say "$matches" | sed 's/^/  > /'
  fi
}

say "== World Bundle Audit =="
say "bundle: ${BUNDLE_DIR}"

[[ -d "$BUNDLE_DIR" ]] || { err "bundle dir missing"; exit 1; }
[[ -f "$INDEX_FILE" ]] || { err "missing docs/world_bible_index_v2.md"; exit 1; }
[[ -d "$WB_DIR" ]] || { err "missing world_bible dir"; exit 1; }
command -v rg >/dev/null 2>&1 || { err "rg command not found"; exit 1; }

zone_count=$(find "$BUNDLE_DIR" -type f -name '*:Zone.Identifier' | wc -l | tr -d ' ')
if [[ "$zone_count" != "0" ]]; then
  warn "Zone.Identifier 파일 ${zone_count}개 발견 (운영 대상에서 제외 권장)"
fi

# Canonical vocabulary guard for active docs/log.
active_docs=(
  "${BUNDLE_DIR}/docs"
  "${BUNDLE_DIR}/world_bible"
  "${ROOT_DIR}/docs/handoff/next_steps.md"
)
check_forbidden_literal "role_track" "field name must be 'vocation'" "${active_docs[@]}"
check_forbidden_literal "신전기숙사" "dorm label must be '신전동군'" "${active_docs[@]}"
check_forbidden_literal "신전별 기숙사" "dorm label must be '신전동군'" "${active_docs[@]}"
check_forbidden_literal "탑기숙사" "group label should be '7탑 기숙사군'" "${active_docs[@]}"
check_forbidden_literal "연구·조교" "grade label must be '연구과정'" "${active_docs[@]}"
check_forbidden_literal "연구과정/조교" "grade label must be '연구과정'" "${active_docs[@]}"

if [[ -f "$POP_CSV" ]]; then
  csv_header="$(head -n1 "$POP_CSV")"
  if [[ "$csv_header" == *",tower,"* || "$csv_header" == tower,* || "$csv_header" == *,tower || "$csv_header" == "tower" ]]; then
    err "population_slots.csv header contains deprecated column: tower"
  fi

  for col in crest_vision_holder dorm grade mana_color major vocation; do
    if ! echo "$csv_header" | tr ',' '\n' | grep -Fxq "$col"; then
      err "population_slots.csv missing required column: ${col}"
    fi
  done
else
  warn "population CSV missing: ${POP_CSV}"
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
