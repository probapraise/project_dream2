# 집필 주입 패킷

- episode_id: `ep002`
- packet_version: `v1`
- purpose: `draft_generation`
- target_output: `drafts/draft_<source>_v1.txt`
- recent_canon_1_path: `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
- recent_canon_1_sha256: `c735a280646418f27377c4fee2ccb1f749b64f8dfb115e24757de0fd52c3251b`
- recent_canon_2_path: `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v3.md`
- recent_canon_2_sha256: `7bfb24d6125718677474b396a512fd3a0c71f92adf15fadba887901bb0ce8b81`
- recent_canon_3_path: `none`
- recent_canon_3_sha256: `none`

## 역할
- 이 문서는 2화 집필 당시의 컨텍스트 패킷을 최신 구조 기준으로 사후 백필한 것이다.
- raw canon은 요약이 아니라 원문 파일 자체를 순서대로 주입한다.
- `world/live/docs/memory_tiers/*.md`는 raw canon window가 밀려날 때 놓치기 쉬운 상태값을 보정하는 global compiled memory다.
- `prompt_v1.md`는 마지막 비트 지시층이며, 문체와 설정 사실은 앞 문서가 먼저 고정한다.

## Authority order
1. `episode_style_constitution_v1.md`
2. `setting_brief_v1.md`
3. 최근 raw canon 원문
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
3. `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
4. `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v3.md`
5. `world/live/docs/memory_tiers/recent.md`
6. `world/live/docs/memory_tiers/current_arc.md`
7. `world/live/docs/memory_tiers/entity_registry.md`
8. `world/live/docs/memory_tiers/knowledge_state_registry.md`
9. `world/live/docs/memory_tiers/access_control_matrix.md`
10. `world/live/docs/memory_tiers/long_term.md`
11. `long_range_summary_v1.md`
12. `prompt_v1.md`

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
- 2화 시점에는 prior canon이 2회차뿐이라 recent raw canon도 2개만 주입한다.
- token이 빠듯하면 long-range summary보다 memory tiers를 먼저 유지한다.
- long-range 정보는 비어 있으므로 `현재 없음` 상태로 유지한다.
- 이 파일은 구조 백필용이므로, 당시 실제 집필 입력과 1:1 완전 복제는 아니다.
