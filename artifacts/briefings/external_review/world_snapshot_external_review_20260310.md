# Project Dream2 World Snapshot for External Review

- snapshot_date: 2026-03-10
- repo_head: `d67f941`
- document_role: 외부 모델 자문용 단일 브리핑 snapshot
- ssot_status: non-SSOT
- source_priority:
  - 1. `world/live/`
  - 2. `docs/handoff/next_steps.md`
  - 3. `artifacts/writing/episodes/*/canon/README.md`
- visibility_policy: 본 문서는 `[PUBLIC]`, `[CONFIDENTIAL]`, `[META]`를 함께 포함한다.
- excluded_by_default:
  - `world_ops/`
  - `world/archive/quarantine/`
  - `artifacts/runs/`
  - `artifacts/batch/`
  - episode 원문 전체 텍스트
- known_drift:
  - `world/live/docs/narrative_state.md`는 아직 `latest_canon_episode: ep001`로 적혀 있다.
  - 그러나 handoff와 canon README 기준 현재 확정 캐논 frontier는 `ep002`까지다.
  - 이 브리핑은 `ep002 canon 확정` 상태를 기준으로 작성한다.

## 1. What This Project Is

- 이 프로젝트는 일반 판타지 학원물이 아니라, "마법 기반 기록/권한 사회에서 검색 가능한 공론장을 발명하는 이야기"다.
- 주인공은 백작가 차남 `키리온 렌바렌`이며, 문장비전도 상속권도 없는 위치에서 정보 인프라를 뒤집는 방향으로 성장한다.
- 핵심 차별점은 전투력 상승보다 `기록`, `정본`, `열람권`, `면허`, `로그`, `검색`, `증거화`가 권력으로 작동한다는 점이다.
- 장기 메인 엔진은 성목(Irminsul)을 LMM 비슷한 학습형 인프라로 진화시켜 `각인광장(Archive Plaza)`이라는 대중 공론장을 만드는 것이다.
- 현재 서사는 아직 학술원 본편 전이다. 렌바렌 저택 내부에서 정체 은폐, 가족 감시, 정보 병목 관찰을 먼저 다루고 있다.

source_of_truth:
- `world/live/world_bible/WB-0003_onepage_summary.md`
- `world/live/docs/narrative_state.md`
- `world/live/docs/story_arcs.md`

## 2. Spoiler / Visibility Guide

- `[PUBLIC]`는 작중 인물과 독자가 초반부터 세상 상식처럼 받아들일 수 있는 정보다.
- `[CONFIDENTIAL]`는 특정 기관이나 상층부만 아는 정보다. 작중 공개 타이밍이 중요하다.
- `[META]`는 작가용 진실이다. 외부 모델이 구조 조언을 할 때는 볼 수 있지만, 작중 노출 방식은 분리해서 다뤄야 한다.
- 본 브리핑은 조언 정확도를 위해 세 레벨을 함께 담지만, 각 항목마다 레벨을 유지한다.
- 외부 자문 결과를 실제 집필에 반영할 때는 "이 조언이 PUBLIC 레벨 장면에 바로 노출 가능한가"를 다시 판정해야 한다.

source_of_truth:
- `world/live/world_bible/WB-0002_loreops_canon_control.md`

## 3. Core World Invariants

### 3.1 Information Is Power

- [PUBLIC] 이 세계에서 핵심 권력 자원은 화폐 자체보다 `정본`, `열람권`, `면허`, `접속권`, `통행권`, `로그`, `보존권`이다.
- [PUBLIC] 마나사인과 정본 체계 때문에 "무엇이 공식 기록으로 남는가"가 곧 법적/정치적 힘이 된다.
- [PUBLIC] 연장각인 자체는 이미 탈희소화되었고, 진짜 희소한 것은 대규모 색인, 검색, 증거화, 권한 배분이다.
- [PUBLIC] 따라서 각인광장은 단순한 게시판이 아니라, 기존 권한 산업을 대중화하고 교란하는 위험한 플랫폼이다.

### 3.2 Magic Is Infrastructure, Not Exotic Mystery

