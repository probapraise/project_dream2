# Phase 2 Report (Collision Scan)

- change_id: CR-20260320-004
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0005.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 직전 문서들에서 `무흔술`을 꽤 강하게 잡아 두었으므로, 이번 보강은 그 유효성을 지우지 않되 `쉽게 의심받지 않음`과 `상한이 뚜렷함`을 함께 박아 과도한 만능화를 막는 방향이 적절하다.
  - 칼리온과 세르반의 묵인 사유는 이미 카드상에 암시가 있으므로, 각각 `차남 생존 버퍼 + 통제 가능한 변수`, `쉽게 노출되지 않고 상한이 뚜렷한 관리 가능한 일탈` 쪽으로 명문화하면 정합적이다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| `무흔술`이 지나치게 만능 전투술처럼 읽힐 수 있음 | `WB-0005`, `WB-0009`, `long_term` | 비마나 전투술 특유의 상한을 명시해 조커 카드 위상으로 묶기 | 무흔술, 상한, 조커 카드 | resolved |
| 데리온의 위험한 훈련이 왜 즉시 제재되지 않는지 공백이 있음 | `EX-0001`, `EX-0005` | 칼리온/세르반의 서로 다른 묵인 논리를 명문화 | 묵인, 칼리온, 세르반 | resolved |
| 왜 주변에서 잘 못 알아보는지 논리가 약할 수 있음 | `WB-0005`, `WB-0009`, `NC-0001` | 외형 유사성, 희소한 인지, 선별 전승을 함께 명시 | 의심 회피, 기사 무예, 선별 전승 | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - `story_arcs`와 `long_term`에 장기 위상 조정까지 함께 반영해 future writing drift를 막았다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - `WB-0026`까지 다시 건드릴 필요는 없었다. 이번 보강은 world rule과 인물 동기 쪽이면 충분하다.

## 5. 판단 근거
- world_bible_index 참조: 없음 (파일 추가/삭제 없음)
- cross-reference 참조:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0005.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/long_term.md

## 6. 분기 결정
- branch: minor
- reason: 기존 정의와 캐릭터 카드의 해석 보강 및 운영 로그 갱신만 필요하며, 구조적 재작성이나 새 파일 설계가 없다.

## 7. 작가 승인
- approved: yes
- note: writer가 `무흔술`의 의심 회피 논리와 묵인/상한 보강을 직접 지시
