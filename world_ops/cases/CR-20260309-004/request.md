# Change Request

- change_id: CR-20260309-004
- date: 2026-03-09
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "악평-헌정 역전" 사례를 실제 workflow로 반영한다.

- 제목: `하도 기계공주 하길래 1화 봤는데 존나 어이가없네 ㅋㅋ`
- 본문 요약:
  - 작품 1화를 욕설과 조롱으로 길게 실황 리뷰함
  - TS 각성 방식, 욕조에 드라이기 장면, 무너지는 말투, 마지막 전개까지 디테일 단위로 집요하게 비난
  - 그러나 총평에서 `2만원 후원`, `평점 5/5`를 밝히며 전체 악평을 역전
- 댓글 요약:
  - `존나 잘 처먹었노`, `이 글이 더 재밌네` 식으로 글쓴이의 감정 드리프트 자체를 즐김
  - 본문 표현(`우우...`)을 재인용해 즉시 밈화
  - 내부 떡밥에는 `믿지마` 식 정정이 붙으며 팬덤 문법이 보강됨

## 2. 정제된 목표 (1문장)
작품을 거칠게 욕하면서도 후원과 고평점으로 마무리하는 역설적 애증 소비 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~009과 충돌 없이 신규 `ATOM-010`으로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-010
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-09
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
