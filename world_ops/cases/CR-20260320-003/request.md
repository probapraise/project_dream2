# Change Request

- change_id: CR-20260320-003
- date: 2026-03-20
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
프롤로그가 `0화`라는 기준을 반영해, 직전 설정 문서들에 들어간 키리온 `무흔술` 반전 공개 화수를 `11화`가 아니라 `10화`로 교정한다.

## 2. 정제된 목표 (1문장)
프롤로그=`0화` 기준으로 episode numbering을 재정렬해 키리온 `무흔술` 반전 공개 시점을 `ep011`에서 `ep010`으로 일관되게 교정한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `NC-0001`, `story_arcs`, `long_term`의 `ep011` 표기를 `ep010`으로 교정
- [x] handoff/master_map/world_change_log와 기존 case 문서의 stale 표기를 함께 정리
- [x] 프롤로그=`0화` 기준이 운영 로그에 반영됨

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
  - world_ops/cases/CR-20260320-002/request.md
  - world_ops/cases/CR-20260320-002/phase2_report.md
  - world_ops/cases/CR-20260320-002/phase3_apply.md
  - world_ops/cases/CR-20260320-002/phase4_sync.md
- impacted_entities:
  - ep010
  - 프롤로그 0화 기준
  - 키리온 무흔술 반전 공개

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-20
- note: writer가 `11화 -> 10화`, `프롤로그 = 0화` 기준으로 즉시 교정하도록 지시
