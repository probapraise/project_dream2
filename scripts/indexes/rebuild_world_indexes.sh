#!/usr/bin/env bash
set -euo pipefail

SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"
BUNDLE_DIR="${1:-${ROOT_DIR}/world/live}"
WB_DIR="${BUNDLE_DIR}/world_bible"
OUT_V2="${BUNDLE_DIR}/docs/world_bible_index_v2.md"
OUT_V1="${BUNDLE_DIR}/docs/world_bible_index.md"

build_index() {
  local out_file="$1"
  {
    echo "# world_bible_index"
    echo
    echo "- regenerated_at: $(date +%F)"
    echo "- source: world_bible/WB-*.md"
    echo "- note: 정리 작업으로 충돌 파일 삭제 후 최소 인덱스로 재생성"
    echo
    echo "## Sections"

    while IFS= read -r file; do
      id="$(grep -m1 '^id:' "$file" | sed -E 's/^id:[[:space:]]*//')"
      title="$(grep -m1 '^title:' "$file" | sed -E 's/^title:[[:space:]]*//; s/^"//; s/"$//')"
      vis="$(grep -m1 '^visibility:' "$file" | sed -E 's/^visibility:[[:space:]]*//')"
      rel="world_bible/$(basename "$file")"
      summary="$(awk '
        /^## 요약\(선택\)/ {in_summary=1; next}
        /^## / {if (in_summary) exit}
        in_summary && /^- / {sub(/^- /, ""); print; exit}
      ' "$file")"

      if [[ -z "$summary" ]]; then
        summary="(요약 미정)"
      fi

      echo "- [${id}] ${title}"
      echo "  - file: ${rel}"
      echo "  - summary: ${summary}"
      echo "  - visibility: ${vis}"
    done < <(find "$WB_DIR" -maxdepth 1 -type f -name 'WB-*.md' | sort)
  } > "$out_file"
}

build_index "$OUT_V2"
build_index "$OUT_V1"

echo "rebuilt: $OUT_V2"
echo "rebuilt: $OUT_V1"
