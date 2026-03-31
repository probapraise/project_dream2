# 집필 주입 패킷

- episode_id: `ep004`
- packet_version: `v1`
- purpose: `draft_generation`
- target_output: `drafts/draft_<source>_v1.txt`
- recent_canon_1_path: `artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md`
- recent_canon_1_sha256: `a132f2c3102c009d65daaba9e2f5ff37e73e092320fb389c1f6470bdab8b135a`
- recent_canon_2_path: `artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md`
- recent_canon_2_sha256: `1d6d85e7574178720cec2be3ebbef994f8d0a33a8d0828b7ce5835fb3c7b757d`
- recent_canon_3_path: `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
- recent_canon_3_sha256: `1fd1ad585fe82ca3240b2590ad8a2dfe0651d948976967bee92449d95dea6c95`

## 역할
- 이 문서는 이번 화 집필에 사용할 컨텍스트 패킷의 주입 순서와 우선순위를 명시한다.
- raw canon은 이 문서에 요약하지 않고, 원문 파일 자체를 순서대로 주입한다.
- `world/live/docs/memory_tiers/*.md`는 raw canon이 밀려나며 사라지기 쉬운 `최근성 / 현재 아크 / 동적 엔티티 / 사실별 지식 비대칭 / 접근 권한 / 장기 불변값`을 보정하는 global compiled memory다.
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
10. `long_range_summary_v1.md` (필요한 경우에만 보조)
11. `prompt_v1.md`

## Conflict rules
- 사실 충돌 시 `raw canon > memory_tiers > long_range_summary > prompt_v1.md`
- 최신성 충돌 시 더 최근 회차 canon이 우선한다.
- 문체 충돌 시 `episode_style_constitution_v1.md`가 우선한다.
- `prompt_v1.md`는 이번 화 비트와 목표를 지시하지만 기존 캐논 사실을 덮어쓰지 않는다.

## Injection order
1. `episode_style_constitution_v1.md`
2. `setting_brief_v1.md`
3. `artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md`
4. `artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md`
5. `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
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
  - `world/live/population/core_cast/NC-0001_P-1027.md` (키리온 VFP — Beat 2 커뮤니티 레지스터 전환 참조)
  - `world/live/external/EX-0004.yaml` (리리아 화법 — Beat 2 대화 톤)
  - `world/live/external/EX-0003.yaml` (데리온 화법 — Beat 4 침묵)
  - `world/live/external/EX-0002.yaml` (셀리아 — Beat 4 그라비온 혈통 참조)
  - `world/live/external/EX-0001.yaml` (칼리온 — Beat 3 인정 톤)
- Layer B 참조 (Beat 2-d 한정):
  - `world/live/docs/community_grammar_layer_b.md` (ATOM-001, 002, 003, 009 / GRAMMAR-001, 002)
- upstream source docs (검증이 필요할 때만):
  - `world/live/docs/narrative_state.md`
  - `world/live/docs/story_arcs.md`
  - `world/live/docs/foreshadow_registry.md`
  - `world/live/docs/episode_deltas.md`
  - `world/live/docs/pre_academy_checkpoint_plan.md`
  - `world/live/world_bible/WB-0026_appendix_crest_arcana.md` (계승조회식/문장비전 팩트체크)

## Operator notes
- 최근 raw canon 3회차는 기본값이지 고정 법칙이 아니다. scene continuity가 길면 window를 늘릴 수 있다.
- 토큰이 빠듯해도 최신 raw canon과 `memory_tiers`를 먼저 유지하고, 그 다음 `long_range_summary_vN.md`를 줄인다.
- long-range 정보가 비면 `현재 없음`으로 적고 빈 문서로 두지 않는다.
- 이번 화에 안 쓰는 설정은 setting brief에 넣지 않는다.
- raw canon이 3회차보다 적으면 남는 슬롯은 `none`으로 둔다.
- pre-academy 구간에서는 `world/live/docs/pre_academy_checkpoint_plan.md`를 집필 직전 planning companion으로 같이 확인한다.
