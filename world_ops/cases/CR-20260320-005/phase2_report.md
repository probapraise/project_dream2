# Phase 2 Report (Collision Scan)

- change_id: CR-20260320-005
- verdict: major

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0030_appendix_muhunsul_doctrine.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0003.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/current_arc.md
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 기존 `무흔술` 관련 live 문서는 세계 규칙, 은폐 논리, 장기 공개 타이밍까지만 잡혀 있고 정본 교본과 형제 변형은 아직 독립 SSOT가 없었다. 이번 추가는 기존 합의를 덮지 않고 세부 전수 로직을 닫아 주는 방향이라 직접 충돌은 없다.
  - 다만 `무흔술`을 너무 완성된 암살술처럼 한 번에 풀면 8세 키리온 시점의 체감과 어긋날 수 있으므로, 정본 전체와 현재 키리온이 실제로 익히는 층위를 분리해 문서화해야 한다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 정본 `무흔술`과 8세 키리온 현재 습득분을 같은 층위로 쓰면 설정이 과하게 보일 수 있음 | `WB-0030`, `NC-0001`, `current_arc` | 정본 원리/훈련 층과 현재 습득 범위를 분리 서술 | 무흔술, 현재 시점, 8세 | resolved |
| 데리온이 아직 10살인데 사부처럼 체계적 사사를 하면 부자연스러움 | `WB-0030`, `EX-0003` | `칼리온 -> 데리온 -> 키리온` relay 구조와 `폭력적 복습` 개념으로 전수 병목을 명시 | 데리온, relay, 전수 병목 | resolved |
| 3화에 교본 설명이 과다 노출되면 장면 긴장이 깨질 수 있음 | `current_arc`, `next_steps` | 현재 아크 문서에 "이상하게 실전적인 형제 대련"까지만 체감시키는 노출 규칙 추가 | ep003, 노출 규칙, 형제 대련 | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - world_bible_index와 handoff/log까지 함께 갱신해 새 부록의 존재를 추적 가능하게 만들면 drift를 막을 수 있다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - `WB-0026`까지 다시 건드릴 필요는 없다. 이번 요청은 식흔/가문 추가 정보보다 `무흔술` 자체의 정본-변형 분해가 핵심이다.

## 5. 판단 근거
- world_bible_index 참조:
  - world/live/docs/world_bible_index_v2.md
- cross-reference 참조:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0003.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/current_arc.md
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md

## 6. 분기 결정
- branch: major
- reason: `무흔술` 전용 부록 신설과 여러 live 문서의 교차 참조/집필 규칙 동기화가 필요해 단순 문장 보강보다 범위가 크다.

## 7. 작가 승인
- approved: yes
- note: writer가 정본 교본과 형제 변형 설계를 직접 지시
