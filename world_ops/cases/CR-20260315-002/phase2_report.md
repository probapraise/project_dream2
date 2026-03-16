# Phase 2 Report (Collision Scan)

- change_id: CR-20260315-002
- verdict: major
- note:
  - 아래 표의 `status`는 `live SSOT 반영 여부`가 아니라 `케이스 설계 차원에서 답이 고정됐는지`를 뜻한다.
  - 즉 `resolved`는 설계 원칙과 산출물 기준이 확정됐다는 뜻이며, live 문서 재작성은 별도 Phase 3/4 작업이다.

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
- case_docs_used_for_resolution:
  - world_ops/cases/CR-20260315-002/design_constitution.md
  - world_ops/cases/CR-20260315-002/growth_architecture_split.md
  - world_ops/cases/CR-20260315-002/community_runtime_architecture.md
  - world_ops/cases/CR-20260315-002/irminsul_contract_ladder.md
  - world_ops/cases/CR-20260315-002/community_unlock_blueprint.md
  - world_ops/cases/CR-20260315-002/lmm_advancement_design.md
  - world_ops/cases/CR-20260315-002/runtime_interface_contract.md
  - world_ops/cases/CR-20260315-002/runtime_governance_state_machine.md
  - world_ops/cases/CR-20260315-002/utility_payoff_matrix.md

## 2. 충돌 후보
- [x] 있음
- details:
  - 현재 active SSOT는 `LMM = 학습형 마나 모델 / 성목 인격 진화` 표현을 너무 이르게, 너무 직접적으로 노출한다.
  - 초기 설계 문서 일부는 `주인공의 특수 정령 계약`을 따로 상정했지만, 최신 합의는 `픽시 계약만 정식 계약`, 그 위는 `동행 / 감리 / 협약 / 공명`이다.
  - live 문서에는 아직 `비공식 운용 -> 감리 허가 -> 시범 운영 -> 드리아드 협약` 상태 기계가 없어서, 공용화가 결과물처럼 읽히고 중간 단계가 사라져 있다.
  - `WB-0008`, `WB-0019`는 플랫폼 스펙이 먼저 고정돼 있고, `그리모어 -> 공용 런타임 -> LMM` 순서의 인터페이스 경계가 빠져 있다.
  - `전투 / 협상 / 정치 / 커뮤니티` 효용은 설계 헌법에서 요구되지만, 기존 live는 전술 정보 공유 외의 보상 구조가 충분히 명시돼 있지 않다.
  - 새 바닥 설정에서 작가가 명시한 원칙은 `LMM 우선, 7색/학파 후행 조정`인데, 현재 live는 반대로 주변 체계가 LMM을 제약하는 형식으로 읽힌다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | status |
|---|---|---|---|---|
| `LMM`이 PUBLIC 문서에서 너무 직접적으로 `학습형 마나 모델`로 정의돼 있음 | `WB-0003`, `WB-0008`, `NC-0001`, 인덱스 | 작중 표면 명칭을 판타지식 용어로 재배치하고 `LMM`은 작가용/후행 학술용으로 후퇴 | LMM, 학습형 마나 모델, 성목 | open |
| 주인공 기연이 `광장 완성 결과물`처럼 보이고 초반 기연성이 약함 | `WB-0003`, `NC-0001`, `story_arcs`, `long_term` | `색인 -> 주석 -> 실타래` 3단계와 이후 `요정/드리아드/성목` 연계 사다리로 재구성 | 기연, 그리모어, 광장 성장 | resolved |
| `픽시 계약 = 인프라 접속권`과 `주인공의 특수 정령 계약`이 그대로는 충돌 | `WB-0005`, `WB-0006`, `WB-0007`, `WB-0008`, `WB-0029` | 정식 계약은 `픽시 계약`만 유지하고, 상위 단계는 `요정 동행 / 드리아드 감리·협약 / 성목 공명`으로 재정의 | 정령 계약, 픽시 계약, 성목 | resolved |
| 공용화 중간 단계가 없어 곧바로 `플랫폼 완성`처럼 읽힘 | `WB-0008`, `WB-0019`, `NC-0001`, `story_arcs` | `비공식 운용 -> 감리 허가 -> 시범 운영 -> 드리아드 협약` 상태 기계를 명시 | 감리 허가, 시범 운영, 드리아드 협약 | resolved |
| 플랫폼 스펙이 기연 단계표보다 먼저 고정됨 | `WB-0008`, `WB-0019`, `NC-0001` | `성장 단계표 -> 인터페이스 계약 -> 거버넌스 -> 플랫폼 스펙` 순서로 의존성을 역전 | 그리모어, 성장 단계, 플랫폼 스펙 | resolved |
| `그리모어 / 성목 분지 / 배지`의 입력 계층과 필드 권한이 섞여 있음 | `WB-0007`, `WB-0008`, `WB-0019`, `NC-0001`, `WB-0029` | `runtime_interface_contract.md` 기준으로 공용 표면, 관리자 필드, 루트 필드를 분리 | 관리자 콘솔, 공용 런타임, 사용자 단말 | resolved |
| `성목 신격 = AI 본체`처럼 읽히는 문장이 후반 조력자/화신 설정과 충돌 | `WB-0003`, `NC-0001`, `story_arcs` | `LMM 코어`와 `성목 신격`을 분리해, 신격은 정렬자이자 독립 캐릭터로 재배치 | 잠든 신, 신격, 아바타, 정렬 | resolved |
| `커뮤니티 = 파워 소스` 구조가 일부 문장에만 있고 효용표가 약함 | `WB-0008`, `WB-0017`, `WB-0019`, `NC-0001` | `utility_payoff_matrix.md`로 전투/협상/정치/커뮤니티 보상과 상한을 단계별 고정 | 커뮤니티, 파워 소스, 효용, 비용 | resolved |
| 새 바닥 기준상 `7색 체계`, `21학파`, `학술원 전공 구조`는 후행 조정 대상이어야 하나 현재는 LMM을 제약하는 배경처럼 읽힘 | `WB-0005`, `WB-0015`, `WB-0029`, `NC-0001` | LMM/광장 live 재작성 이후 별도 패스로 후행 재배치 | 7색 체계, 21학파, 보존각인학파 | open |

