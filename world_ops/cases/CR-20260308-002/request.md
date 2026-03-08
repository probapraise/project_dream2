# Change Request

- change_id: CR-20260308-002
- date: 2026-03-08
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 왕국이 서명귀족 혈통이 섞인 아동을 추적하는 별도 기관을 두고, 이들을 10세가 되는 해마다 왕도로 데려와 문장비전 계승 여부를 일괄 확인하는 제도를 추가한다. 각 가문이 그 전에 조기 검증하는 것은 엄금되며, 표면 명분은 인도적 절차지만 실질 목적은 식흔 같은 기밀 문장비전의 일괄 관리다.

## 2. 정제된 목표 (1문장)
- 벨쿠란 왕국의 서명귀족 혈통 추적/10세 왕도 문장검증 제도를 world bible과 관련 캐릭터 카드에 일관되게 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0009`, `WB-0026`에 10세 왕도 문장검증 제도와 조기 사설 검증 금지 규칙이 반영된다.
- [x] `EX-0001`, `NC-0001`이 이 제도를 현재 이해관계와 위험 구조에 맞게 반영한다.
- [x] `world_bible_index_v2`, `master_map`, `world_change_log`, 케이스 문서가 새 상태를 기록한다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 벨쿠란 왕실
  - 서명귀족 혈통 아동 검증 제도
  - 렌바렌 백작가
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-08
- note: 사용자가 직접 제도와 숨은 목적을 명시적으로 제시했고, live SSOT 반영까지 요청 흐름이 이어졌다.
