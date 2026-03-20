# Change Request

- change_id: CR-20260320-002
- date: 2026-03-20
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
키리온은 마나가 없는 곳에서 왔기 때문에 데리온이 가르치는 실전 검술을 전혀 이상하게 여기지 않고 흡수한다. 다른 귀족들도 당연히 이렇게 수련한다고 오해한 채 자라며, 12세 입학식 때까지 데리온과의 대련 외에는 비교 기준이 없어 자신의 강함을 스스로 알지 못한다.

아르케이온 입학식 모의 탐색전에서는 `색인의 그리모어`를 활용해 세렌을 비롯한 같은 조를 적시적소에 배치하는 운영형 유능감이 먼저 드러나야 한다. 그러나 `ep010` 마지막에는 키리온의 진짜 자산이 `무흔술` 기반 실전 검술이라는 사실이 공개되어, 이미 마법 선행학습을 하고 온 서명귀족들도 고전하던 보스 몬스터를 일격에 처리한다.

그 이후에도 키리온은 비전투 마법을 주력으로 연구하지만, `열상각인` 같은 일부 보조 마법을 `무흔술`에 응용하고 데리온이 잊을 만하면 전투력을 시험하기 때문에 `무흔술`은 조커 카드로 계속 유지된다.

## 2. 정제된 목표 (1문장)
키리온의 `무흔술`을 `입학 전엔 본인도 특수성을 모르는 숨은 자산 -> 입학식에서는 운영형 유능감 뒤에 가려짐 -> ep010에서 반전 공개 -> academy 이후에도 조커 카드로 유지`하는 장기 서사 축으로 고정한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `NC-0001`에 키리온의 `무흔술` 오해, 입학 전 자기 강함 미인지, 입학식/`ep010` 공개 구조를 추가
- [x] `EX-0003`에 데리온의 academy 이후 반복 시험 축을 추가
- [x] `story_arcs`, `memory_tiers/long_term`에 장기 아크/장기 기억 약속을 고정
- [x] `master_map`, `handoff`, `world_change_log`, `world_ops` 케이스 문서를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/external/EX-0003.yaml
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 키리온 렌바렌
  - 데리온 렌바렌
  - 세렌 라베르니온
  - 무흔술
  - ep010 보스 일격 반전

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-20
- note: writer가 키리온 `무흔술` 공개 타이밍과 academy 이후 조커 카드 운용 방향을 직접 지정
