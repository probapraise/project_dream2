# Change Request

- change_id: CR-20260318-004
- date: 2026-03-18
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "불완전한 제목 기억 -> 정답 복구 후 오답 파편 밈 폭주" 사례를 실제 workflow로 반영한다.

- 제목: `혹시 책중에 세,균,맨 이런 이름 달고있는 작품 알고 있는지요`
- 본문 요약:
  - 인류 문명 관련 필독서 제목이 기억나지 않아 불완전한 음절 단서만 제시
- 댓글 요약:
  - 다수가 곧바로 정답 `총균쇠`를 복구
  - 동시에 `세균맨`, `호빵맨 빌런`, `33퍼 맞췄네` 같은 식으로 틀린 파편을 더 오래 가지고 놂
  - 정답 제공보다 "어떻게 그렇게 틀렸는지"와 그 오답의 웃긴 어감이 스레드 중심이 됨

## 2. 정제된 목표 (1문장)
불완전한 제목 기억이 정답 복구 뒤에도 틀린 파편 자체가 더 강한 밈으로 살아남는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~015와 충돌 없이 신규 `ATOM-016`로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-016
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-18
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
