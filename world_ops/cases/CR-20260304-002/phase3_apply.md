> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Phase 3 Apply

- change_id: CR-20260304-002
- branch: minor

## 1. 실제 수정 파일
- deleted:
  - world_bible/WB-0014_lore_checklist.md
  - world_bible/WB-0022_appendix_change_log_sample.md
  - docs/character_index.md
  - docs/character_index_v2.md
  - docs/simulation_playbook.md
- updated:
  - docs/world_bible_index_v2.md (자동 재생성)
  - docs/world_bible_index.md (자동 재생성)
  - docs/master_map.md (포인터 정리)

## 2. 변경 요약 (diff 요약 수준)
- 1차 후 잔존 충돌군 5개 파일군 삭제
- 남은 월드바이블(22개) 기준 인덱스 재생성
- 마스터맵 포인터 정리

## 3. 예상 외 영향
- [ ] 없음
- details:
  - character_index/simulation_playbook 참조 기능은 재정의 전까지 비활성.

## 4. 미해결 항목
- [ ] 없음
- details:
  - 3차 정리 후보(WB-0001/WB-0002)는 별도 판단 필요.

## 5. 작가 승인
- approved: yes
- note: 적용 승인
