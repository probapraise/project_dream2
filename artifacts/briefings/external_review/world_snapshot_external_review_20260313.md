# Project Dream2 World Snapshot for External Review

- snapshot_date: 2026-03-13
- repo_head: `644ce78`
- document_role: 외부 리뷰어용 단일 브리핑 snapshot
- ssot_status: non-SSOT
- source_priority:
  - 1. `world/live/`
  - 2. `docs/handoff/next_steps.md`
  - 3. `artifacts/writing/episodes/*/canon/README.md`
- visibility_policy: 본 문서는 `[PUBLIC]`, `[CONFIDENTIAL]`, `[META]`를 함께 설명한다.
- excluded_by_default:
  - `world_ops/` 상세 절차 문서 원문
  - `world/archive/quarantine/`
  - `artifacts/runs/` 세부 로그
  - `artifacts/batch/`
  - episode 원문 전체 텍스트
- known_limits:
  - 현재 확정 캐논 frontier는 `ep002`다.
  - `ep003`는 집필 패킷과 스캐폴드만 준비된 상태이며, 아직 캐논이 아니다.
  - 본 문서는 저장소 전체를 전부 복제하지 않고, 외부 리뷰에 필요한 구조와 원리만 압축한다.

## 1. What This Project Is

- Project Dream2는 단순한 세계관 메모 저장소가 아니라, 장기 연재형 웹소설을 위한 `세계관 SSOT + 모집단 엔진 + 커뮤니티/시뮬레이션 레이어 + 집필 오케스트레이션` 저장소다.
- 작품 자체는 판타지 학원물 외형을 띠지만, 서사의 핵심은 전투력 성장보다 `기록`, `정본`, `열람권`, `접속권`, `로그`, `검색`, `증거화`가 권력으로 작동하는 사회를 설계하는 데 있다.
- 주인공 `키리온 렌바렌`은 귀족가 내부의 감시와 위장 생존을 통과한 뒤, 장기적으로 `각인광장(Archive Plaza)`이라는 공론장/정보 인프라를 구축하는 방향으로 움직인다.
- 즉 이 저장소의 목표는 "설정을 보관하는 것"이 아니라, "연재 중에도 세계 상태와 서사 상태를 일관되게 갱신 가능한 운영 체계로 유지하는 것"이다.

## 2. Project Goal

### 2.1 Story Goal

- [PUBLIC] 마법 기반 기록 사회에서 정보 접근권과 정본 통제권이 어떻게 계급과 권력을 만드는지 보여주는 장편 서사를 구축한다.
- [META] 주인공의 장기 엔진은 성목(Irminsul)과 배지 네트워크를 활용해 `각인광장`을 만들고, 기존 권한 산업을 대중화하며 뒤집는 것이다.
- [META] 초반부는 학술원 본편이 아니라 렌바렌 저택 내부에서의 검증, 감시, 독서, 정보 병목 관찰을 먼저 다루도록 설계돼 있다.

### 2.2 Repository Goal

- `world/live/`를 살아 있는 정본 번들로 유지한다.
- 설정 변경, 캐논 수정, 시뮬레이션 결과, 집필 패턴이 서로 충돌하지 않도록 감사 가능한 운영 흐름을 둔다.
- 연재 회차가 쌓일수록 프롬프트와 집필 문서가 오히려 흔들리지 않게, 파생 문서와 SSOT를 분리해 관리한다.

## 3. Current Implementation Snapshot

- 학생 모집단 SSOT는 `world/live/population/`의 `P-*` 슬롯과 `population_slots.csv`다.
- 총 학생 슬롯은 `3600`개이며, 현재 named core cast는 `NC-0001` 한 명이 활성화돼 있다.
- 커뮤니티 레이어는 Layer A 창발형 규칙과 Layer B 작가 투사형 문법을 모두 갖추고 있다.
- Quick Sim 기본 레인과 API fallback 레인이 분리돼 있다.
- 집필 워크플로우는 `멀티 초고 수집 -> 조립 수정 -> 캐논 스냅샷 승격 -> live sync audit` 기준으로 정리돼 있다.
- 현재 서사 frontier는 `ep002`까지 확정이며, `ep003`는 준비 중이다.

### 3.1 Audit Snapshot on 2026-03-13

