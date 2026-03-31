# 집필 주입 패킷

- episode_id: `ep006`
- packet_version: `v1`
- purpose: `draft_generation`
- target_output: `drafts/draft_<source>_v1.txt`
- author_preference_registry_path: `artifacts/writing/style/author_preference_registry.md`
- recent_canon_1_path: `artifacts/writing/episodes/ep005/canon/5화_리라이트_v1.md`
- recent_canon_1_sha256: `d21365cdd3a435619872316e13b9cd408c46bcb65f97490e71dfd074370d45e8`
- recent_canon_2_path: `artifacts/writing/episodes/ep004/canon/4화_리라이트_v1.md`
- recent_canon_2_sha256: `4b3b443b7e80f44e51636775e8322dbf82d028cdba23febecf38f58b53182a3e`
- recent_canon_3_path: `artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md`
- recent_canon_3_sha256: `abbc7ade90d6f234489ce1b6d4b65205bae0964e6832e1f21114025bb13aef51`

## 역할
- 이 문서는 이번 화 집필에 사용할 컨텍스트 패킷의 주입 순서와 우선순위를 명시한다.
- `author_preference_registry.md`는 과거 회차 diff에서 검증된 `작가의 기본 취향` 레이어다.
- raw canon은 이 문서에 요약하지 않고, 원문 파일 자체를 순서대로 주입한다.
- `world/live/docs/memory_tiers/*.md`는 raw canon이 밀려나며 사라지기 쉬운 `최근성 / 현재 아크 / 동적 엔티티 / 사실별 지식 비대칭 / 접근 권한 / 장기 불변값`을 보정하는 global compiled memory다.
- `prompt_vN.md`는 패킷의 마지막 지시층이다. 문체와 설정 사실을 새로 정의하지 않는다.

## Authority order
1. `episode_style_constitution_v1.md`
2. `artifacts/writing/style/author_preference_registry.md`
3. `setting_brief_v1.md`
4. 최근 3회차 raw canon 원문 (최신 회차 우선)
5. `world/live/docs/memory_tiers/recent.md`
6. `world/live/docs/memory_tiers/current_arc.md`
7. `world/live/docs/memory_tiers/entity_registry.md`
8. `world/live/docs/memory_tiers/knowledge_state_registry.md`
9. `world/live/docs/memory_tiers/access_control_matrix.md`
10. `world/live/docs/memory_tiers/long_term.md`
11. `long_range_summary_v1.md` (필요한 경우에만 보조)
12. `prompt_v1.md`

## Conflict rules
- 사실 충돌 시 `raw canon > memory_tiers > long_range_summary > prompt_v1.md`
- 최신성 충돌 시 더 최근 회차 canon이 우선한다.
- 문체/취향 충돌 시 `episode_style_constitution_v1.md > author_preference_registry.md > prompt_v1.md`를 따른다.
- `prompt_v1.md`는 이번 화 비트와 목표를 지시하지만 기존 캐논 사실을 덮어쓰지 않는다.

## Injection order
1. `artifacts/writing/style/author_preference_registry.md`
2. `episode_style_constitution_v1.md`
3. `setting_brief_v1.md`
4. `artifacts/writing/episodes/ep005/canon/5화_리라이트_v1.md`
5. `artifacts/writing/episodes/ep004/canon/4화_리라이트_v1.md`
6. `artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md`
7. `world/live/docs/memory_tiers/recent.md`
8. `world/live/docs/memory_tiers/current_arc.md`
9. `world/live/docs/memory_tiers/entity_registry.md`
10. `world/live/docs/memory_tiers/knowledge_state_registry.md`
11. `world/live/docs/memory_tiers/access_control_matrix.md`
12. `world/live/docs/memory_tiers/long_term.md`
13. `long_range_summary_v1.md`
14. `prompt_v1.md`

## Optional companion docs
- 관련 인물 VFP/캐릭터 카드:
  - ``
- upstream source docs (검증이 필요할 때만):
  - `world/live/docs/narrative_state.md`
  - `world/live/docs/story_arcs.md`
  - `world/live/docs/foreshadow_registry.md`
  - `world/live/docs/episode_deltas.md`
  - `world/live/docs/pre_academy_checkpoint_plan.md`

## Operator notes
- 최근 raw canon 3회차는 기본값이지 고정 법칙이 아니다. scene continuity가 길면 window를 늘릴 수 있다.
- 토큰이 빠듯해도 `author_preference_registry.md`, 최신 raw canon, `memory_tiers`를 먼저 유지하고, 그 다음 `long_range_summary_vN.md`를 줄인다.
- long-range 정보가 비면 `현재 없음`으로 적고 빈 문서로 두지 않는다.
- 이번 화에 안 쓰는 설정은 setting brief에 넣지 않는다.
- raw canon이 3회차보다 적으면 남는 슬롯은 `none`으로 둔다.
- pre-academy 구간에서는 `world/live/docs/pre_academy_checkpoint_plan.md`를 집필 직전 planning companion으로 같이 확인한다.
- `author_preference_registry.md`에는 반복 검증된 취향만 승격한다. continuity 수정이나 1회성 플롯 필요는 넣지 않는다.
