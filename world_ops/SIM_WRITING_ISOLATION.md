# Simulation/Writing Isolation

## 목적
- 오케스트레이터는 META를 알고 운영한다.
- 시뮬레이션/집필 모델에는 META가 절대 주입되지 않도록 실행 컨텍스트를 분리한다.
- 현재 기본 시뮬레이션 경로는 `Quick Sim`, API run은 fallback이다.
- 경로가 달라도 META 차단 원칙은 동일하다.

## 경로 표기 규칙
- 이 문서에서 `world_bible/`, `docs/`, `characters/`, `quarantine/`, `runs/`는 모두 bundle 루트(`world/live/`) 기준 상대경로다.
- 실행 스크립트 경로만 저장소 루트 기준 실제 경로(`scripts/ops/...`)를 사용한다.

## 접근권한 매트릭스
| profile | PUBLIC | CONFIDENTIAL | META |
|---|---|---|---|
| orchestrator | allow | allow | allow |
| simulation | allow | allow(허용 목록 기반) | deny |
| writing | allow | allow(장면 한정 허용 목록 기반) | deny |

## 실행 트랙

### Quick Sim (default)
- orchestrator가 execution packet을 만들고, Codex 멀티 에이전트에 그 패킷만 전달한다.
- sub-agent에게 raw bundle 경로를 직접 열게 하지 않는다.
- 산출물은 `artifacts/quick_sims/<run_id>/`에 저장한다.
- live 반영 전용 경로가 아니라 `explore only`를 기본값으로 한다.

### API Sim (fallback)
- 기존 `compile -> pre-injection gate -> sim_runner -> output leak scan` 체인을 사용한다.
- 산출물은 `artifacts/runs/<run_id>/`에 저장한다.
- `official candidate` 또는 hard isolation 필요 상황에 사용한다.

## 실행 파이프라인
1. execution view compile
  - 명령: `bash scripts/ops/world_ops_compile_execution_views.sh <run_id> <call_spec_env> [bundle_dir]`
  - 산출물:
    - `artifacts/runs/<run_id>/views/<call_id>.view.md`
    - `artifacts/runs/<run_id>/manifests/<call_id>.manifest.md`

2. pre-injection gate
  - 명령: `bash scripts/ops/world_ops_pre_injection_gate.sh <run_id> <call_spec_env> <payload_file> [bundle_dir]`
  - 검사:
    - payload가 실행뷰 경로를 참조하는지
    - 원본 경로(`world_bible/`, `characters/`, `docs/`, `quarantine/`) 우회 참조가 없는지
    - non-orchestrator payload에 META 금지 패턴이 없는지
  - 실패 시 non-zero 종료

3. output leak scan
  - 명령: `bash scripts/ops/world_ops_output_leak_scan.sh <run_id> <call_spec_env> <model_output_file> [bundle_dir]`
  - 검사:
    - `[META]`, `작가 전용`, `세계의 진실` 등 하드 누출 패턴
    - 고위험 비밀 키워드 누출
  - simulation/writing에서 hard hit 발생 시 실패 처리

## 운영 규칙
- 모델 입력은 항상 `artifacts/runs/<run_id>/views/<call_id>.view.md`만 사용한다.
- model request payload는 gate 통과본(`*.gated.txt`)만 사용한다.
- gate 실패 결과는 재시도 전에 반드시 수정한다.
- Quick Sim에서도 원칙은 같다.
  - agent 입력에는 raw live 문서 경로 대신 execution packet 또는 요약 패키지만 전달한다.
  - Quick Sim 결과는 API 검증 또는 작가 승인 없이 live에 직접 반영하지 않는다.
  - 가능하면 Quick Sim 결과에도 leak hygiene 검토를 붙인다.

## call spec
- 템플릿: `world_ops/templates/execution_call_spec.env`
- 필수 키:
  - `call_id`
  - `profile` (`orchestrator|simulation|writing`)
  - `source_files` (bundle 기준 상대경로, comma-separated)
- 선택 키:
  - `allow_confidential` (`yes|no`)
  - `allow_character_confidential` (`yes|no`)
  - `allow_confidential_ids` (예: `WB-0011,WB-0015`)
