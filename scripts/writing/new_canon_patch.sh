#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: bash scripts/writing/new_canon_patch.sh <episode_id> <new_canon_filename>" >&2
  exit 1
fi

episode_id="$1"
new_canon_filename="$2"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../.." && pwd)"
canon_dir="$repo_root/artifacts/writing/episodes/$episode_id/canon"
canon_readme="$canon_dir/README.md"
refresh_script="$repo_root/scripts/writing/refresh_canon_metadata.py"

if [[ ! -f "$canon_readme" ]]; then
  echo "missing canon README: $canon_readme" >&2
  exit 1
fi

current_text_canon="$(sed -n 's/^- current_text_canon: //p' "$canon_readme" | head -n 1)"
new_canon_path="$canon_dir/$new_canon_filename"

if [[ -e "$new_canon_path" ]]; then
  echo "destination already exists: $new_canon_path" >&2
  exit 1
fi

if [[ -n "$current_text_canon" && "$current_text_canon" != "none" ]]; then
  cp "$canon_dir/$current_text_canon" "$new_canon_path"
else
  : > "$new_canon_path"
fi

python3 "$refresh_script" "$episode_id" --set-current-text-canon "$new_canon_filename" >/dev/null

echo "created canon patch snapshot:"
echo "$new_canon_path"
echo
echo "next:"
echo "1. edit the new current canon snapshot"
echo "2. bash scripts/writing/post_canon_sync.sh $episode_id"