- [PUBLIC] 마법은 이 세계의 사회 인프라다. 특권층만의 기적이 아니라 행정, 물류, 치안, 계약, 기록을 떠받치는 기반 기술이다.
- [PUBLIC] 모든 시전자에게는 마나핵과 MP가 있고, 표준식은 누구나 시도할 수 있지만 정합도, 마나색, 훈련, 학파에 따라 효율이 크게 갈린다.
- [PUBLIC] 등록식은 사회 기능 단위의 마법이다. 절차, 권한, 실패 모드까지 포함한 제도적 시스템에 가깝다.
- [PUBLIC] 마나색 7계열은 `적/청/녹/황/자/백/흑`이며, 흑은 침식/저주/오염 계열이라 금기 취급 가능성이 높다.

### 3.3 Signature Houses Matter

- [PUBLIC] 문장비전(Crest Arcana)은 혈통잠금된 특수 등록식이다.
- [PUBLIC] 서명귀족은 문장비전과 마나 결절, 내성, 봉건적 책임을 함께 떠안는 전략 자산 집단이다.
- [PUBLIC] 국가의 국력은 강력한 등록식과 문장비전을 얼마나 보유/운용하느냐와 직결된다.
- [PUBLIC] 벨쿠란 왕국에는 24개 문장대장 가문이 있으며, 왕가/공작가 일부는 2~3개 안정 시그니처를 전승한다.

### 3.4 Irminsul, Badge, and Archive Plaza

- [PUBLIC] 성목(Irminsul)은 대규모 마법 인프라 코어가 될 수 있는 희귀 신목이다.
- [PUBLIC] 배지는 단순 신분증이 아니라 학내 표준 프로토콜 단말이다. 정보 표시, 출입/열람 인증, 공지 수신, 실습 로그 기록을 함께 수행한다.
- [PUBLIC] 각인광장은 배지를 통해 입력된 발화를 문장 단위 텍스트 패킷으로 저장하고, 스레드/댓글/추천/신고/잠금/보존권 같은 규칙으로 공론장을 만든다.
- [PUBLIC] 영상은 정보량이 커서 극히 희소하다. 그래서 `영상 슬롯` 자체가 권력이다.
- [META] 주인공은 성목에 축적되는 문장/정서/의도 데이터를 학습시키는 방식으로 LMM 비슷한 시스템 진화를 노린다.

### 3.5 Economy Runs on Scarce Rights

- [PUBLIC] 이 세계의 돈은 `열람권`, `노드 사용권`, `통행권`, `등록식/면허`, `광장 보존권`, `영상 슬롯` 같은 희소 권리와 접근성으로 정의된다.
- [PUBLIC] 마력 회복과 촉매 공급은 생산성과 직결되어 계층 격차를 키운다.
- [PUBLIC] 각인술 일반 업무는 탈희소화되었지만, 영상 각인, 대규모 색인, 봉문 최적화, 오염 환경 판독은 여전히 희소하다.
- [PUBLIC] 이것이 주인공의 장기 야망을 "기술 창업"이 아니라 "권한 산업 재편"으로 만든다.

source_of_truth:
- `world/live/world_bible/WB-0004_world_common_sense.md`
- `world/live/world_bible/WB-0005_magic_system.md`
- `world/live/world_bible/WB-0006_irminsul_infra.md`
- `world/live/world_bible/WB-0007_badge_network.md`
- `world/live/world_bible/WB-0008_archive_plaza_overview.md`
- `world/live/world_bible/WB-0017_economy_resources.md`
- `world/live/world_bible/WB-0026_appendix_crest_arcana.md`

## 4. Political and Institutional Frame

### 4.1 The 7+1 Power Axes

- [PUBLIC] 주요 권력 축은 왕실/등록청, 공보회, 칠원합, 서약원, 서명귀족, 상단연합/브로커, 학술원 규율기구, 그리고 각인광장이다.
- [PUBLIC] 기존 질서는 정본 접수, 열람권, 면허, 기록 감정, 징계권을 장악한 기관들이 유지한다.
- [PUBLIC] 각인광장은 이 질서를 깨뜨리지만, 동시에 `정렬`, `봉문`, `보존권`, `영상 슬롯`이라는 새 권력 자원을 만든다.

### 4.2 Belkuran's Core Control Mechanism

- [PUBLIC] 벨쿠란 왕국은 서명귀족 혈통 아동을 추적한다.
- [PUBLIC] 10세가 되는 해 왕도 세르비온으로 소집해 `계승조회식`을 실시하고 문장비전 계승 여부를 일괄 판정한다.
- [PUBLIC] `계승조회식` 이전 조기 사설 검증은 금지된다.
- [PUBLIC] 같은 논리로 `계승조회식` 이전 체계적 마법 수련도 금지된다.
- [PUBLIC] 이론 교육은 가능하지만, 실제 시전 가능 상태가 되도록 마나핵/회로를 활성화하는 것은 중죄에 가깝다.
- [PUBLIC] 이 제도가 가능한 이유는 마법 사용 경험자와 미사용자 사이에 마나핵/회로 감정 결과 차이가 남기 때문이다.
- [CONFIDENTIAL] 왕가, 공작가, 일부 상위 가문은 사실상 조기 수련 특권을 누린다.

