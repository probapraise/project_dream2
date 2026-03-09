# Change Request

- change_id: CR-20260309-001
- date: 2026-03-09
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "지시문 오독 + 음담화" 사례를 실제 workflow로 반영한다.

- 제목: `시발 ㅋㅋㅋㅋㅋㅋㅋ`
- 본문 요약:
  - 외부 스크린샷에서 코딩 AI에게 `뒤로가기 기능`을 요청했는데,
    모델이 단어를 엉뚱하게 해석해 전혀 다른 성적 의미의 결과물을 만든다는 농담이 핵심
  - 게시자는 "지금 받은 코드 전체가 이 수준"이라며 모델의 실무 무능과 천박한 오독을 한 번에 조롱
- 댓글 요약:
  - `끄응`, `응기잇`, `오고고곡` 같은 신음형 추임새가 연쇄적으로 붙음
  - `ASI`, `어쨌든 뒤로는 갔죠?`처럼 오독을 역으로 고지능 판정 농담으로 뒤집음
  - 못 알아들은 사람에게 누군가 직접 설명하고, 그 설명까지 다시 웃음 포인트가 됨
  - 중간에는 실제 코딩 AI 실무 체감 비교 의견이 짧게 끼어듦

## 2. 정제된 목표 (1문장)
지시문 오독이 음담성 말장난과 인간 우월 농담으로 번지는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~006과 충돌 없이 신규 `ATOM-007`로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-007
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-09
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
