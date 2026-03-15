# Change Request

- change_id: CR-20260315-001
- date: 2026-03-15
- requester: writer
- status: draft
- source_of_truth:
  - primary: world/live/docs/master_map.md + 관련 live bundle 문서
  - secondary: docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- `프라미시오_무대용_설정_통합정리.docx`의 내용을 바탕으로 world bible의 바닥 설정을 재정비한다.
- 단, `마왕 로노모고스`, `Axis-Ronomogos`, `워든 통제 프로토콜` 등 로노모고스 직결 축은 이번 작품 반영 대상에서 제외한다.
- 실제 문서 수정 전에, 반영 대상 항목과 각 항목의 공개 레벨(`PUBLIC` / `CONFIDENTIAL` / `META`)을 먼저 확정한다.

## 2. 정제된 목표 (1문장)
로노모고스 축을 제외한 프라미시오 바닥 설정을 world bible 기준으로 재구성하고, 표면 규칙과 비공개 우주론의 경계를 공개 레벨 태깅으로 먼저 고정한다.

## 3. 변경 유형
- add
- modify
- deprecate
- retcon

## 4. 성공 기준 (DoD)
- [ ] 로노모고스 제외 기준으로 반영할 바닥 설정 항목 목록이 확정된다.
- [ ] 각 항목의 공개 레벨(`PUBLIC` / `CONFIDENTIAL` / `META`)이 작가 승인 상태로 정리된다.
- [ ] 우주론 SSOT 신설 대상과 기존 교체 대상 문서가 구분된다.
- [ ] 현행 live bundle의 구 바닥 설정 잔존 지점이 후속 정리 대상으로 명시된다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/world_bible_index.md
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0010_planet_continents_naming.md
  - world/live/world_bible/WB-0011_echo_zone_rifts.md
  - world/live/world_bible/WB-0013_timeline_event_engine.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0016_social_stratification.md
  - world/live/world_bible/WB-0017_economy_resources.md
  - world/live/world_bible/WB-0018_evidence_records_glossary.md
  - world/live/world_bible/WB-0025_appendix_naming_constitution.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/long_term.md
- impacted_entities:
  - 표준식
  - 등록식
  - 문장비전
  - 마나 사인
  - 하급 정령 계약
  - 권능의 서명
  - 학파
  - 마나색
  - 마력석
  - 특수 지형 / 마나 노드 / 신격 / 정령군
  - 관찰자 / 심연 / 아키텍트 / 워든 / 앵커 / Axis / Branch (META only)

## 6. 작가 확인 필요 항목
- Q1: `하급 정령 계약`의 구체적 기능 범위를 어디까지 `PUBLIC`로 둘 것인가
- Q2: `권능의 서명`, `학파`, `마력석 생성 원리`를 각각 어느 공개 레벨까지 허용할 것인가
- Q3: 현행 `열구 / 외계 문명 유입 / 시뮬레이션 분기 세계` 축을 어떤 표면 설정으로 치환할 것인가

## 7. 승인 기록
- approved: yes | no
- approved_by:
- approved_at:
- note:
