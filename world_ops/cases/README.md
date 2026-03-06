# Cases

변경 건당 `world_ops/cases/<change_id>/` 디렉터리를 생성한다.

- 새 변경 건은 기존 케이스 문서를 복붙하지 말고 `bash scripts/ops/world_ops_new_case.sh <change_id>`로 생성한다.
- 2026-03-06 이전 케이스 다수는 당시 경로 규칙(`docs/...`, `world_bible/...`, `worldbible_refined_bundle_20260303/...`)을 그대로 보존한 히스토리 문서다.
- 과거 케이스를 참고하더라도 경로 표기는 현재 규칙으로 다시 해석해야 한다.
- 케이스 문서의 경로 표기는 저장소 루트 기준 실제 경로를 사용한다.
- 예: `world/live/docs/master_map.md`, `world/live/world_bible/WB-0002_loreops_canon_control.md`

기본 파일:
- `request.md`
- `phase2_report.md`
- `phase3_apply.md`
- `phase4_sync.md`

조건부 파일:
- `major_prompt_log.md` (major only)
- `tri_diff_verify.md` (major only)
- `deletion_gate.md` (삭제 포함 시)
- `pause_log.md` (중단/사고 기록 시)
