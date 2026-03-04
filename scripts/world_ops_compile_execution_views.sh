#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
usage: world_ops_compile_execution_views.sh <run_id> <call_spec_env> [bundle_dir]
example:
  bash scripts/world_ops_compile_execution_views.sh RUN-20260304-SIM world_ops/templates/execution_call_spec.env
EOF
}

trim() {
  local s="$1"
  s="${s#"${s%%[![:space:]]*}"}"
  s="${s%"${s##*[![:space:]]}"}"
  printf '%s' "$s"
}

csv_has() {
  local needle="$1"
  local csv="$2"
  local item
  IFS=',' read -ra __csv_items <<< "$csv"
  for item in "${__csv_items[@]}"; do
    item="$(trim "$item")"
    [[ -z "$item" ]] && continue
    if [[ "$item" == "$needle" ]]; then
      return 0
    fi
  done
  return 1
}

if [[ $# -lt 2 ]]; then
  usage
  exit 1
fi

RUN_ID="$1"
SPEC_FILE="$2"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLE_DIR="${3:-${ROOT_DIR}/worldbible_refined_bundle_20260303}"

if [[ ! -f "$SPEC_FILE" ]]; then
  echo "[fail] call spec 없음: ${SPEC_FILE}"
  exit 1
fi

if [[ ! -d "$BUNDLE_DIR" ]]; then
  echo "[fail] bundle dir 없음: ${BUNDLE_DIR}"
  exit 1
fi

call_id=""
profile=""
mode=""
round=""
source_files=""
allow_confidential="no"
allow_character_confidential="no"
allow_confidential_ids=""

while IFS= read -r raw_line || [[ -n "$raw_line" ]]; do
  line="$(trim "$raw_line")"
  [[ -z "$line" ]] && continue
  [[ "${line:0:1}" == "#" ]] && continue
  [[ "$line" != *=* ]] && continue

  key="$(trim "${line%%=*}")"
  value="$(trim "${line#*=}")"

  if [[ "$value" == \"*\" && "$value" == *\" ]]; then
    value="${value:1:${#value}-2}"
  elif [[ "$value" == \'*\' && "$value" == *\' ]]; then
    value="${value:1:${#value}-2}"
  fi

  case "$key" in
    call_id) call_id="$value" ;;
    profile) profile="$value" ;;
    mode) mode="$value" ;;
    round) round="$value" ;;
    source_files) source_files="$value" ;;
    allow_confidential) allow_confidential="$value" ;;
    allow_character_confidential) allow_character_confidential="$value" ;;
    allow_confidential_ids) allow_confidential_ids="$value" ;;
  esac
done < "$SPEC_FILE"

profile="$(echo "$profile" | tr '[:upper:]' '[:lower:]')"
mode="$(echo "$mode" | tr '[:upper:]' '[:lower:]')"
allow_confidential="$(echo "$allow_confidential" | tr '[:upper:]' '[:lower:]')"
allow_character_confidential="$(echo "$allow_character_confidential" | tr '[:upper:]' '[:lower:]')"

if [[ -z "$call_id" || -z "$profile" || -z "$source_files" ]]; then
  echo "[fail] call spec 필수 키 누락 (call_id/profile/source_files)"
  exit 1
fi

case "$profile" in
  orchestrator|simulation|writing) ;;
  *)
    echo "[fail] profile 지원값 아님: ${profile}"
    echo "       supported: orchestrator|simulation|writing"
    exit 1
    ;;
esac

if [[ -z "$mode" ]]; then
  mode="$profile"
fi

if [[ "$profile" == "orchestrator" ]]; then
  allow_confidential="yes"
  allow_character_confidential="yes"
fi

RUN_DIR="${BUNDLE_DIR}/runs/${RUN_ID}"
VIEW_DIR="${RUN_DIR}/views"
MANIFEST_DIR="${RUN_DIR}/manifests"
CALL_DIR="${RUN_DIR}/calls"
mkdir -p "$VIEW_DIR" "$MANIFEST_DIR" "$CALL_DIR"

VIEW_FILE="${VIEW_DIR}/${call_id}.view.md"
MANIFEST_FILE="${MANIFEST_DIR}/${call_id}.manifest.md"
ALLOWED_FILE="${MANIFEST_DIR}/${call_id}.allowed_paths.txt"
BLOCKED_FILE="${MANIFEST_DIR}/${call_id}.blocked_paths.txt"

cp "$SPEC_FILE" "${CALL_DIR}/${call_id}.env"
: > "$VIEW_FILE"
: > "$ALLOWED_FILE"
: > "$BLOCKED_FILE"

META_LINE_REGEX='(\[META\]|작가[[:space:]]*전용|세계의[[:space:]]*진실|정합성[[:space:]]*운영[[:space:]]*규약|LoreOps|캐논[[:space:]]*컨트롤|Invariants|Episode[[:space:]]*Seed|public_lore_pack|외부세계[[:space:]]*개발자|B18[[:space:]]*초대망|조각[[:space:]]*지식[[:space:]]*교환[[:space:]]*루트|기록[[:space:]]*공백|잠재[[:space:]]*사고)'
CONF_LINE_REGEX='(\[CONFIDENTIAL\]|정보[[:space:]]*레벨[[:space:]]*\):[[:space:]]*\[CONFIDENTIAL\])'

included=0
blocked=0
missing=0
redacted_total=0

{
  echo "# execution_view"
  echo
  echo "- run_id: ${RUN_ID}"
  echo "- call_id: ${call_id}"
  echo "- profile: ${profile}"
  echo "- mode: ${mode}"
  echo "- round: ${round:-N/A}"
  echo "- generated_at: $(date '+%F %T %z')"
  echo "- source_spec: ${SPEC_FILE}"
  echo
  echo "## included_sources"
} >> "$VIEW_FILE"

