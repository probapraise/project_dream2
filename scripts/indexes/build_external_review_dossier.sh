#!/usr/bin/env bash
set -euo pipefail

SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"
BUNDLE_DIR="${ROOT_DIR}/world/live"
INDEX_FILE="${BUNDLE_DIR}/docs/world_bible_index_v2.md"
OUTPUT_FILE="${1:-${ROOT_DIR}/artifacts/briefings/external_review/world_dossier_external_review_full_$(date +%Y%m%d).md}"

mkdir -p "$(dirname "$OUTPUT_FILE")"

TMP_FILE="$(mktemp)"
trap 'rm -f "$TMP_FILE"' EXIT

mapfile -t WORLD_BIBLE_REL_PATHS < <(sed -n 's/^  - file: //p' "$INDEX_FILE" | sed 's#^#world/live/#')

FULL_SUPPLEMENT_REL_PATHS=(
  "world/live/docs/narrative_state.md"
  "world/live/docs/story_arcs.md"
  "world/live/docs/foreshadow_registry.md"
  "world/live/docs/episode_deltas.md"
  "world/live/docs/community_map.md"
  "world/live/docs/community_memory.md"
  "world/live/docs/community_grammar_layer_a.md"
  "world/live/docs/community_grammar_layer_b.md"
  "world/live/docs/core_cast_bootstrap_v1.md"
  "world/live/population/core_cast/NC-0001_P-1027.md"
)

strip_frontmatter() {
  local file="$1"
  awk '
    NR == 1 && $0 == "---" {in_fm=1; next}
    in_fm && $0 == "---" {in_fm=0; next}
    in_fm {next}
    {print}
  ' "$file"
}

yaml_field() {
  local key="$1"
  local file="$2"
  grep -m1 "^${key}:" "$file" | sed -E "s/^${key}:[[:space:]]*//; s/^\"//; s/\"$//" || true
}

heading_field() {
  local file="$1"
  sed -n 's/^# //p' "$file" | head -n 1
}

doc_title() {
  local file="$1"
  local title
  title="$(yaml_field "title" "$file")"
  if [[ -n "$title" ]]; then
    printf '%s\n' "$title"
  else
    heading_field "$file"
  fi
}

doc_visibility() {
  local file="$1"
  yaml_field "visibility" "$file"
}

doc_id() {
  local file="$1"
  yaml_field "id" "$file"
}

append_full_doc() {
  local rel="$1"
  local abs="${ROOT_DIR}/${rel}"
  local title visibility id

  title="$(doc_title "$abs")"
  visibility="$(doc_visibility "$abs")"
  id="$(doc_id "$abs")"

  {
    if [[ -n "$id" ]]; then
      echo "## [${id}] ${title}"
    else
      echo "## ${title}"
    fi
    echo
    echo "- source_path: \`${rel}\`"
    echo "- inclusion_mode: full"
    if [[ -n "$visibility" ]]; then
      echo "- visibility: ${visibility}"
    fi
    echo
    strip_frontmatter "$abs"
    echo
  } >> "$TMP_FILE"
}

append_character_index_excerpt() {
  local rel="world/live/docs/character_index_v2.md"
  local abs="${ROOT_DIR}/${rel}"

  {
    echo "## character_index_v2 (selected excerpt)"
    echo
    echo "- source_path: \`${rel}\`"
    echo "- inclusion_mode: excerpt"
    echo "- excerpt_rule: file header + status registry + background distribution + dorm distribution only"
    echo "- omitted: coordinate occupancy registry and large reverse-index tables"
    echo
    awk '
      $0 ~ /^## 3\) Coordinate Occupancy Registry/ {exit}
      {print}
    ' "$abs"
    echo
  } >> "$TMP_FILE"
}

append_handoff_excerpt() {
  local rel="docs/handoff/next_steps.md"
  local abs="${ROOT_DIR}/${rel}"

  {
    echo "## 다음 작업 목록 (current-state excerpt)"
    echo
    echo "- source_path: \`${rel}\`"
    echo "- inclusion_mode: excerpt"
    echo "- excerpt_rule: \`현재 실제 상태 요약\` section only"
    echo "- omitted: priority backlog and future task list"
    echo
    awk '
      $0 ~ /^## 현재 실제 상태 요약/ {in_range=1}
      $0 ~ /^## 우선순위 A: 지금 바로 할 일/ {exit}
      in_range {print}
    ' "$abs"
    echo
  } >> "$TMP_FILE"
}

append_manifest() {
  {
    echo "## Included Source Manifest"
    echo
    echo "### Full world bible documents"
    echo
    for rel in "${WORLD_BIBLE_REL_PATHS[@]}"; do
      echo "- \`${rel}\`"
    done
    echo
    echo "### Full live-state supplements"
    echo
    for rel in "${FULL_SUPPLEMENT_REL_PATHS[@]}"; do
      echo "- \`${rel}\`"
    done
    echo
    echo "### Selected excerpts"
    echo
    echo "- \`world/live/docs/character_index_v2.md\`"
    echo "- \`docs/handoff/next_steps.md\`"
    echo
  } >> "$TMP_FILE"
}

