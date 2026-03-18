# Change Request

- change_id: CR-20260318-007
- date: 2026-03-18
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
Layer B 강화를 위해 아래 "장르 규범 -> 비열한 실전주의 찬양" 사례를 실제 workflow로 반영한다.

- 제목: `기술명을 외치는게 뭐가 비효율적이란 거냐.`
- 본문 요약:
  - 비열한 전술가 캐릭터가 `베기라 외치고 찌르기 하면 잘 먹힌다`는 식으로 속임수 전술을 옹호
- 댓글 요약:
  - 안 보이는 동생이 더 무섭다는 식으로 기습형 공포를 재평가
  - `비열님`, `효율님`, `참닌자`처럼 비열함을 오히려 전문성으로 칭송
  - 기술명 외치기 같은 장르 규범을 낭만이 아니라 비효율로 비웃음

## 2. 정제된 목표 (1문장)
장르적 정석과 낭만을 기만과 기습의 실전주의로 뒤집고, 댓글이 그 비열함을 오히려 역할 정체성의 진짜 본질처럼 칭송하는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~017과 충돌 없이 신규 `ATOM-018`로 정리
- [x] 필요 시 현행 `GRAMMAR-*`의 `synthesis_of`를 미세 조정
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-018
  - GRAMMAR-003
  - BOARD-001

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-18
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
