# Phase 3 Apply

- change_id: CR-20260315-001
- branch: minor

## 1. 실제 수정 파일
- world/live/world_bible/WB-0005_magic_system.md
- world/live/world_bible/WB-0006_irminsul_infra.md
- world/live/world_bible/WB-0007_badge_network.md
- world/live/world_bible/WB-0009_power_structure_factions.md
- world/live/world_bible/WB-0010_planet_continents_naming.md
- world/live/world_bible/WB-0011_echo_zone_rifts.md
- world/live/world_bible/WB-0013_timeline_event_engine.md
- world/live/world_bible/WB-0016_social_stratification.md
- world/live/world_bible/WB-0017_economy_resources.md
- world/live/world_bible/WB-0025_appendix_naming_constitution.md
- world/live/world_bible/WB-0026_appendix_crest_arcana.md
- world/live/world_bible/WB-0028_appendix_hidden_cosmology_ssot.md
- world/live/world_bible/WB-0029_appendix_aptitude_signature_materials.md
- world/live/population/core_cast/NC-0001_P-1027.md
- world/live/docs/memory_tiers/long_term.md

## 2. 변경 요약 (diff 요약 수준)
- `WB-0028`을 `META` 전용 비공개 우주론 SSOT로 신설했다.
- `WB-0029`를 혈통, 종족, 권능의 서명, 마나색, 마력석의 공통 기준 문서로 신설했다.
- `WB-0005`를 `표준식 / 등록식 / 문장비전 / 계약 / 수련 초월` 중심 구조로 전면 재작성했다.
- `WB-0006`을 성목 단독 문서에서 `특수 지형 노드 / 신격 / 정령군` 중심 문서로 확장 재작성했다.
- `WB-0007`을 `마나 사인 + 하급 정령 계약 + 배지` 3층 구조로 전면 재작성했다.
- `WB-0016`을 혈통 편중, 종족별 전문화, 혼혈 희소성, 봉건적 차별 구조 중심으로 재작성했다.
- `WB-0017`을 권한 경제, 노드 접근권, 마력석 3분류 활용 중심으로 재작성했다.
- `WB-0026`의 개념부를 새 문장비전 기준으로 재정의하고, 24가문 상세는 유지한 채 상위 설명만 교체했다.
- `NC-0001`, `long_term`의 주인공 정체성 메타를 `완전한 타인 빙의`나 구 우주론 용어 대신 `외래 기억·사고 구조의 잔향이 키리온으로 수렴한다`는 기준으로 정리했다.
- `WB-0010`, `WB-0011`, `WB-0013`, `WB-0025`, `WB-0009`의 구 `열구 = 외계 유입 / 시뮬레이션 결함` 계열 문장을 새 표면 설정으로 교체했다.
- `EX-0001`, `EX-0003`, `WB-0003`, `community_grammar_layer_b`, `story_arcs`, `episode_deltas`, `memory_tiers/entity_registry`, `WB-0028`에 남아 있던 `빙의 / 전생 / 외계 유입` 잔존 표현을 `외래 기억 잔향 / 고대 유산 / 심층 금역` 기준으로 최종 정리했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 비공개 우주론 SSOT 신설 | `WB-0028` 전체 | 관찰자, 심연, 아키텍트, 워든, Axis / Branch, 앵커, 메아리 | 표면 문서에 메타 설명이 다시 새지 않도록 후속 문서 동기화 필요 |
| 적성 체계 공통 기준 신설 | `WB-0029` 전체 | 혈통 편중, 종족별 전문화, 권능의 서명, 마나색, 마력석 | 참조 문서와의 표현 드리프트만 후속 감시 |
| 마법 시스템 기준 재정립 | `WB-0005` 전체 | 표준식, 등록식, 문장비전, 영창, 마법진, 촉매, 수련 초월 | `WB-0015`, 일부 집필 문서와 용어 재동기화 필요 |
| 노드 / 성목 / 정령군 구조 반영 | `WB-0006` 전체 | 특수 지형 노드, 성목, 잠든 신, 정령군 | 지역별 노드 사례를 later pass에서 추가 가능 |
| 배지 인프라 구조 반영 | `WB-0007` 전체 | 마나 사인, 하급 정령 계약, 배지, 수심, 중계주 | 기관별 권한 편차와 악용 케이스는 later pass에서 보강 가능 |
| 사회 구조 재정렬 | `WB-0016` 전체 | 혈통 편중, 종족 차별, 혼혈 희소성, 벨쿠란 관용의 한계 | 지역별 인종 관습 차이는 later pass에서 추가 가능 |
| 경제 구조 재정렬 | `WB-0017` 전체 | 권한 경제, 노드 접근권, 마력석, 광장 경제 | 세부 가격표와 지역별 시장차는 later pass에서 보강 가능 |
| 문장비전 개념부 재정의 | `WB-0026` F.1 | 서명귀족, 혈통키, 비전관, 계승조회식 | 가문별 상세 개정은 필요 시 별도 케이스로 분리 |
| 주인공 메타 정렬 | `NC-0001`, `long_term`, `EX-0001`, `EX-0003`, `WB-0003`, `community_grammar_layer_b`, `story_arcs`, `episode_deltas`, `memory_tiers/entity_registry` | 외래 기억 잔향, 키리온으로의 수렴, 정체성 처리 방침 | 활성 집필 패킷 기준 정리 완료, 이후 신규 문서 드리프트만 후속 감시 |
| 구 바닥 설정 표면 치환 | `WB-0009`, `WB-0010`, `WB-0011`, `WB-0013`, `WB-0025`, `WB-0028`, `master_map` | 열구, 잔향역, 심층 마나층 균열, 고대 재앙 상흔 | 활성 SSOT와 로그 문구 기준 정리 완료, 이후 신규 문서 드리프트만 후속 감시 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 이번 단계의 변경은 기초 SSOT와 직접 충돌하던 표면 설정을 정리하는 데 집중했다.
  - `WB-0016`, `WB-0017`, `WB-0026`, `NC-0001`, `long_term`까지 반영한 뒤에도 감사 기준에서 오류나 경고는 발생하지 않았다.

## 4. 미해결 항목
- [ ] 없음
- details:
  - 후속 점검 후보:
  - 신규 집필 문서 생성 시 `외래 기억 잔향` 표현 기준이 재이탈하지 않는지 후속 감시가 필요하다.

## 5. 작가 승인
- approved: yes
- note:
  - 세부 태깅 합의와 `열구` 표면 치환안 승인 이후 기초 SSOT 반영 단계까지 적용 완료.
