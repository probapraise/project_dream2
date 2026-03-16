# Full Setting Audit

- change_id: CR-20260315-002
- audit_date: 2026-03-16
- status: active

## 1. 왜 전수 감사가 필요한가

- 이번 변경은 용어 몇 개를 바꾸는 수준이 아니라, `주인공 성장선`, `학술원 pacing`, `플랫폼 개화 순서`, `LMM 상한`을 함께 갈아엎은 구조 변경이다.
- 특히 기존의 `하급 과정은 맛보기/병목 확인`, `상급 과정부터 본편`, `성목-LMM이 곧바로 전면 목표` 축은 이제 SSOT 불변식이 아니다.
- 따라서 검색 치환만으로는 부족하고, 문서군을 `현재 집필에 직접 주입되는 층`, `live SSOT 층`, `역사 보존 아티팩트 층`으로 나눠 감사해야 한다.

## 2. 이번 변경의 새 불변식

1. `하급 과정 = 준비 구간`이 아니다.
   하급 과정부터 `조회 -> 보충 -> 질문 -> 초기 검색` 같은 저단계 기능을 실제로 하나씩 연다.
2. `상급 과정 = 커뮤니티 시작점`이 아니다.
   상급 과정은 하급 과정에서 축적된 기능을 확장/제도화하고, 후행 `현상 각인/영상 각인술`과 학파 정치로 가속하는 구간이다.
3. `그리모어 -> 성목 분지 -> 배지`가 플랫폼의 기본 삼층이다.
   배지는 끝까지 얇은 표준 단말이고, `현상 열람실`은 고정식 예외 설비다.
4. `LMM`은 공용 표면의 전면 목표가 아니다.
   학생 체감 상한은 추천/정렬/의도 색인 수준이고, 더 깊은 추론선은 후행 비공개 레인이다.
5. `영상 슬롯` 경제는 폐기됐다.
   현재 권력 자원은 `영상 업로더 할당량`, `현상 열람 자격`, `기록 등급`, `플랫폼 정렬/보존권` 축으로 읽는다.

## 3. 감사 범위와 처리 원칙

### A. 반드시 수정

- `world/live/world_bible/*`
- `world/live/docs/*` 중 `narrative_state`, `story_arcs`, `memory_tiers/*`, `core_cast_bootstrap_v1`, 인덱스/허브 문서
- `world/live/population/core_cast/*` 중 현재 서사 방향을 직접 설명하는 카드
- `docs/handoff/*` 중 다음 세션 방향을 고정하는 문서

### B. 수정 또는 강한 경고 필요

- `artifacts/writing/episodes/*/prompt_v*.md`
- 현재도 사람이 재참조할 가능성이 높은 과거 집필 프롬프트

### C. 역사 보존으로 남기되 감사표에 기록

- `artifacts/briefings/external_review/*`
- `artifacts/runs/*`
- 과거 리뷰/실행 뷰/런 로그

원칙:
- 이 범주는 과거 시점 산출물이라 본문을 무리하게 현대화하지 않는다.
- 다만 이후 검색에서 혼선을 줄 필요가 있으면 별도 경고 문구나 참조 금지 원칙을 붙인다.

## 4. 2026-03-16 1차 발견 사항

### 즉시 수정 대상

- `world/live/docs/narrative_state.md`
  - 여전히 `하급 과정 병목 확인 -> 3년 스킵 -> 상급 과정 본편` 축이 남아 있다.
- `world/live/docs/story_arcs.md`
  - ARC-003이 아직 `하급 과정 진입과 상급 과정 점프`를 기본 아크 질문으로 잡고 있다.
- `world/live/docs/memory_tiers/long_term.md`
  - 장기 약속 문서가 구 성장선을 다시 주입한다.
- `world/live/population/core_cast/NC-0001_P-1027.md`
  - 학원 진입선 설명이 아직 `병목 파악 -> 상급 과정 입학 즉시 선택` 중심이다.
- `world/live/world_bible/WB-0012_core_conflict_arcs.md`
  - 플랫폼 갈등을 단일 사건처럼 압축해 단계별 개시가 보이지 않는다.
- `world/live/world_bible/WB-0015_academy_bible.md`
  - 하급 과정 커리큘럼에 `초기 각인광장 기능 해금`이 제도적으로 써 있지 않다.
- `docs/handoff/next_steps.md`
  - 하급 과정 축소/3년 후 점프 전제가 다음 세션 지침으로 남아 있다.

### 고위험 참조 아티팩트

- `artifacts/writing/episodes/ep000_prologue/prompt_v1.md`
- `artifacts/writing/episodes/ep001/prompt_v1.md`
- `artifacts/writing/episodes/ep001/prompt_v2.md`
- `artifacts/writing/episodes/ep002/prompt_v1.md`

공통 문제:
- 로그라인이 아직 `성목을 학습형 마나 모델(LMM)로 진화시켜` 계열이다.
- 현행 기준에서는 deprecated growthline이므로 최소한 최신 로그라인과 경고 문구가 필요하다.

