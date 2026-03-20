# Change Request

- change_id: CR-20260320-001
- date: 2026-03-20
- requester: writer
- status: approved
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
주인공 무력 설정을 보강하면서, 이 세계의 제도권 기사/귀족 무예가 실전 격투술이 아니라 `마나 + 식`으로 기적 발동을 유도하는 의례형 동작에 가깝다는 점을 명시한다.

추가로 수경원 계열 비밀 서명귀족은 식흔만으로 모든 공작 흔적을 덮을 수 없으므로, 지난 수백 년 동안 마나 없이도 사람을 죽일 수 있는 비마나 실전 전투술 `무흔술`을 체계적으로 발전시켜 왔다는 설정을 live SSOT에 반영한다.

세부 조건:
- 일반 귀족 자제의 pre-academy 준비는 체력단련, 초식 모사, 독서/교양 중심이다.
- 비마나 실전 전투술은 세계 전역에 산발적으로 존재하지만, 주로 타국 변경, 암살자 집단, 특정 종교 집단 등에 남아 있을 뿐 일반인이 흔히 접하는 무예는 아니다.
- 데리온이 키리온에게 강압적으로 쥐여주는 무력은 일반 품새가 아니라 `무흔술` 기초여야 한다.

## 2. 정제된 목표 (1문장)
제도권 기사 무예와 비제도권 비마나 실전술의 차이를 `무흔술` 개념으로 정리하고, 수경원/렌바렌 비밀 전승 및 데리온-키리온 단련 축까지 live SSOT 문서에 일관되게 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0005`에 제도권 기사/귀족 무예의 의례형 성격과 비마나 실전술 분포를 추가
- [x] `WB-0009`, `WB-0026`에 `수경원`의 `무흔술` 전승을 반영
- [x] `EX-0001`, `EX-0003`, `NC-0001`, `memory_tiers/long_term`에 데리온-키리온 단련 축을 동기화
- [x] `master_map`, `handoff`, `world_change_log`, `world_ops` 케이스 문서를 함께 갱신

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0003.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 무흔술
  - 수경원
  - 렌바렌 백작가
  - 데리온 렌바렌
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-20
- note: writer가 `무흔술` 명칭을 승인하고 세계 규칙/캐릭터 카드 반영을 직접 지시
