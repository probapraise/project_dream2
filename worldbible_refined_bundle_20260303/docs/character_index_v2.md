# character_index_v2 (dynamic)

- generated_at: 2026-03-04
- mode: dynamic
- note: 고정 board/zone 맵핑 기반 인덱스는 사용하지 않는다.

## usage
- 현재 `community_map.md` 기준으로 필요한 축만 임시 인덱싱한다.
- 기본 축: affiliation, role_tags, activity_intensity, topic_affinity
- board/zone 고정 분류는 금지한다.

## bootstrap
- 아직 동적 인덱스 재생성 전.
- 캐릭터 원본은 `characters/`를 SSOT로 사용.
