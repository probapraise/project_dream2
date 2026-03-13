#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: bash scripts/writing/new_episode_scaffold.sh <episode_id>" >&2
  exit 1
fi

episode_id="$1"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../.." && pwd)"
episode_dir="$repo_root/artifacts/writing/episodes/$episode_id"
canon_dir="$episode_dir/canon"
style_template="$repo_root/artifacts/writing/style/episode_style_selection_template.md"
style_selection_file="$episode_dir/style_selection_v1.md"

if [[ -e "$episode_dir" ]]; then
  echo "episode directory already exists: $episode_dir" >&2
  exit 1
fi

mkdir -p "$canon_dir"

cat > "$canon_dir/README.md" <<EOF
# canon

- episode_id: $episode_id
- current_text_canon: none
- current_word_canon: none

## Policy

- 이 폴더에는 현재 또는 과거에 정식 반영된 canon 스냅샷만 둔다.
- canon은 고정 불변이 아니다. 새 리비전이 정식 채택되면 이 폴더 안에 새 canon 파일을 추가하고 위 current 항목을 갱신한다.
- superseded canon은 비교와 회고를 위해 이 폴더에 남길 수 있다.
EOF

if [[ -f "$style_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$style_template" > "$style_selection_file"
fi

echo "created episode scaffold:"
echo "$episode_dir"
echo "$canon_dir/README.md"
if [[ -f "$style_selection_file" ]]; then
  echo "$style_selection_file"
fi
