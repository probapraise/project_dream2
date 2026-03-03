#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <change_id>"
  echo "example: $0 CR-20260303-001"
  exit 1
fi

CHANGE_ID="$1"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TPL_DIR="${ROOT_DIR}/world_ops/templates"
SESS_DIR="${ROOT_DIR}/world_ops/sessions"

mkdir -p "$SESS_DIR"

cp "${TPL_DIR}/change_request.md" "${SESS_DIR}/${CHANGE_ID}_request.md"
cp "${TPL_DIR}/phase2_report.md" "${SESS_DIR}/${CHANGE_ID}_phase2_report.md"
cp "${TPL_DIR}/phase3_apply.md" "${SESS_DIR}/${CHANGE_ID}_phase3_apply.md"
cp "${TPL_DIR}/major_prompt_log.md" "${SESS_DIR}/${CHANGE_ID}_major_prompt_log.md"
cp "${TPL_DIR}/tri_diff_verify.md" "${SESS_DIR}/${CHANGE_ID}_tri_diff_verify.md"
cp "${TPL_DIR}/phase4_sync.md" "${SESS_DIR}/${CHANGE_ID}_phase4_sync.md"

for f in "${SESS_DIR}/${CHANGE_ID}_"*.md; do
  sed -i "s/CR-YYYYMMDD-001/${CHANGE_ID}/g" "$f"
done

printf 'created session files:\n'
ls -1 "${SESS_DIR}/${CHANGE_ID}_"*.md