- `python3 scripts/writing/audit_live_sync.py`: 통과
- `python3 scripts/population/audit_population_invariants.py`: 통과
- `bash scripts/ops/world_ops_audit_bundle.sh`: 통과
- population invariant 결과: `slots=3600`, `violations=0`

## 4. Repository Structure

```text
project_dream2/
├─ world/live/              # 현재 살아 있는 SSOT 번들
│  ├─ docs/                 # 인덱스, 상태, 스타일, 서사 허브
│  ├─ world_bible/          # 활성 세계관 문서
│  ├─ population/           # P-* 학생 슬롯 + core_cast
│  ├─ external/             # EX-* 외곽 인물
│  ├─ nonstudent/           # NS-* 비학생 슬롯
│  ├─ board_states/         # 시뮬레이션 후 상태
│  └─ layer_b/              # 게시판 문화/문법 산출물
├─ artifacts/               # 집필/브리핑/실험 산출물
│  ├─ writing/              # 회차별 초고, 조립본, 캐논, 스타일 패킷
│  └─ briefings/            # 외부 리뷰용 요약/도감
├─ scripts/                 # population / indexes / ops / sim / writing 자동화
├─ docs/                    # 아키텍처, handoff, 설명서
└─ world_ops/               # 변경관리용 control plane
```

## 5. Core Operating Model

### 5.1 Single Source of Truth

- 오케스트레이터의 상시 로딩 문서는 `world/live/docs/master_map.md` 하나다.
- 다른 문서는 `master_map`의 포인터를 따라 필요할 때만 읽는다.
- `world/live/` 바깥의 문서는 대부분 파생 문서, 설명 문서, 산출물로 취급한다.

### 5.2 Live Bundle and Derived Docs

- `world/live/world_bible/`는 제도, 정치, 마법, 사회, 권한 구조 등 정적 설정의 SSOT다.
- `world/live/docs/`의 `narrative_state`, `story_arcs`, `foreshadow_registry`, `episode_deltas`, `style_bible`는 캐논 진행에 따라 갱신되는 live 보조 문서다.
- 이 보조 문서는 캐논과 분리된 독립 창작물이 아니라, 최신 캐논을 요약하고 재사용하기 위한 파생 메모리다.

### 5.3 Change Management

- 큰 설정 변경은 `world_ops/`의 4단계 체인으로 처리하도록 설계돼 있다.
- 핵심 원칙은 `요청 정제 -> 충돌 탐색 -> 적용 -> 동기화`다.
- 실제 외부 리뷰에서는 세부 절차보다, "이 저장소가 임의 수정이 아니라 변경관리형으로 운영된다"는 점이 중요하다.

### 5.4 Quarantine Strategy

- 충돌 가능성이 있는 레거시 문서는 바로 삭제하지 않고 `world/archive/quarantine/`로 격리한다.
- live 인덱스에서 빠진 문서는 기본 실행 경로에서 제외되며, 필요할 때만 재검토한다.
- 이 전략 덕분에 과거 설정을 잃지 않으면서도 활성 설정의 일관성을 지킬 수 있다.

## 6. Population and Simulation Engine

### 6.1 Population System

- 세계의 학생 사회는 무작위 군중이 아니라, `3600`개의 명시적 슬롯으로 관리된다.
- 각 슬롯은 배경, 학년, 기숙사, 마나색, 전공, 직능, 성향 파생값을 갖는다.
- 코어 캐스트는 이 모집단 위에서 선발되고, named 상태 전환은 인덱스와 카드에 동시에 반영된다.

### 6.2 Population Pipeline

- 대표 흐름:
  - `generate_population_slots`
  - `add_student_fields`
  - `recompute_derived` 또는 batch derived 경로
  - 정책 보정 스크립트
  - `bootstrap_core_cast`
  - `rebuild_character_index_v2`
  - `audit_population_invariants`
- 이 구조 덕분에 등장인물 카드만 따로 떠다니지 않고, 전체 사회 분포와 코어 인물이 같은 기반 데이터 위에 서 있게 된다.

### 6.3 Community and Simulation Layers

- Layer A는 시뮬레이션에서 창발하는 커뮤니티 문화 후보를 다루는 레이어다.
- Layer B는 작가가 의도적으로 이식한 인터넷 커뮤니티 문법을 ATOM/GRAMMAR 단위로 관리하는 레이어다.
- 게시판은 고정 18보드 체계를 폐기하고, `concept_only -> registered -> stateful -> retired`의 동적 라이프사이클로 운영한다.
- Quick Sim은 기본 탐색 레인이고, API 기반 시뮬레이션은 fallback 또는 고정밀 검증 레인이다.

