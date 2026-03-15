# Phase 2 Report (Collision Scan)

- change_id: CR-20260315-002
- verdict: major

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0003_onepage_summary.md
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0006_irminsul_infra.md
  - world/live/world_bible/WB-0007_badge_network.md
  - world/live/world_bible/WB-0008_archive_plaza_overview.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0017_economy_resources.md
  - world/live/world_bible/WB-0019_platform_spec.md
  - world/live/world_bible/WB-0029_appendix_aptitude_signature_materials.md
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/story_arcs.md
  - docs/handoff/next_steps.md
  - 프라미시오_LMM_각색고도화본_v2.docx
  - 프라미시오_무대용_설정_통합정리.docx

## 2. 충돌 후보
- [x] 있음
- details:
  - 현재 active SSOT는 `LMM = 학습형 마나 모델 / 성목 인격 진화` 표현을 너무 이르게, 너무 직접적으로 노출한다.
  - `픽시 계약 = 픽시 군집 기반 공공 인프라 접속권`이라는 새 바닥 규칙과, LMM 청사진의 `주인공 특수 정령 계약`이 그대로는 충돌한다.
  - 현재 logline과 NC 카드에는 이미 `성목을 LMM으로 진화시킨다`는 결과 문장이 박혀 있어, 주인공 기연의 획득 구조와 성장 단계가 서사보다 먼저 확정된 상태다.
  - `WB-0008`, `WB-0019`는 플랫폼 스펙이 먼저 고정되어 있고, 주인공이 왜 그 플랫폼에 도달하는지 보여줄 `기연의 단계감`은 부족하다.
  - 새 바닥 설정에서 작가가 명시한 원칙은 `LMM 우선, 7색/학파 후행 조정`인데, 현재 live는 반대로 주변 체계가 LMM을 제약하는 형식으로 읽힌다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| `LMM`이 PUBLIC 문서에서 너무 직접적으로 `학습형 마나 모델`로 정의돼 있음 | `WB-0003`, `WB-0008`, `NC-0001`, 인덱스 | 작중 표면 명칭을 판타지식 용어로 재배치하고 `LMM`은 작가용/후행 학술용으로 후퇴 | LMM, 학습형 마나 모델, 성목 | open |
| 주인공 기연이 `광장 완성 결과물`처럼 보이고 초반 기연성이 약함 | `WB-0003`, `NC-0001`, `story_arcs`, `long_term` | `기연 획득 -> 광장 성장 -> LMM 심화` 순서로 재설계 | 기연, 그리모어, 광장 성장 | open |
| `픽시 계약 = 인프라 접속권`과 `주인공의 특수 정령 계약`이 그대로는 충돌 | `WB-0005`, `WB-0006`, `WB-0007`, `WB-0008`, `WB-0029` | 주인공 전용 계약을 공용 인프라 계약과 분리된 비표준/상위 계약으로 재정의 | 정령 계약, 픽시 계약, 노드, 성목 | open |
| 현재 구조는 플랫폼 스펙이 먼저 고정되고, 독자가 좋아할 단계형 기연 설계가 부족함 | `WB-0008`, `WB-0019`, `NC-0001` | `기연 단계표 -> 플랫폼 스펙` 순서로 의존성을 역전 | 그리모어, 성장 단계, 플랫폼 스펙 | open |
| `성목 화신` 등 후반 결과형 조력자 설정이 너무 일찍 확정됨 | `NC-0001` | 조력자/화신 설정은 LMM 성장 최종안 이후 재배치 | 성목 화신, 조력자 | open |
| `커뮤니티 = 파워 소스` 구조가 일부 문장에만 있고 시스템 설계로는 아직 약함 | `WB-0008`, `WB-0017`, `WB-0019`, `community_grammar_layer_b` | `광장 성장/오염이 기연 강약을 결정`하는 명시적 설계 표를 신설 | 커뮤니티, 광장, 보존권, 오염 | open |
| 새 바닥 기준상 `7색 체계`, `21학파`, `학술원 전공 구조`는 후행 조정 대상이어야 하나 현재는 LMM을 제약하는 배경처럼 읽힘 | `WB-0005`, `WB-0015`, `WB-0029`, `NC-0001` | LMM 설계 완료 후 이 체계들을 재배치하는 별도 패스 지정 | 7색 체계, 21학파, 보존각인학파 | open |

## 3. 누락 후보
- [x] 있음
- details:
  - 주인공이 초반에 `정확히 무엇을 얻는가`에 대한 명시적 설계 문서가 아직 없다.
  - `표면 명칭 / 작중 학술 명칭 / 작가용 약칭`을 분리하는 용어 문서가 없다.
  - `성장 단계표`, `획득 조건`, `전투 효용`, `대가`, `커뮤니티 연동`이 하나의 문서로 정리돼 있지 않다.
  - `LMM` 축이 `7색 체계`, `학파`, `학술원 전공`에 미칠 역방향 수정 범위를 정의한 문서가 없다.

## 4. 중복/불필요 정보 후보
- [x] 있음
- details:
  - `성목을 LMM으로 진화시켜 각인광장을 만든다`는 결과 문장이 `WB-0003`, `NC-0001`, 인덱스, 집필 프롬프트 계열에 중복돼 있다.
  - `패턴 학습 + 유지비 자동 배분 루프` 같은 내부 구현 문장이 PUBLIC 문서에 너무 직접적으로 반복된다.
  - `플랫폼 스펙`과 `주인공 기연 핵심`이 `WB-0008`, `WB-0019`, `NC-0001`에서 섞여 있다.

## 5. 판단 근거
- world_bible_index 참조:
  - `WB-0003`, `WB-0008`, `WB-0019`가 현재 LMM/광장 축의 PUBLIC 표면 설명을 소유한다.
  - `WB-0005`, `WB-0006`, `WB-0007`, `WB-0029`가 새 바닥 설정상 허용되는 마법/노드/정령/서명 구조를 규정한다.
- cross-reference 참조:
  - `NC-0001`, `long_term`, `story_arcs`, `next_steps`에 현재 주인공 기연의 장기 방향이 묶여 있다.
  - `프라미시오_LMM_각색고도화본_v2.docx`는 `그리모어 + 특수 정령 계약 + 광장 성장 + 의도 읽기` 축을 제안한다.
  - `프라미시오_무대용_설정_통합정리.docx`는 `특수 지형 노드`, `신격`, `정령군`, `서명`, `혈통`, `초월력`의 바닥 규칙을 제공한다.

## 6. 분기 결정
- branch: major
- reason:
  - 주인공의 핵심 기연, logline, 플랫폼 설계, 정령 계약, 성목/노드 활용, 학술원 장기선, 7색/학파 후행 조정까지 연결되는 코어 리빌드다.
  - `WB-0003`, `WB-0008`, `WB-0019`, `NC-0001` 같은 중심 문서가 직접 영향 범위에 들어가므로 minor로 처리할 수 없다.

## 7. 작가 승인
- approved: yes
- note:
  - 현재 단계의 승인 범위는 `대전제 고정 + major 판정 + 초기 충돌 지도 작성`까지다.
