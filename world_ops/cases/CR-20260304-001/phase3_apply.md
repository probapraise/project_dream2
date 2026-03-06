> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Phase 3 Apply

- change_id: CR-20260304-001
- branch: minor

## 1. 실제 수정 파일
- deleted:
  - world_bible/WB-0020_community_boards_18.md
  - world_bible/WB-0023_appendix_schema_cheatsheet.md
  - world_bible/WB-0027_appendix_character_pack_schema.md
  - docs/community_map.md
  - docs/legacy_id_map.md
  - docs/.wb_part_0001_0009.json
  - docs/.wb_part_0010_0018.json
  - docs/.wb_part_0019_0027.json
  - layer_b/* (18개 파일)
  - *:Zone.Identifier (전량)
- updated:
  - docs/world_bible_index_v2.md (자동 재생성)
  - docs/world_bible_index.md (자동 재생성)
  - docs/master_map.md (포인터 정리)
- added:
  - scripts/indexes/rebuild_world_indexes.sh

## 2. 변경 요약 (diff 요약 수준)
- 충돌 고정 규약 파일 1차 제거
- 남은 월드바이블(24개) 기준 최소 인덱스 재생성
- 마스터맵에 정리 상태 반영

## 3. 예상 외 영향
- [ ] 없음
- details:
  - community_map/layer_b 관련 기능은 재생성 전까지 비활성 상태.

## 4. 미해결 항목
- [ ] 없음
- details:
  - 2차 후보(character_index 계열, WB-0014/0022 등)는 후속 판단 필요.

## 5. 작가 승인
- approved: yes
- note: 1차 정리 완료 승인
