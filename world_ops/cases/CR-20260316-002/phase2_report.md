# Phase 2 Report (Collision Scan)

- change_id: CR-20260316-002
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0003_onepage_summary.md
  - world/live/world_bible/WB-0006_irminsul_infra.md
  - world/live/world_bible/WB-0008_archive_plaza_overview.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0017_economy_resources.md
  - world/live/world_bible/WB-0019_platform_spec.md
  - world/live/docs/master_map.md
  - world/live/docs/world_bible_index.md
  - world/live/docs/world_bible_index_v2.md
  - world_ops/world_change_log.md
  - world_ops/cases/CR-20260315-002/major_prompt_log.md
  - world_ops/cases/CR-20260315-002/mana_node_frontier_draft.md
  - world_ops/cases/CR-20260315-002/community_unlock_blueprint.md
  - world_ops/cases/CR-20260315-002/irminsul_contract_ladder.md

## 2. 충돌 후보
- [x] 있음
- details:
  - `WB-0006`는 아직 `특수 지형 노드`를 일부 예외적 장소처럼 읽히게 하며, `주좌 / 전위권`, `성목 = 자생 노드`, 일반 노드/성목의 신격 차이를 담지 못한다.
  - `WB-0015`는 하급/상급 과정의 기능 해금은 반영했지만, 학술원의 핵심 실무가 `전위권 토벌 / 길찾기 / 탐사 / 기믹 활용`이라는 바닥 규칙이 약하다.
  - `WB-0017`은 노드 권리와 플랫폼 경제는 정리됐지만, `frontier-feudal` 구조와 `노드 안정화`의 경제적 함의가 드러나지 않는다.
  - `WB-0008`, `WB-0019`는 `픽시 둥지화`와 `요정 동행`, 자동 서명 채널은 있으나 `픽시 둥지화 이상 신호 -> 요정 접근`, `질의 인장 / 기록 인장` 메커니즘이 중간 단계 없이 끊겨 있다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| `주좌 / 전위권` 정의 부재 | `WB-0006`, `WB-0003`, `WB-0015`, `WB-0017` | `WB-0006`에 정의를 내리고, 요약/실무/경제 문서에 필요한 만큼 연결한다 | `주좌`, `전위권`, `frontier-feudal` | open |
| `특수 지형 노드`의 본질 정의 드리프트 | `WB-0006`, `WB-0017` | `모든 마나 노드가 결국 특수 지형 노드`라는 바닥 규칙으로 재서술한다 | `특수 지형 노드`, `자생 노드` | open |
| 성목/일반 노드의 신격·정령군 차이 누락 | `WB-0006` | 일반 노드=`주좌의 주인`/`지형 원소 구현형`, 성목=`나무 자체`/`마나 수집·중계형` 대비를 추가한다 | `잠든 신`, `정령군` | open |
| 학술원 실무와 노드 세계의 연결 약함 | `WB-0015` | 하급/상급 과정의 핵심 실무를 전위권 토벌, 길찾기, 탐사, 기믹 활용으로 명시한다 | `전위권 토벌`, `길찾기`, `탐사` | open |
| 경제 문서의 `노드 안정화` 누락 | `WB-0017` | 노드 안정화를 국책 사업/경제 병목으로 명시하고 frontier 구조를 연결한다 | `노드 안정화`, `국책 사업` | open |
| `픽시 둥지화 -> 요정 접근`, `질의 인장 / 기록 인장` 누락 | `WB-0008`, `WB-0019` | 성장/운영 문단에 인과와 인장형 입출력 구조를 추가한다 | `픽시 둥지화`, `질의 인장`, `기록 인장` | open |

## 3. 누락 후보
- [x] 있음
- details:
  - `영상 슬롯 경제`를 제외하면, 이번 라운드에서 확인한 미반영 항목은 모두 `CR-20260315-002` 설계 문서에 근거가 있다.
  - 특히 `major_prompt_log`에서 직접 합의된 문구가 live world bible 본문으로 충분히 내려오지 않은 항목이 이번 수정 대상이다.

## 4. 중복/불필요 정보 후보
- [x] 있음
- details:
  - `WB-0006`의 현행 첫머리 표현은 `일부 특수 지형만 노드`처럼 읽혀, 새 바닥 규칙과 충돌하는 중복 인상을 만든다.
  - `WB-0019`의 자동 채널 설명은 남기되, `질의 인장 / 기록 인장` 구조를 덧붙여 의미를 명확히 하는 편이 낫다.

## 5. 판단 근거
- world_bible_index 참조:
  - `WB-0006`, `WB-0015`, `WB-0017`, `WB-0019`
- cross-reference 참조:
  - `world_ops/cases/CR-20260315-002/major_prompt_log.md`
  - `world_ops/cases/CR-20260315-002/mana_node_frontier_draft.md`
  - `world_ops/cases/CR-20260315-002/community_unlock_blueprint.md`
  - `world_ops/cases/CR-20260315-002/irminsul_contract_ladder.md`

## 6. 분기 결정
- branch: minor
- reason:
  - 새 설정을 발명하는 작업이 아니라, 이미 승인된 `CR-20260315-002` 설계의 live SSOT 누락분을 본문/요약층에 내려 적는 동기화 작업이기 때문이다.

## 7. 작가 승인
- approved: yes
- note:
  - `영상 슬롯 경제`는 명시적으로 제외하고 나머지 누락 설정만 반영한다.