### 경계 대상

- `world/live/docs/core_cast_bootstrap_v1.md`
  - academy current-term bootstrap 문서인데, 현재 서사 시점과 혼동될 수 있다.
- `world/live/population/P-1027.yaml`
  - academy 스냅샷 슬롯이므로 즉시 수정 대상은 아니지만, 현재 narrative state와 혼동되지 않게 구분해야 한다.

## 5. 2026-03-16 1차 조치

### 수정 완료

- `world/live/docs/narrative_state.md`
- `world/live/docs/story_arcs.md`
- `world/live/docs/memory_tiers/long_term.md`
- `world/live/world_bible/WB-0012_core_conflict_arcs.md`
- `world/live/world_bible/WB-0015_academy_bible.md`
- `world/live/population/core_cast/NC-0001_P-1027.md`
- `world/live/docs/core_cast_bootstrap_v1.md`
- `docs/handoff/next_steps.md`
- `artifacts/writing/episodes/ep000_prologue/prompt_v1.md`
- `artifacts/writing/episodes/ep001/prompt_v1.md`
- `artifacts/writing/episodes/ep001/prompt_v2.md`
- `artifacts/writing/episodes/ep002/prompt_v1.md`

### 역사 보존 대상으로 남긴 범주

- `artifacts/briefings/external_review/*`
- `artifacts/runs/*`

설명:
- 이 범주는 과거 시점 산출물이므로 본문을 현재 SSOT에 맞춰 재작성하지 않았다.
- 대신 현재 집필에 직접 주입되는 층에서는 구 성장선이 다시 살아나지 않도록 허브, handoff, prompt artifact에 경고와 최신 표현을 반영했다.

## 6. 현재 작업 패킷

- 패킷 A: live SSOT의 구조 드리프트 수정
- 패킷 B: prompt-facing/handoff 드리프트 수정
- 패킷 C: historical artifact 처리 원칙 고정

## 7. 2026-03-16 2차 발견 사항

### 시점 혼선 위험군

- `world/live/docs/character_index_v2.md`
  - academy current-term bootstrap 인덱스인데, 현재 narrative time의 활성 인원표처럼 오독될 수 있다.
- `world/live/docs/population_grammar.md`
  - 3,600명 모집단 분포를 설명하지만, pre-academy current canon과의 시간축 분리가 약하다.
- `world/live/population/profiles/current_term_snapshot_v1.yaml`
  - snapshot 프로필이라는 설명은 있으나, 현재 서사 시점과 별개인 academy layer라는 경계가 더 필요하다.
- `world/live/docs/simulation_playbook.md`
  - registered board, exploratory run, current canon run 사이의 시간축 구분 규칙이 약하다.
- `world/live/docs/simulation_state_index.md`
  - 경로가 등록된 run/board_state가 current canon 개방 상태로 오해될 수 있다.
- `world/live/docs/simulation_feedback.md`
  - cold-start baseline을 기본적으로 academy_sandbox로 읽어야 한다는 규칙이 빠져 있다.
- `world/live/docs/community_map.md`
  - registered board registry와 현재 narrative frontier에서 실제 개방된 표면 사이의 경계가 약하다.
- `world/live/docs/community_grammar_layer_b.md`
  - `낙서장` 문법 정의가 곧 현재 canon 개방으로 오독될 수 있다.
- `world/live/board_states/README.md`
  - state snapshot 존재 자체가 current canon 상태 확정처럼 읽힐 수 있다.

## 8. 2026-03-16 2차 조치

### 수정 완료

- `scripts/indexes/rebuild_character_index_v2.py`
- `world/live/docs/character_index.md`
- `world/live/docs/population_grammar.md`
- `world/live/population/profiles/current_term_snapshot_v1.yaml`
- `scripts/README.md`
- `scripts/population/add_student_fields.py`
- `world/live/docs/simulation_playbook.md`
- `world/live/docs/simulation_state_index.md`
- `world/live/docs/simulation_feedback.md`
- `world/live/docs/community_map.md`
- `world/live/docs/community_grammar_layer_b.md`
- `world/live/board_states/README.md`

설명:
- `population/index` 문서군에는 `academy current-term snapshot`과 `current narrative time`의 경계를 명시했다.
- `simulation/community` 문서군에는 `registered board registry`, `temporal_frame`, `academy_sandbox` 해석 규칙을 추가했다.
- 생성기가 다시 문서를 덮어써도 시점 경계가 유지되도록 `character_index_v2` 생성 스크립트와 population snapshot 스크립트 설명도 함께 갱신했다.
- `P-*` 원본 슬롯은 3,600개 전체를 즉시 재기록하지 않고, 우선 상위 허브/프로필/생성기 층에서 시점 경계를 고정했다. 자주 읽히는 `P-1027` 원본 슬롯에는 직접 경고 주석을 추가했다.
