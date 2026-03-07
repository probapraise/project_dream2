# 다음 작업 목록

최종 업데이트: 2026-03-07 (프롤로그/1화 리라이트 캐논 반영 및 live sync)
진행 상태 기준 커밋: `9767b54c8d7e9152458338fb0fe0109f617d51dc`

---

## 이 문서의 기준

- 이 문서는 과거 Step 회고가 아니라, **현재 저장소에 실제로 남아 있는 상태와 작가 결정**을 기준으로 다음 작업을 정리한다.
- live SSOT는 `world/live/`다.
- 변경관리 이슈는 `world_ops` 케이스로 처리한다.
- 로컬 감사 결과:
  - `bash scripts/ops/world_ops_audit_bundle.sh`
  - 결과: `errors=0`, `warnings=0`

---

## 현재 실제 상태 요약

### 1. 월드/모집단
- 학생 슬롯 SSOT:
  - `world/live/population/P-*.yaml`
  - `world/live/population/population_slots.csv`
- 총 슬롯: `3600`
- 상태 분포:
  - `uninstantiated=3599`
  - `named=1`
- 현재 named 슬롯:
  - `P-1027 -> NC-0001`

### 2. 코어 캐스트
- `world/live/population/core_cast/NC-0001_P-1027.md`만 존재한다.
- `world/live/docs/core_cast_bootstrap_v1.md` 상태는 `partial`이다.
- 다만 **NC-0002 이후 코어 캐스트 추가는 지금 바로 하지 않는다.**
- 작가 결정:
  - 주인공이 학술원에 입학한 뒤
  - 본격적인 시뮬레이션을 돌리면서
  - 그 흐름 속에서 NC를 추가한다.

### 3. 커뮤니티 구조
- 기존 고정 18보드 설정은 폐기됐다.
- 2026-03-06 기준으로 live `board_states/`의 `BOARD-0001_b01.md` ~ `BOARD-0018_b18.md` bootstrap stub은 제거 완료.
- 현재 원칙:
  - 커뮤니티/게시판은 동적 생성
  - `concept_only -> registered -> stateful -> retired` lifecycle로 관리
  - 필요한 보드만 `community_map.md`와 `board_states/`에 추가
  - 선제적으로 18개 보드를 깔아두지 않음
  - 새 ID는 `BOARD-001`, `BOARD-002` 식 3자리 증가형만 사용
- 과거 18보드 역사 자료는 `world/archive/quarantine/`에만 남긴다.

### 4. 시뮬레이션 산출물
- 현재 live에 있는 시뮬레이션 JSON:
  - `world/live/board_states/simrun-001_cold_start.json`
  - `world/live/board_states/simrun-002_pro_cold_start.json`
  - `world/live/board_states/simrun-003_pro_thinking_cold_start.json`
- 작가 결정:
  - 이 산출물들은 **간략 smoke test 결과물**
  - 당분간 정식 Layer A 문화 판단 근거로 쓰지 않음
  - `community_memory.md`나 `community_grammar_layer_a.md`에 승격하지 않음

### 5. Layer B
- `world/live/docs/community_grammar_layer_b.md`에 `ATOM-001~ATOM-006` 누적 완료
- 현재 단계:
  - ATOM 축적 진행 중
  - 상위 `GRAMMAR-*` 합성은 아직 시작 전

### 6. 집필
- 확정 원고:
  - `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v2.md`
  - `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md` (`current canon`)
- `artifacts/writing/style/style_constitution.md`는 리라이트 캐논의 결말 박자에 맞춰 S-07/S-08을 보정했고, live `style_bible.md`도 새 캐논 기준으로 재동기화됨
- 에피소드 폴더 규칙:
  - 각 에피소드 폴더는 생성 시점부터 `canon/` 하위 폴더 포함
  - 정식 반영된 최종본은 `canon/` 안에만 둠
  - `canon/README.md`가 current canon을 명시
  - canon은 수정 가능하며, 새 리비전 채택 시 `canon/` 내부에서 current를 갱신
  - 새 episode 폴더 생성은 `bash scripts/writing/new_episode_scaffold.sh <episode_id>`를 사용
- live 서사 상태 문서:
  - `world/live/docs/narrative_state.md` -> 현재 활성 서사 허브
  - `world/live/docs/story_arcs.md` -> 아크 단위 압축 메모리
  - `world/live/docs/foreshadow_registry.md` -> 활성 복선 레지스트리
  - `world/live/docs/episode_deltas.md` -> 회차별 상태 변화 로그
- 문체 상태 문서:
  - `world/live/docs/style_bible.md` -> 리라이트 캐논 기준 현재 필체 요약 반영 완료

### 7. VFP
- `world/live/docs/voice_fingerprint_spec.md` 존재
- NC-0001 카드에는 VFP v1 반영 완료
- 하지만 실행 체인에는 아직 주입/검증 코드가 연결되지 않았다.

### 8. 문서/레지스트리 드리프트
- `world/live/docs/simulation_state_index.md`
  - 실제 `artifacts/runs/`와 일부 불일치
- `world/live/docs/character_index_v2.md`
  - 헤더 `source_csv`가 예전 절대 경로를 가리킴
- `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`
  - 대상 루트가 예전 절대 경로로 남아 있음

---

## 우선순위 A: 지금 바로 할 일

### A-1. `ep002` 집필 입력 정리

이유:
- 장기 연재용 narrative context 허브와 live `style_bible`은 정리됐지만, 리라이트된 캐논을 바탕으로 한 `ep002` 입력 패키지는 아직 미완이다.

