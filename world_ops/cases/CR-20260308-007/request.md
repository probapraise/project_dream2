# Change Request

- change_id: CR-20260308-007
- date: 2026-03-08
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/character_population_methodology.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 렌바렌 장남의 이름을 `데리온`으로 확정하고, 고정 말투 앵커 3개를 포함한 캐릭터 카드를 작성한다.

## 2. 정제된 목표 (1문장)
- 데리온 렌바렌을 named 외곽 인물 카드(EX-0003)로 등록하고, 가족 카드/키리온 카드/handoff/change log에 실명 참조와 핵심 운용 목적을 동기화한다.

## 3. 변경 유형
- add

## 4. 성공 기준 (DoD)
- [x] `world/live/external/EX-0003.yaml`이 생성된다.
- [x] `EX-0001`, `EX-0002`, `NC-0001`에 데리온 실명 참조가 반영된다.
- [x] `docs/handoff/next_steps.md`, `master_map.md`, `world_change_log.md`가 새 named 인물 상태를 기록한다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/external/EX-0003.yaml
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0002.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - docs/handoff/next_steps.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 데리온 렌바렌
  - 렌바렌 가족 관계 축
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-08
- note: 사용자가 이름 `데리온`과 고정 대사 3개를 직접 확정했다.
