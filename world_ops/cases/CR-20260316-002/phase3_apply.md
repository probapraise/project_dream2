# Phase 3 Apply

- change_id: CR-20260316-002
- branch: minor

## 1. 실제 수정 파일
- `world/live/world_bible/WB-0003_onepage_summary.md`
- `world/live/world_bible/WB-0006_irminsul_infra.md`
- `world/live/world_bible/WB-0008_archive_plaza_overview.md`
- `world/live/world_bible/WB-0015_academy_bible.md`
- `world/live/world_bible/WB-0017_economy_resources.md`
- `world/live/world_bible/WB-0019_platform_spec.md`
- `world/live/docs/master_map.md`
- `world_ops/world_change_log.md`

## 2. 변경 요약 (diff 요약 수준)
- `WB-0006`에 `주좌 / 전위권`, `모든 마나 노드 = 특수 지형 노드`, 성목의 `자생 노드` 성격, 일반 노드/성목의 신격·정령군 차이를 live 본문으로 내렸다.
- `WB-0003/0015/0017`에 `frontier-feudal` 질서, 학술원의 `전위권 토벌 / 길찾기 / 탐사 / 기믹 활용` 실무, `노드 안정화`의 경제적 함의를 보강했다.
- `WB-0008/0019`에 `픽시 둥지화 -> 요정 동행` 인과와 `질의 인장 / 기록 인장` 메커니즘을 추가해 `CR-20260315-002`의 미반영 중간 단계를 닫았다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| `주좌 / 전위권` 정의와 자생 노드 규칙 반영 | `WB-0006` 요약, `4.1`, `4.2`, `4.4`, `4.6`; `WB-0003` 요약 | `주좌`, `전위권`, `자생 노드` | 관련 전투/던전 서사 세부는 후속 사건 설계에서 더 내려야 함 |
| 학술원/경제를 frontier 구조와 재결속 | `WB-0015` `13.1`, `13.2`, `13.10`; `WB-0017` `15.1`, `15.5.1`, `15.5.3` | `frontier-feudal`, `노드 안정화` | `WB-0012`나 실습 과제 문서의 더 세밀한 사건 배치는 후속 가능 |
| 픽시 둥지화 인과와 인장형 입출력 반영 | `WB-0008` `6.3`, `6.4`; `WB-0019` `17.3`, `17.4.1` | `픽시 둥지화`, `질의 인장`, `기록 인장` | 학생 표면 UX/승급 장면은 별도 설계 과제 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 본 변경은 `CR-20260315-002`의 승인 범위를 넘지 않는 본문 보강과 용어 정합화만 수행했다.

## 4. 미해결 항목
- [x] 없음
- details:
  - 사용자 요청에서 제외한 `영상 슬롯 경제`는 건드리지 않았다.

## 5. 작가 승인
- approved: yes
- note:
  - `영상 슬롯 경제` 제외 조건을 유지한 채 live SSOT 본문 동기화로 처리
