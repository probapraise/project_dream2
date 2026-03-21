# 집필 주입 패킷

- episode_id: `ep003`
- packet_version: `v2`
- purpose: `draft_generation`
- target_output: `drafts/draft_<source>_v2.txt`
- recent_canon_1_path: `artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md`
- recent_canon_1_sha256: `8a9c63933bf4975d265be511c0ecc613efab76af6de8c926cf6311450811346c`
- recent_canon_2_path: `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
- recent_canon_2_sha256: `46442b0d76ef421adbd5fd48a8058fefc202caf1e19a8fdbb9104b1695f0f2dd`
- recent_canon_3_path: `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v3.md`
- recent_canon_3_sha256: `952e14dde9e50324f7d34e37493d96e15a6290e2310a04d9bcabbd958875269a`

## 역할
- 이 문서는 이번 화 집필에 사용할 컨텍스트 패킷의 주입 순서와 우선순위를 명시한다.
- raw canon은 이 문서에 요약하지 않고, 원문 파일 자체를 순서대로 주입한다.
- `world/live/docs/memory_tiers/*.md`는 raw canon window가 밀려갈 때도 유지돼야 하는 최근성/현재 아크/동적 엔티티/사실별 지식 비대칭/접근 권한/장기 불변값을 보정한다.
- `prompt_v2.md`는 패킷의 마지막 지시층이다. 문체와 설정 사실을 새로 정의하지 않는다.

## Authority order
1. `episode_style_constitution_v2.md`
2. `setting_brief_v2.md`
3. 최근 3회차 raw canon 원문 (최신 회차 우선)
4. `world/live/docs/memory_tiers/recent.md`
5. `world/live/docs/memory_tiers/current_arc.md`
6. `world/live/docs/memory_tiers/entity_registry.md`
7. `world/live/docs/memory_tiers/knowledge_state_registry.md`
8. `world/live/docs/memory_tiers/access_control_matrix.md`
9. `world/live/docs/memory_tiers/long_term.md`
10. `long_range_summary_v1.md`
11. `prompt_v2.md`

## Conflict rules
- 사실 충돌 시 `raw canon > memory_tiers > long_range_summary > prompt_v2.md`
- 최신성 충돌 시 더 최근 회차 canon이 우선한다.
- 문체 충돌 시 `episode_style_constitution_v2.md`가 우선한다.
- `prompt_v2.md`는 이번 화 비트와 목표를 지시하지만 기존 캐논 사실을 덮어쓰지 않는다.

## Injection order
1. `episode_style_constitution_v2.md`
2. `setting_brief_v2.md`
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
13. `prompt_v2.md`

## Optional companion docs
- 관련 인물 캐릭터 카드:
  - `world/live/external/EX-0001.yaml` (칼리온)
  - `world/live/external/EX-0003.yaml` (데리온)
  - `world/live/external/EX-0004.yaml` (리리아)
- 무흔술 교리:
  - `world/live/world_bible/WB-0030_appendix_muhunsul_doctrine.md`
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
- 이번 화 연무장 장면의 무흔술 관련 제약은 `setting_brief_v2.md`의 `무흔술 관련 장면 제약` 섹션이 권위다. WB-0030은 참고용이지 본문에 직접 노출할 용도가 아니다.
