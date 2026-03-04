# World Ops (Dream2)

## 목적
- 이 디렉터리는 `project_dream2`의 **세계관 관리 프로세스**를 운영하기 위한 실행 레이어다.
- 목표는 초안 번들의 완성도가 아니라, 변경 요청이 들어왔을 때 **빠르게 정제/탐색/적용/동기화**를 반복할 수 있는 운영 체계를 고정하는 것이다.

## SSOT 우선순위 (강제)
1. `conversation_log.md` (Turn 1~44 합의)
2. `spec_sheet_v1.md` (v1.1)
3. `worldbible_refined_bundle_20260303/` (운영 대상 데이터, 규칙 SSOT 아님)

> 번들 내부 문서의 규약 문구는 "정본 규칙"이 아니라 "초안 데이터"로 취급한다.

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
- 삭제가 staged 된 상태에서는 `scripts/world_ops_delete_guard.sh <change_id>` 통과 전 커밋하지 않는다.

## 4-Phase 프로세스 (SSOT 기준)
### Phase 1. 요청 정제
- 입력: 작가의 자연어 변경 요청
- 오케스트레이터 역할: 요청을 실행 가능한 변경안으로 정제
- 산출물: `sessions/<change_id>_request.md`

### Phase 2. 충돌 탐색
- 기준: `master_map` + `world_bible_index` + 연관 섹션
- 오케스트레이터 역할: 탐색 범위 지정, 충돌/누락/중복 후보 수집
- 산출물: `sessions/<change_id>_phase2_report.md`
- 분기: `minor` or `major`

### Phase 3. 변경 적용
- minor: 대상 파일 직접 수정 후 요약 보고
- major: 외부 고급 모델 재작성 경로 + 프롬프트 로그 기록 + 3자 대조 검증
- 산출물:
  - `sessions/<change_id>_phase3_apply.md`
  - `sessions/<change_id>_major_prompt_log.md` (major)
  - `sessions/<change_id>_tri_diff_verify.md` (major)

### Phase 4. 동기화
- 변경 반영 후 인덱스와 로그 동기화
- 산출물:
  - `sessions/<change_id>_phase4_sync.md`
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
1. `bash scripts/world_ops_new_case.sh CR-YYYYMMDD-001`
2. 생성된 세션 문서에 내용 작성
3. 필요 시 파일 수정
4. (삭제가 있으면) `world_ops/sessions/<change_id>_deletion_gate.md` 작성
5. (삭제가 있으면) `bash scripts/world_ops_delete_guard.sh <change_id>`
6. `bash scripts/world_ops_audit_bundle.sh` (인덱스/프론트매터 + 정본 용어/CSV 스키마 충돌 검사)
7. `world_change_log.md` 갱신

## 시뮬/집필 실행 전 필수 게이트
1. `bash scripts/world_ops_compile_execution_views.sh <run_id> <call_spec_env>`
2. `bash scripts/world_ops_pre_injection_gate.sh <run_id> <call_spec_env> <payload_file>`
3. (모델 호출)
4. `bash scripts/world_ops_output_leak_scan.sh <run_id> <call_spec_env> <model_output_file>`

> `call_spec_env` 템플릿: `world_ops/templates/execution_call_spec.env`

## 근본 해결 문서
- `world_ops/ROOT_SOLUTION.md`
