# Magic System 3.1 Conflict Audit

기준 소스: `/home/dlwhdgus/project_dream2/docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md`

작성 목적:
- `프라미시오 마법 도감 3.1` 기준으로 현재 저장소의 semantic collision을 식별한다.
- 즉시 갈아엎어야 하는 SSOT와, 이름만 정리하면 되는 파생 문서를 분리한다.
- `각인`이 더 이상 형 이름이 아니라는 점이 어떤 층위에 영향을 주는지 고정한다.

## 이번 감사의 기준 규칙

1. 정형화 마법의 전면 분류는 `색 × 형 × 잔류`다.
2. 형은 `사출 / 전개 / 피복 / 기동 / 표식 / 탐지` 6형만 쓴다.
3. `복원`, `판독`은 형이 아니라 태그다.
4. `각인`은 형 이름이 아니라 기술명·학파명·전통어로만 남길 수 있다.
5. 보존각인학파는 `기억 조작`보다 `표식 + 탐지 기반 아카이빙` 학파로 읽는다.
6. 상급 과정 마법사 학파 기준은 21학파다.

## 그대로 유지 가능한 용례

아래는 이번 개정과 직접 충돌하지 않는다.

- `각인광장`: 플랫폼 고유명사이므로 유지 가능
- `마나사인`, `연장각인`, `발췌각인`, `영상 각인`: 기술명/서비스명/전통어로 유지 가능
- `문장비전`, `문장`, `인장`, `봉문`: 형 이름이 아니라 제도·기술·객체 설명이면 유지 가능

주의:
- 위 용례도 주문 분류나 학파 설명을 할 때는 반드시 `표식` 또는 `탐지`로 재해석해야 한다.
- 즉, 이름은 남길 수 있지만 분류 체계의 축으로 쓰면 안 된다.

## Critical

### 1. `WB-0005_magic_system.md`는 마법 시스템 SSOT로서 사실상 폐기 수준의 충돌이 있다

- 파일: `world/live/world_bible/WB-0005_magic_system.md`
- 핵심 충돌:
  - `표준식 코어 12식`을 `원소 / 강화 / 방어 / 치유 / 해독 / 감지` 축으로 설명한다.
  - `감지`를 별도 범주로 쓰고, `잔흔분석`을 core spell 범주로 묶는다.
  - `색 × 형 × 잔류`와 6형 체계가 전혀 반영되지 않았다.
- 근거 라인:
  - `WB-0005_magic_system.md:60-81`
  - `WB-0005_magic_system.md:87-206`
  - `WB-0005_magic_system.md:202-208`
- 영향:
  - 이 문서가 살아 있는 한, 다른 문서를 무엇으로 바꿔도 마법 체계 SSOT가 서로 충돌한다.
- 권장 조치:
  - `WB-0005`는 부분 수정이 아니라 `마법 도감 3.1` 기준 재작성 또는 대체가 맞다.

### 2. `WB-0015_academy_bible.md`는 학제/학파/주인공 전공선이 대량 충돌한다

- 파일: `world/live/world_bible/WB-0015_academy_bible.md`
- 핵심 충돌:
  - 마법사 전공이 `10개 학부/학과` 체계로 고정되어 있다.
  - `각인학파`를 주인공 학파로 두고 있다.
  - `전장연산학파` 등 구 학파명이 남아 있다.
  - `학술원 협력 교수 2(각인술·전심술)` 및 `각인술 교수` 명칭이 구 체계에 묶여 있다.
  - `24개` 내외 학파 구조를 전제로 작성돼 있다.
- 근거 라인:
  - `WB-0015_academy_bible.md:114-124`
  - `WB-0015_academy_bible.md:154`
  - `WB-0015_academy_bible.md:159-166`
  - `WB-0015_academy_bible.md:280-348`
  - `WB-0015_academy_bible.md:339-348`
- 영향:
  - 새 정본의 하급 3년 커리큘럼, 상급 21학파, 보존각인학파 재정의가 전부 여기서 다시 깨진다.
- 권장 조치:
  - `13.4`, `13.5`, 자탑/황탑/백탑/흑탑 세부 파트를 우선 재작성.

### 3. 주인공 전공 정보가 population SSOT와 core cast에서 구 체계로 고정돼 있다

- 파일:
  - `world/live/population/P-1027.yaml`
  - `world/live/population/population_slots.csv`
  - `world/live/population/core_cast/NC-0001_P-1027.md`
