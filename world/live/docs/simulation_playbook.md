# simulation_playbook (dynamic draft)

## 상태
- 이 문서는 강제(`hard/required`) 규칙 문서가 아니다.
- 실행 규칙은 매 실행마다 작가 승인 루프를 통해 조정한다.

## 기본 원칙
- 고정 커뮤니티 구조를 전제하지 않는다.
- 같은 라운드 내 정보 격리만 엔진 규칙으로 유지한다.
- 산출물은 `official`(작품 반영 후보)과 `explore`(탐색 메모)를 분리한다.
- run 결과가 곧바로 새 live 보드 생성/승격을 뜻하지 않는다.
- 모든 run은 `temporal_frame`(`current_canon` / `academy_sandbox` / `future_outline`)를 먼저 명시한다.
- registered 보드를 사용해도 그 보드가 current canon에서 이미 개방됐다는 뜻은 아니다.
- `current_canon` run은 `docs/narrative_state.md`와 해당 회차 canon에서 실제로 열린 표면만 사용한다.
- 기본 시뮬레이션 경로는 `Quick Sim`이다.
- API run은 fallback이자 검증 레인으로 사용한다.

## 실행 트랙

### 1. Quick Sim (default)
- Codex 멀티 에이전트를 활용한 기본 탐색 경로다.
- 산출물은 `artifacts/quick_sims/<run_id>/`에 남긴다.
- 목표:
  - 시드 사건 탐색
  - 게시판 초반 댓글 흐름 샘플
  - Layer B 밈/문법 발화 여부 확인
  - 반응자 선발 논리 점검
- 등급:
  - 기본값은 `explore only`
  - live 직접 반영 금지

### 2. API Sim (fallback / verify)
- gated API runner를 통한 검증 경로다.
- 산출물은 `artifacts/runs/<run_id>/`에 남긴다.
- 목표:
  - hard isolation
  - leak scan
  - board_state promote 직전 검증
  - Quick Sim 결과가 마음에 들지 않을 때 재실행
- 등급:
  - `official candidate`

## 보드 선택 규칙

### 1. 기존 registered 보드 사용
- 이미 `community_map.md`에 등록된 보드를 대상으로 실행한다.
- 같은 보드의 지속 상태가 필요하면 기존 `board_states/` 요약 또는 직전 승인 스냅샷을 함께 참조한다.
- 단, `academy_sandbox` 등록 보드는 current canon에서 아직 미개방일 수 있으므로 run brief에 시간축을 함께 적는다.

### 2. `concept_only` 보드 후보로 탐색
- 장면상 새 게시판이 필요해 보이지만 recurring surface인지 아직 모를 때 사용한다.
- 이 경우:
  - `BOARD-###` ID를 부여하지 않는다.
  - `community_map.md`를 갱신하지 않는다.
  - run 결과는 `simrun-*.json` 탐색 산출물로만 남긴다.

### 3. 새 registered/stateful 보드 승격
- 아래가 충족될 때만 live 보드로 올린다.
  - 작가 승인
  - 기존 보드로는 역할이 대체되지 않음
  - 반복 사용 가능성이 명확함
- 승격 시 순서:
  1. `community_map.md`에 새 보드 등록
  2. 다음 `BOARD-###` ID 부여
  3. 필요하면 `board_states/` 상태 파일 생성
  4. 변경 건(`CR-*`) 기록

## 상태 파일 생성 규칙

- 기본 출력은 `simrun-*.json` 탐색/실행 스냅샷이다.
- 아래 중 하나가 생겼을 때만 보드 전용 상태 파일을 만든다.
  - ongoing conflict
  - moderation precedent
  - recurring meme / rumor chain
  - 다음 회차 실행이 직전 상태를 직접 필요로 함
- smoke test나 분위기 탐색만 한 경우에는 보드 전용 상태 파일을 만들지 않는다.

## 절차 템플릿
1. 입력 정의: 목표 장면, 관련 캐논 범위, 금지/주의 항목 확정
2. 실행 트랙 결정: 기본은 `Quick Sim`, 필요 시 `API Sim`
3. 보드 범위 결정: 기존 registered 보드인지, `concept_only` 후보인지, 승격 검토 대상인지 확정
4. 참여자 구성: 역할 카드 배정, 공개/비공개 정보 경계 설정
5. 라운드 진행: 라운드별 입력 -> 행동/발화 -> 로그 기록
6. 수렴 판정: 충돌 감소 여부, 근거 등급, 남은 모순 점검
7. 결과 분리: `official`과 `explore`를 분리 제출
8. promote 판정: live 반영, 상태 파일 생성, 신규 보드 등록 여부를 별도 판단

## 조절 가능한 파라미터
- 참여자 수: 최소 1명, 상한은 장면 복잡도 기준으로 결정
- 라운드 수: 고정값 없음(수렴 시 조기 종료 가능)
- 출력 포맷: markdown / json / 혼합 중 선택
- 보고 길이: 실행 목적에 맞게 가변
- 근거 임계치: `S/A/B/C/D` 중 이번 실행 기준을 사전 합의

## 금지 규칙
- 토큰 수/문자 수의 고정 범위를 강제하지 않는다.
- 에이전트당 출력 개수 고정(예: JSON 1개 고정)을 강제하지 않는다.
- "항상 같은 규칙" 문구로 운영을 경직시키지 않는다.

## 운영
- 시뮬레이션 관련 변경은 별도 변경 건(`CR-*`)으로 기록한다.
- 과거 강제형 플레이북은 `quarantine/docs/simulation_playbook.md`에 보존한다.
- 기본 진입점은 `Quick Sim`이다.
  - 스캐폴드: `bash scripts/sim/new_quick_sim_run.sh <run_id>`
  - 이후 `artifacts/quick_sims/<run_id>/inputs/`를 채우고 Codex 멀티 에이전트로 실행한다.
  - 결과는 `thread_sample`, `participant_notes`, `scorecard`, `summary`까지 남긴다.
- API fallback 진입점:
  - `bash scripts/ops/world_ops_run_sim.sh <run_id> <call_spec_env> <sim_id> <board_state_file>`
- exploratory/smoke run의 `board_state_file`은 기본적으로 `simrun-*.json` 계열을 사용한다.
- 새 보드가 필요해 보인다고 해서 run 출력만으로 `BOARD-###`를 자동 발급하지 않는다.
- `python3 scripts/sim/sim_runner.py` 직접 실행은 금지한다. 이 스크립트는 API fallback용 gated payload 소비 하위 실행기다.
- 저수준 디버깅이 필요할 때만 아래 순서를 수동으로 사용한다.
  - compile: `scripts/ops/world_ops_compile_execution_views.sh`
  - pre-injection gate: `scripts/ops/world_ops_pre_injection_gate.sh`
  - gated worker: `scripts/sim/sim_runner.py --gated-payload ... --output-json ...`
  - output leak scan: `scripts/ops/world_ops_output_leak_scan.sh`
  - leak scan 통과 후 artifact output을 `board_states/`로 promote

## 트랙 선택 규칙

### Quick Sim부터 시작하는 경우
- 새 사건을 처음 탐색할 때
- Layer B / 낙서장처럼 반응 결과 밈 감도가 중요한 경우
- 작가가 시드 문장을 빠르게 다듬고 싶은 경우
- 반응자 결 차이와 아이디어 밀도를 먼저 보고 싶은 경우

### API로 올리는 경우
- Quick Sim 결과가 마음에 들지 않을 때
- leak scan이 꼭 필요할 때
- live 반영 후보로 승격 검토할 때
- META/CONFIDENTIAL 의존도가 높을 때
- 격리된 재실행이 필요할 때
