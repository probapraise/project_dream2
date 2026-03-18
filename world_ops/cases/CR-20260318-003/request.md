# Change Request

- change_id: CR-20260318-003
- date: 2026-03-18
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "비밀 공개형 제목 -> 적자 사실 한 줄 종결" 사례를 실제 workflow로 반영한다.

- 제목: `모픽이 뭘로 돈버는지 알려줌`
- 본문 요약:
  - 매출이 크게 꺾이는 재무표 스크린샷을 제시
  - 결론은 `돈을 못벌고 있음....` 한 줄
- 댓글 요약:
  - 대부분 `ㅋㅋㅋ`, `100%`, `팩트임` 같은 짧은 웃음/승인
  - 일부는 시기, 시장 진입 타이밍, 과거 유료화 여부를 덧붙여 맥락을 보충
  - 그래도 스레드의 중심은 "복잡한 비밀이 아니라 그냥 못 버는 중"이라는 허무한 결론에 머묾

## 2. 정제된 목표 (1문장)
비밀 폭로나 경영 분석을 예고하는 제목이 적자 스크린샷과 `못 벌고 있음` 한 줄로 붕괴하고, 댓글이 그 공허한 정직함을 웃음과 팩트 승인으로 봉인하는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~014와 충돌 없이 신규 `ATOM-015`로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-015
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-18
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
