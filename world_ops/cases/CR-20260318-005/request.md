# Change Request

- change_id: CR-20260318-005
- date: 2026-03-18
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "진지한 등급명 -> 생활어/폭력어 어감 붕괴" 사례를 실제 workflow로 반영한다.

- 제목: `가정권력급은 뭐냨ㅋ`
- 본문 요약:
  - 웹소설 속 헌터 등급표를 캡처해 올림
  - `가정권력급`, `동네권력급`, `도시권력급`, `국가권력급` 같은 명칭이 제시됨
  - 글쓴이는 "존나 짜치는 등급"이라고 평함
- 댓글 요약:
  - 다수가 `가정폭력`, `집구석여포`, `자택경비원`, `가정파괴범` 같은 생활권/범죄 연상을 붙여 조롱
  - 일부는 원래 의도가 생활권 단위 방어력 같은 것 아니냐고 설명
  - 그래도 스레드의 중심은 명칭이 주는 우스운 첫인상과 조롱 별칭 생성에 머묾

## 2. 정제된 목표 (1문장)
진지하고 장엄해야 할 등급명이 생활어/폭력어 어감으로 붕괴하고, 댓글이 그 네이밍 실패를 일상 조롱과 범죄 연상으로 봉인하는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~016과 충돌 없이 신규 `ATOM-017`로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-017
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-18
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
