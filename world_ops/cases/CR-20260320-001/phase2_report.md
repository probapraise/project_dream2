# Phase 2 Report (Collision Scan)

- change_id: CR-20260320-001
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0003.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md

## 2. 충돌 후보
- [x] 없음
- details:
  - `수련 초월`이 실재한다는 기존 규칙은 유지해야 하므로, "제도권 기사 교범의 큰 비중이 의례형 동작"이라는 설명으로 한정해 정리한다.
  - `무흔술`을 벨쿠란만의 유일 기술로 쓰면 과도하므로, 세계 전역에 산발적 비마나 실전술이 존재하되 `수경원`이 이를 가장 제도적으로 체계화했다는 방향으로 정리한다.
  - 데리온의 강압적 훈련 동기를 새로 만들기보다, 기존 `타가문 집행자 대비` 축 위에 `무흔술` 명칭과 전승 맥락만 덧붙이는 것이 정합적이다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 기사/무인의 공인 초월 경로가 약화된 것처럼 읽힐 수 있음 | `WB-0005` 수련 초월 섹션 | 수련 초월의 실재성은 유지하고, 제도권 초중급 교범의 교육 방식만 의례형으로 규정 | 수련 초월, 기사 교범, 의례형 동작 | resolved |
| `무흔술`이 벨쿠란 독점처럼 과장될 수 있음 | `WB-0005`, handoff | 타국 변경/암살자/종교 집단 등 산발적 존재를 명시 | 무흔술, 비마나 실전술, 변경 | resolved |
| 데리온의 훈련 동기가 기존 카드와 따로 놀 수 있음 | `EX-0003`, `NC-0001` | 기존 보호 충동/질투 축은 유지하고, 훈련 내용만 `무흔술` 기초로 구체화 | 데리온, 키리온, 연무장 | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - `WB-0026` 렌바렌 상세 부록까지 함께 갱신해 secret-family SSOT를 보완했다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 새 파일 추가 없이 기존 SSOT 섹션에 최소 범위로 삽입하는 편이 적절하다.

## 5. 판단 근거
- world_bible_index 참조: 없음 (기존 파일 추가/삭제 없음)
- cross-reference 참조:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0003.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/long_term.md

## 6. 분기 결정
- branch: minor
- reason: 기존 문서 내부 정의 보강과 캐릭터 카드/운영 로그 동기화만 필요하며, 신규 파일 구조 변경이나 외부 모델 재작성 경로가 필요하지 않다.

## 7. 작가 승인
- approved: yes
- note: writer가 `무흔술` 명칭과 세계 규칙 방향을 승인하고 즉시 반영을 지시