### 4.3 Renbaren's Real Place in the World

- [PUBLIC] 렌바렌 백작가는 공식적으로는 라베르니온 공작가 분가 대귀족이자 비서명귀족처럼 보인다.
- [CONFIDENTIAL] 실제로는 흑 주색 문장비전 `식흔(蝕痕)`을 가진 비밀 서명귀족이다.
- [CONFIDENTIAL] 렌바렌은 독립적 정보 가문이라기보다, 라베르니온 공작가의 수면거울 감시 체계를 식흔으로 은폐하는 종속 협력 가문이다.
- [CONFIDENTIAL] 가주의 `왕국 최상위 정보기관 수장` 직위는 명예직 성격이 강하고, 실권은 라베르니온이 쥔다.
- [CONFIDENTIAL] 식흔 계승이 랜덤이기 때문에 후계 안정화 뒤 형제자매를 제거하는 `방계 청소` 관행이 있다.
- [CONFIDENTIAL] 이 관행은 왕실과 라베르니온이 묵인하는 최상위 흑역사다.

### 4.4 Important Supporting Houses

- [PUBLIC] 라베르니온 공작가는 수계 감시와 원격 시야/단문 통신 축을 쥐는 강력한 공작가다.
- [PUBLIC] 그라비온 백작가는 문서/유물 진위감정과 위변조 판독에 특화된 마법 명문이다.
- [PUBLIC] 이 둘은 주인공의 가문, 증거 체계, 장기 공론장 갈등과 매우 강하게 연결된다.

source_of_truth:
- `world/live/world_bible/WB-0009_power_structure_factions.md`
- `world/live/world_bible/WB-0018_evidence_records_glossary.md`
- `world/live/world_bible/WB-0026_appendix_crest_arcana.md`
- `docs/handoff/next_steps.md`

## 5. Academy and Population Snapshot

### 5.1 Academy Structure

- [PUBLIC] 아르케이온은 `12~14세 하급 과정 3년`과 `15세 이후 상급 과정 4년`으로 나뉜다.
- [PUBLIC] 10세 `계승조회식` 이후 합법적 기초 수련 창구가 열리고, 12세에 하급 과정 입학이 가능해진다.
- [PUBLIC] 하급 과정은 기숙 적응, 공통 정형문, 기초 체술, 안전, 기록 습관, 저위험 표준식 실습을 담당한다.
- [PUBLIC] 15세 봄 `상급 과정 진입성취평가`가 열리고, 점수대별로 전공 선택 우선권이 갈린다.
- [PUBLIC] 상급 과정은 입학 즉시 전공이 확정되며, 등록식/면허 생산을 사실상 독점하는 준국가기관이다.

### 5.2 Why the Academy Matters to the Main Plot

- [PUBLIC] 주인공의 장기 프로젝트인 각인광장은 학술원의 배지망, 기록 체계, 중계망, 열람권 구조와 직접 연결된다.
- [PUBLIC] 학술원은 단순 배경이 아니라 "권한 산업"이 응축된 제도 허브다.
- [META] 설계상 주인공은 12세 하급 과정에서 게시판 설계의 병목을 파악하고, 15세 상급 과정 진입 시 `입학 즉시 각인술 선택`으로 모두를 놀라게 해야 한다.

### 5.3 Population Model Status

- [PUBLIC] 상급 과정 모집단 모델은 3,600 슬롯 규모다.
- [PUBLIC] 현재 활성 named 슬롯은 `P-1027 -> NC-0001` 하나뿐이며, 나머지는 대부분 unnamed 상태다.
- [PUBLIC] 분포상 일반귀족이 압도적 다수이고, 서명귀족은 소수 핵심층이다.
- [PUBLIC] 기숙 체계는 마법사 7탑, 기사동, 신전동군, 비전관으로 나뉜다.
- [META] 코어 캐스트 확장은 지금 당장 하지 않고, 주인공의 학술원 입학 이후 시뮬레이션을 돌리며 추가할 계획이다.

