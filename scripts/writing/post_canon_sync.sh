#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "usage: bash scripts/writing/post_canon_sync.sh <episode_id> [--no-audit]" >&2
  exit 1
fi

episode_id="$1"
audit_mode="${2:-}"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../.." && pwd)"
canon_readme="$repo_root/artifacts/writing/episodes/$episode_id/canon/README.md"
summary_path="$repo_root/artifacts/writing/episodes/$episode_id/summary_v1.md"
audit_script="$repo_root/scripts/writing/audit_live_sync.py"

if [[ ! -f "$canon_readme" ]]; then
  echo "missing canon README: $canon_readme" >&2
  exit 1
fi

current_text_canon="$(sed -n 's/^- current_text_canon: //p' "$canon_readme" | head -n 1)"
if [[ -z "$current_text_canon" || "$current_text_canon" == "none" ]]; then
  echo "episode has no current_text_canon yet: $episode_id" >&2
  exit 1
fi

canon_path="$repo_root/artifacts/writing/episodes/$episode_id/canon/$current_text_canon"

echo "post-canon sync target"
echo "- episode_id: $episode_id"
echo "- canon: $canon_path"
if [[ -f "$summary_path" ]]; then
  echo "- summary: $summary_path"
else
  echo "- summary: missing ($summary_path)"
fi
echo
echo "sync targets"
python3 "$audit_script" --print-targets
echo
echo "recommended order"
echo "1. summary_v1.md and style_pattern_library.md update"
echo "2. required live docs update: narrative_state, episode_deltas, style_bible"
echo "3. conditional live docs update: story_arcs, foreshadow_registry"
echo "4. manual live docs check: master_map"

if [[ "$audit_mode" != "--no-audit" ]]; then
  echo
  python3 "$audit_script" --episode-id "$episode_id"
fi
