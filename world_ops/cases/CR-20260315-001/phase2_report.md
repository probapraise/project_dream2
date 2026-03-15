# Phase 2 Report (Collision Scan)

- change_id: CR-20260315-001
- verdict: major

## 1. 탐색 범위
- files:
  - world/live/docs/world_bible_index_v2.md
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0006_irminsul_infra.md
  - world/live/world_bible/WB-0007_badge_network.md
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
  - world_ops/cases/CR-20260315-001/tagging_draft.md

## 2. 충돌 후보
- [ ] 없음
- details:
  - `무대용 설정 통합정리` 기준의 새 바닥 설정은 현행 live bundle과 부분 수정 수준이 아니라, `우주론 SSOT 부재 + 표면 규칙 재정의 + 구 메타 잔존 제거`가 동시에 필요한 상태다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 비공개 우주론을 소유하는 정식 WB 문서가 없음 | world_bible 구조 전체 | 새 `META` 전용 SSOT 신설 | 관찰자, 심연, 아키텍트, 워든, Axis/Branch, 앵커 | open |
| 구 바닥 설정 파편이 행성/열구/작명 문서에 흩어져 있음 | WB-0010, WB-0011, WB-0013, WB-0025 | 우주론 직결 문장 제거 후 표면 설정으로 재작성, 일부는 치환안 확정 전 보류 | 열구, 외계 문명 유입, 시뮬레이션 분기 세계 | open |
| 마법 시스템의 공식 분류가 새 합의와 어긋남 | WB-0005 | `표준식 / 등록식 / 문장비전 / 7색 주색` 중심으로 재구성 | 공리마법, 구축마법, 마나색, 서명 | open |
| 정령/성목/배지 인프라 설명이 `하급 정령 계약 = 노드 접속권` 구조를 아직 반영하지 않음 | WB-0006, WB-0007 | 성목을 특수 지형 노드 일반론으로 확장하고, 배지 인프라를 마나 사인 + 하급 정령 계약 기반으로 재설명 | 성목, 정령군, 배지, 중계망 | open |
| 혈통·종족·서명·학파·마나색·마력석 설정이 여러 문서에 분산돼 일관된 기준점이 없음 | WB-0005, WB-0016, WB-0017, WB-0026 | 새 공통 정의 문서 신설 후 기존 문서가 참조하도록 재배치 | 혈통 편중, 종족 차이, 권능의 서명, 마력석 | open |
| 렌바렌/주인공 정체성 메타가 구 우주론 기반으로 적혀 있음 | NC-0001, long_term | 새 우주론 확정 후 별도 재정의 | 상위관찰자, 제네시스 표본, 앵커 기억 제거 | deferred |
| 로노모고스 축을 제외하기로 했으나 구 문서군의 하부 구조는 여전히 이에 의존함 | 무대 전체 구조 | 로노모고스 직결 문장 제거, 대체 표면 갈등축 별도 확정 필요 | Axis-Ronomogos, 워든 통제 프로토콜 | open |

## 3. 누락 후보
- [ ] 없음
- details:
  - `META` 전용 우주론 SSOT 누락
  - 혈통·종족·서명·학파·마나색·마력석 공통 정의 문서 누락
  - `하급 정령 계약`과 `특수 지형 노드`를 정식으로 묶어 설명하는 최신 기준 누락

## 4. 중복/불필요 정보 후보
- [ ] 없음
- details:
  - `열구 / 외계 문명 유입 / 시뮬레이션 분기 세계` 계열 설명이 여러 문서에 중복 반영됨
  - `마법 시스템`과 `문장비전` 관련 설명이 WB-0005와 WB-0026 사이에서 중복/엇갈림
  - `정체성 메타`가 master_map 로그, NC-0001, long_term에 분산 기록됨

## 5. 판단 근거
- world_bible_index 참조:
  - WB-0005, WB-0006, WB-0007, WB-0010, WB-0011, WB-0013, WB-0016, WB-0017, WB-0025, WB-0026
- cross-reference 참조:
  - `프라미시오_무대용_설정_통합정리.docx`
  - `world_ops/cases/CR-20260315-001/tagging_draft.md`

## 6. 분기 결정
- branch: major
- reason:
  - 새 바닥 설정 반영은 단일 문서 수정이 아니라 `신설 SSOT + 다수 문서 재작성 + 기존 메타 파편 제거 + 인덱스 동기화`를 동반한다.
  - 특히 현행 표면 설정의 일부가 구 우주론과 직접 결박되어 있어, 단순한 부분 패치로는 정합성을 보장하기 어렵다.

## 7. 작가 승인
- approved: no
- note:
  - 항목별 공개 레벨 태깅 초안은 상당 부분 합의됐으나, 구 `열구 / 외계 유입` 축을 어떤 표면 설정으로 치환할지 등 후속 결정이 남아 있다.
