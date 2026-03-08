# Change Request

- change_id: CR-20260308-009
- date: 2026-03-08
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 문장비전 계승 여부에 따라 부모 중 한쪽의 성을 따르는 세계에서, 혼인했다고 남편의 성을 따라가는 관행은 어색하므로 셀리아 표기를 출생 가문 성 유지 방식으로 수정한다.

## 2. 정제된 목표 (1문장)
- 혼인 후 성 표기를 `출생 가문 성 유지 + 혼인 가문 직위 사용` 규칙으로 정리하고, 셀리아 관련 live 문서 표기를 `셀리아 그라비온`으로 동기화한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] `EX-0002`의 이름/로마자/소속 표기가 새 규칙으로 교정된다.
- [x] 가족 카드와 키리온/서사 상태 문서의 셀리아 참조가 `셀리아 그라비온`으로 동기화된다.
- [x] handoff/master_map/change_log가 이번 규칙 정리를 기록한다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/external/EX-0002.yaml
  - world/live/external/EX-0001.yaml
  - world/live/external/EX-0003.yaml
  - world/live/external/EX-0004.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/narrative_state.md
  - world/live/docs/episode_deltas.md
  - docs/handoff/next_steps.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 셀리아 그라비온
  - 렌바렌 혼인 표기 규칙

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-08
- note: 사용자가 혼인 후 성 표기 규칙 재정의를 직접 승인했다.