source_of_truth:
- `world/live/world_bible/WB-0015_academy_bible.md`
- `world/live/docs/character_index_v2.md`
- `world/live/docs/core_cast_bootstrap_v1.md`
- `docs/handoff/next_steps.md`

## 6. Current Narrative Position

- current_canon_frontier_for_this_briefing: `ep002`
- macro_position: Part 1 오프닝 / 렌바렌 저택 생존 부트스트랩 / 하급 과정 진입 전

### 6.1 What Has Happened So Far

- `ep000`에서 주인공은 낯선 세계와 렌바렌 저택 내부에서 살아남기 위해 위장 모드로 들어간다.
- `ep000~ep001`에서 칼리온은 직접 추궁보다 질문 구조, 맥락 전환, 관찰 장치를 통해 키리온의 정합성을 시험한다.
- `ep001`에서 치유사 검사는 통과하지만, 그건 정체 문제까지 해소한 것이 아니다.
- `ep001` 말미 칼리온은 `흑색 표준식 입문서`를 전달해 읽기 행위 자체를 장기 관찰 대상으로 바꾼다.
- `ep002` 기준으로는 저택 내부 관찰전과 서고/독서/감시 압력이 더 강화된 상태로 간주한다.

### 6.2 Active Arcs

- ARC-001: 키리온은 아버지의 검증망 아래에서 얼마나 오래 "정상적인 8세 차남"으로 위장할 수 있는가.
- ARC-002: 저택의 정보 병목과 사람들의 자생적 문답 문화를 관찰한 주인공의 공론장 욕망이 언제 현실적 설계로 바뀌는가.
- ARC-003: 하급 과정 입학과 15세 상급 과정 점프 사이에 무엇을 먼저 보여줘야 학술원 본편이 가장 강하게 열리는가.

### 6.3 Open Foreshadow

- FS-001: 칼리온은 이미 정체 변조 가능성을 의심하고 있다.
- FS-002: 셀리아의 온기는 안전지대이면서 동시에 긴장을 풀게 만드는 위험한 이완 장치다.
- FS-003: 렌바렌 저택의 행정/정보 흐름에는 집사실 중심의 병목이 있다.
- FS-004: `흑색 표준식 입문서`는 선물이 아니라 지속형 심문 장치다.
- FS-005: 치유사 통과는 임시 안전일 뿐이다.
- FS-006: 주인공의 장기 목표는 이 세계의 정보 인프라/커뮤니티 구조를 만드는 것이다.

### 6.4 Planned Long-Range Pacing

- [META] 아르케이온 권역 첫 진입은 잠정적으로 `ep010` 전후를 목표로 둔다.
- [META] 하급 과정에서는 교수법, 생활 리듬, 병목 구조를 맛보기로 보여준다.
- [META] 이후 `3년 후` 점프로 15세 `상급 과정 진입성취평가 -> 상위권 우선권 -> 입학 즉시 전공 선택 -> 각인술 선택` 클리프행어를 연다.
- [META] 입학 전 저택 파트에서는 칼리온의 완전한 확언까지 가지 않는다. "일단 버텼다" 정도의 안도만 확보하면 된다.

source_of_truth:
- `world/live/docs/narrative_state.md`
- `world/live/docs/story_arcs.md`
- `world/live/docs/foreshadow_registry.md`
- `docs/handoff/next_steps.md`

## 7. Key Cast for External Review

### 7.1 NC-0001 Kirion Renbaren

- [PUBLIC] 렌바렌 백작가 차남. 표면상 비서명귀족 백작가의 차남이다.
- [CONFIDENTIAL] 실제로는 비밀 서명귀족 가문의 차남이지만, 본인은 가문 비밀을 모른다.
- [META] 완전한 타인 빙의보다, 외부 표본의 지식/사고 구조가 덧입혀져 결국 `키리온 렌바렌`으로 수렴하는 존재로 설계되어 있다.
- [PUBLIC] 핵심 욕망 구조는 `평온 -> 부/성공 -> 증명` 체인이다.
- [PUBLIC] 전생 잔향은 커뮤니티 운영 감각, 정보 구조 집착, 개발자적 사고 습관의 형태로만 남아 있다.
- [PUBLIC] 장기적으로는 성목 LMM화와 각인광장 구축을 통해 권력의 방향을 뒤집을 인물이다.
- [PUBLIC] 현재는 야심가보다 생존형 관찰자에 가깝다.

### 7.2 Kallion Renbaren

