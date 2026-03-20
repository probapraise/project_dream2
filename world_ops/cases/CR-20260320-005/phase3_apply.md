# Phase 3 Apply

- change_id: CR-20260320-005
- branch: major

## 1. 실제 수정 파일
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
- world_ops/cases/CR-20260320-005/request.md
- world_ops/cases/CR-20260320-005/phase2_report.md
- world_ops/cases/CR-20260320-005/phase3_apply.md
- world_ops/cases/CR-20260320-005/phase4_sync.md

## 2. 변경 요약 (diff 요약 수준)
- `WB-0030` 부록을 신설해 정본 `무흔술`의 목적, 판정 기준, 5원칙, 훈련 층, 전수 병목, 데리온형/키리온형 변형, 형제 대련형 쌍방상승을 정리했다.
- `WB-0005/0009`에 새 부록 교차 참조를 추가하고, `EX-0001/0003`, `NC-0001`에 `칼리온 -> 데리온 -> 키리온` relay 구조와 현재 시점 습득 범위를 반영했다.
- `current_arc/story_arcs/long_term`에 3화 집필용 형제 대련 노출 규칙과 장기 drift 방지 포인트를 넣고, 인덱스/로그/case 문서를 동기화했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 정본 `무흔술` 전용 SSOT 부록 신설 | `WB-0030` 전체, `world_bible_index_v2` | 무흔술, WB-0030 | 이후 전투 장면 설계에서 각 원칙이 과잉 설명으로 새지 않게 관리 필요 |
| `칼리온 -> 데리온 -> 키리온` relay 전수 병목 명문화 | `EX-0001`, `EX-0003`, `NC-0001`, `long_term` | 칼리온, 데리온, 키리온, relay | academy 이후 데리온 시험 장면에도 같은 원리를 유지해야 함 |
| 3화용 형제 대련 노출 규칙 추가 | `current_arc`, `next_steps`, `master_map` | ep003, 형제 대련, 노출 규칙 | 실제 집필 시 교본 해설보다 교정 대사/압력에 비중을 둬야 함 |
| world rule 교차 참조와 운영 로그 동기화 | `WB-0005/0009`, `world_change_log`, case docs | CR-20260320-005, WORLDBUILD-032 | 추후 `WB-0030`을 참조하는 추가 문서가 생기면 index 재생성 필요 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 기존 `ep010` 공개 타이밍이나 `무흔술`의 상한 설정은 건드리지 않았다.

## 4. 미해결 항목
- [x] 없음
- details:
  - `열상각인`을 `무흔술`에 어떻게 접합하는지는 여전히 후속 전투 설계 과제다.

## 5. 작가 승인
- approved: yes
- note: writer 지시에 따라 live SSOT 반영 완료
