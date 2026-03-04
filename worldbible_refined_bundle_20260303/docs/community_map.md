# community_map (dynamic)

## 상태
- 이 문서는 고정 4권역/18보드 모델을 사용하지 않는다.
- 커뮤니티/게시판 수는 작품 진행에 따라 증감한다.
- 본 문서는 현재 활성 구조만 기록한다.

## Active communities

### BOARD-001 (레이어 B 대상)
- `board_id`: BOARD-001
- `display_name`: 낙서장
- `tone`: 혼돈·냉소·내부자 유머
- `anonymity_mode`: 완전 익명
- `taboos[]`: (ATOM 누적 후 도출)
- `content_types[]`: (ATOM 누적 후 도출)
- `moderation_style`: 주인공 직접 관리
- `user_power_structure`: 평등 익명 — 계급 무효
- `incident_patterns[]`: (ATOM 누적 후 도출)
- `meme_seeds[]`: (ATOM 누적 후 도출)
- `layer_b`: true
- `narrative_role`: 주인공의 취미 공간. 상업적 목적 배제. 조력자들의 폐쇄 압박 vs. 주인공의 고집이 서사 마찰 생성.
- `spec`: docs/community_grammar_layer_b.md

## 분류 원칙
- 고정 zone(A/B/C/D) 대신 태그 기반 동적 분류를 사용한다.
- 권장 태그 축:
  - `tone`
  - `anonymity_mode`
  - `taboos`
  - `content_types`
  - `moderation_style`
  - `user_power_structure`
  - `incident_patterns`
  - `meme_seeds`
- 태그 축은 필요 시 추가/삭제 가능하며, 필수 개수는 강제하지 않는다.

## 템플릿
### community card (dynamic)
- `community_id`
- `display_name`
- `boards[]`
- `policy_tags[]`

### board culture card (dynamic)
- `board_id`
- `display_name`
- `tone`
- `anonymity_mode`
- `taboos[]`
- `content_types[]`
- `moderation_style`
- `user_power_structure`
- `incident_patterns[]`
- `meme_seeds[]`

## 운영 규칙
- 새 커뮤니티/게시판은 작가-오케스트레이터 합의 후 추가한다.
- 삭제/통합/이름변경은 변경 건(`CR-*`)으로 기록한다.
- 과거 고정 매핑 데이터는 `quarantine/docs/community_map.md`를 참고한다.
