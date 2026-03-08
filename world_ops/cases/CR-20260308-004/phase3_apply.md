# Phase 3 Apply

- change_id: CR-20260308-004
- branch: minor

## 1. 실제 수정 파일
- world/live/world_bible/WB-0005_magic_system.md
- world/live/world_bible/WB-0009_power_structure_factions.md
- world/live/world_bible/WB-0015_academy_bible.md
- world/live/world_bible/WB-0026_appendix_crest_arcana.md
- world/live/external/EX-0001.yaml
- world/live/population/core_cast/NC-0001_P-1027.md
- world/live/docs/world_bible_index_v2.md
- world/live/docs/master_map.md
- world_ops/world_change_log.md
- world_ops/cases/CR-20260308-004/request.md
- world_ops/cases/CR-20260308-004/phase2_report.md
- world_ops/cases/CR-20260308-004/phase3_apply.md
- world_ops/cases/CR-20260308-004/phase4_sync.md

## 2. 변경 요약 (diff 요약 수준)
- `WB-0005`에 벨쿠란의 아동 마법 금지 규정, 이론 교육 허용 범위, 마나 회로/마나핵 활성화 보조 금지, 반역죄급 조사 구조를 추가했다.
- `WB-0009`, `WB-0026`에 이 규정이 귀족 견제 장치이자 왕실 통제 장치라는 점, 독학 천재 사례까지 조사 명분이 되는 점, 특권 예외 가문 구조를 반영했다.
- `WB-0015`에 왕가/공작가/2시그니처 가문 선행학습 특권이 입학 직후 성적 상위권 독점으로 이어진다는 구조를 추가했다.
- `EX-0001`, `NC-0001`에 칼리온의 통제 목표와 키리온의 현재 리스크를 새 규정 기준으로 보강했다.
- 인덱스와 변경 로그, 케이스 문서를 새 상태 기준으로 동기화했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 아동 마법 금지 규정 명시 | `WB-0005` 3.1-A, `WB-0009` 7.1/7.2-A, `WB-0026` 0-E/2) | 계승조회식 이전 수련 금지 | 향후 법령명이나 조사기관 명칭을 붙일 수 있음 |
| 귀족 견제와 특권 예외 연결 | `WB-0009`, `WB-0026`, `EX-0001` | 특별조사, 왕가/공작가 특권 | 특권 가문 범위를 더 세밀하게 정하면 후속 확장 가능 |
| 학술원 성적 편중 구조 반영 | `WB-0015` 13.10/13.11 | 선행학습, 상위권 독식 | 후속으로 입학생 문화/열등감 문법을 community나 narrative에 넣을 수 있음 |
| 키리온 현재 리스크 보강 | `NC-0001` 가문 배경 | NC-0001 | 집필 허브에 언제 노출할지는 후속 서사 작업에서 판단 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - narrative hub나 에피소드 캐논 본문은 직접 수정하지 않았다.

## 4. 미해결 항목
- [x] 없음
- details:
  - 없음. 다만 특권 예외의 공식 법적 이름, 조사기관 이름, 대표 스캔들 사례를 더 세우려면 별도 케이스가 적절하다.

## 5. 작가 승인
- approved: yes
- note: 사용자가 제시한 왕국 규정과 특권 구조를 live SSOT에 반영 완료.
