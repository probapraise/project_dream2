# Phase 3 Apply

- change_id: CR-20260320-006
- branch: minor

## 1. 실제 수정 파일
- world/live/world_bible/WB-0030_appendix_muhunsul_doctrine.md
- world/live/external/EX-0003.yaml
- world/live/external/EX-0004.yaml
- world/live/population/core_cast/NC-0001_P-1027.md
- world/live/docs/story_arcs.md
- world/live/docs/memory_tiers/long_term.md
- world/live/docs/master_map.md
- docs/handoff/next_steps.md
- world_ops/world_change_log.md
- world_ops/cases/CR-20260320-006/request.md
- world_ops/cases/CR-20260320-006/phase2_report.md
- world_ops/cases/CR-20260320-006/phase3_apply.md
- world_ops/cases/CR-20260320-006/phase4_sync.md

## 2. 변경 요약 (diff 요약 수준)
- `WB-0030`에 치유 세계 기준 과훈련의 피지컬 상한, 독자 수련 입력 구조, `10~12세` 키리온 피지컬 성장 곡선, 12세 전투력 상한을 추가했다.
- `EX-0003`, `EX-0004`, `NC-0001`에 방학 재교정과 리리아의 호신 입력, `기술 곡선 > 피지컬 곡선` 원칙을 반영했다.
- `story_arcs`, `long_term`, handoff/log와 case 문서를 동기화했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 치유 세계의 과훈련과 피지컬 상한 명문화 | `WB-0030` I.10~I.13 | 키리온, 성장판, 피지컬 곡선 | 후속 집필에서 회복력을 만능처럼 쓰지 않도록 유지 필요 |
| 리리아 개입을 호신/이탈 입력으로 제한 | `EX-0004`, `WB-0030`, `NC-0001` | 리리아, 호신, 이탈 | 향후 리리아가 직접 전투원처럼 비약하지 않게 관리 필요 |
| 방학 데리온 재교정과 `ep010` 출력 논리 보강 | `EX-0003`, `story_arcs`, `next_steps` | 데리온, 방학, ep010 | 보스 몬스터의 약점/지형 설계는 후속 전투 장면 과제 |
| 운영 로그 동기화 | `master_map`, `world_change_log`, case docs | CR-20260320-006, WORLDBUILD-033 | 차기 handoff 갱신 시 0-D 요약 유지 필요 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 기존 `무흔술` 공개 타이밍과 조커 카드 위상은 유지했다.

## 4. 미해결 항목
- [x] 없음
- details:
  - `ep010` 보스 몬스터의 구체적 약점 구조는 여전히 후속 액션 설계 과제로 남는다.

## 5. 작가 승인
- approved: yes
- note: writer 지시에 따라 live SSOT 반영 완료