append_intro() {
  local repo_head
  repo_head="$(git -C "$ROOT_DIR" rev-parse --short HEAD)"

  {
    echo "# Project Dream2 Full World Dossier for External Review"
    echo
    echo "- generated_at: $(date +%F)"
    echo "- repo_head: \`${repo_head}\`"
    echo "- document_role: 외부 고급 모델용 상세 설정 도감"
    echo "- ssot_status: non-SSOT compiled artifact"
    echo "- source_priority:"
    echo "  - 1. \`world/live/\`"
    echo "  - 2. \`docs/handoff/next_steps.md\`"
    echo "  - 3. \`artifacts/writing/episodes/*/canon/README.md\`"
    echo "- visibility_policy: 본 문서는 \`[PUBLIC]\`, \`[CONFIDENTIAL]\`, \`[META]\`를 모두 포함한다."
    echo "- intended_use:"
    echo "  - 세계관 정합성 전수 점검"
    echo "  - 빈틈/과밀 구간 탐지"
    echo "  - 장기 서사/제도/플랫폼 구조 아이디어 도출"
    echo "- excluded_by_default:"
    echo "  - \`world_ops/\` 운영 절차"
    echo "  - \`world/archive/quarantine/\`"
    echo "  - \`artifacts/runs/\`"
    echo "  - \`artifacts/batch/\`"
    echo "  - episode 원고 전문"
    echo "- known_drift:"
    echo "  - \`world/live/docs/narrative_state.md\`는 아직 \`latest_canon_episode: ep001\` 상태다."
    echo "  - handoff와 canon README 기준 현재 확정 캐논 frontier는 \`ep002\`까지다."
    echo "  - 이 도감은 현재 live state + handoff delta를 함께 반영한다."
    echo
    echo "## Reading Note"
    echo
    echo "- 이 파일은 짧은 브리핑이 아니라, 외부 모델이 한 번에 훑고 구조 점검을 할 수 있도록 active 설정을 거의 전부 싣는 목적의 compiled dossier다."
    echo "- world bible 활성 문서는 전부 full inclusion으로 수록한다."
    echo "- live-state 문서는 현재 서사/인물/커뮤니티 판단에 필요한 문서만 full inclusion 또는 selected excerpt로 붙인다."
    echo "- 운영 로그와 장편 원고 전문은 의도적으로 제외한다."
    echo
    echo "## Review Focus Suggested to External Model"
    echo
    echo "- 설정 간 충돌 또는 중복 설명"
    echo "- 초반 도입부에서 과밀한 제도/용어 축"
    echo "- 학술원 진입 이전 저택 파트의 긴장 유지 방식"
    echo "- 각인광장/권한 경제/문장비전 축의 차별점과 취약점"
    echo "- Layer B와 전체 작품 톤의 균형"
    echo
  } >> "$TMP_FILE"
}

append_outro() {
  {
    echo "## External Review Questions"
    echo
    echo "1. 현재 설정 패키지 전체를 봤을 때, 가장 강한 차별점과 가장 취약한 과밀 구간은 각각 무엇인가."
    echo "2. 제도 설정 중 서로 충돌하거나 암묵적 보정이 필요한 항목은 어디인가."
    echo "3. 렌바렌 가문, 계승조회식, 조기 수련 금지, 학술원 구조가 초반 서사에서 과설명 없이 작동하려면 어떤 정보가 앞당겨지거나 뒤로 밀려야 하는가."
    echo "4. 각인광장과 권한 경제는 장기 메인 엔진으로 충분히 강한가. 더 선명하게 만들 핵심 장면/제도는 무엇인가."
    echo "5. Layer B와 커뮤니티 구조는 독창성 강화 요소인가, 톤 오염 리스크가 더 큰가. 균형점은 어디인가."
    echo "6. 하급 과정 3년 -> 상급 과정 진입성취평가 점프 구조가 가장 설득력 있게 작동하려면, 하급 과정 파트에서 반드시 보여줘야 할 경험은 무엇인가."
    echo
  } >> "$TMP_FILE"
}

: > "$TMP_FILE"
append_intro
append_manifest

{
  echo "## Part I. Active World Bible Compilation"
  echo
} >> "$TMP_FILE"

for rel in "${WORLD_BIBLE_REL_PATHS[@]}"; do
  append_full_doc "$rel"
done

{
  echo "## Part II. Live-State Supplements"
  echo
} >> "$TMP_FILE"

for rel in "${FULL_SUPPLEMENT_REL_PATHS[@]}"; do
  append_full_doc "$rel"
done

append_character_index_excerpt
append_handoff_excerpt
append_outro

mv "$TMP_FILE" "$OUTPUT_FILE"
trap - EXIT

echo "generated: $OUTPUT_FILE"
