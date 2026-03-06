> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Phase 3 Apply

- change_id: CR-20260303-002
- branch: minor

## 1. 실제 수정 파일
- world_bible/WB-0025_appendix_naming_constitution.md
- docs/world_bible_index_v2.md
- docs/world_bible_index.md

## 2. 변경 요약 (diff 요약 수준)
- WB-0025 frontmatter: `visibility: CONFIDENTIAL` -> `visibility: META`
- world_bible_index_v2의 WB-0025 항목 visibility: `CONFIDENTIAL` -> `META`
- world_bible_index(legacy)의 WB-0025 항목 visibility: `CONFIDENTIAL` -> `META`

## 3. 예상 외 영향
- [x] 없음
- details:
  - 본문/엔티티/depends_on은 유지, 가시성 라벨만 교정.

## 4. 미해결 항목
- [ ] 없음
- details:
  - 향후 정책: META 항목이 작중 노출 후보로 참조되지 않도록 후속 가드 검토 필요.

## 5. 작가 승인
- approved: yes
- note: 적용 승인