- [PUBLIC] 아버지이자 감시자.
- [CONFIDENTIAL] 렌바렌의 실제 기밀과 권력 구조를 아는 핵심 인물이다.
- [PUBLIC] 직접 폭력보다 장기 관찰, 검증 장치, 정보 통제에 강하다.
- [PUBLIC] 현재 위협은 즉석 심문보다 독서 습관과 반응 패턴 추적으로 이동했다.

### 7.3 Celia Gravion

- [PUBLIC] 어머니. 주인공에게 유일한 무계산 온기를 제공하는 보호자 축이다.
- [PUBLIC] 다만 작품 기능상 완전한 안전지대가 되면 긴장이 죽으므로, "위험한 이완 장치"로 운용된다.
- [PUBLIC] 혼인 후 표기는 남편 성 추종이 아니라 `셀리아 그라비온`, 직위는 `렌바렌 백작부인`이다.

### 7.4 Derion and Liria

- [CONFIDENTIAL] 데리온 렌바렌은 10세 장남이며, 현재 식흔 후계자다.
- [CONFIDENTIAL] 그는 두 달 전 `계승조회식` 이후 가문 비밀과 장래의 방계 청소 의무를 전수받아 혼란 상태다.
- [PUBLIC] 독자 체감 목표는 "강압적 형 -> 계속 도움 되는 형 -> 트루 브라더" 전환이다.
- [CONFIDENTIAL] 리리아 렌바렌은 막내딸이며, 정식 계승자는 아니지만 그라비온 진위감정 혈통의 잔향이 남아 사람의 표정과 말결을 비정상적으로 잘 읽는다.
- [PUBLIC] 리리아는 장차 밝은 인싸 축이자 보호 대상, 그리고 데리온 재평가 장치로 작동할 예정이다.

source_of_truth:
- `world/live/population/core_cast/NC-0001_P-1027.md`
- `docs/handoff/next_steps.md`

## 8. Community / Platform Culture Model

### 8.1 Current Community Structure

- [PUBLIC] 이 작품은 고정 18보드 모델을 폐기했다.
- [PUBLIC] 게시판은 `concept_only -> registered -> stateful -> retired`의 동적 라이프사이클로 운영한다.
- [PUBLIC] 현재 live에서 활성 등록된 보드는 `BOARD-001 낙서장` 하나다.

### 8.2 Why BOARD-001 Matters

- [PUBLIC] `낙서장`은 주인공이 직접 관리하는 완전 익명 게시판이다.
- [PUBLIC] 상업성과 효율을 위해서가 아니라, 주인공의 취미와 정체성 때문에 유지되는 공간이다.
- [PUBLIC] 조력자들은 나중에 이 보드를 없애라고 압박하지만, 주인공은 포기하지 못한다.
- [PUBLIC] 이 갈등은 `합리적 플랫폼 경영자 vs 감성적 커뮤니티 덕후`라는 캐릭터 긴장을 만든다.

### 8.3 Layer B Grammar

- [PUBLIC] Layer B는 작가 투사 레이어다. 주인공이 전생에서 사랑했던 인터넷 커뮤니티 문법을 의도적으로 이식하는 계층이다.
- [PUBLIC] 실제 커뮤니티 사례를 `ATOM` 단위로 분해하고, 일정량 누적 후 `GRAMMAR` 규칙으로 합성한다.
- [PUBLIC] 현재는 `ATOM-001~011`과 `GRAMMAR-001~003` 초안이 쌓인 상태다.
- [PUBLIC] 이 문법은 각인광장 전체가 아니라 `낙서장` 단일 보드에만 적용된다.

### 8.4 External-Review Relevance

- 이 축은 단순 개그가 아니라 작품의 장기 테마와 직결된다.
- 주인공이 만들고 싶은 것은 중립적 정보 시스템이 아니라, 사람들의 문답 온도와 커뮤니티 자생성을 품는 플랫폼이다.
- 동시에 Layer B가 강해질수록 작품 톤 오염, 서사 몰입 분산, 한국 커뮤 로컬성 과잉 같은 리스크도 커진다.

source_of_truth:
- `world/live/docs/community_map.md`
- `world/live/docs/community_grammar_layer_b.md`

## 9. Main Constraints the External Advisor Should Understand

