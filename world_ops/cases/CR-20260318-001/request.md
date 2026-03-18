# Change Request

- change_id: CR-20260318-001
- date: 2026-03-18
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "장엄한 서정문 -> 하찮은 구걸 착지" 사례를 실제 workflow로 반영한다.

- 제목: `슬픈 사연 있는데 들어와줘...`
- 본문 요약:
  - 사라진 초원 민족과 영혼의 형제, 별과 바람, 기마 전설을 비장한 문체로 길게 회고
  - 마지막에 갑자기 싸이버거 구입과 계좌 송금을 요청
- 댓글 요약:
  - 첫 문장과 첫 문단을 명문으로 재인용하며 감탄
  - `판타지 대작 첫 문장 같다`, `21세기 윤동주가 싸이버거 구걸한다` 같은 식으로
    문장력과 목적의 낙차를 함께 소비
  - 일부는 스키타이/거란족 등 역사 소재를 따로 해설하며 반쯤 진지하게 반응

## 2. 정제된 목표 (1문장)
문학적 격조를 사소한 음식 구걸에 소모하는 낙차와, 댓글이 첫 문장 자체를 집단 숭배하는 반응 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~012와 충돌 없이 신규 `ATOM-013`으로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-013
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-18
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
