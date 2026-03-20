# Change Request

- change_id: CR-20260320-005
- date: 2026-03-20
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
`3화` 집필을 위해 `무흔술`을 좀 더 체계화한다. 우선 칼리온이 배우는 정본 `무흔술`부터 최대한 논리적으로 구체화하고, 그 다음 데리온은 매일 칼리온에게 수련받은 내용을 다음날 키리온에게 대련 형태로 가르친다는 조건 아래, 아직 10살인 데리온은 체계적인 사사를 할 수 없다는 점과 형제의 치고받는 대련에서만 성립하는 쌍방상승을 분리해 설계한다.

## 2. 정제된 목표 (1문장)
정본 `무흔술`의 원리와 판정 기준, `칼리온 -> 데리온 -> 키리온` 전수 병목, 데리온형/키리온형 변형과 형제 대련형 쌍방상승을 live SSOT에 독립 부록으로 정리하고 3화 집필용 현재 아크 규칙까지 동기화한다.

## 3. 변경 유형
- add + modify

## 4. 성공 기준 (DoD)
- [x] `WB-0030` 신규 부록에 정본 `무흔술` 원리, 훈련 층, 전수 병목, 데리온형/키리온형 변형을 정리
- [x] `WB-0005/0009`, `EX-0001/0003`, `NC-0001`에 새 부록 기준 교차 참조와 핵심 로직을 반영
- [x] `current_arc/story_arcs/long_term`, world_bible_index, handoff/log, case 문서를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/world_bible_index_v2.md
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0030_appendix_muhunsul_doctrine.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0003.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/current_arc.md
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 무흔술
  - 칼리온 렌바렌
  - 데리온 렌바렌
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-20
- note: writer가 `무흔술` 정본 교본과 형제 변형 설계를 직접 지시
