# 집필 주입 패킷 템플릿

- episode_id: `<episode_id>`
- packet_version: `v1`
- purpose: `draft_generation`
- target_output: `drafts/draft_<source>_v1.txt`

## 역할
- 이 문서는 이번 화 집필에 사용할 컨텍스트 패킷의 주입 순서와 우선순위를 명시한다.
- raw canon은 이 문서에 요약하지 않고, 원문 파일 자체를 순서대로 주입한다.
- `prompt_vN.md`는 패킷의 마지막 지시층이다. 문체와 설정 사실을 새로 정의하지 않는다.

## Authority order
1. `episode_style_constitution_v1.md`
2. `setting_brief_v1.md`
3. 최근 3회차 raw canon 원문 (최신 회차 우선)
4. `long_range_summary_v1.md`
5. `prompt_v1.md`

## Conflict rules
- 사실 충돌 시 `raw canon > long_range_summary > prompt_v1.md`
- 최신성 충돌 시 더 최근 회차 canon이 우선한다.
- 문체 충돌 시 `episode_style_constitution_v1.md`가 우선한다.
- `prompt_v1.md`는 이번 화 비트와 목표를 지시하지만 기존 캐논 사실을 덮어쓰지 않는다.

## Injection order
1. `episode_style_constitution_v1.md`
2. `setting_brief_v1.md`
3. `<recent_canon_1>`
4. `<recent_canon_2>`
5. `<recent_canon_3>`
6. `long_range_summary_v1.md`
7. `prompt_v1.md`

## Optional companion docs
- 관련 인물 VFP/캐릭터 카드:
  - ``
- 필요 시 참고:
  - `world/live/docs/narrative_state.md`
  - `world/live/docs/foreshadow_registry.md`

## Operator notes
- 토큰이 빠듯해도 최신 raw canon부터 유지한다.
- long-range 정보가 비면 `현재 없음`으로 적고 빈 문서로 두지 않는다.
- 이번 화에 안 쓰는 설정은 setting brief에 넣지 않는다.
