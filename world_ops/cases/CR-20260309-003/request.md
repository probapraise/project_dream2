# Change Request

- change_id: CR-20260309-003
- date: 2026-03-09
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "미담 범죄화/조폭 재해석" 사례를 실제 workflow로 반영한다.

- 제목: `삼국지 초반에 상인들이 유비한테 말이랑 무기 그냥 준 거 있잖아`
- 본문 요약:
  - 미화된 고전 서술을 믿기 어렵고, 사실은 유비가 약탈하거나 강제로 뜯어낸 것 아니냐는 의심 제기
  - "그만한 재산을 꽁으로 준다는 게 말이 안 된다", "진짜 거래였으면 나중에 관직을 받았어야 한다"는 현실 논리 제시
- 댓글 요약:
  - `자진입대 비슷한 거임 / 자진(아님)` 같은 즉시 뒤집기 농담이 붙음
  - 유비/관우/장비를 `돗자리파 두목`, `따까리` 같은 조폭 RP로 재호명
  - 상납, 페이백, 인맥 투자, 수금 등 음지 거래 프레임으로 해석이 확장
  - 마지막에는 "돗자리 깔고 앉아서 수금한 거임" 같은 한 줄 판결로 스레드가 봉인됨

## 2. 정제된 목표 (1문장)
미화된 역사/전기 서술을 약탈·수금·조폭 서사로 재해석하는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~008과 충돌 없이 신규 `ATOM-009`로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-009
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-09
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
