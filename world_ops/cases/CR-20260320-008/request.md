# Change Request

- change_id: CR-20260320-008
- date: 2026-03-20
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
`10세`의 키리온과 `12세`의 키리온의 외형 묘사 문장 10개를 뽑아 live SSOT에 반영해 둔다.

## 2. 정제된 목표 (1문장)
키리온의 `10세`, `12세` 시점 외형을 집필에 바로 쓸 수 있는 문장형 가이드로 정리하고, 장기 기억과 운영 로그에도 압축 요약을 남긴다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `NC-0001`에 `10세`, `12세` 외형 묘사 문장 가이드를 추가
- [x] `memory_tiers/long_term`와 handoff에 압축 요약을 반영
- [x] world_ops 케이스/로그를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-20
- note: writer가 키리온 연령별 외형 묘사 문장 반영을 직접 지시
