# Change Request

- change_id: CR-20260306-003
- date: 2026-03-06
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 기존 18개 보드 설정은 폐기하기로 했는데 아직 live에 잔존물이 남아 있다. 이것부터 해결한다.

## 2. 정제된 목표 (1문장)
- live bundle에서 은퇴한 고정 18보드 bootstrap 잔존물을 제거하고, 현행 커뮤니티 운영 기준을 동적/온디맨드 모델로 다시 고정한다.

## 3. 변경 유형
- deprecate

## 4. 성공 기준 (DoD)
- [x] `world/live/board_states/`에서 `BOARD-0001~BOARD-0018` bootstrap stub이 제거된다.
- [x] live 문서가 더 이상 고정 18보드 이름/ID를 현행 규칙으로 사용하지 않는다.
- [x] `master_map`, `docs/handoff/next_steps.md`, `world_ops/world_change_log.md`가 현재 결정에 맞게 동기화된다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/board_states/BOARD-0001_b01.md
  - world/live/board_states/BOARD-0018_b18.md
  - world/live/board_states/README.md
  - world/live/docs/community_map.md
  - world/live/docs/master_map.md
  - world/live/docs/dynamic_guide.md
  - world/live/docs/population_grammar.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0021_appendix_terms_aliases.md
  - world/live/world_bible/WB-0025_appendix_naming_constitution.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - BOARD-0001~BOARD-0018 bootstrap model
  - dynamic community model
  - BOARD-001 (낙서장) 운영 규칙

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-06
- note: 사용자 지시로 18보드 live 잔존물 정리를 최우선 처리.
