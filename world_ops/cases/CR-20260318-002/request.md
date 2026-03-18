# Change Request

- change_id: CR-20260318-002
- date: 2026-03-18
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "거창한 전문가 제목 -> 무책임한 한 줄 결론" 사례를 실제 workflow로 반영한다.

- 제목: `경영학도가 보는, 모픽이 당장 적자나도 괜찮은 이유`
- 본문 요약:
  - 깊은 경영 분석을 예고하는 제목
  - 실제 본문은 `내 돈 아님` 한 줄로 종료
- 댓글 요약:
  - `맞는 말이다`, `이건 경영학도 맞네` 같은 짧은 승인 반응
  - `하버드`, `석사`, `노벨경제학상` 등 과잉 학력/전문성 칭호를 붙이며 찬양
  - 실질 분석은 없는데도 그 무책임한 솔직함을 오히려 통찰처럼 소비

## 2. 정제된 목표 (1문장)
거창한 분석 제목이 이해관계 부재를 드러내는 한 줄로 붕괴하고, 댓글이 그 최소주의를 학술 통찰처럼 과잉 찬양하는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~013과 충돌 없이 신규 `ATOM-014`로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-014
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-18
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
