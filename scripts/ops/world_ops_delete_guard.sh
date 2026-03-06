#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <change_id>"
  echo "example: $0 CR-20260304-003"
  exit 1
fi

CHANGE_ID="$1"
SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"

# Staged deletions inside bundle
mapfile -t deleted_files < <(git -C "$ROOT_DIR" diff --cached --name-status | awk '$1=="D" {print $2}' | grep -E '^(world/live/|worldbible_refined_bundle_20260303/)' || true)

if [[ ${#deleted_files[@]} -eq 0 ]]; then
  echo "[ok] staged deletion 없음"
  exit 0
fi

gate_file="${ROOT_DIR}/world_ops/cases/${CHANGE_ID}/deletion_gate.md"
legacy_gate_file="${ROOT_DIR}/world_ops/sessions/${CHANGE_ID}_deletion_gate.md"
if [[ ! -f "$gate_file" && -f "$legacy_gate_file" ]]; then
  gate_file="$legacy_gate_file"
fi
if [[ ! -f "$gate_file" ]]; then
  echo "[fail] deletion gate 파일 없음: ${gate_file}"
  echo "삭제 파일 수: ${#deleted_files[@]}"
  printf '%s\n' "${deleted_files[@]}"
  exit 1
fi

missing=0
for path in "${deleted_files[@]}"; do
  if ! grep -Fq "$path" "$gate_file"; then
    echo "[fail] deletion gate에 대상 파일 누락: $path"
    missing=$((missing + 1))
  fi
done

if [[ "$missing" -gt 0 ]]; then
  exit 1
fi

echo "[ok] deletion gate 확인 완료 (${#deleted_files[@]} files)"