## 7. Writing Workflow

### 7.1 Why the Writing System Exists

- 이 저장소의 집필 파이프라인은 단순 프롬프트 보관소가 아니다.
- 회차가 늘어날수록 문체, 설정, 최근 캐논, 장기 맥락을 분리해 넣지 않으면 프롬프트가 오염되기 때문에, 집필 입력도 구조화돼 있다.

### 7.2 Current Episode Production Flow

1. 아이디어 회의로 이번 회차 비트를 고도화한다.
2. `episode_style_constitution`, `setting_brief`, 최근 3회차 raw canon, `long_range_summary`, `prompt_packet`, `prompt_vN`으로 주입 패킷을 만든다.
3. 외부 모델들과 내부 집필을 병렬로 돌려 멀티 초고를 수집한다.
4. 사용자가 여러 초고를 조립·수정해 합성 수정본을 만든다.
5. 초고들과 수정본의 차이를 분석해 스타일 패턴과 캐논 변화를 기록한다.
6. 수정본을 캐논 스냅샷으로 승격한다.
7. 이후 live 문서와 다음 회차 패킷이 stale 상태인지 audit한다.

### 7.3 Writing Inputs Are Now Packetized

- 과거에는 `prompt_vN.md` 한 문서에 많은 내용을 압축했다.
- 현재는 역할을 나눈 입력 패킷 구조를 쓴다.
- 핵심 파일:
  - `episode_style_constitution_vN.md`
  - `setting_brief_vN.md`
  - 최근 3회차 raw canon 전문
  - `long_range_summary_vN.md`
  - `prompt_packet_vN.md`
  - `prompt_vN.md`
- 이 구조의 목적은 문체 규칙, 설정 사실, 최근 맥락, 이번 회차 지시를 서로 다른 권한으로 분리하는 것이다.

### 7.4 Canon Patch Policy

- 의미 변화가 있는 캐논 수정은 기존 파일을 조용히 덮어쓰지 않는다.
- `canon/` 안에 새 스냅샷 파일을 만들고, `canon/README.md`에서 current canon을 다시 가리키는 방식이 기본 원칙이다.
- 이 정책은 diff 추적, live sync, 롤백, 외부 리뷰 정합성에 유리하다.

### 7.5 Style Governance

- 문체 규칙은 `house_rules`, `style_pattern_library`, `style_selection`으로 분리돼 있다.
- `house_rules`는 항상 적용되는 고정 규약이다.
- `style_pattern_library`는 과거 원고에서 추출한 후보 패턴 모음이다.
- `style_selection`은 이번 회차에 실제로 적용할 패턴만 고르는 선택 레이어다.
- 즉, 에피소드 특수성이 다음 화의 강제 규칙으로 잘못 승격되지 않도록 막는 구조다.

## 8. Current Narrative State

### 8.1 Narrative Frontier

- 현재 확정 frontier는 `ep002`다.
- 초반부는 아직 학술원 입학 이전이며, 렌바렌 저택 내부의 감시와 정보 병목이 핵심 긴장이다.
- `ep003` 준비 방향은 "보상처럼 보이는 서고 접근과 독서 기회가 동시에 감시 장치로 작동하는 구도"를 유지하는 쪽으로 정리돼 있다.

### 8.2 Core Story Pressure

- [PUBLIC] 키리온은 평범한 8세 차남처럼 보여야 한다.
- [CONFIDENTIAL] 아버지 칼리온은 이미 정체 변조 가능성을 강하게 의심하고 있다.
- [META] 초반 메인 갈등은 무력 성장보다, 관찰당하는 아이가 어떤 방식으로 정보 구조를 읽고 살아남는가에 있다.

### 8.3 Medium-Term Story Shape

- [META] 하급 과정 진입은 12세, 본격적인 상급 과정은 15세 진입성취평가 이후로 설계돼 있다.
- [META] 학술원 본편은 잠정적으로 `ep010` 전후 진입을 목표로 한다.
- [META] 이 전까지는 저택 내부의 감시, 형제관계, 독서 패턴, 제도 이해, 각인광장 욕망의 씨앗을 먼저 심는다.

## 9. How the Project Actually Runs

