> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Phase 2 Report (Collision Scan)

- change_id: CR-20260304-002
- verdict: minor

## 1. 탐색 범위
- files:
  - world_bible/WB-0014_lore_checklist.md
  - world_bible/WB-0022_appendix_change_log_sample.md
  - docs/character_index.md
  - docs/character_index_v2.md
  - docs/simulation_playbook.md

## 2. 충돌 후보
- [ ] 없음
- details:
  - WB-0014: B01~B18 준수 검수 규칙으로 동적 구조 원칙과 충돌
  - WB-0022: 4권역·18보드 정합을 샘플 로그로 재강화
  - character_index*: 고정 커뮤니티/zone 분류 전제
  - simulation_playbook: hard/required 형태의 경직 규칙

## 3. 누락 후보
- [x] 없음
- details:
  - 이번 범위는 충돌군 제거 및 정리이며 신규 데이터 추가는 아님.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 삭제 대상 모두 기존 1차 정리 후 잔존 충돌군으로 분류.

## 5. 판단 근거
- world_bible_index 참조:
  - 대상 문서가 인덱스에 잔존해 재전파되고 있음.
- cross-reference 참조:
  - 1차 정리 후에도 규약 충돌 신호가 지속.

## 6. 분기 결정
- branch: minor
- reason: 외부 재작성 없이 파일 삭제 + 인덱스 재생성으로 처리 가능.

## 7. 작가 승인
- approved: yes
- note: 삭제 진행 승인
