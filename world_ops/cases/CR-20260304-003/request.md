> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Change Request

- change_id: CR-20260304-003
- date: 2026-03-04
- requester: writer
- status: approved
- source_of_truth: conversation_log.md + spec_sheet_v1.md

## 1. 원 요청
"삭제 파일 전부 복원하고, 근본적인 해결책부터 다시 세우자."

## 2. 정제된 목표 (1문장)
삭제된 번들 파일을 전량 복원하고, 향후 통삭제 재발을 막는 운영 가드(정책+검증)를 도입한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 번들 파일이 복원 기준 커밋(f0fa447) 상태와 일치
- [x] 통삭제 금지/예외 삭제 게이트 정책 문서화
- [x] 삭제 가드 스크립트 추가
- [x] 감사 스크립트 통과(errors=0)

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - worldbible_refined_bundle_20260303/** (복원)
  - world_ops/README.md
  - world_ops/ROOT_SOLUTION.md
  - world_ops/templates/deletion_gate.md
  - scripts/ops/world_ops_delete_guard.sh

## 6. 작가 확인 필요 항목
- Q1: 이후 정리는 파일 통삭제 대신 구간 단위 정리로만 진행할지?

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-04
- note: 복원+재발방지 우선
