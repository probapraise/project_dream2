# Change Request

- change_id: CR-20260309-006
- date: 2026-03-09
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "명칭 literal reading / 음절 납치" 사례를 실제 workflow로 반영한다.

- 제목: `트롤의 왕이면 모든트롤써야하는거 아닌가`
- 본문 요약:
  - 게임 설정상 `트롤의 왕`인 캐릭터 일러스트를 두고
  - 이름에 `트롤`이 들어가니 `트롤해머`도 써야 한다는 문자 그대로의 요구를 제기
- 댓글 요약:
  - 실제 어원/의미를 아는 댓글이 반박하지만 곧 웃음으로 흡수됨
  - `자이언트 슬레이어`, `트평`, `트카콜라` 같은 말장난 파생이 이어짐
  - "이름에 트롤 들어가면 다 트롤" 식의 허술한 분류 규칙이 집단 승인됨

## 2. 정제된 목표 (1문장)
이름 음절 하나를 근거로 장비와 분류 체계를 과잉 확장하는 문자주의 말장난 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~010과 충돌 없이 신규 `ATOM-011`로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-011
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-09
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
