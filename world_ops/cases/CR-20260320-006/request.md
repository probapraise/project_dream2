# Change Request

- change_id: CR-20260320-006
- date: 2026-03-20
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
기존에 정리한 `데리온 academy 입학 후 2년 동안 키리온이 독자적으로 수련하며 12세까지 강해지는 축`에 피지컬 성장 곡선을 추가해 더 정합성 있게 고도화한다.

핵심 조건:
- 데리온이 키리온을 굴리던 시절처럼 심각한 훈련이 계속되는 것이 아니라, 키리온은 자기 분석과 복습으로 독자 수련을 진행한다.
- 리리아는 살벌한 무예 교관이 아니라, 자기가 체득한 짧은 호신 요령을 가볍게 던져 주는 역할에 가깝다.
- 방학마다 돌아오는 데리온과는 다시 몇 주간 강도 높은 대련을 한다.
- 치유사 상주, 귀족가 회복 인프라, 정신병자 수준의 훈련 강박 때문에 훈련 밀도는 현실보다 훨씬 높지만, 성장판과 체급 한계는 남는다.

## 2. 정제된 목표 (1문장)
`무흔술` 기술 성장선 위에 `10~12세` 키리온의 피지컬 성장 곡선과 한계를 겹쳐, 독자 수련/리리아 개입/방학 재교정 구조가 실제 전투력으로 어떻게 번역되는지 live SSOT에 정리한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0030`에 치유 세계 기준 피지컬 성장 제약, 독자 수련 입력 구조, `10~12세` 키리온 피지컬 성장 곡선을 추가
- [x] `EX-0004`, `EX-0003`, `NC-0001`, `story_arcs`, `memory_tiers/long_term`에 리리아 개입과 방학 재교정, 전투력 상한을 반영
- [x] handoff/log와 case 문서를 동기화

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0030_appendix_muhunsul_doctrine.md
  - world/live/external/EX-0003.yaml
  - world/live/external/EX-0004.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 키리온 렌바렌
  - 데리온 렌바렌
  - 리리아 렌바렌
  - 무흔술

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-20
- note: writer가 `무흔술` 피지컬 성장 곡선 보강을 직접 지시