해야 할 일:
- `world/live/docs/narrative_state.md`, `story_arcs.md`, `foreshadow_registry.md`, `episode_deltas.md`를 참조해 `ep002` 기획 입력을 정리
  - 책 읽기 = 관찰 장치 구도
  - 렌바렌 저택 정보 병목과 집사실 문답 온도의 후속 관찰 범위
  - 아직 설계/실행으로 점프하지 않는 박자 유지
  - 학술원까지 4년이라는 시간축을 당장 외부 확장 트리거로 쓰지 않는 박자 유지

완료 조건:
- 다음 집필 프롬프트가 live narrative hub와 style 문서를 함께 참조할 수 있다.

### A-2. 실행 레지스트리/경로 드리프트 정리

해야 할 일:
- `world/live/docs/simulation_state_index.md`를 실제 `artifacts/runs/` 구조에 맞게 갱신
- `world/live/docs/character_index_v2.md` 재생성 또는 헤더 정리
- `docs/architecture/PROJECT_ARCHITECTURE_MAP.md` 루트 경로 정정

완료 조건:
- 사람이 읽는 인덱스 문서와 실제 파일 시스템이 다시 일치한다.

### A-3. Layer B ATOM 계속 누적

현재 상태:
- ATOM 6개 누적
- 아직 상위 문법 합성 전

해야 할 일:
- 실제 커뮤니티 사례를 더 수집해 `ATOM-007+` 이어서 추가
- 10~15개 축적 후 상위 `GRAMMAR-*`로 묶을지 판단

---

## 보류/조건부 작업

### 코어 캐스트 확장
- 보류 이유:
  - 지금은 시점이 이름 붙이기보다 입학 이후 시뮬레이션 설계가 먼저다.
- 재개 조건:
  - 주인공 학술원 입학 이후
  - 본격 시뮬레이션에서 반복적으로 포착되는 인물 축이 생길 때

### 현재 simrun 결과의 Layer A 승격
- 보류 이유:
  - 현재 `simrun-001~003`은 smoke test 취급
- 재개 조건:
  - 정식 목적과 참여자 조건을 갖춘 시뮬레이션을 다시 실행했을 때

### VFP 실행 파이프라인 연결
- 보류 이유:
  - 반복 등장 인물과 본격 시뮬레이션 루프가 아직 충분히 열리지 않았다.
- 재개 조건:
  - 실제 recurring cast와 정식 sim/writing 사이클이 돌기 시작했을 때

---

## 조건부/트리거 작업

### 새 게시판을 live에 추가할 때
- `community_map.md` 먼저 갱신
- 필요 시에만 `board_states/`에 상태 파일 생성
- 변경 건이면 `world_ops` 케이스 기록

### 새 named/core cast를 추가할 때
- `python3 scripts/indexes/rebuild_character_index_v2.py`
- 필요 시 `bash scripts/ops/world_ops_audit_bundle.sh`

### 다음 회차 원고 캐논 확정 직후
- `artifacts/writing/episodes/<episode_id>/canon/`에 정식 반영본 배치
- `artifacts/writing/episodes/<episode_id>/canon/README.md` current 항목 갱신
- `artifacts/writing/style/style_constitution.md` 갱신
- `world/live/docs/style_bible.md` 갱신
- `world/live/docs/narrative_state.md` 갱신
- `world/live/docs/episode_deltas.md`에 상태 변화 추가
- 필요 시 `world/live/docs/story_arcs.md`, `world/live/docs/foreshadow_registry.md` 압축 갱신

### 정식 시뮬레이션 실행 직후
- `world/live/docs/simulation_state_index.md` 갱신
- `community_memory.md` 반영 여부 판단
- recurring 인물 VFP 후보 추출 여부 판단

---

## 지금 당장 다시 돌릴 필요 없는 것

- 모집단 생성 스크립트 전량 재실행
- 파생지표 배치 재생성
- 외국인 origin 재배정
- dorm/major 재계산
- 현재 smoke test simrun을 Layer A 문서로 승격하는 작업
- NC-0002 이후 코어 캐스트 선제 추가

이유:
- 현재 감사(`world_ops_audit_bundle.sh`)는 통과 상태다.
- 작가 판단상 시뮬레이션과 코어 캐스트는 **입학 이후 본격 루프에서 다시 잡는 게 맞다.**

---

## 다음 세션 권장 시작 순서

1. `world/live/docs/style_bible.md`를 채우고, 새 narrative hub(`narrative_state`/`story_arcs`/`foreshadow_registry`/`episode_deltas`) 기준으로 `ep002` 기획 입력을 만든다.
2. `world/live/docs/simulation_state_index.md`, `world/live/docs/character_index_v2.md`, `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`의 경로 드리프트를 정리한다.
3. `community_grammar_layer_b.md`의 ATOM을 계속 누적한다.
4. 그 다음에야 입학 이후 정식 시뮬레이션과 NC 코어 캐스트 확장으로 넘어간다.

---

## 참고 문서

- `world/live/docs/master_map.md`
- `world/live/docs/community_map.md`
- `world/live/docs/simulation_playbook.md`
- `world/live/board_states/README.md`
- `world/live/docs/community_grammar_layer_b.md`
- `world/live/docs/narrative_state.md`
- `world/live/docs/story_arcs.md`
- `world/live/docs/foreshadow_registry.md`
- `world/live/docs/episode_deltas.md`
- `world/live/docs/style_bible.md`
- `world/live/docs/voice_fingerprint_spec.md`
- `world/live/docs/simulation_state_index.md`
- `world/live/docs/core_cast_bootstrap_v1.md`
- `artifacts/writing/README.md`
- `artifacts/writing/episodes/README.md`
- `scripts/writing/new_episode_scaffold.sh`
- `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`