## 3. 누락 후보
- [x] 있음
- details:
  - 이전 누락이던 `공용 문법 vs 그리모어 전용 확장`은 `runtime_interface_contract.md`로 보강됐다.
  - 이전 누락이던 `감리 허가 -> 시범 운영 -> 협약` 중간 상태는 `runtime_governance_state_machine.md`로 보강됐다.
  - 이전 누락이던 `전투 / 협상 / 정치 / 커뮤니티` 효용표는 `utility_payoff_matrix.md`로 보강됐다.
  - 다만 최종 `표면 명칭 매핑`, `live 재작성 순서`, `학술원 타임라인 매핑`, `7색/21학파 후행 조정 패킷`은 아직 별도 정리 문서가 더 필요하다.

## 4. 중복/불필요 정보 후보
- [x] 있음
- details:
  - `성목을 LMM으로 진화시켜 각인광장을 만든다`는 결과 문장이 `WB-0003`, `NC-0001`, 인덱스, 집필 프롬프트 계열에 중복돼 있다.
  - `패턴 학습 + 유지비 자동 배분 루프` 같은 내부 구현 문장이 PUBLIC 문서에 너무 직접적으로 반복된다.
  - `플랫폼 스펙`, `공용 문법`, `주인공 기연 핵심`이 `WB-0008`, `WB-0019`, `NC-0001`에서 섞여 있다.
  - `성목 신격`, `수심에 굳은 패턴`, `그리모어 루트 접근`의 층위가 분리되지 않은 채 한 문단에서 섞인 표현이 남아 있을 가능성이 높다.

## 5. 판단 근거
- world_bible_index 참조:
  - `WB-0003`, `WB-0008`, `WB-0019`가 현재 LMM/광장 축의 PUBLIC 표면 설명을 소유한다.
  - `WB-0005`, `WB-0006`, `WB-0007`, `WB-0029`가 새 바닥 설정상 허용되는 마법/노드/정령/서명 구조를 규정한다.
- cross-reference 참조:
  - `NC-0001`, `long_term`, `story_arcs`, `next_steps`에 현재 주인공 기연의 장기 방향이 묶여 있다.
  - `community_unlock_blueprint.md`가 Track B의 단계별 해금 논리를 제공한다.
  - `lmm_advancement_design.md`가 `시드 -> 성목 성장 -> 정신 서명 -> 의도 색인` 후반부 구조를 제공한다.
  - `runtime_interface_contract.md`, `runtime_governance_state_machine.md`, `utility_payoff_matrix.md`가 이번 라운드에서 프로세스 빈칸을 메우는 보조 문서다.

## 6. 분기 결정
- branch: major
- reason:
  - 주인공의 핵심 기연, logline, 플랫폼 설계, 정령 계약, 성목/노드 활용, 학술원 장기선, 7색/학파 후행 조정까지 연결되는 코어 리빌드다.
  - `WB-0003`, `WB-0008`, `WB-0019`, `NC-0001` 같은 중심 문서가 직접 영향 범위에 들어가므로 minor로 처리할 수 없다.

## 7. 작가 승인
- approved: yes
- note:
  - 현재 단계의 승인 범위는 `케이스 설계 문서 정합화`까지다.
  - live SSOT 반영과 인덱스 동기화는 아직 시작하지 않았다.
