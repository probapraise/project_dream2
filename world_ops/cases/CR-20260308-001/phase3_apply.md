# Phase 3 Apply

- change_id: CR-20260308-001
- branch: minor

## 1. 실제 수정 파일
- world/live/world_bible/WB-0009_power_structure_factions.md
- world/live/world_bible/WB-0026_appendix_crest_arcana.md
- world/live/external/EX-0001.yaml
- world/live/population/core_cast/NC-0001_P-1027.md
- world/live/docs/world_bible_index_v2.md
- world/live/docs/master_map.md
- world_ops/world_change_log.md
- world_ops/cases/CR-20260308-001/request.md
- world_ops/cases/CR-20260308-001/phase2_report.md
- world_ops/cases/CR-20260308-001/phase3_apply.md
- world_ops/cases/CR-20260308-001/phase4_sync.md

## 2. 변경 요약 (diff 요약 수준)
- `WB-0009`에 렌바렌 가주의 정보기관 수장 직위가 명예직이며, 실권은 라베르니온 공작가가 쥔다는 점을 명시했다.
- `WB-0009`, `WB-0026`에 식흔 후계 승계 후 형제자매를 암살해 방계를 청소하는 혈통 관리 규약을 추가했다.
- `EX-0001`에 칼리온의 목표, 비밀, 관계 동학을 새 권력 구조와 방계 청소 규칙 기준으로 재정의했다.
- `NC-0001`에 키리온의 실제 구조적 위험을 추가하고, 가문 배경 서술을 보강했다.
- `world_bible_index_v2`, `master_map`, `world_change_log`에 변경 흔적을 동기화했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 렌바렌-라베르니온 권력 위계 명시 | `WB-0009` 7.2-A, `WB-0026` F.4, `EX-0001` role/goals/relationships | 렌바렌, 라베르니온 | 향후 라베르니온 공작가 카드가 생기면 같은 구조를 직접 반영해야 함 |
| 방계 청소 규약 추가 | `WB-0009` 7.2-A, `WB-0026` F.4, `EX-0001` secrets, `NC-0001` 가문 배경 | 식흔, 방계 청소 | 장남/여동생 개별 카드 생성 시 후속 정합화 필요 |
| 인덱스/로그 동기화 | `world_bible_index_v2`, `master_map`, `world_change_log` | WORLDBUILD-003, CR-20260308-001 | 없음 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - narrative 허브나 집필 캐논 텍스트는 직접 수정하지 않았다. 이번 반영은 세계관/캐릭터 설정 계층에 한정된다.

## 4. 미해결 항목
- [x] 없음
- details:
  - 없음. 다만 라베르니온 공작가, 장남, 여동생 카드가 구체화되면 이번 설정을 그 카드들에 확장해야 한다.

## 5. 작가 승인
- approved: yes
- note: 사용자가 직접 제시한 설정을 live SSOT에 반영 완료.
