# Phase 3 Apply

- change_id: CR-20260320-004
- branch: minor

## 1. 실제 수정 파일
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
- world_ops/cases/CR-20260320-004/request.md
- world_ops/cases/CR-20260320-004/phase2_report.md
- world_ops/cases/CR-20260320-004/phase3_apply.md
- world_ops/cases/CR-20260320-004/phase4_sync.md

## 2. 변경 요약 (diff 요약 수준)
- `WB-0005`, `WB-0009`에 `무흔술`이 쉽게 의심받지 않는 이유와 비마나 전투술로서의 뚜렷한 상한을 추가했다.
- `EX-0001`, `EX-0005`에 칼리온과 세르반이 데리온의 위험한 가르침을 서로 다른 이유로 묵인하는 논리를 반영했다.
- `NC-0001`, `story_arcs`, `long_term`에 키리온의 둔감한 자기인식과 `무흔술`의 장기 위상을 "숨은 칼 같은 조커 카드"로 조정했다.
- 운영 로그와 case 문서를 갱신했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| `무흔술`의 의심 회피 논리/상한 보강 | `WB-0005`, `WB-0009` | 무흔술, 비마나 전투술 | 후속 전투 설계에서 실제 한계 연출 필요 |
| 칼리온·세르반 묵인 사유 명문화 | `EX-0001`, `EX-0005` | 칼리온, 세르반, 데리온 | 이후 둘의 묵인이 언제 종료되는지 임계점은 후속 갈등 설계 과제 |
| 키리온 자기인식과 조커 카드 위상 조정 | `NC-0001`, `story_arcs`, `long_term` | 키리온, 조커 카드, 상한 | 중반 이후 너무 자주 꺼내면 희소성이 죽으니 사용 빈도 관리 필요 |
| 운영 로그 동기화 | `master_map`, `docs/handoff`, `world_change_log`, `world_ops/cases/CR-20260320-004/*` | CR-20260320-004, WORLDBUILD-031 | 다음 handoff 갱신 때 0-B 요약과 충돌 없이 유지 필요 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 기존 화수/academy 타이밍 구조는 건드리지 않았다.

## 4. 미해결 항목
- [x] 없음
- details:
  - `열상각인` 자체의 상세 스펙은 여전히 후속 설계 대상으로 남는다.

## 5. 작가 승인
- approved: yes
- note: writer 지시에 따라 live SSOT 반영 완료
