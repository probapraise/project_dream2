# Phase 2 Report (Collision Scan)

- change_id: CR-20260308-003
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 기능/제도 내용은 이미 확정되어 있고, 이번 변경은 공식 용어를 정하는 수준이다.
  - live 계층만 명칭을 통일하면 충분하며, 과거 케이스 CR-20260308-002는 당시 표현을 보존해도 운영상 문제 없다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 공식 명칭 부재로 설명형 표현이 난립 | live world bible, character cards, index | `계승조회식`으로 통일하고 첫 설명만 기능형으로 유지 | 계승조회식 | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - master_map과 change log에도 명칭 확정 기록을 추가한다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 기능 설명을 삭제하지 않고, 명칭만 공식화한다.

## 5. 판단 근거
- world_bible_index 참조:
  - world/live/docs/world_bible_index_v2.md
- cross-reference 참조:
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md

## 6. 분기 결정
- branch: minor
- reason: 새로운 설정 추가가 아니라 이미 반영된 제도의 공식 용어 확정 및 문구 통일 작업이다.

## 7. 작가 승인
- approved: yes
- note: 사용자가 명칭을 `계승조회식`으로 확정했다.
