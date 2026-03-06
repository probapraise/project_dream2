# dynamic_guide

## 목적
- `quarantine/`에 보존된 레거시 문서에서 재사용 가능한 운영 원칙만 추출해 활성 문서에 반영한다.
- 특정 세계관 시점값/고정 수치/고정 매핑은 정본 규칙으로 승격하지 않는다.

## 핵심 원칙
- SSOT와 실행 뷰를 분리한다.
  - SSOT: `world_bible/`, `population/`
  - 실행 뷰: `docs/*.md` 경량 파생 문서
- 구조는 강제 스키마가 아니라 선택 모듈로 유지한다.
  - 예: `nodes/edges/events/glossary/claims/taxonomy_terms`
- 인덱스는 동적 파생으로 생성한다.
  - `frontmatter` 우선, 누락 시 본문 추론, 추론 표기 유지

## 재사용 가능한 카드 패턴
- 캐릭터 최소 카드:
  - `offline_core + online_persona + rationale`
- 커뮤니티/보드 문화 카드:
  - `tone`, `anonymity_mode`, `taboos`, `content_types`, `moderation_style`
  - `user_power_structure`, `incident_patterns`, `meme_seeds`
- 시뮬레이션 절차:
  - 입력 정의 -> 라운드 루프 -> 정보 격리 -> 수렴 -> `official/explore` 분리

## 폐기 기준
- 고정 매핑:
  - `Board(B01~B18) -> Zone(A~D)` 류 강제 규칙
- 고정 총량/고정 분배:
  - 인원수, 비율, 필드 개수 강제
- 고정 포맷/고정 길이:
  - 토큰/문자/출력 개수 강제
- 특정 시점 콘텐츠를 일반 규칙으로 승격:
  - 리트콘 사례, 단일 프로젝트 전용 사건값

## 반영 위치
- 캐릭터: `docs/character_index_v2.md`
- 시뮬레이션: `docs/simulation_playbook.md`
- 커뮤니티: `docs/community_map.md`
- 정합성 운영: `world_bible/WB-0002_loreops_canon_control.md`

## 근거 보관 위치
- `quarantine/world_bible/WB-0023_appendix_schema_cheatsheet.md`
- `quarantine/world_bible/WB-0027_appendix_character_pack_schema.md`
- `quarantine/docs/character_index_v2.md`
- `quarantine/docs/simulation_playbook.md`
- `quarantine/docs/community_map.md`
