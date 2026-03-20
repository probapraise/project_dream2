# Phase 3 Apply

- change_id: CR-20260320-002
- branch: minor

## 1. 실제 수정 파일
- world/live/population/core_cast/NC-0001_P-1027.md
- world/live/external/EX-0003.yaml
- world/live/docs/story_arcs.md
- world/live/docs/memory_tiers/long_term.md
- world/live/docs/master_map.md
- docs/handoff/next_steps.md
- world_ops/world_change_log.md
- world_ops/cases/CR-20260320-002/request.md
- world_ops/cases/CR-20260320-002/phase2_report.md
- world_ops/cases/CR-20260320-002/phase3_apply.md
- world_ops/cases/CR-20260320-002/phase4_sync.md

## 2. 변경 요약 (diff 요약 수준)
- 키리온이 `무흔술`을 특수 비밀 전승으로 인식하지 않고, 다른 귀족도 다 이 정도는 배우는 줄 안 채 성장한다는 인식 구조를 `NC-0001`과 `long_term`에 추가했다.
- 입학식 모의 탐색전에서 `색인의 그리모어` 기반 운영형 유능감이 먼저 드러나고, `ep010` 말미 보스 몬스터 일격으로 `무흔술`이 반전 공개되는 구조를 `NC-0001`, `story_arcs`, `long_term`에 반영했다.
- academy 이후에도 데리온의 반복 시험과 일부 보조 마법 접합으로 `무흔술`이 조커 카드로 유지된다는 점을 `NC-0001`, `EX-0003`, `long_term`에 추가했다.
- 운영 로그와 케이스 문서를 동기화했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 키리온의 `무흔술` 오해와 자기 강함 미인지 고정 | `NC-0001`, `long_term` | 무흔술, 마나 없는 세계 잔향 | 입학 전 장면에서 "왜 의심하지 않나"를 자연스럽게 보여 주는 서술 장치 필요 |
| 입학식 운영형 첫 인상 -> `ep010` 반전 구조 고정 | `NC-0001`, `story_arcs`, `long_term` | 세렌, 모의 탐색전, ep010 | 실제 보스 종류/시험 규칙 세부 설계는 후속 academy 설계 문서에서 닫아야 함 |
| academy 이후 반복 시험/조커 카드 유지 반영 | `EX-0003`, `NC-0001`, `long_term` | 데리온, 열상각인, 조커 카드 | `열상각인` 세부 기능 정의는 추후 마법/기술 조합 설계 시 보강 가능 |
| 운영 로그 동기화 | `master_map`, `docs/handoff`, `world_change_log`, `world_ops/cases/CR-20260320-002/*` | CR-20260320-002, WORLDBUILD-029 | 다음 handoff 갱신 때 0-A/0-B 요약 충돌 없이 유지 필요 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 현재 canon frontier나 recent/current_arc 문서는 건드리지 않았다.

## 4. 미해결 항목
- [x] 없음
- details:
  - 모의시험 보스의 정확한 종족/기믹, `열상각인` 상세 스펙은 후속 academy 전투 설계 시 구체화 가능하다.

## 5. 작가 승인
- approved: yes
- note: writer 지시에 따라 live SSOT에 직접 반영 완료
