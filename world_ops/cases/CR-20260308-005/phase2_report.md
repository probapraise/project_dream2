# Phase 2 Report (Collision Scan)

- change_id: CR-20260308-005
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0018_evidence_records_glossary.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 기존 조기 수련 금지 규정은 있었지만, 왜 왕실이 이를 실제로 적발할 수 있는지의 감정적 근거가 비어 있었다.
  - 이번 변경은 규정의 집행 가능성을 보강하는 설명 추가이며, 기존 식흔/잔흔/포렌식 축과 자연스럽게 이어진다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 조기 수련 금지 규정의 실효 근거 부재 | WB-0005, WB-0009, WB-0026 | 사용 경험자와 미사용자의 마나핵/회로 감정 차이를 명시 | 마나핵 감정, 조기 수련 | resolved |
| 조사에서 어떤 증거를 보는지 불명확 | WB-0018 | 마나핵/회로 감정을 증거 유형으로 추가 | 포렌식, 증거 | resolved |
| 키리온 개인 리스크가 추상적 | NC-0001 | 조기 시전 시 변명 여지가 급감한다는 점 추가 | NC-0001 | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - 인덱스와 change log까지 갱신해 검색 경로 누락을 막는다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 학술원/경제 문서까지 확장하지 않고, 직접 관련된 마법/증거/권력 문서에 한정한다.

## 5. 판단 근거
- world_bible_index 참조:
  - world/live/docs/world_bible_index_v2.md
- cross-reference 참조:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0018_evidence_records_glossary.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/population/core_cast/NC-0001_P-1027.md

## 6. 분기 결정
- branch: minor
- reason: 제도 자체를 바꾸는 retcon이 아니라, 이미 도입된 규정의 집행 가능성을 설명하는 보강 문구 추가다.

## 7. 작가 승인
- approved: yes
- note: 사용자가 직접 실효 근거와 예외를 명시했다.
