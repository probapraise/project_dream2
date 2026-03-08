# Change Request

- change_id: CR-20260308-004
- date: 2026-03-08
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 벨쿠란 왕국이 `계승조회식` 이전 아동의 체계적 마법 수련을 금지한다는 설정을 추가한다. 이론 교육은 허용되지만, 마나 회로/마나핵 활성화를 도와 실제 시전이 가능해지게 하는 것은 엄금되며, 적발 시 부모와 영지가 반역죄급 조사 대상이 된다. 왕가·공작가·일부 2시그니처 이상 가문은 사실상 조기 수련 특권을 누리고, 이 격차가 아카데미 상위권을 만든다.

## 2. 정제된 목표 (1문장)
- `계승조회식` 이전 아동 마법 수련 금지 규정과 귀족 견제/특권 선행학습 구조를 마법 시스템, 권력 구조, 문장비전 규칙, 학술원, 관련 캐릭터 카드에 일관되게 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0005`, `WB-0009`, `WB-0026`에 아동 마법 수련 금지와 특별조사 규정이 반영된다.
- [x] `WB-0015`에 선행학습 특권이 학술원 초기 성적 서열로 이어지는 구조가 반영된다.
- [x] `EX-0001`, `NC-0001`, 인덱스/로그/케이스 문서가 새 상태를 기록한다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 벨쿠란 왕실
  - 계승조회식 이전 아동 마법 수련 금지 규정
  - 왕가/공작가/2시그니처 가문 특권
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-08
- note: 사용자가 왕국 규정과 특권 예외, 학술원 성적 격차까지 포함해 명시적으로 설정을 제시했다.
