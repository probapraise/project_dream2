# Change Request

- change_id: CR-20260308-001
- date: 2026-03-08
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 렌바렌 가문의 설정을 보강한다. 비밀 유지의 핵심에 `방계 청소` 관행을 추가하고, 렌바렌 가주의 정보기관 수장 직위가 명예직일 뿐 실권은 라베르니온 공작가가 쥔다는 권력 구도를 명시한다.

## 2. 정제된 목표 (1문장)
- 렌바렌 가문의 비밀 유지 메커니즘과 권력 종속 구조를 world bible, 인덱스, 관련 캐릭터 카드에 일관되게 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0009`, `WB-0026`에 방계 청소 규약과 라베르니온-렌바렌 권력 구도가 반영된다.
- [x] `EX-0001`, `NC-0001`이 새 비밀 구조를 캐릭터 레벨에서 반영한다.
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
  - 렌바렌 백작가
  - 라베르니온 공작가
  - 칼리온 렌바렌
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-08
- note: 사용자가 직접 새 설정을 제시했고, live SSOT 반영까지 요청 흐름이 이어졌다.
