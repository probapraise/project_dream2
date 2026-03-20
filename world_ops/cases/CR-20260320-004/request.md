# Change Request

- change_id: CR-20260320-004
- date: 2026-03-20
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
주인공의 `무흔술`이 주변에서 쉽사리 의심받지 않는 이유는 겉보기에는 다른 기사들이 수련하는 무예와 별다를 것이 없고, 그 존재를 아는 자들이 소수에 불과하며 전승도 선별적으로 진행되기 때문이다.

또한 수경원 소속이 아닌 키리온에게 `무흔술`을 가르치는 데리온의 행동은 수경원 입장에서 분명 위험한 선타기지만, 칼리온과 세르반 라베르니온은 각자의 이유로 눈감아 준다.

키리온은 그저 데리온이 가르쳐 준 검술이 의외로 굉장히 쓸 만하다고 느낄 뿐, 이게 특별히 대단한 것이라는 자각은 없다. 애초에 비마나 전투술은 마법의 세계에서 한계가 뚜렷하므로 초반 이후로는 그렇게 눈에 띄지 않는다는 점도 함께 반영한다.

## 2. 정제된 목표 (1문장)
`무흔술`의 은폐 논리, 칼리온·세르반의 각기 다른 묵인 사유, 키리온 본인의 둔감한 자기인식, 비마나 전투술로서의 상한을 live SSOT에 일관되게 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0005`, `WB-0009`에 `무흔술`의 은폐 논리와 비마나 전투술 상한을 추가
- [x] `EX-0001`, `EX-0005`에 칼리온·세르반의 서로 다른 묵인 사유를 반영
- [x] `NC-0001`, `story_arcs`, `memory_tiers/long_term`에 키리온의 자기인식과 조커 카드 위상 조정을 반영
- [x] `master_map`, `handoff`, `world_change_log`, case 문서를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0005.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 무흔술
  - 칼리온 렌바렌
  - 세르반 라베르니온
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-20
- note: writer가 `무흔술`의 의심 회피 논리와 묵인/상한 보강을 직접 지시