- 핵심 충돌:
  - `major: 각인학파`
  - `각인학파 유일 주전공자`
  - `15세 ... 입학 즉시 각인술을 골라`
- 근거 라인:
  - `P-1027.yaml:7`
  - `population_slots.csv:1028`
  - `NC-0001_P-1027.md:78`
  - `NC-0001_P-1027.md:123-124`
- 영향:
  - 주인공 장기 아크와 학술원 진입선이 새 정본과 다른 전공명으로 고정된다.
- 권장 조치:
  - `각인학파`를 `보존각인학파`로 바꿀지, 혹은 더 좁은 세부 전공 표현을 둘지 먼저 정책 결정 필요.

## High

### 4. `WB-0004_world_common_sense.md`는 내용 골격은 맞지만 용어 프레이밍이 구형이다

- 파일: `world/live/world_bible/WB-0004_world_common_sense.md`
- 핵심 충돌:
  - `연장각인`, `보존각인 산업`, `각인술 학파`를 old framing으로 설명한다.
  - 새 정본의 `표식/탐지 기반 아카이빙` 설명이 빠져 있다.
- 근거 라인:
  - `WB-0004_world_common_sense.md:22-26`
- 영향:
  - 상식 문서가 여전히 “각인술 붐 -> 학파 붕괴” 서사만 유지해, 새 학파 재정의가 약하게 읽힌다.
- 권장 조치:
  - `보존각인학파` 명칭과 `표식/탐지` 재해석을 넣되, `마나사인/연장각인` 기술명은 유지.

### 5. `WB-0017_economy_resources.md`는 산업 서사가 새 정본과 절반만 맞는다

- 파일: `world/live/world_bible/WB-0017_economy_resources.md`
- 핵심 충돌:
  - `보존각인 산업`, `각인술 업계`, `왕립학술원 각인학파` 서술이 남아 있다.
  - 새 정본의 핵심인 `희소한 영역 = 영상 각인 / 해시·위변조 탐지 / 대규모 색인 / 봉문 / 오염 환경 판독`은 이미 일부 맞지만, 학파명과 설명 프레임이 구형이다.
- 근거 라인:
  - `WB-0017_economy_resources.md:18-27`
  - `WB-0017_economy_resources.md:80-84`
- 영향:
  - 경제 엔진은 유지 가능하지만, 주인공이 왜 `보존각인학파`를 다시 가치 있게 만드는지 설명 층이 어긋난다.
- 권장 조치:
  - `각인학파` 표현을 정리하고, 희소 기술을 `표식/탐지 기반 아카이브 실무`로 재서술.

### 6. `WB-0013_timeline_event_engine.md`도 old 산업명에 묶여 있다

- 파일: `world/live/world_bible/WB-0013_timeline_event_engine.md`
- 핵심 충돌:
  - `보존각인 사업`이라는 old naming이 남아 있다.
- 근거 라인:
  - `WB-0013_timeline_event_engine.md:12-18`
- 영향:
  - 연표의 사건 이름은 유지 가능하지만, 배경 산업 설명은 새 정본 기준으로 한 번 정리해야 한다.

### 7. naming/handoff 문서에 구 전공명이 남아 있다

- 파일:
  - `world/live/world_bible/WB-0025_appendix_naming_constitution.md`
  - `docs/handoff/next_steps.md`
- 핵심 충돌:
  - `미렌 (각인학파 견습/천재 ...)`
  - `각인술 선택 클리프행어`, `각인광장 구현에 필요한 ... 각인술`
- 근거 라인:
  - `WB-0025_appendix_naming_constitution.md:42`
  - `next_steps.md:60-61`
  - `next_steps.md:169-170`
- 영향:
  - 차기 기획 문서가 다시 old naming으로 회귀할 수 있다.

## Medium

### 8. `WB-0026_appendix_crest_arcana.md`는 대체로 살릴 수 있지만 표기 원칙 정리가 필요하다

- 파일: `world/live/world_bible/WB-0026_appendix_crest_arcana.md`
- 핵심 관찰:
  - 문장비전 자체는 새 정본과 공존 가능하다.
  - 다만 일부 설명에서 `표식`, `탐지`, `판독`, `약점탐지`가 혼용되고 있어, 문장비전도 `색 하나, 형 하나, 잔류 하나, 태그 최대 셋` 원칙에 맞게 presentation을 맞춰야 한다.
  - `보존각인`이라는 old 기술명도 일부 남아 있다.
