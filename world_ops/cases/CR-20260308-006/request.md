# Change Request

- change_id: CR-20260308-006
- date: 2026-03-08
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 렌바렌 가문의 문장비전 후계자를 주인공의 여동생에서 형으로 변경한다. 형은 현재 10세이며 두 달 전 `계승조회식`을 마친 뒤 가문의 어두운 비밀을 전수받았고, 동생들을 향한 부러움/질투/공포가 뒤엉킨 상태다. 프롤로그 직전 키리온을 목검으로 세게 때린 사건도 이런 혼란에서 비롯된 것으로 재정의한다.

## 2. 정제된 목표 (1문장)
- 렌바렌의 현 식흔 후계자를 장남으로 retcon하고, 그에 따라 가족 비밀 공유 범위, sibling risk, 목검 사건의 동기를 live world bible/character 카드/handoff에 동기화한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0009`, `WB-0026`에 렌바렌 현 후계자가 10세 장남이라는 현재 상태가 반영된다.
- [x] `EX-0001`, `EX-0002`, `NC-0001`에 가족 관계와 장남의 심리 상태/목검 사건 동기가 동기화된다.
- [x] `docs/handoff/next_steps.md`, `master_map.md`, `world_change_log.md`가 새 상태를 기록한다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0002.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - docs/handoff/next_steps.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 렌바렌 백작가 승계 구도
  - 장남(현 식흔 후계자)
  - 키리온 렌바렌
  - 셀리아 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-08
- note: 사용자가 장남 후계 retcon과 목검 사건의 새 동기를 직접 확정했다.
