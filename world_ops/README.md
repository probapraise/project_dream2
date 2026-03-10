# World Ops (Dream2)

## 목적
- 이 디렉터리는 `project_dream2`의 **세계관 관리 프로세스**를 운영하기 위한 실행 레이어다.
- 목표는 초안 번들의 완성도가 아니라, 변경 요청이 들어왔을 때 **빠르게 정제/탐색/적용/동기화**를 반복할 수 있는 운영 체계를 고정하는 것이다.

## 문서 역할과 기준
- `world/live/`
  - 현재 실제로 운영되는 세계관 데이터 번들이다.
  - 변경 요청, 실행, 시뮬레이션, 인덱스, 상태 점검의 **1차 SSOT** 다.
  - 실제 작업 시작은 `world/live/docs/master_map.md`를 먼저 읽는 것을 기본으로 한다.
- `docs/history/대화 로그.txt`
  - 스펙 시트 초안을 만들기 전에 기록한 초기 대화 로그다.
  - 현재 운영 규칙의 SSOT가 아니라, 설계 배경과 의도 추적용 히스토리 문서로 취급한다.
- `docs/design/spec_sheet_v1.md`
  - 프로젝트 구현을 위해 작성한 상위 설계/요구사항 문서다.
  - 시스템 방향, 제약, 구현 목표를 해석할 때 쓰는 **2차 설계 기준** 이다.
  - live bundle과 충돌하면 직접 경로 지시문으로 쓰지 않고 변경관리 이슈로 올린다.
- `artifacts/batch/`
  - 파생 지표 배치 요청/응답/병합본처럼 재생성 가능한 산출물을 보관한다.
  - 운영 정책 문서나 SSOT로 취급하지 않는다.
- `artifacts/runs/`, `artifacts/writing/`
  - 실행 게이트 산출물과 집필 산출물의 실제 저장 위치다.
  - live bundle 쪽에서는 호환 링크를 통해 접근한다.

> 요약: `world/live/`가 1차 SSOT, `docs/design/spec_sheet_v1.md`는 2차 설계 기준, `docs/history/대화 로그.txt`는 과거 맥락이다. 재생성 가능한 배치 산출물은 `artifacts/batch/`에 분리 보관한다. 문서 간 충돌은 world_ops 변경관리 절차로 정리한다.

## 범위
- 포함: 세계관 변경 관리 (4-Phase, minor/major 분기, 승인 루프, 인덱스 동기화)
- 제외: 시뮬레이션 실행, 집필 파이프라인, 스타일 학습

## 실행 격리 (시뮬/집필)
- 오케스트레이터는 META 접근권한이 있으나, 시뮬레이션/집필 모델은 META 비노출이 기본 규칙이다.
- 세부 규칙과 커맨드: `world_ops/SIM_WRITING_ISOLATION.md`

## 통삭제 금지 규칙 (중요)
- 기본값은 **파일 단위 삭제 금지**다.
- 충돌은 반드시 구간(line span) 단위로 식별하고, 부분 수정/격리를 우선한다.
- 파일 삭제가 필요한 경우에만 `deletion_gate` 문서를 작성해 예외 처리한다.
- 삭제가 staged 된 상태에서는 `scripts/ops/world_ops_delete_guard.sh <change_id>` 통과 전 커밋하지 않는다.

## 경로 표기 규칙
- 케이스 문서의 `impacted_files`와 산출물 경로는 저장소 루트 기준 실제 경로로 기록한다.
- 예:
  - `world/live/docs/master_map.md`
  - `world/live/docs/world_bible_index_v2.md`
  - `world/live/world_bible/WB-0002_loreops_canon_control.md`
- bundle 내부 별칭(`docs/...`, `world_bible/...`)은 본문 설명용으로만 쓰고, 파일 목록에는 쓰지 않는다.

## 4-Phase 프로세스 (SSOT 기준)
### Phase 1. 요청 정제
- 입력: 작가의 자연어 변경 요청
- 오케스트레이터 역할: 요청을 실행 가능한 변경안으로 정제
- 산출물: `world_ops/cases/<change_id>/request.md`

