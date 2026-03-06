> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Phase 2 Report (Collision Scan)

- change_id: CR-20260304-004
- verdict: minor

## 1. 탐색 범위
- files:
  - world_bible/WB-0014, 0020, 0022, 0023, 0027
  - docs/community_map, character_index*, legacy_id_map, simulation_playbook
  - layer_b/*.md

## 2. 충돌 후보
- [ ] 없음
- details:
  - 고정 4x18 구조 강제
  - 구조화 스키마(nodes/edges/events/rules/glossary) 강제
  - RAG/world_pack 전제 문구
  - hard/required 규약 문구

## 3. 누락 후보
- [x] 없음
- details:
  - 데이터 보존형 이동(quarantine)으로 정보 손실 최소화.

## 4. 중복/불필요 정보 후보
- [x] 없음

## 5. 판단 근거
- 멀티 에이전트 3건 교집합 결과(high/medium 충돌군)

## 6. 분기 결정
- branch: minor
- reason: 파일 삭제가 아니라 경로 이동 + 활성 템플릿 재작성으로 처리 가능.

## 7. 작가 승인
- approved: yes
- note: 진행 승인