- 이 저장소는 단일 실행 바이너리나 웹 서비스가 아니다.
- 실제 운영은 `문서 SSOT + 자동화 스크립트 + audit`의 조합으로 이뤄진다.
- 대표적 실행 원리:
  - 세계관과 population은 스크립트로 생성·보정·감사한다.
  - 커뮤니티 실험은 Quick Sim 또는 API 시뮬레이션으로 돌린다.
  - 집필은 회차 스캐폴드 생성, 패킷 작성, 멀티 초고 수집, 캐논 승격, stale audit 순으로 운용한다.
  - live 문서와 집필 패킷은 별도 audit 스크립트로 최신 캐논과의 어긋남을 잡는다.

### 9.1 Key Operational Scripts

- population:
  - `scripts/population/audit_population_invariants.py`
- indexes and bundle:
  - `scripts/indexes/rebuild_world_indexes.sh`
  - `scripts/ops/world_ops_audit_bundle.sh`
- writing:
  - `scripts/writing/new_episode_scaffold.sh`
  - `scripts/writing/new_canon_patch.sh`
  - `scripts/writing/refresh_canon_metadata.py`
  - `scripts/writing/post_canon_sync.sh`
  - `scripts/writing/audit_live_sync.py`
  - `scripts/writing/audit_prompt_packet.py`
- external review:
  - `scripts/indexes/build_external_review_dossier.sh`

## 10. What Is Already Strong

- 세계관 문서와 서사 문서가 분리돼 있어, 설정과 스토리 진행을 별개 축으로 관리할 수 있다.
- population 슬롯 기반 구조 덕분에 "세계 전체 분포"와 "핵심 인물"이 같은 기반 위에서 움직인다.
- Layer A/B, Quick Sim, VFP, style governance 등 후속 확장 포인트가 이미 설계돼 있다.
- 캐논 사후 수정과 live 문서 드리프트 문제를 audit 중심으로 통제하려는 방향이 명확하다.

## 11. Main Constraints and Open Boundaries

- 현재 named core cast는 거의 비어 있어, 대규모 캐릭터 드라마 단계까지는 아직 가지 않았다.
- 학술원 본편과 각인광장 운영은 장기 설계가 강하고, 실제 서사 구현은 아직 저택 초반부에 머물러 있다.
- `ep003` 이후 집필이 누적되기 전까지는 새 패킷형 집필 시스템의 장기 안정성이 완전히 증명된 것은 아니다.
- Layer A의 창발 문화 후보는 존재하지만, 어떤 문화를 정식 CULTURE 레코드로 승격할지는 아직 더 축적이 필요하다.

## 12. Recommended Reading Order for External Review

1. 이 문서
2. `world/live/docs/master_map.md`
3. `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`
4. `docs/handoff/next_steps.md`
5. `world/live/docs/narrative_state.md`
6. `world/live/docs/story_arcs.md`
7. `world/live/docs/foreshadow_registry.md`
8. `world/live/population/core_cast/NC-0001_P-1027.md`
9. `world/live/world_bible/WB-0003_onepage_summary.md`
10. `world/live/world_bible/WB-0005_magic_system.md`
11. `world/live/world_bible/WB-0008_archive_plaza_overview.md`
12. `artifacts/writing/episodes/ep002/canon/README.md`

## 13. Suggested External Review Questions

1. 이 프로젝트의 가장 강한 차별점은 무엇이며, 그것이 현재 구조에서 충분히 살아 있는가.
2. 정보 권력, 기록 인프라, 귀족 제도, 학술원 구조가 서로 충돌 없이 한 작품 엔진으로 묶이는가.
3. 저택 파트가 길어질 때 긴장을 유지하는 핵심 장치가 충분한가.
4. 학술원 본편 진입 전까지 반드시 선행돼야 할 세계관/감정/제도 노출은 무엇인가.
5. population 기반 설계와 커뮤니티/플랫폼 장기 엔진이 실제 서사로 이어질 때 가장 취약한 연결부는 어디인가.

## 14. If Deeper Review Is Needed

- 압축본이 아니라 거의 전체 live 문서를 읽는 상세판이 필요하면 아래 파일을 사용하면 된다.
- `artifacts/briefings/external_review/world_dossier_external_review_full_20260310.md`
- 이 스냅샷은 상세판의 대체물이 아니라, 현재 구조와 목적을 빠르게 이해시키기 위한 상위 브리핑이다.
