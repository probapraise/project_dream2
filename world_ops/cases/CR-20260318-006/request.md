# Change Request

- change_id: CR-20260318-006
- date: 2026-03-18
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
Layer B 누적 ATOM이 17개까지 늘어났으니 기존 `GRAMMAR-001~003` 초안을 다시 합성해 현행 상위 규칙 구조를 재정렬한다.

## 2. 정제된 목표 (1문장)
`ATOM-001~017` 전체를 다시 검토해 설명력이 떨어진 기존 3축 초안을 현행 사례 분포에 맞는 상위 `GRAMMAR-*` 구조로 2차 재합성하고 활성 문서와 운영 로그를 동기화한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `ATOM-001~017` 전체를 다시 훑고 기존 3축 초안의 설명력 부족 지점을 명시
- [x] `community_grammar_layer_b.md`의 `GRAMMAR-*`를 현행 사례 분포 기준으로 재합성
- [x] `master_map`, `next_steps`, `world_change_log`, `world_ops` 케이스 로그까지 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - GRAMMAR-001
  - GRAMMAR-002
  - GRAMMAR-003
  - GRAMMAR-004
  - BOARD-001

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-18
- note: writer가 Layer B 누적 후속으로 GRAMMAR 재합성을 바로 시작하라고 지시함
