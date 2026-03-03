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
4. `bash scripts/world_ops_audit_bundle.sh`
5. `world_change_log.md` 갱신

