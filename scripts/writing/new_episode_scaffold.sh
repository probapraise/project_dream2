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
drafts_dir="$episode_dir/drafts"
assembled_dir="$episode_dir/assembled"
analysis_dir="$episode_dir/analysis"
style_template="$repo_root/artifacts/writing/style/episode_style_selection_template.md"
style_selection_file="$episode_dir/style_selection_v1.md"
style_constitution_template="$repo_root/artifacts/writing/episode_style_constitution_template.md"
style_constitution_file="$episode_dir/episode_style_constitution_v1.md"
setting_brief_template="$repo_root/artifacts/writing/episode_setting_brief_template.md"
setting_brief_file="$episode_dir/setting_brief_v1.md"
long_range_summary_template="$repo_root/artifacts/writing/long_range_summary_template.md"
long_range_summary_file="$episode_dir/long_range_summary_v1.md"
prompt_packet_template="$repo_root/artifacts/writing/prompt_packet_template.md"
prompt_packet_file="$episode_dir/prompt_packet_v1.md"
prompt_template="$repo_root/artifacts/writing/prompt_template.md"
prompt_file="$episode_dir/prompt_v1.md"
assembly_template="$repo_root/artifacts/writing/assembly_notes_template.md"
assembly_file="$assembled_dir/assembly_notes_v1.md"
revision_delta_template="$repo_root/artifacts/writing/revision_delta_template.md"
revision_delta_file="$analysis_dir/revision_delta_v1.md"

if [[ -e "$episode_dir" ]]; then
  echo "episode directory already exists: $episode_dir" >&2
  exit 1
fi

mkdir -p "$canon_dir" "$drafts_dir" "$assembled_dir" "$analysis_dir"
touch "$drafts_dir/.gitkeep"

cat > "$canon_dir/README.md" <<EOF
# canon

- episode_id: $episode_id
- current_text_canon: none
- current_text_canon_sha256: none
- current_word_canon: none

## Policy

- 이 폴더에는 현재 또는 과거에 정식 반영된 canon 스냅샷만 둔다.
- canon은 고정 불변이 아니다. 새 리비전이 정식 채택되면 이 폴더 안에 새 canon 파일을 추가하고 위 current 항목을 갱신한다.
- superseded canon은 비교와 회고를 위해 이 폴더에 남길 수 있다.
EOF

if [[ -f "$style_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$style_template" > "$style_selection_file"
fi

if [[ -f "$style_constitution_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$style_constitution_template" > "$style_constitution_file"
fi

if [[ -f "$setting_brief_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$setting_brief_template" > "$setting_brief_file"
fi

if [[ -f "$long_range_summary_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$long_range_summary_template" > "$long_range_summary_file"
fi

if [[ -f "$prompt_packet_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$prompt_packet_template" > "$prompt_packet_file"
fi

if [[ -f "$prompt_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$prompt_template" > "$prompt_file"
fi

if [[ -f "$assembly_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$assembly_template" > "$assembly_file"
fi

if [[ -f "$revision_delta_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$revision_delta_template" > "$revision_delta_file"
fi

echo "created episode scaffold:"
echo "$episode_dir"
echo "$canon_dir/README.md"
if [[ -f "$style_selection_file" ]]; then
  echo "$style_selection_file"
fi
if [[ -f "$style_constitution_file" ]]; then
  echo "$style_constitution_file"
fi
if [[ -f "$setting_brief_file" ]]; then
  echo "$setting_brief_file"
fi
if [[ -f "$long_range_summary_file" ]]; then
  echo "$long_range_summary_file"
fi
if [[ -f "$prompt_packet_file" ]]; then
  echo "$prompt_packet_file"
fi
if [[ -f "$prompt_file" ]]; then
  echo "$prompt_file"
fi
if [[ -d "$drafts_dir" ]]; then
  echo "$drafts_dir/"
fi
if [[ -f "$assembly_file" ]]; then
  echo "$assembly_file"
fi
if [[ -f "$revision_delta_file" ]]; then
  echo "$revision_delta_file"
fi
