# Change Request

- change_id: CR-20260320-007
- date: 2026-03-20
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
리리아 관련 축이 잘못 들어갔다. 리리아는 키리온에게 `호신 입력`을 주는 교관 쪽이 아니라, 자기도 체술을 배우고 싶다고 떼를 써서 키리온이 가르쳐 주는 입장이다.

## 2. 정제된 목표 (1문장)
데리온 academy 부재기 `10~12세` 키리온 성장선에서 리리아의 역할을 `입력 제공자`가 아니라 `호신술을 배우는 제자`로 교정하고, 키리온이 가르치는 과정에서 자기 체계를 더 설명 가능하게 정리한다는 로직으로 live SSOT를 재정렬한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0030`, `EX-0004`, `NC-0001`에 리리아 역할 축을 learner 구조로 교정
- [x] `story_arcs`, `memory_tiers/long_term`, handoff/log에 동일한 교정을 반영
- [x] world_ops 케이스/로그를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0030_appendix_muhunsul_doctrine.md
  - world/live/external/EX-0004.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 리리아 렌바렌
  - 키리온 렌바렌
  - 무흔술

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-20
- note: writer가 리리아 역할 축 오해를 직접 교정
