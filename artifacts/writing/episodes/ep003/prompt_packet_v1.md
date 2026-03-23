# 집필 주입 패킷

- episode_id: `ep003`
- packet_version: `v1`
- purpose: `draft_generation`
- target_output: `drafts/draft_<source>_v1.txt`
- recent_canon_1_path: `artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md`
- recent_canon_1_sha256: `1d6d85e7574178720cec2be3ebbef994f8d0a33a8d0828b7ce5835fb3c7b757d`
- recent_canon_2_path: `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
- recent_canon_2_sha256: `c735a280646418f27377c4fee2ccb1f749b64f8dfb115e24757de0fd52c3251b`
- recent_canon_3_path: `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v3.md`
- recent_canon_3_sha256: `7bfb24d6125718677474b396a512fd3a0c71f92adf15fadba887901bb0ce8b81`

## 역할
- 이 문서는 이번 화 집필에 사용할 컨텍스트 패킷의 주입 순서와 우선순위를 명시한다.
- raw canon은 이 문서에 요약하지 않고, 원문 파일 자체를 순서대로 주입한다.
- `world/live/docs/memory_tiers/*.md`는 raw canon window가 밀려갈 때도 유지돼야 하는 최근성/현재 아크/동적 엔티티/사실별 지식 비대칭/접근 권한/장기 불변값을 보정한다.
- `prompt_vN.md`는 패킷의 마지막 지시층이다. 문체와 설정 사실을 새로 정의하지 않는다.

## Authority order
1. `episode_style_constitution_v1.md`
2. `setting_brief_v1.md`
3. 최근 3회차 raw canon 원문 (최신 회차 우선)
4. `world/live/docs/memory_tiers/recent.md`
5. `world/live/docs/memory_tiers/current_arc.md`
6. `world/live/docs/memory_tiers/entity_registry.md`
7. `world/live/docs/memory_tiers/knowledge_state_registry.md`
8. `world/live/docs/memory_tiers/access_control_matrix.md`
9. `world/live/docs/memory_tiers/long_term.md`
10. `long_range_summary_v1.md`
11. `prompt_v1.md`

## Conflict rules
- 사실 충돌 시 `raw canon > memory_tiers > long_range_summary > prompt_v1.md`
- 최신성 충돌 시 더 최근 회차 canon이 우선한다.
- 문체 충돌 시 `episode_style_constitution_v1.md`가 우선한다.
- `prompt_v1.md`는 이번 화 비트와 목표를 지시하지만 기존 캐논 사실을 덮어쓰지 않는다.

## Injection order
1. `episode_style_constitution_v1.md`
2. `setting_brief_v1.md`
3. `artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md`
4. `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
5. `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v3.md`
6. `world/live/docs/memory_tiers/recent.md`
7. `world/live/docs/memory_tiers/current_arc.md`
8. `world/live/docs/memory_tiers/entity_registry.md`
9. `world/live/docs/memory_tiers/knowledge_state_registry.md`
10. `world/live/docs/memory_tiers/access_control_matrix.md`
11. `world/live/docs/memory_tiers/long_term.md`
12. `long_range_summary_v1.md`
13. `prompt_v1.md`

## Optional companion docs
- 관련 인물 VFP/캐릭터 카드:
  - `world/live/population/core_cast/NC-0001_P-1027.md`
- upstream source docs (검증이 필요할 때만):
  - `world/live/docs/narrative_state.md`
  - `world/live/docs/story_arcs.md`
  - `world/live/docs/foreshadow_registry.md`
  - `world/live/docs/episode_deltas.md`
  - `world/live/docs/pre_academy_checkpoint_plan.md`

## Operator notes
- 최근 raw canon 3회차는 기본값이지 고정 법칙이 아니다. continuity 체인이 길면 window를 늘릴 수 있다.
- 토큰이 빠듯해도 최신 raw canon과 memory tiers를 먼저 유지한다.
- long-range 정보가 비면 `현재 없음`으로 적고 빈 문서로 두지 않는다.
- 이번 화에 안 쓰는 설정은 setting brief에 넣지 않는다.
- pre-academy 구간에서는 `world/live/docs/pre_academy_checkpoint_plan.md`를 planning companion으로 같이 본다.
