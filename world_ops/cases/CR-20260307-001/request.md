# Change Request

- change_id: CR-20260307-001
- date: 2026-03-07
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 프롤로그와 1화 캐논을 새 리라이트 버전으로 교체해 넣어두었으니, 저장소의 current canon 포인터와 live 상태 문서에 그 업데이트를 반영해 달라.

## 2. 정제된 목표 (1문장)
- 새 프롤로그/1화 캐논 파일을 current canon으로 승격하고, 그 캐논을 재서술하거나 참조하는 live/집필/변경관리 문서를 새 내용 기준으로 동기화한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `ep000_prologue`, `ep001`의 `canon/README.md`가 새 캐논 파일명을 current로 가리킨다.
- [x] `narrative_state`, `episode_deltas`, `story_arcs`, `foreshadow_registry`, `style_bible`, `NC-0001`이 새 캐논 내용 기준으로 동기화된다.
- [x] `artifacts/writing` 인덱스, handoff, `master_map`, `world_change_log`, 케이스 문서가 새 상태를 반영한다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - artifacts/writing/README.md
  - artifacts/writing/episodes/README.md
  - artifacts/writing/episodes/ep000_prologue/canon/README.md
  - artifacts/writing/episodes/ep001/canon/README.md
  - artifacts/writing/style/style_constitution.md
  - scripts/writing/new_episode_scaffold.sh
  - world/live/docs/narrative_state.md
  - world/live/docs/episode_deltas.md
  - world/live/docs/story_arcs.md
  - world/live/docs/foreshadow_registry.md
  - world/live/docs/style_bible.md
  - world/live/population/core_cast/NC-0001_P-1027.md
  - docs/handoff/next_steps.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md
- impacted_entities:
  - current canon pointers
  - live narrative hub
  - NC-0001 live characterization snapshot
  - writing index / handoff sync

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-07
- note: 사용자가 새 프롤로그/1화 캐논을 이미 배치해 두었고, 저장소 전반의 current 상태 반영을 요청함.
