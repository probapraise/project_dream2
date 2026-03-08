# Change Request

- change_id: CR-20260308-005
- date: 2026-03-08
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 벨쿠란이 조기 수련을 단속할 수 있는 이유를 보강한다. 마법을 한 번이라도 사용해본 사람과 지금까지 마법을 사용하지 않은 사람 사이에는 뚜렷한 차이가 있으며, 이 차이를 감정할 수 있다. 물론 이를 은닉하는 방법이 아예 없는 것은 아니다.

## 2. 정제된 목표 (1문장)
- 조기 수련 금지 규정의 실효 근거로 "사용 경험자와 미사용자의 감정 차이"를 마법 시스템, 증거 문서, 관련 규칙/캐릭터 카드에 반영한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `WB-0005`, `WB-0009`, `WB-0026`에 감정 차이와 제한적 은닉 가능성이 반영된다.
- [x] `WB-0018`에 관련 포렌식 증거 유형이 추가된다.
- [x] `NC-0001`, 인덱스/로그/케이스 문서가 새 상태를 기록한다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0018_evidence_records_glossary.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 벨쿠란 조기 수련 금지 규정
  - 마나핵/회로 감정
  - 키리온 렌바렌

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-08
- note: 사용자가 규정의 실효 근거와 제한적 은닉 가능성을 직접 제시했다.
