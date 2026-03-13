# 집필 주입 패킷

- episode_id: `ep000_prologue`
- packet_version: `v1`
- purpose: `draft_generation`
- target_output: `drafts/draft_<source>_v1.txt`
- recent_canon_1_path: `none`
- recent_canon_1_sha256: `none`
- recent_canon_2_path: `none`
- recent_canon_2_sha256: `none`
- recent_canon_3_path: `none`
- recent_canon_3_sha256: `none`

## 역할
- 이 문서는 프롤로그 집필 입력을 현재 패킷 구조 기준으로 사후 백필한 운영 기록이다.
- 시리즈 시작점이므로 prior raw canon slot은 모두 비어 있다.
- `world/live/docs/memory_tiers/*.md`는 현재 저장소 운영 체계의 기본층이지만, historical replay 시에는 ep000 이후 정보가 섞이지 않도록 주의해야 한다.

## Authority order
1. `episode_style_constitution_v1.md`
2. `setting_brief_v1.md`
3. prior raw canon 없음 (`ep000_prologue`는 시리즈 시작점)
4. `world/live/docs/memory_tiers/recent.md`
5. `world/live/docs/memory_tiers/current_arc.md`
6. `world/live/docs/memory_tiers/entity_registry.md`
7. `world/live/docs/memory_tiers/knowledge_state_registry.md`
8. `world/live/docs/memory_tiers/access_control_matrix.md`
9. `world/live/docs/memory_tiers/long_term.md`
10. `long_range_summary_v1.md`
11. `prompt_v1.md`

## Conflict rules
- 사실 충돌 시 `episode-local docs > memory_tiers > prompt_v1.md`로 본다.
- historical replay 시 ep000 이후에 확정된 memory tier 정보가 프롤로그 원문을 덮어쓰면 안 된다.
- 문체 충돌 시 `episode_style_constitution_v1.md`가 우선한다.
- `prompt_v1.md`는 이번 화 비트와 목표를 지시하지만 episode-local 설정 사실을 덮어쓰지 않는다.

## Injection order
1. `episode_style_constitution_v1.md`
2. `setting_brief_v1.md`
3. `world/live/docs/memory_tiers/recent.md`
4. `world/live/docs/memory_tiers/current_arc.md`
5. `world/live/docs/memory_tiers/entity_registry.md`
6. `world/live/docs/memory_tiers/knowledge_state_registry.md`
7. `world/live/docs/memory_tiers/access_control_matrix.md`
8. `world/live/docs/memory_tiers/long_term.md`
9. `long_range_summary_v1.md`
10. `prompt_v1.md`

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
- 프롤로그는 prior raw canon이 없으므로 episode-local style/setting/prompt 문서의 비중이 특히 크다.
- 현재 global memory tiers는 ep002 시점까지 누적된 운영 문서이므로, 프롤로그 재생성 용도로는 episode-local docs와 raw canon 없음 상태를 더 강하게 본다.
- 이 파일은 구조 표준화용 백필 문서이며, 당시 실제 입력을 1:1 완전 복제한 것은 아니다.
