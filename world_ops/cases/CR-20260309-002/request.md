# Change Request

- change_id: CR-20260309-002
- date: 2026-03-09
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 강화를 위해 아래 "황당한 난동 사유 + 집단 정당화" 사례를 실제 workflow로 반영한다.

- 제목: `식당에 경찰 옴`
- 본문 요약:
  - 식당에서 경찰이 괴한을 제압하는 스크린샷 2장이 올라옴
  - 글쓴이는 사건 사유를 `불고기가 없어서 깽판(설렁탕집임)` 한 줄로 압축
- 댓글 요약:
  - 다수 댓글이 `불고기는 중대사항이지`, `인정이지`처럼 황당한 명분을 정당화
  - 일부는 퍼온짤 여부, 실시간 여부, 추가사진 업로드로 현장성을 확인
  - 메뉴명 변주, 조건 반전, 사회면 예고 드립으로 스레드가 확장

## 2. 정제된 목표 (1문장)
황당한 난동 사유를 집단이 능청스럽게 승인하고 정당화 밈으로 소비하는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서와 운영 로그에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~007과 충돌 없이 신규 `ATOM-008`로 정리
- [x] `world/live/docs/community_grammar_layer_b.md`와 bootstrap/change log/handoff를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-008
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-09
- note: writer가 source 글/댓글을 제공하고 Layer B 강화 작업을 즉시 진행하도록 지시
