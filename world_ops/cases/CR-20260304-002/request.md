> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Change Request

- change_id: CR-20260304-002
- date: 2026-03-04
- requester: writer
- status: approved
- source_of_truth: conversation_log.md + spec_sheet_v1.md

## 1. 원 요청
"2차 정리 진행해"

## 2. 정제된 목표 (1문장)
1차 정리 후 남은 충돌군 중 medium/low 후보(`character_index*`, `WB-0014`, `WB-0022`, `simulation_playbook`)를 삭제해 규약 충돌을 추가 축소한다.

## 3. 변경 유형
- deprecate

## 4. 성공 기준 (DoD)
- [x] 대상 5개 파일군 삭제 완료
- [x] world_bible_index(v2/legacy) 재생성 완료
- [x] master_map 포인터 정리 완료
- [x] 감사 스크립트 통과(errors=0)

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world_bible/WB-0014_lore_checklist.md
  - world_bible/WB-0022_appendix_change_log_sample.md
  - docs/character_index.md
  - docs/character_index_v2.md
  - docs/simulation_playbook.md
  - docs/world_bible_index_v2.md
  - docs/world_bible_index.md
  - docs/master_map.md
- impacted_entities:
  - B01~B18 강제 검수 지침
  - 고정 인덱스/샘플 충돌 로그
  - 시뮬레이션 강제 플레이북

## 6. 작가 확인 필요 항목
- Q1: 3차 정리에서 `WB-0001/WB-0002`까지 정리 대상으로 볼지?

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-04
- note: 2차 정리 진행 승인