- 이 작품의 메인 긴장은 초반부터 세계 전체를 열지 않고, 매우 좁은 공간에서 정체 은폐와 감시를 쌓는 방식으로 출발한다.
- 학술원과 플랫폼 본편은 핵심이지만, 바로 들어가지 않는다.
- 전투력 성장보다 정보 인프라 성장, 권한 구조 재편, 공론장 발명 쪽이 더 중요하다.
- 주인공은 차가운 천재 CEO형보다 "생존형 관찰자 + 문제 풀기 좋아하는 장인"에 가깝다.
- 렌바렌 가문 설정은 강력하지만, 지나치게 빨리 다 까면 서사 압축이 깨질 수 있다.
- Layer B는 큰 개성이지만, 너무 전면화하면 세계관과 장르 톤을 잡아먹을 위험이 있다.

## 10. Questions for External Review

1. 현재 설정 기준으로, 저택 생존 파트에서 학술원 본편으로 넘어가는 pacing은 어떤 장면/정보를 더 준비해야 가장 자연스럽게 강해지는가.
2. 렌바렌의 비밀 서명귀족 설정, 방계 청소, 아동 수련 금지, 계승조회식 구조가 과밀하거나 과도하게 설명 의존적으로 느껴지는 지점이 있는가.
3. 주인공의 장기 테마인 "정보 인프라/공론장 창설"이 초반 저택 파트에서도 충분히 매력적으로 예고되고 있는가.
4. 칼리온-키리온-셀리아 삼각 구도는 현재 상태만으로도 긴장과 감정 이완의 균형이 잡혀 보이는가.
5. 하급 과정 3년 -> 15세 상급 과정 점프 구조가 독자 체감상 설득력 있게 이어지려면, 12세 파트에서 반드시 보여줘야 할 경험은 무엇인가.
6. `낙서장`과 Layer B 문법은 작품 전체의 독창성으로 보이는가, 아니면 톤 분산 리스크가 더 커 보이는가.
7. 문장비전, 정본, 열람권, 배지, 각인광장, 영상 슬롯 등 제도/용어 밀도가 높은데, 외부 독자 기준 어디가 가장 헷갈리기 쉬운가.
8. 이 설정 패키지에서 가장 강한 차별점과, 반대로 가장 취약하거나 과밀한 축은 각각 무엇인가.

## 11. Suggested Boundaries for the Advisor

- 이 브리핑에 대한 조언은 `설정 정합성`, `장기 서사 구조`, `도입부 설계`, `톤 관리`, `독자 이해도`에 집중하는 것이 좋다.
- 문체나 문장 레벨 평가는 본 문서만으로는 부정확할 수 있다.
- world_ops 절차나 실제 저장소 운영 체계에 대한 조언은 필요 없다.
- 캐논 재편 제안이 나오더라도 `world/live/` SSOT를 바로 바꾸기보다, 먼저 변경 단위로 분해해야 한다.

## 12. Source Map

### Primary

- `world/live/docs/world_bible_index_v2.md`
- `world/live/world_bible/WB-0002_loreops_canon_control.md`
- `world/live/world_bible/WB-0003_onepage_summary.md`
- `world/live/world_bible/WB-0005_magic_system.md`
- `world/live/world_bible/WB-0008_archive_plaza_overview.md`
- `world/live/world_bible/WB-0009_power_structure_factions.md`
- `world/live/world_bible/WB-0015_academy_bible.md`
- `world/live/world_bible/WB-0017_economy_resources.md`
- `world/live/world_bible/WB-0026_appendix_crest_arcana.md`

### Current-state supplements

- `world/live/docs/narrative_state.md`
- `world/live/docs/story_arcs.md`
- `world/live/docs/foreshadow_registry.md`
- `world/live/docs/community_map.md`
- `world/live/docs/community_grammar_layer_b.md`
- `world/live/docs/character_index_v2.md`
- `world/live/population/core_cast/NC-0001_P-1027.md`
- `docs/handoff/next_steps.md`
- `artifacts/writing/episodes/ep000_prologue/canon/README.md`
- `artifacts/writing/episodes/ep001/canon/README.md`
- `artifacts/writing/episodes/ep002/canon/README.md`

## Appendix A. What This File Intentionally Does Not Do

- world bible 원문 전체를 그대로 합치지 않는다.
- episode 원고 전문을 재수록하지 않는다.
- 시뮬레이션 smoke test 결과를 문화 정본처럼 다루지 않는다.
- world_ops 변경관리 절차를 외부 자문 문서 본문에 섞지 않는다.
- quarantine 문서를 활성 캐논처럼 끌어오지 않는다.

