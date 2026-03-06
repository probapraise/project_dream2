> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Change Request

- change_id: CR-20260303-002
- date: 2026-03-03
- requester: writer
- status: approved
- source_of_truth: conversation_log.md + spec_sheet_v1.md

## 1. 원 요청
"원본 지구 파생 시뮬레이션 설정은 작중 절대 등장하면 안 된다. CONFIDENTIAL 분류는 부적절하다."

## 2. 정제된 목표 (1문장)
WB-0025의 가시성 라벨을 작중 비노출 전제에 맞춰 `CONFIDENTIAL`에서 `META`로 수정한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] WB-0025 frontmatter visibility가 META로 변경됨
- [x] world_bible_index_v2의 WB-0025 visibility가 META로 동기화됨
- [x] legacy index(world_bible_index.md)도 동일하게 동기화됨

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world_bible/WB-0025_appendix_naming_constitution.md
  - docs/world_bible_index_v2.md
  - docs/world_bible_index.md
- impacted_entities:
  - PNC-1.0
  - 원본 지구 파생 시뮬레이션 설정

## 6. 작가 확인 필요 항목
- Q1: 해당 설정을 향후 공개/기밀 경로에서 완전히 배제할지?

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-03
- note: 작중 절대 비노출 정책 반영
