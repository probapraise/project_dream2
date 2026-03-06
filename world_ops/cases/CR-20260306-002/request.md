# Change Request

- change_id: CR-20260306-002
- date: 2026-03-06
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
레이어 B 반영 테스트를 위해 아래 종족 명명법 농담 글을 실제 workflow로 태운다.

- 제목: `엘프제=엘븐 드워프제=드워븐 인간제=?`
- 본문 요약:
  - `맨-메이드는 느낌이 안 사는데`
  - `orcish/demonic/elfish의 인간버전은 뭐인 것 같음?`
- 댓글 요약:
  - 드워프가 인간제 물건은 사실상 `볼품없는` 것과 같다고 선언
  - 엘프/드워프 간 외모·수염·주정뱅이 편견을 던지며 대댓글 난투
  - 주변 유저가 `ㅋㅋㅋ`로 판을 키우고 마지막에 종족 찬가 한 줄로 마무리

## 2. 정제된 목표 (1문장)
명명법 질문이 종족 RP형 상호 비하 배틀로 번지는 문법을 Layer B용 신규 ATOM으로 정리해 활성 문서에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 게시글/댓글 묶음을 Layer B 3레이어(core_pattern / emotional_register / in_group_mechanics)로 분해
- [x] 기존 ATOM-001~005와 충돌 없이 신규 `ATOM-006`으로 정리
- [x] `world/live/docs/community_grammar_layer_b.md` 및 변경 로그 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/community_grammar_layer_b.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md
- impacted_entities:
  - ATOM-006
  - BOARD-001
  - 낙서장

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-06
- note: 실제 workflow 테스트로 바로 반영 승인
