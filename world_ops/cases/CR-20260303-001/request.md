> Historical case note (2026-03-06)
> This case predates the current repo-root path convention and may contain legacy path notation such as `docs/...`, `world_bible/...`, or `worldbible_refined_bundle_20260303/...`.
> Do not copy path notation from this file. For new work, create a fresh case with `bash scripts/ops/world_ops_new_case.sh <change_id>` and use repo-root paths like `world/live/...`.

# Change Request

- change_id: CR-20260303-001
- date: 2026-03-03
- requester: writer
- status: approved
- source_of_truth: conversation_log.md + spec_sheet_v1.md

## 1. 원 요청
"배지 분실/위조 상황에서도 학내 인증이 우회되지 않는다는 규칙을 세계관에 추가하고 싶다."

## 2. 정제된 목표 (1문장)
배지 인증 우회 불가 규칙이 이미 SSOT에 존재하는지 검증하고, 없다면 최소 범위로 추가한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] 관련 섹션(WB-0007, 연관 규정) 탐색 완료
- [x] 기존 규칙 존재 여부 판정 완료
- [x] 불필요 중복 추가 방지 결정 문서화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - docs/world_bible_index_v2.md
  - world_bible/WB-0007_badge_network.md
  - world_bible/WB-0015_academy_bible.md
- impacted_entities:
  - 배지
  - 출입/열람 인증
  - 권한 증빙

## 6. 작가 확인 필요 항목
- Q1: 중복이면 문서 반영 없이 종료할지?
- Q2: 명시 강화가 필요하면 어떤 공개 레벨(PUBLIC/META)로 둘지?

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-03
- note: 시스템 드라이런 목적의 테스트 케이스로 실행
