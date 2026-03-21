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
episode_scorecard_template="$repo_root/artifacts/writing/episode_scorecard_template.md"
episode_scorecard_file="$analysis_dir/episode_scorecard_v1.md"

if [[ "$episode_id" =~ ^ep([0-9]+) ]]; then
  target_episode_num=$((10#${BASH_REMATCH[1]}))
else
  echo "unsupported episode id format: $episode_id" >&2
  exit 1
fi

recent_canon_paths=()
recent_canon_hashes=()
while IFS= read -r readme; do
  readme_episode_id="$(basename "$(dirname "$(dirname "$readme")")")"
  if [[ ! "$readme_episode_id" =~ ^ep([0-9]+) ]]; then
    continue
  fi
  readme_episode_num=$((10#${BASH_REMATCH[1]}))
  if (( readme_episode_num >= target_episode_num )); then
    continue
  fi

  current_text_canon="$(sed -n 's/^- current_text_canon: //p' "$readme" | head -n 1)"
  current_text_canon_sha256="$(sed -n 's/^- current_text_canon_sha256: //p' "$readme" | head -n 1)"
  if [[ -z "$current_text_canon" || "$current_text_canon" == "none" ]]; then
    continue
  fi

  recent_canon_paths+=("artifacts/writing/episodes/$readme_episode_id/canon/$current_text_canon")
  if [[ -n "$current_text_canon_sha256" ]]; then
    recent_canon_hashes+=("$current_text_canon_sha256")
  else
    recent_canon_hashes+=("none")
  fi

  if (( ${#recent_canon_paths[@]} == 3 )); then
    break
  fi
done < <(find "$repo_root/artifacts/writing/episodes" -path '*/canon/README.md' | sort -r)

recent_canon_1="${recent_canon_paths[0]:-none}"
recent_canon_1_sha256="${recent_canon_hashes[0]:-none}"
recent_canon_2="${recent_canon_paths[1]:-none}"
recent_canon_2_sha256="${recent_canon_hashes[1]:-none}"
recent_canon_3="${recent_canon_paths[2]:-none}"
recent_canon_3_sha256="${recent_canon_hashes[2]:-none}"

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

- 이 폴더에는 README.md를 제외하고 현재 정식 canon 파일 1개만 둔다.
- 과거 canon snapshot, patch snapshot, Word 복제본은 이 폴더에 두지 않는다. 비교와 회고는 git history, assembled/, analysis/로 처리한다.
- current_text_canon은 위 단일 canon 파일과 항상 같아야 하며, current_word_canon은 단일 파일 원칙 때문에 none으로 유지한다.
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
  sed \
    -e "s#<episode_id>#$episode_id#g" \
    -e "s#<recent_canon_1>#$recent_canon_1#g" \
    -e "s#<recent_canon_1_sha256>#$recent_canon_1_sha256#g" \
    -e "s#<recent_canon_2>#$recent_canon_2#g" \
    -e "s#<recent_canon_2_sha256>#$recent_canon_2_sha256#g" \
    -e "s#<recent_canon_3>#$recent_canon_3#g" \
    -e "s#<recent_canon_3_sha256>#$recent_canon_3_sha256#g" \
    "$prompt_packet_template" > "$prompt_packet_file"
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

if [[ -f "$episode_scorecard_template" ]]; then
  sed "s/<episode_id>/$episode_id/g" "$episode_scorecard_template" > "$episode_scorecard_file"
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
if [[ -f "$episode_scorecard_file" ]]; then
  echo "$episode_scorecard_file"
fi
