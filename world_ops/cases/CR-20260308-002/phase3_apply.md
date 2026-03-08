# Phase 3 Apply

- change_id: CR-20260308-002
- branch: minor

## 1. 실제 수정 파일
- world/live/world_bible/WB-0009_power_structure_factions.md
- world/live/world_bible/WB-0026_appendix_crest_arcana.md
- world/live/external/EX-0001.yaml
- world/live/population/core_cast/NC-0001_P-1027.md
- world/live/docs/world_bible_index_v2.md
- world/live/docs/master_map.md
- world_ops/world_change_log.md
- world_ops/cases/CR-20260308-002/request.md
- world_ops/cases/CR-20260308-002/phase2_report.md
- world_ops/cases/CR-20260308-002/phase3_apply.md
- world_ops/cases/CR-20260308-002/phase4_sync.md

## 2. 변경 요약 (diff 요약 수준)
- `WB-0009`에 왕실/등록청이 서명귀족 혈통 추적과 10세 왕도 문장검증 행사를 독점 주관한다는 점을 추가했다.
- `WB-0009`, `WB-0026`에 각 가문의 조기 사설 검증 금지와, 그 표면 명분/실질 목적을 명시했다.
- `EX-0001`에 칼리온의 목표와 비밀 구조를 10세 왕도 검증 제도 기준으로 보강했다.
- `NC-0001`에 키리온의 10세 왕도 검증이 2년 뒤 도래하는 하드 데드라인임을 추가했다.
- `world_bible_index_v2`, `master_map`, `world_change_log`에 변경 흔적을 동기화했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 왕실 혈통 추적/10세 검증 제도 명시 | `WB-0009` 7.2, 7.2-A / `WB-0026` 0-E, 2) | 10세 왕도 문장검증 | 향후 왕실 행정기관 이름과 의식 절차를 구체화할 수 있음 |
| 조기 사설 검증 금지와 숨은 목적 반영 | `WB-0009`, `WB-0026`, `EX-0001` secrets | 식흔, 전략 자산 은닉 | 다른 비밀 문장비전 가문이 추가되면 같은 룰을 공유시켜야 함 |
| 키리온 리스크에 데드라인 추가 | `NC-0001` 가문 배경 | NC-0001 | narrative 허브에 이 타이머를 노출할지는 후속 집필 작업에서 판단 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 이번 반영은 narrative hub나 에피소드 캐논 텍스트는 직접 수정하지 않았다.

## 4. 미해결 항목
- [x] 없음
- details:
  - 없음. 다만 추후 왕실 행정기관 명칭, 검증 의식 절차, 호송 규칙이 필요하면 별도 worldbuild 케이스로 확장 가능하다.

## 5. 작가 승인
- approved: yes
- note: 사용자가 직접 제시한 제도 설정을 live SSOT에 반영 완료.
