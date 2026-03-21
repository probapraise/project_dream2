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

if [[ ! -f "$canon_readme" ]]; then
  echo "missing canon README: $canon_readme" >&2
  exit 1
fi

echo "deprecated: canon/ must contain exactly one non-README file." >&2
echo "requested episode: $episode_id" >&2
echo "requested filename: $new_canon_filename" >&2
echo >&2
echo "do this instead:" >&2
echo "1. edit the current canon file in place" >&2
echo "2. keep comparison material in assembled/ or analysis/" >&2
echo "3. run python3 scripts/writing/refresh_canon_metadata.py $episode_id" >&2
echo "4. run bash scripts/writing/post_canon_sync.sh $episode_id" >&2
exit 1
