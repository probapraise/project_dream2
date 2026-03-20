# Phase 3 Apply

- change_id: CR-20260320-001
- branch: minor

## 1. 실제 수정 파일
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
- world_ops/cases/CR-20260320-001/request.md
- world_ops/cases/CR-20260320-001/phase2_report.md
- world_ops/cases/CR-20260320-001/phase3_apply.md
- world_ops/cases/CR-20260320-001/phase4_sync.md

## 2. 변경 요약 (diff 요약 수준)
- 제도권 기사/귀족 무예가 `마나 + 식` 기반 의례형 동작 학습 비중이 큰 체계라는 점을 `WB-0005`에 추가했다.
- 비마나 실전술이 세계 전역에 산발적으로 존재하지만 드물고, `수경원`은 이를 수백 년 동안 `무흔술`로 체계화했다는 점을 `WB-0005/0009/0026`에 반영했다.
- 데리온이 키리온에게 강요하는 무력이 일반 품새가 아니라 `무흔술` 기초라는 점을 `EX-0001/0003`, `NC-0001`, `long_term`에 동기화했다.
- `master_map`, `handoff`, `world_change_log`, 케이스 문서를 갱신했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 제도권 기사 무예의 의례형 성격 명시 | `WB-0005` / 요약, `3.10 수련 초월` | 무흔술, 수련 초월 | 후속 집필에서 "품새 vs 실전술" 장면 차이를 실제 서사 동작으로 보여줄 필요 |
| 수경원의 비마나 실전술 체계화 반영 | `WB-0009`, `WB-0026` / 렌바렌·수경원 섹션 | 무흔술, 수경원, 렌바렌 | 다른 비밀 서명귀족 가문의 대응 훈련 체계는 추후 필요 시 확장 |
| 데리온-키리온 단련 축 구체화 | `EX-0001`, `EX-0003`, `NC-0001`, `long_term` | 데리온, 키리온, 무흔술 | 실제 장면에서 어느 수준까지 익혔는지는 회차별로 조절 필요 |
| 운영 로그 동기화 | `master_map`, `docs/handoff`, `world_change_log`, `world_ops/cases/CR-20260320-001/*` | CR-20260320-001, WORLDBUILD-028 | 후속 세계관 확정 시 handoff 상단 상태 문구 갱신 유지 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 신규 파일이나 인덱스 파일 추가는 발생하지 않았다.

## 4. 미해결 항목
- [x] 없음
- details:
  - 현 시점에서는 `무흔술` 개념 정의와 렌바렌/주인공 연결까지만 반영했다. 구체 기술 체계나 세부 교범명은 후속 확장 가능하다.

## 5. 작가 승인
- approved: yes
- note: writer 지시에 따라 live SSOT에 직접 반영 완료
