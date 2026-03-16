# Change Request

- change_id: CR-20260316-002
- date: 2026-03-16
- requester: writer
- status: approved
- source_of_truth:
  - primary:
    - world/live/docs/master_map.md
    - world/live/world_bible/WB-0003_onepage_summary.md
    - world/live/world_bible/WB-0006_irminsul_infra.md
    - world/live/world_bible/WB-0008_archive_plaza_overview.md
    - world/live/world_bible/WB-0015_academy_bible.md
    - world/live/world_bible/WB-0017_economy_resources.md
    - world/live/world_bible/WB-0019_platform_spec.md
  - secondary:
    - world_ops/cases/CR-20260315-002/major_prompt_log.md
    - world_ops/cases/CR-20260315-002/mana_node_frontier_draft.md
    - world_ops/cases/CR-20260315-002/community_unlock_blueprint.md
    - world_ops/cases/CR-20260315-002/irminsul_contract_ladder.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- `CR-20260315-002` 이후에도 live world bible에 완전히 내려오지 않은 설정을 찾는다.
- `영상 슬롯 경제` 항목은 제외하고, 나머지 누락 설정은 모두 live SSOT에 동기화한다.
- 특히 `주좌 / 전위권`, `모든 마나 노드 = 특수 지형 노드 본질`, `성목 = 자생 노드`, `일반 노드/성목의 신격·정령군 차이`, `frontier-feudal` 세계 구조, `노드 안정화`, `학술원의 전위권 실무`, `픽시 둥지화 -> 요정 접근`, `질의 인장 / 기록 인장` 메커니즘을 live에 반영한다.

## 2. 정제된 목표 (1문장)
`CR-20260315-002`에서 이미 합의된 노드·frontier·그리모어 연계 규칙 가운데 live world bible에 누락된 항목을, `영상 슬롯 경제`를 제외한 범위에서 live SSOT와 운영 로그에 재동기화한다.

## 3. 변경 유형
- modify | retcon

## 4. 성공 기준 (DoD)
- [ ] `WB-0006`에 `주좌 / 전위권`, `자생 노드`, 일반 노드와 성목의 신격/정령군 차이가 명시된다.
- [ ] `WB-0003`, `WB-0015`, `WB-0017`에 frontier-feudal 구조, 학술원의 전위권 실무, 노드 안정화/경제 함의가 반영된다.
- [ ] `WB-0008`, `WB-0019`에 `픽시 둥지화 -> 요정 접근` 인과와 `질의 인장 / 기록 인장` 메커니즘이 반영되고, index/log가 동기화된다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/master_map.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/world_bible_index.md
  - world/live/world_bible/WB-0003_onepage_summary.md
  - world/live/world_bible/WB-0006_irminsul_infra.md
  - world/live/world_bible/WB-0008_archive_plaza_overview.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0017_economy_resources.md
  - world/live/world_bible/WB-0019_platform_spec.md
  - world_ops/world_change_log.md
- impacted_entities:
  - 주좌
  - 전위권
  - 특수 지형 노드
  - 성목(Irminsul)
  - 노드 안정화
  - 픽시 둥지화
  - 질의 인장
  - 기록 인장

## 6. 작가 확인 필요 항목
- 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-16
- note:
  - `영상 슬롯 경제`는 이번 반영 범위에서 제외한다.
