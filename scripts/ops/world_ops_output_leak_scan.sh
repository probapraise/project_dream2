#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
usage: world_ops_output_leak_scan.sh <run_id> <call_spec_env> <model_output_file> [bundle_dir]
example:
  bash scripts/ops/world_ops_output_leak_scan.sh RUN-20260304-SIM world_ops/templates/execution_call_spec.env /tmp/model_output.txt
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
MODEL_OUTPUT="$3"
SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"
BUNDLE_DIR="${4:-${ROOT_DIR}/world/live}"

if [[ ! -f "$SPEC_FILE" ]]; then
  echo "[fail] call spec 없음: ${SPEC_FILE}"
  exit 1
fi
if [[ ! -f "$MODEL_OUTPUT" ]]; then
  echo "[fail] model output 파일 없음: ${MODEL_OUTPUT}"
  exit 1
fi
if [[ ! -d "$BUNDLE_DIR" ]]; then
  echo "[fail] bundle dir 없음: ${BUNDLE_DIR}"
  exit 1
fi

call_id=""
profile=""

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
  esac
done < "$SPEC_FILE"

profile="$(echo "$profile" | tr '[:upper:]' '[:lower:]')"
if [[ -z "$call_id" || -z "$profile" ]]; then
  echo "[fail] call spec 필수 키 누락 (call_id/profile)"
  exit 1
fi

RUNS_DIR="${ROOT_DIR}/artifacts/runs"
RUN_DIR="${RUNS_DIR}/${RUN_ID}"
GATE_DIR="${RUN_DIR}/gates"
mkdir -p "$GATE_DIR"

REPORT_FILE="${GATE_DIR}/${call_id}_output_leak_scan.md"

HARD_REGEX='(\[(META|CONFIDENTIAL)\]|(visibility|정보[[:space:]]*레벨)[[:space:]]*:[[:space:]]*(META|CONFIDENTIAL)\b|META/CONFIDENTIAL|작가[[:space:]]*전용|세계의[[:space:]]*진실|정합성[[:space:]]*운영[[:space:]]*규약|LoreOps|캐논[[:space:]]*컨트롤|불변식|Invariants|Episode[[:space:]]*Seed|public_lore_pack|외부세계[[:space:]]*개발자|B18[[:space:]]*초대망(\(추천인\))?|조각[[:space:]]*지식[[:space:]]*교환[[:space:]]*루트|기록[[:space:]]*공백|잠재[[:space:]]*사고)'
SOFT_REGEX='(금서관|봉문([[:space:]]*유도[[:space:]]*단어)?|요주의[[:space:]]*학생|감찰단[[:space:]]*라인|비공식[[:space:]]*채널|유령계정|익명[[:space:]]*부계정|위조[[:space:]]*열람권|출입[[:space:]]*로그[[:space:]]*열람권|암시장|도핑)'

hard_hits="$(grep -Ein "$HARD_REGEX" "$MODEL_OUTPUT" || true)"
soft_hits="$(grep -Ein "$SOFT_REGEX" "$MODEL_OUTPUT" || true)"

hard_count=0
soft_count=0
if [[ -n "$hard_hits" ]]; then
  hard_count="$(printf '%s\n' "$hard_hits" | sed '/^$/d' | wc -l | tr -d ' ')"
fi
if [[ -n "$soft_hits" ]]; then
  soft_count="$(printf '%s\n' "$soft_hits" | sed '/^$/d' | wc -l | tr -d ' ')"
fi

status="pass"
if [[ "$profile" != "orchestrator" ]] && [[ "$hard_count" -gt 0 ]]; then
  status="fail"
fi

{
  echo "# output_leak_scan"
  echo
  echo "- run_id: ${RUN_ID}"
  echo "- call_id: ${call_id}"
  echo "- profile: ${profile}"
  echo "- scanned_at: $(date '+%F %T %z')"
  echo "- status: ${status}"
  echo
  echo "## summary"
  echo "- hard_hits: ${hard_count}"
  echo "- soft_hits: ${soft_count}"
  echo
  if [[ "$profile" == "orchestrator" ]]; then
    echo "## note"
    echo "- orchestrator 프로필은 META 접근권한이 있으므로 hard hit으로 실패 처리하지 않는다."
    echo
  fi
  echo "## hard_hits_detail"
  if [[ -n "$hard_hits" ]]; then
    echo '```'
    echo "$hard_hits"
    echo '```'
  else
    echo "- 없음"
  fi
  echo
  echo "## soft_hits_detail"
  if [[ -n "$soft_hits" ]]; then
    echo '```'
    echo "$soft_hits"
    echo '```'
  else
    echo "- 없음"
  fi
} > "$REPORT_FILE"

if [[ "$status" != "pass" ]]; then
  echo "[fail] output leak detected: ${REPORT_FILE}"
  exit 1
fi

echo "[ok] output leak scan: ${REPORT_FILE}"