### Phase 2. 충돌 탐색
- 기준: `world/live/docs/master_map.md` + `world/live/docs/world_bible_index_v2.md` + 연관 섹션
- 오케스트레이터 역할: 탐색 범위 지정, 충돌/누락/중복 후보 수집
- 산출물: `world_ops/cases/<change_id>/phase2_report.md`
- 분기: `minor` or `major`

### Phase 3. 변경 적용
- minor: 대상 파일 직접 수정 후 요약 보고
- major: 외부 고급 모델 재작성 경로 + 프롬프트 로그 기록 + 3자 대조 검증
- 산출물:
  - `world_ops/cases/<change_id>/phase3_apply.md`
  - `world_ops/cases/<change_id>/major_prompt_log.md` (major)
  - `world_ops/cases/<change_id>/tri_diff_verify.md` (major)

### Phase 4. 동기화
- 변경 반영 후 인덱스와 로그 동기화
- 산출물:
  - `world_ops/cases/<change_id>/phase4_sync.md`
  - `world_ops/world_change_log.md`

## 승인 원칙
- 모든 정식 반영은 `제안 → 작가 승인/수정 → 반영` 순서를 따른다.
- 승인 전에는 "임시 제안" 상태로만 유지한다.

## 완료 조건 (DoD)
- 변경 목표 충족
- 미해결 충돌이 없거나 보류 사유가 문서화됨
- 인덱스 참조가 실제 파일과 일치
- 세션 문서와 변경 로그가 기록됨

## 사용 순서
1. `bash scripts/ops/world_ops_new_case.sh CR-YYYYMMDD-001`
2. 생성된 케이스 문서에 내용 작성
3. 필요 시 파일 수정
4. (major면) `bash scripts/ops/world_ops_new_case.sh <change_id> --major`
5. (삭제가 있으면) `world_ops/cases/<change_id>/deletion_gate.md` 작성 또는 `--deletion-gate`로 생성
6. (삭제가 있으면) `bash scripts/ops/world_ops_delete_guard.sh <change_id>`
7. `bash scripts/ops/world_ops_audit_bundle.sh` (인덱스/프론트매터 + 정본 용어/CSV 스키마 충돌 검사)
8. `world_ops/world_change_log.md` 갱신

## 시뮬/집필 실행 전 필수 게이트
### 기본 경로 (Quick Sim)
- `bash scripts/sim/new_quick_sim_run.sh <run_id>`
- 이 스캐폴드 아래 `artifacts/quick_sims/<run_id>/inputs/`를 채우고, Codex 멀티 에이전트로 run을 진행한다.
- Quick Sim은 기본적으로 `explore only`이며 live 직접 반영 경로가 아니다.

### fallback 경로 (API simulation)
- `bash scripts/ops/world_ops_run_sim.sh <run_id> <call_spec_env> <sim_id> <board_state_file>`
- 이 래퍼가 `compile -> pre-injection gate -> sim_runner -> output leak scan -> live promote`를 순서대로 수행한다.
- `python3 scripts/sim/sim_runner.py` 직접 실행은 지원하지 않는다. `sim_runner.py`는 API fallback용 gated payload 소비 하위 실행기다.

### 저수준 수동 절차
1. `bash scripts/ops/world_ops_compile_execution_views.sh <run_id> <call_spec_env>`
2. `bash scripts/ops/world_ops_pre_injection_gate.sh <run_id> <call_spec_env> <payload_file>`
3. `python3 scripts/sim/sim_runner.py --gated-payload <gated_payload> --output-json <artifact_output_json> --output-report <artifact_output_report>`
4. `bash scripts/ops/world_ops_output_leak_scan.sh <run_id> <call_spec_env> <artifact_output_report>`
5. leak scan 통과 후에만 `artifacts/runs/<run_id>/outputs/*.json`을 `world/live/board_states/`로 promote

> `call_spec_env` 템플릿: `world_ops/templates/execution_call_spec.env`

## 근본 해결 문서
- `world_ops/ROOT_SOLUTION.md`
