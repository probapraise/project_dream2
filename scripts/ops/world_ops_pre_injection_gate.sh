#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
usage: world_ops_pre_injection_gate.sh <run_id> <call_spec_env> <payload_file> [bundle_dir]
example:
  bash scripts/ops/world_ops_pre_injection_gate.sh RUN-20260304-SIM world_ops/templates/execution_call_spec.env /tmp/payload.txt
EOF
}

trim() {
  local s="$1"
  s="${s#"${s%%[![:space:]]*}"}"
  s="${s%"${s##*[![:space:]]}"}"
  printf '%s' "$s"
}

if [[ $# -lt 3 ]]; then
  usage
  exit 1
fi

RUN_ID="$1"
SPEC_FILE="$2"
PAYLOAD_FILE="$3"
SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"
BUNDLE_DIR="${4:-${ROOT_DIR}/world/live}"

if [[ ! -f "$SPEC_FILE" ]]; then
  echo "[fail] call spec 없음: ${SPEC_FILE}"
  exit 1
fi
if [[ ! -f "$PAYLOAD_FILE" ]]; then
  echo "[fail] payload 파일 없음: ${PAYLOAD_FILE}"
  exit 1
fi
if [[ ! -d "$BUNDLE_DIR" ]]; then
  echo "[fail] bundle dir 없음: ${BUNDLE_DIR}"
  exit 1
fi

call_id=""
profile=""
round=""

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
    round) round="$value" ;;
  esac
done < "$SPEC_FILE"

profile="$(echo "$profile" | tr '[:upper:]' '[:lower:]')"

if [[ -z "$call_id" || -z "$profile" ]]; then
  echo "[fail] call spec 필수 키 누락 (call_id/profile)"
  exit 1
fi

RUNS_DIR="${ROOT_DIR}/artifacts/runs"
RUN_DIR="${RUNS_DIR}/${RUN_ID}"
VIEW_FILE="${RUN_DIR}/views/${call_id}.view.md"
ALLOWED_FILE="${RUN_DIR}/manifests/${call_id}.allowed_paths.txt"
GATE_DIR="${RUN_DIR}/gates"
OUT_PAYLOAD_DIR="${RUN_DIR}/payloads"
mkdir -p "$GATE_DIR" "$OUT_PAYLOAD_DIR"

GATE_REPORT="${GATE_DIR}/${call_id}_pre_injection_gate.md"
GATED_PAYLOAD="${OUT_PAYLOAD_DIR}/${call_id}.gated.txt"

fail_count=0
notes=()

if [[ ! -f "$VIEW_FILE" ]]; then
  notes+=("compiled view 없음: artifacts/runs/${RUN_ID}/views/${call_id}.view.md")
  fail_count=$((fail_count + 1))
fi

if [[ ! -f "$ALLOWED_FILE" ]]; then
  notes+=("allowed paths manifest 없음: artifacts/runs/${RUN_ID}/manifests/${call_id}.allowed_paths.txt")
  fail_count=$((fail_count + 1))
fi

expected_rel="artifacts/runs/${RUN_ID}/views/${call_id}.view.md"
legacy_rel="runs/${RUN_ID}/views/${call_id}.view.md"
bundle_rel="world/live/runs/${RUN_ID}/views/${call_id}.view.md"
BUNDLE_VIEW_FILE="${BUNDLE_DIR}/runs/${RUN_ID}/views/${call_id}.view.md"
payload_references_view="no"
if grep -Fq "$expected_rel" "$PAYLOAD_FILE" \
  || grep -Fq "$legacy_rel" "$PAYLOAD_FILE" \
  || grep -Fq "$bundle_rel" "$PAYLOAD_FILE" \
  || grep -Fq "$VIEW_FILE" "$PAYLOAD_FILE" \
  || grep -Fq "$BUNDLE_VIEW_FILE" "$PAYLOAD_FILE"; then
  payload_references_view="yes"
fi

if [[ "$payload_references_view" != "yes" ]]; then
  notes+=("payload에 실행뷰 참조 누락: ${expected_rel}")
  fail_count=$((fail_count + 1))
fi

RAW_SOURCE_REGEX='(^|[^[:alnum:]_])(world_bible|characters|docs|layer_b|quarantine)/|world/live/(world_bible|characters|docs|layer_b|quarantine)/'
raw_hits="$(grep -Ein "$RAW_SOURCE_REGEX" "$PAYLOAD_FILE" || true)"
if [[ -n "$raw_hits" ]]; then
  notes+=("payload가 원본 경로를 직접 참조함 (실행뷰 우회 금지)")
  fail_count=$((fail_count + 1))
fi

META_PAYLOAD_REGEX='(\[META\]|작가[[:space:]]*전용|세계의[[:space:]]*진실|정합성[[:space:]]*운영[[:space:]]*규약|LoreOps|캐논[[:space:]]*컨트롤|Invariants|Episode[[:space:]]*Seed|public_lore_pack|외부세계[[:space:]]*개발자|B18[[:space:]]*초대망|조각[[:space:]]*지식[[:space:]]*교환[[:space:]]*루트|기록[[:space:]]*공백|잠재[[:space:]]*사고)'
meta_payload_hits=""
if [[ "$profile" != "orchestrator" ]]; then
  meta_payload_hits="$(grep -Ein "$META_PAYLOAD_REGEX" "$PAYLOAD_FILE" || true)"
  if [[ -n "$meta_payload_hits" ]]; then
    notes+=("payload에 META 금지 패턴 포함")
    fail_count=$((fail_count + 1))
  fi
fi

status="pass"
if [[ "$fail_count" -gt 0 ]]; then
  status="fail"
else
  cp "$PAYLOAD_FILE" "$GATED_PAYLOAD"
fi

{
  echo "# pre_injection_gate"
  echo
  echo "- run_id: ${RUN_ID}"
  echo "- call_id: ${call_id}"
  echo "- profile: ${profile}"
  echo "- round: ${round:-N/A}"
  echo "- checked_at: $(date '+%F %T %z')"
  echo "- status: ${status}"
  echo
  echo "## checks"
  echo "- compiled_view_exists: $([[ -f "$VIEW_FILE" ]] && echo yes || echo no)"
  echo "- allowed_manifest_exists: $([[ -f "$ALLOWED_FILE" ]] && echo yes || echo no)"
  echo "- payload_references_view: ${payload_references_view}"
  echo "- raw_source_bypass: $([[ -z "$raw_hits" ]] && echo no || echo yes)"
  echo "- meta_pattern_in_payload: $([[ -z "$meta_payload_hits" ]] && echo no || echo yes)"
  echo
  echo "## notes"
  if [[ ${#notes[@]} -gt 0 ]]; then
    for n in "${notes[@]}"; do
      echo "- ${n}"
    done
  else
    echo "- 없음"
  fi
  echo
  if [[ -n "$raw_hits" ]]; then
    echo "## raw_source_hits"
    echo '```'
    echo "$raw_hits"
    echo '```'
    echo
  fi
  if [[ -n "$meta_payload_hits" ]]; then
    echo "## meta_payload_hits"
    echo '```'
    echo "$meta_payload_hits"
    echo '```'
    echo
  fi
  echo "## outputs"
  echo "- gated_payload: artifacts/runs/${RUN_ID}/payloads/${call_id}.gated.txt"
  echo "- report: artifacts/runs/${RUN_ID}/gates/${call_id}_pre_injection_gate.md"
} > "$GATE_REPORT"

if [[ "$status" != "pass" ]]; then
  echo "[fail] pre-injection gate 실패: ${GATE_REPORT}"
  exit 1
fi

echo "[ok] gate report: ${GATE_REPORT}"
echo "[ok] gated payload: ${GATED_PAYLOAD}"
