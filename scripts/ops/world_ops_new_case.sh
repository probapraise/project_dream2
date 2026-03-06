#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <change_id> [--major] [--deletion-gate]"
  echo "example: $0 CR-20260303-001 --major"
  exit 1
fi

CHANGE_ID="$1"
shift

CREATE_MAJOR=0
CREATE_DELETION_GATE=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --major)
      CREATE_MAJOR=1
      ;;
    --deletion-gate)
      CREATE_DELETION_GATE=1
      ;;
    *)
      echo "unknown option: $1"
      exit 1
      ;;
  esac
  shift
done

SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"
TPL_DIR="${ROOT_DIR}/world_ops/templates"
CASE_DIR="${ROOT_DIR}/world_ops/cases/${CHANGE_ID}"

if compgen -G "${CASE_DIR}/*.md" >/dev/null; then
  echo "case already exists: ${CASE_DIR}"
  exit 1
fi

mkdir -p "$CASE_DIR"

cp "${TPL_DIR}/change_request.md" "${CASE_DIR}/request.md"
cp "${TPL_DIR}/phase2_report.md" "${CASE_DIR}/phase2_report.md"
cp "${TPL_DIR}/phase3_apply.md" "${CASE_DIR}/phase3_apply.md"
cp "${TPL_DIR}/phase4_sync.md" "${CASE_DIR}/phase4_sync.md"

if [[ "$CREATE_MAJOR" -eq 1 ]]; then
  cp "${TPL_DIR}/major_prompt_log.md" "${CASE_DIR}/major_prompt_log.md"
  cp "${TPL_DIR}/tri_diff_verify.md" "${CASE_DIR}/tri_diff_verify.md"
fi

if [[ "$CREATE_DELETION_GATE" -eq 1 ]]; then
  cp "${TPL_DIR}/deletion_gate.md" "${CASE_DIR}/deletion_gate.md"
fi

for f in "${CASE_DIR}"/*.md; do
  sed -i "s/CR-YYYYMMDD-001/${CHANGE_ID}/g" "$f"
done

printf 'created case files:\n'
ls -1 "${CASE_DIR}"/*.md
printf '\n'
echo "note: create new cases with this script; do not copy historical case docs because older cases may contain legacy path notation."