IFS=',' read -ra src_list <<< "$source_files"
for raw_rel in "${src_list[@]}"; do
  rel="$(trim "$raw_rel")"
  [[ -z "$rel" ]] && continue

  if [[ "$rel" == /* ]]; then
    echo "[fail] absolute path 금지: ${rel}"
    exit 1
  fi
  if [[ "$rel" == *".."* ]]; then
    echo "[fail] parent path 금지: ${rel}"
    exit 1
  fi

  full="${BUNDLE_DIR}/${rel}"
  if [[ ! -f "$full" ]]; then
    echo "[missing] ${rel}" >> "$BLOCKED_FILE"
    missing=$((missing + 1))
    continue
  fi

  file_id="$(grep -m1 '^id:' "$full" | sed -E 's/^id:[[:space:]]*//; s/"//g' || true)"
  file_vis="$(grep -m1 '^visibility:' "$full" | sed -E 's/^visibility:[[:space:]]*//; s/"//g' || true)"
  file_vis="$(echo "$file_vis" | tr '[:lower:]' '[:upper:]')"
  [[ -z "$file_vis" ]] && file_vis="UNSPECIFIED"
  [[ -z "$file_id" ]] && file_id="$(basename "$rel")"

  decision="include"
  reason="-"

  if [[ "$profile" != "orchestrator" ]]; then
    if [[ "$file_vis" == "META" ]]; then
      decision="block"
      reason="file_visibility_META"
    elif [[ "$file_vis" == "CONFIDENTIAL" ]]; then
      if [[ "$allow_confidential" != "yes" ]] && ! csv_has "$file_id" "$allow_confidential_ids"; then
        decision="block"
        reason="confidential_not_whitelisted"
      fi
    fi
  fi

  if [[ "$decision" == "block" ]]; then
    echo "${rel}|${file_id}|${file_vis}|${reason}" >> "$BLOCKED_FILE"
    blocked=$((blocked + 1))
    continue
  fi

  tmp_file="$(mktemp)"
  cp "$full" "$tmp_file"
  orig_lines="$(wc -l < "$tmp_file" | tr -d ' ')"

  if [[ "$profile" != "orchestrator" ]]; then
    if grep -Eiq "$META_LINE_REGEX" "$tmp_file"; then
      grep -Eiv "$META_LINE_REGEX" "$tmp_file" > "${tmp_file}.meta" || true
      mv "${tmp_file}.meta" "$tmp_file"
    fi

    if [[ "$allow_character_confidential" != "yes" ]] && [[ "$allow_confidential" != "yes" ]]; then
      if grep -Eiq "$CONF_LINE_REGEX" "$tmp_file"; then
        grep -Eiv "$CONF_LINE_REGEX" "$tmp_file" > "${tmp_file}.conf" || true
        mv "${tmp_file}.conf" "$tmp_file"
      fi
    fi
  fi

  new_lines="$(wc -l < "$tmp_file" | tr -d ' ')"
  redacted=$((orig_lines - new_lines))
  redacted_total=$((redacted_total + redacted))

  {
    echo "- ${rel} (id=${file_id}, visibility=${file_vis}, redacted=${redacted})"
    echo
    echo "### source: ${rel}"
    echo
    cat "$tmp_file"
    echo
  } >> "$VIEW_FILE"

  echo "$rel" >> "$ALLOWED_FILE"
  rm -f "$tmp_file"
  included=$((included + 1))
done

view_hard_hits=""
if [[ "$profile" != "orchestrator" ]]; then
  view_hard_hits="$(grep -Ein "$META_LINE_REGEX" "$VIEW_FILE" || true)"
fi

status="pass"
if [[ "$missing" -gt 0 ]]; then
  status="fail"
fi
if [[ "$included" -eq 0 ]]; then
  status="fail"
fi
if [[ -n "$view_hard_hits" ]]; then
  status="fail"
fi

{
  echo "# execution_view_manifest"
  echo
  echo "- run_id: ${RUN_ID}"
  echo "- call_id: ${call_id}"
  echo "- profile: ${profile}"
  echo "- generated_at: $(date '+%F %T %z')"
  echo "- status: ${status}"
  echo
  echo "## summary"
  echo "- included: ${included}"
  echo "- blocked: ${blocked}"
  echo "- missing: ${missing}"
  echo "- redacted_lines_total: ${redacted_total}"
  echo "- allowed_paths_file: runs/${RUN_ID}/manifests/${call_id}.allowed_paths.txt"
  echo "- blocked_paths_file: runs/${RUN_ID}/manifests/${call_id}.blocked_paths.txt"
  echo
  echo "## blocked_sources"
  if [[ -s "$BLOCKED_FILE" ]]; then
    echo "| rel_path | source_id | visibility | reason |"
    echo "|---|---|---|---|"
    while IFS='|' read -r b_rel b_id b_vis b_reason; do
      [[ -z "$b_rel" ]] && continue
      echo "| ${b_rel} | ${b_id} | ${b_vis} | ${b_reason} |"
    done < "$BLOCKED_FILE"
  else
    echo "- 없음"
  fi
  echo
  echo "## hard_meta_hits_in_view"
  if [[ -n "$view_hard_hits" ]]; then
    echo '```'
    echo "$view_hard_hits"
    echo '```'
  else
    echo "- 없음"
  fi
} > "$MANIFEST_FILE"

if [[ "$status" != "pass" ]]; then
  echo "[fail] execution view compile 실패: ${MANIFEST_FILE}"
  exit 1
fi

echo "[ok] compiled view: ${VIEW_FILE}"
echo "[ok] manifest: ${MANIFEST_FILE}"
