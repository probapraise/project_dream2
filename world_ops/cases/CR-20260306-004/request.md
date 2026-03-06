# Change Request

- change_id: CR-20260306-004
- date: 2026-03-06
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 18보드 잔존물 정리 후, 앞으로 동적 게시판을 언제 만들고 언제 state file로 승격하는지 규칙까지 문서로 고정한다.

## 2. 정제된 목표 (1문장)
- 동적 게시판을 `concept_only -> registered -> stateful -> retired` lifecycle로 정의하고, ID 발급/상태 파일 생성/시뮬레이션 promote 규칙을 live 문서에 명시한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `community_map.md`에 보드 lifecycle과 ID 규칙이 명시된다.
- [x] `simulation_playbook.md`에 새 보드 승격과 exploratory run promote 규칙이 명시된다.
- [x] `board_states/README.md`, `master_map.md`, `docs/handoff/next_steps.md`, `world_ops/world_change_log.md`가 동기화된다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_map.md
  - world/live/docs/simulation_playbook.md
  - world/live/board_states/README.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - BOARD lifecycle
  - BOARD-### ID allocation rule
  - simrun snapshot promote rule

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-06
- note: 18보드 cleanup 직후 동적 게시판 생성 규칙 문서화 진행.
