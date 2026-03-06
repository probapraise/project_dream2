# Change Request

- change_id: CR-20260306-005
- date: 2026-03-06
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 100화 이상 장기 연재 시 과거 스토리 전체를 다시 읽느라 컨텍스트가 낭비되지 않도록, 상태 기반 서사 관리 구조를 설계하고 live 문서로 반영한다.

## 2. 정제된 목표 (1문장)
- `narrative_state`를 활성 허브로 재작성하고, 아크/복선/회차 델타를 별도 압축 문서로 분리해 장기 연재용 컨텍스트 로딩 체계를 만든다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `world/live/docs/narrative_state.md`가 활성 서사 허브 역할과 기본 로딩 규칙을 명시한다.
- [x] `world/live/docs/story_arcs.md`, `world/live/docs/foreshadow_registry.md`, `world/live/docs/episode_deltas.md`가 추가된다.
- [x] `ep000`/`ep001` 캐논 기준 최소 부트스트랩 상태가 새 문서들에 반영된다.
- [x] `master_map.md`, `docs/handoff/next_steps.md`, `world_ops/world_change_log.md`가 동기화된다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/narrative_state.md
  - world/live/docs/story_arcs.md
  - world/live/docs/foreshadow_registry.md
  - world/live/docs/episode_deltas.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - narrative context loading policy
  - active arc compression
  - foreshadow state registry
  - episode state-change logging

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-06
- note: 사용자가 장기 연재 컨텍스트 관리 구조 설계를 요청했고 즉시 live 문서 반영 진행.
