# Simulation/Writing Isolation

## 목적
- 오케스트레이터는 META를 알고 운영한다.
- 시뮬레이션/집필 모델에는 META가 절대 주입되지 않도록 실행 컨텍스트를 분리한다.

## 접근권한 매트릭스
| profile | PUBLIC | CONFIDENTIAL | META |
|---|---|---|---|
| orchestrator | allow | allow | allow |
| simulation | allow | allow(허용 목록 기반) | deny |
| writing | allow | allow(장면 한정 허용 목록 기반) | deny |

## 실행 파이프라인
1. execution view compile
  - 명령: `bash scripts/world_ops_compile_execution_views.sh <run_id> <call_spec_env> [bundle_dir]`
  - 산출물:
    - `runs/<run_id>/views/<call_id>.view.md`
    - `runs/<run_id>/manifests/<call_id>.manifest.md`

2. pre-injection gate
  - 명령: `bash scripts/world_ops_pre_injection_gate.sh <run_id> <call_spec_env> <payload_file> [bundle_dir]`
  - 검사:
    - payload가 실행뷰 경로를 참조하는지
    - 원본 경로(`world_bible/`, `characters/`, `docs/`, `quarantine/`) 우회 참조가 없는지
    - non-orchestrator payload에 META 금지 패턴이 없는지
  - 실패 시 non-zero 종료

3. output leak scan
  - 명령: `bash scripts/world_ops_output_leak_scan.sh <run_id> <call_spec_env> <model_output_file> [bundle_dir]`
  - 검사:
    - `[META]`, `작가 전용`, `세계의 진실` 등 하드 누출 패턴
    - 고위험 비밀 키워드 누출
  - simulation/writing에서 hard hit 발생 시 실패 처리

## 운영 규칙
- 모델 입력은 항상 `runs/<run_id>/views/<call_id>.view.md`만 사용한다.
- model request payload는 gate 통과본(`*.gated.txt`)만 사용한다.
- gate 실패 결과는 재시도 전에 반드시 수정한다.

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
