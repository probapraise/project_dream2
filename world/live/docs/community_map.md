# community_map (dynamic)

## 상태
- 이 문서는 고정 4권역/18보드 모델을 사용하지 않는다.
- 커뮤니티/게시판 수는 작품 진행에 따라 증감한다.
- 본 문서는 `registered` 커뮤니티/게시판 레지스트리다.
- 여기에는 `current_canon`뿐 아니라 `academy_sandbox`용 등록 표면도 함께 들어갈 수 있다.
- 보드가 여기에 등록되어 있어도 현재 narrative frontier에서 이미 개방됐다는 뜻은 아니다.
- 현재 서사 시점의 실제 개방 여부는 `docs/narrative_state.md`와 해당 회차 canon을 우선 참조한다.
- 과거 고정 18보드 bootstrap stub은 live에서 제거되었고, 역사 자료는 quarantine에만 남긴다.

## Registered communities

### BOARD-001 (레이어 B 대상)
- `board_id`: BOARD-001
- `display_name`: 낙서장
- `lifecycle_status`: registered
- `temporal_frame`: academy_current_term_bootstrap
- `canon_open_status`: pre-academy frontier에서는 아직 미개방
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
- `state_file`: 실제 서사 상태를 추적할 필요가 생길 때만 `board_states/`에 생성

## Board Lifecycle

### 1. `concept_only`
- 장면 기획/시뮬레이션 시드 안에서만 쓰는 임시 보드 후보
- 아직 recurring surface가 아니므로 `BOARD-###` ID를 부여하지 않는다.
- `community_map.md` Registered communities에 등록하지 않는다.
- run 문서나 프롬프트 안에서는 기능 설명형 이름으로만 부른다.

### 2. `registered`
- 작가가 반복 사용 가능한 게시판으로 승인한 상태
- 이 단계에서만 새 `BOARD-###` ID를 부여한다.
- `community_map.md` Registered communities에 등록한다.
- 아직 지속 상태가 필요 없다면 `board_states/` 파일은 만들지 않는다.

### 3. `stateful`
- 밈, 운영 이슈, ongoing conflict, 누적된 판례처럼 다음 장면에도 남겨야 할 상태가 생긴 보드
- 이 단계부터 `board_states/`에 요약 상태 파일 또는 승인된 상태 스냅샷을 둔다.
- 같은 보드의 run 결과가 여러 번 나오더라도, live에 남길 정보는 승인 후 선별 반영한다.

### 4. `retired`
- 더 이상 활성 구조에 쓰지 않는 상태
- Registered communities에서 제거한다.
- 필요 시 history/quarantine에만 흔적을 남긴다.

## ID Policy

- 새 보드 ID는 `BOARD-001`, `BOARD-002`, `BOARD-003`처럼 **3자리 증가형**을 사용한다.
- ID는 `registered` 단계에서만 발급한다.
- 한 번 쓴 ID는 재사용하지 않는다.
- legacy `BOARD-0001~BOARD-0018` 형식은 은퇴했으며 다시 살리지 않는다.

## State Tracking Rule

- 기본값은 **state file 없음**이다.
- 아래 중 하나라도 충족될 때만 `stateful`로 승격한다.
  - 같은 보드가 정식 장면/정식 시뮬레이션에서 반복 사용된다.
  - moderation precedent, conflict, meme, rumor chain처럼 누적 기억이 필요하다.
  - 다음 실행에서 직전 상태를 직접 참조하지 않으면 맥락이 깨진다.
- 단발성 실험, smoke test, 분위기 탐색용 run은 `simrun-*.json`만 남기고 보드 상태 문서로 승격하지 않는다.

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
- `concept_only` 단계의 보드는 live 문서에 등록하지 않는다.
- 새 보드가 필요하면 먼저 recurring surface인지 판단하고, 그렇지 않으면 run/scene 내부 별칭으로만 다룬다.
- 새 `board_state` 파일은 보드가 실제로 활성화되고 상태 누적이 필요할 때만 만든다.
- 삭제/통합/이름변경은 변경 건(`CR-*`)으로 기록한다.
- 과거 고정 매핑 데이터는 `quarantine/docs/community_map.md`와 `quarantine/layer_b/`를 참고한다.
