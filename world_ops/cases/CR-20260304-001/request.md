> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Change Request

- change_id: CR-20260304-001
- date: 2026-03-04
- requester: writer
- status: approved
- source_of_truth: conversation_log.md + spec_sheet_v1.md

## 1. 원 요청
"번들에 남아 있는 현재 프로젝트 성격과 배치되는 규약/설정을 멀티 에이전트로 찾아 삭제하자."

## 2. 정제된 목표 (1문장)
고정 4x18/스키마 강제/RAG 전제 등 SSOT와 충돌하는 구 규약·설정 파일을 1차 삭제하고 인덱스를 재정렬한다.

## 3. 변경 유형
- deprecate

## 4. 성공 기준 (DoD)
- [x] 멀티 에이전트 분석 3건 완료
- [x] 교집합 high-priority 충돌 파일 삭제 완료
- [x] 인덱스/마스터맵 재동기화 완료
- [x] 감사 스크립트 통과(errors=0)

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world_bible/WB-0020, WB-0023, WB-0027
  - docs/community_map.md, docs/legacy_id_map.md, docs/.wb_part_*.json
  - layer_b/*
  - docs/world_bible_index_v2.md, docs/world_bible_index.md, docs/master_map.md
- impacted_entities:
  - 고정 4권역/18보드 규약
  - nodes/edges/events/rules/glossary 구조화 규약
  - RAG/world_pack 전제 문구

## 6. 작가 확인 필요 항목
- Q1: medium/low 충돌군(예: character_index 계열)도 2차 삭제할지?

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-04
- note: 1차 삭제 우선 적용