- 근거 라인:
  - `WB-0026_appendix_crest_arcana.md:147`
  - `WB-0026_appendix_crest_arcana.md:164-170`
  - `WB-0026_appendix_crest_arcana.md:196-198`
  - `WB-0026_appendix_crest_arcana.md:414`
- 영향:
  - 치명적 충돌은 아니지만, 문장법 3.1을 이미 따르는 새 정본과 presentation layer가 달라질 수 있다.

### 9. `WB-0018_evidence_records_glossary.md`는 이름은 유지 가능하지만 메타 주석이 있으면 좋다

- 파일: `world/live/world_bible/WB-0018_evidence_records_glossary.md`
- 핵심 관찰:
  - `발췌각인`, `영상 각인`은 그대로 기술명으로 유지 가능하다.
  - 다만 독자가 이걸 형 이름으로 오해하지 않도록, legacy naming임을 한 줄 적는 편이 안전하다.
- 근거 라인:
  - `WB-0018_evidence_records_glossary.md:12-28`

### 10. 집필 프롬프트/브리핑에는 미래 전공명 drift가 남아 있다

- 파일:
  - `artifacts/writing/episodes/ep000_prologue/prompt_v1.md`
  - `artifacts/writing/episodes/ep001/prompt_v1.md`
  - `artifacts/writing/episodes/ep001/prompt_v2.md`
  - `artifacts/briefings/external_review/world_snapshot_external_review_20260310.md`
- 핵심 충돌:
  - 구 로그라인과 미래 전공명, `각인술 교수`, `각인학파` 기반 설명이 일부 남아 있다.
- 영향:
  - 기록성 산출물이라 우선순위는 낮지만, 재사용 시 old setting을 다시 주입할 수 있다.

## False Positive / 바로 건드릴 필요 없는 것

아래는 `각인`이 들어가도 이번 개정과 직접 충돌하지 않는 층이다.

- `각인광장` 플랫폼 관련 문서 전반
- `발췌각인`, `영상 각인`, `연장각인`, `마나사인`
- 문장비전 도상/인장/봉문/표식석 같은 객체명
- legacy/history 로그

즉, 검색 결과에서 `각인`이 많이 나온다고 전부 충돌 문서는 아니다.

## 우선 수정 순서

1. `WB-0005_magic_system.md`
2. `WB-0015_academy_bible.md`
3. `P-1027.yaml`, `population_slots.csv`, `NC-0001_P-1027.md`
4. `WB-0004_world_common_sense.md`
5. `WB-0017_economy_resources.md`
6. `WB-0013_timeline_event_engine.md`
7. `WB-0025_appendix_naming_constitution.md`, `next_steps.md`
8. 이후 writing prompts / external briefings 백필

## 권장 반영 정책

### 정책 A. `각인`의 허용 범위를 먼저 문장으로 못 박기

권장 문구:

- `각인`은 더 이상 정형화 마법의 형 이름이 아니다.
- 다만 `마나사인`, `연장각인`, `발췌각인`, `영상 각인`, `각인광장`, `보존각인학파` 같은 고유 기술명·전통어·기관명에는 남길 수 있다.
- 실제 분류 설명에서는 항상 `표식` 또는 `탐지`로 재해석한다.

### 정책 B. 주인공 전공명은 빠르게 고정

선결 질문:

- 주인공의 전공명을 공식적으로 `보존각인학파`로 바꿀 것인가
- 아니면 `보존각인학파` 내부 세부 트랙을 별도 명칭으로 둘 것인가

이 결정이 늦어지면 `WB-0015`, `P-1027`, `next_steps`, future prompt 전부가 함께 흔들린다.

### 정책 C. `WB-0005`는 diff 수정이 아니라 재작성으로 다루기

이 문서는 old classification이 너무 깊게 박혀 있어서 부분 수정보다 교체가 안전하다.

## 결론

이번 개정의 진짜 충격점은 `각인`이라는 단어 자체가 아니라, 다음 세 가지다.

1. 마법 분류 SSOT가 `색 × 형 × 잔류`로 완전히 재정렬된다.
2. 학술원 상급 과정의 학파 구조와 이름이 크게 바뀐다.
3. 주인공의 장래 전공 서사가 `각인학파` 기준에서 다시 고정돼 있던 문서들을 전부 흔든다.

따라서 1차 반영은 `WB-0005 -> WB-0015 -> P-1027 축`으로 잡는 것이 가장 안전하다.
