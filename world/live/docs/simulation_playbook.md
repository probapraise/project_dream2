# simulation_playbook (dynamic draft)

## 상태
- 이 문서는 강제(`hard/required`) 규칙 문서가 아니다.
- 실행 규칙은 매 실행마다 작가 승인 루프를 통해 조정한다.

## 기본 원칙
- 고정 커뮤니티 구조를 전제하지 않는다.
- 같은 라운드 내 정보 격리만 엔진 규칙으로 유지한다.
- 산출물은 `official`(작품 반영 후보)과 `explore`(탐색 메모)를 분리한다.

## 절차 템플릿
1. 입력 정의: 목표 장면, 관련 캐논 범위, 금지/주의 항목 확정
2. 참여자 구성: 역할 카드 배정, 공개/비공개 정보 경계 설정
3. 라운드 진행: 라운드별 입력 -> 행동/발화 -> 로그 기록
4. 수렴 판정: 충돌 감소 여부, 근거 등급, 남은 모순 점검
5. 결과 분리: `official`과 `explore`를 분리 제출

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
- `python3 scripts/sim/sim_runner.py` 직접 실행은 금지한다. 이 스크립트는 gated payload 소비용 하위 실행기다.
- 저수준 디버깅이 필요할 때만 아래 순서를 수동으로 사용한다.
  - compile: `scripts/ops/world_ops_compile_execution_views.sh`
  - pre-injection gate: `scripts/ops/world_ops_pre_injection_gate.sh`
  - gated worker: `scripts/sim/sim_runner.py --gated-payload ... --output-json ...`
  - output leak scan: `scripts/ops/world_ops_output_leak_scan.sh`
  - leak scan 통과 후 artifact output을 `board_states/`로 promote
