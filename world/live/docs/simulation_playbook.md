# simulation_playbook (dynamic draft)

## 상태
- 이 문서는 강제(`hard/required`) 규칙 문서가 아니다.
- 실행 규칙은 매 실행마다 작가 승인 루프를 통해 조정한다.

## 기본 원칙
- 고정 커뮤니티 구조를 전제하지 않는다.
- 같은 라운드 내 정보 격리만 엔진 규칙으로 유지한다.
- 산출물은 `official`(작품 반영 후보)과 `explore`(탐색 메모)를 분리한다.
- run 결과가 곧바로 새 live 보드 생성/승격을 뜻하지 않는다.

## 보드 선택 규칙

### 1. 기존 registered 보드 사용
- 이미 `community_map.md`에 등록된 보드를 대상으로 실행한다.
- 같은 보드의 지속 상태가 필요하면 기존 `board_states/` 요약 또는 직전 승인 스냅샷을 함께 참조한다.

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
2. 보드 범위 결정: 기존 registered 보드인지, `concept_only` 후보인지, 승격 검토 대상인지 확정
3. 참여자 구성: 역할 카드 배정, 공개/비공개 정보 경계 설정
4. 라운드 진행: 라운드별 입력 -> 행동/발화 -> 로그 기록
5. 수렴 판정: 충돌 감소 여부, 근거 등급, 남은 모순 점검
6. 결과 분리: `official`과 `explore`를 분리 제출
7. promote 판정: live 반영, 상태 파일 생성, 신규 보드 등록 여부를 별도 판단

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
- 실제 모델 실행은 `bash scripts/ops/world_ops_run_sim.sh <run_id> <call_spec_env> <sim_id> <board_state_file>`를 기본 진입점으로 사용한다.
- exploratory/smoke run의 `board_state_file`은 기본적으로 `simrun-*.json` 계열을 사용한다.
- 새 보드가 필요해 보인다고 해서 run 출력만으로 `BOARD-###`를 자동 발급하지 않는다.
- `python3 scripts/sim/sim_runner.py` 직접 실행은 금지한다. 이 스크립트는 gated payload 소비용 하위 실행기다.
- 저수준 디버깅이 필요할 때만 아래 순서를 수동으로 사용한다.
  - compile: `scripts/ops/world_ops_compile_execution_views.sh`
  - pre-injection gate: `scripts/ops/world_ops_pre_injection_gate.sh`
  - gated worker: `scripts/sim/sim_runner.py --gated-payload ... --output-json ...`
  - output leak scan: `scripts/ops/world_ops_output_leak_scan.sh`
  - leak scan 통과 후 artifact output을 `board_states/`로 promote
