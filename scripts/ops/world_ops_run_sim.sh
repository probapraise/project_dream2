#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
usage: world_ops_run_sim.sh <run_id> <call_spec_env> <sim_id> <board_state_file> [options]

example:
  bash scripts/ops/world_ops_run_sim.sh \
    RUN-20260306-SIM \
    world_ops/templates/execution_call_spec.env \
    simrun-001 \
    simrun-001_cold_start.json

options:
  --mode <mode>               Simulation mode label (default: cold_start)
  --seed-label <label>        Human-readable seed label
  --participants <n>          Number of sampled participants (default: 12)
  --sample-seed <n>           Sampling RNG seed (default: 42)
  --vertex-key <path>         Vertex service account JSON path
  --bundle-dir <path>         Bundle dir (default: world/live)
  --dry-run                   Stop after gated payload generation
EOF
}

trim() {
  local s="$1"
  s="${s#"${s%%[![:space:]]*}"}"
  s="${s%"${s##*[![:space:]]}"}"
  printf '%s' "$s"
}

read_spec_value() {
  local key="$1"
  local file="$2"
  local line value
  while IFS= read -r line || [[ -n "$line" ]]; do
    line="$(trim "$line")"
    [[ -z "$line" ]] && continue
    [[ "${line:0:1}" == "#" ]] && continue
    [[ "$line" != *=* ]] && continue
    if [[ "$(trim "${line%%=*}")" == "$key" ]]; then
      value="$(trim "${line#*=}")"
      value="${value%\"}"
      value="${value#\"}"
      value="${value%\'}"
      value="${value#\'}"
      printf '%s' "$value"
      return 0
    fi
  done < "$file"
  return 1
}

if [[ $# -lt 4 ]]; then
  usage
  exit 1
fi

RUN_ID="$1"
SPEC_FILE="$2"
SIM_ID="$3"
BOARD_STATE_FILE="$4"
shift 4

MODE="cold_start"
SEED_LABEL="각인광장 베타 오픈 첫날"
PARTICIPANTS="12"
SAMPLE_SEED="42"
VERTEX_KEY=""
DRY_RUN="no"

SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"
BUNDLE_DIR="${ROOT_DIR}/world/live"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      MODE="$2"
      shift 2
      ;;
    --seed-label)
      SEED_LABEL="$2"
      shift 2
      ;;
    --participants)
      PARTICIPANTS="$2"
      shift 2
      ;;
    --sample-seed)
      SAMPLE_SEED="$2"
      shift 2
      ;;
    --vertex-key)
      VERTEX_KEY="$2"
      shift 2
      ;;
    --bundle-dir)
      BUNDLE_DIR="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN="yes"
      shift
      ;;
    *)
      echo "[fail] unknown option: $1"
      usage
      exit 1
      ;;
  esac
done

if [[ ! -f "$SPEC_FILE" ]]; then
  echo "[fail] call spec 없음: ${SPEC_FILE}"
  exit 1
fi

if [[ ! -d "$BUNDLE_DIR" ]]; then
  echo "[fail] bundle dir 없음: ${BUNDLE_DIR}"
  exit 1
fi

if [[ "$BOARD_STATE_FILE" == /* || "$BOARD_STATE_FILE" == *".."* ]]; then
  echo "[fail] board_state_file must be a relative filename under board_states/"
  exit 1
fi

CALL_ID="$(read_spec_value call_id "$SPEC_FILE" || true)"
if [[ -z "$CALL_ID" ]]; then
  echo "[fail] call spec 필수 키 누락: call_id"
  exit 1
fi

RUN_DIR="${ROOT_DIR}/artifacts/runs/${RUN_ID}"
PAYLOAD_DIR="${RUN_DIR}/payloads"
OUTPUT_DIR="${RUN_DIR}/outputs"
mkdir -p "$PAYLOAD_DIR" "$OUTPUT_DIR"

VIEW_REL="artifacts/runs/${RUN_ID}/views/${CALL_ID}.view.md"
RAW_PAYLOAD="${PAYLOAD_DIR}/${CALL_ID}.payload.env"
GATED_PAYLOAD="${PAYLOAD_DIR}/${CALL_ID}.gated.txt"
OUTPUT_JSON="${OUTPUT_DIR}/${SIM_ID}.json"
OUTPUT_REPORT="${OUTPUT_DIR}/${SIM_ID}.md"
PROMOTE_PATH="${BUNDLE_DIR}/board_states/${BOARD_STATE_FILE}"

bash "${ROOT_DIR}/scripts/ops/world_ops_compile_execution_views.sh" "${RUN_ID}" "${SPEC_FILE}" "${BUNDLE_DIR}"

cat > "$RAW_PAYLOAD" <<EOF
input_view=${VIEW_REL}
sim_id=${SIM_ID}
mode=${MODE}
seed_label=${SEED_LABEL}
participants=${PARTICIPANTS}
sample_seed=${SAMPLE_SEED}
EOF

bash "${ROOT_DIR}/scripts/ops/world_ops_pre_injection_gate.sh" "${RUN_ID}" "${SPEC_FILE}" "$RAW_PAYLOAD" "${BUNDLE_DIR}"

echo "[ok] gated payload: ${GATED_PAYLOAD}"
echo "[ok] planned output json: ${OUTPUT_JSON}"
echo "[ok] planned live promote: ${PROMOTE_PATH}"

if [[ "$DRY_RUN" == "yes" ]]; then
  echo "[ok] dry run complete"
  exit 0
fi

SIM_CMD=(
  python3
  "${ROOT_DIR}/scripts/sim/sim_runner.py"
  --gated-payload "${GATED_PAYLOAD}"
  --output-json "${OUTPUT_JSON}"
  --output-report "${OUTPUT_REPORT}"
  --population-csv "${BUNDLE_DIR}/population/population_slots.csv"
)

if [[ -n "$VERTEX_KEY" ]]; then
  SIM_CMD+=(--vertex-key "${VERTEX_KEY}")
fi

"${SIM_CMD[@]}"

bash "${ROOT_DIR}/scripts/ops/world_ops_output_leak_scan.sh" "${RUN_ID}" "${SPEC_FILE}" "${OUTPUT_REPORT}" "${BUNDLE_DIR}"

mkdir -p "$(dirname "$PROMOTE_PATH")"
cp "${OUTPUT_JSON}" "${PROMOTE_PATH}"

echo "[ok] promoted board state: ${PROMOTE_PATH}"
