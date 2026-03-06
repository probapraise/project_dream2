# Change Request

- change_id: CR-20260306-006
- date: 2026-03-06
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- episode 폴더마다 최종적으로 반영된 캐논을 명시할 수 있도록 `canon/` 하위 폴더를 기본 구조로 도입하고, 현재 캐논은 분명히 표시하되 이후에도 수정 가능해야 한다.

## 2. 정제된 목표 (1문장)
- 모든 episode 폴더가 `canon/` 하위 폴더와 current canon 지시 파일을 가지도록 구조를 바꾸고, 기존 `ep000`/`ep001` 캐논 파일과 참조 경로를 그 규칙에 맞게 재배치한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `artifacts/writing/episodes/<episode_id>/canon/`이 표준 구조로 문서화된다.
- [x] `ep000_prologue`, `ep001`의 current canon 파일이 `canon/` 하위로 이동하고 current 지시 파일이 추가된다.
- [x] 관련 참조 문서와 로그가 새 경로 규칙으로 동기화된다.
- [x] 새 episode 폴더 생성 시 `canon/`이 자동으로 생기는 스캐폴드 스크립트가 추가된다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - artifacts/writing/README.md
  - artifacts/writing/episodes/README.md
  - artifacts/writing/episodes/ep000_prologue/canon/revision_v1.txt
  - artifacts/writing/episodes/ep000_prologue/canon/revision_v1.docx
  - artifacts/writing/episodes/ep001/canon/revision_v2.txt
  - world/live/docs/narrative_state.md
  - world/live/docs/episode_deltas.md
  - docs/handoff/next_steps.md
  - scripts/writing/new_episode_scaffold.sh
  - world_ops/world_change_log.md
- impacted_entities:
  - writing episode folder contract
  - current canon path conventions
  - mutable canon manifest rule

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-06
- note: 사용자가 episode별 `canon/` 폴더 도입과 mutable canon 전제를 명시해 달라고 요청해 즉시 반영 진행.
