# Change Request

- change_id: CR-20260315-002
- date: 2026-03-15
- requester: writer
- status: draft
- source_of_truth:
  - primary:
    - world/live/docs/master_map.md
    - world/live/world_bible/WB-0003_onepage_summary.md
    - world/live/world_bible/WB-0005_magic_system.md
    - world/live/world_bible/WB-0006_irminsul_infra.md
    - world/live/world_bible/WB-0007_badge_network.md
    - world/live/world_bible/WB-0008_archive_plaza_overview.md
    - world/live/world_bible/WB-0019_platform_spec.md
    - world/live/world_bible/WB-0029_appendix_aptitude_signature_materials.md
    - world/live/population/core_cast/NC-0001_P-1027.md
  - secondary:
    - 프라미시오_LMM_각색고도화본_v2.docx
    - 프라미시오_무대용_설정_통합정리.docx
    - docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 밑바닥 공사를 마친 뒤, 주인공의 핵심 기연에 해당하는 `LMM` 관련 설정을 새 바닥 설정 위에서 처음부터 다시 설계한다.
- 작업 방식은 `문서를 남기며 신중하게 진행`하는 것으로 고정한다.
- 작가가 승인한 대전제는 아래 두 가지다.
  - 1) 밑바닥 설정에 위배되지 않게 처음부터 다시 설계한다.
  - 2) 웹소설의 핵심 재미인 주인공의 기연에 해당하는 부분이므로 `LMM` 관련 설정을 최우선으로 품질 높게 설계하고, 필요하면 `7색 체계`, `21학파` 등 기존 주변 설정은 그에 맞춰 변형/수정할 각오를 한다.

## 2. 정제된 목표 (1문장)
새 바닥 설정을 침범하지 않으면서도 웹소설적 기연으로서 강하게 작동하는 `주인공의 LMM/그리모어/광장 성장` 축을 처음부터 재설계하고, 그 결과를 기준으로 주변 마법 체계와 학파 구조까지 재정렬할 준비를 끝낸다.

## 3. 변경 유형
- modify | retcon

## 4. 성공 기준 (DoD)
- [ ] LMM 재설계의 대전제, 비타협 원칙, 작업 순서가 케이스 문서에 명시된다.
- [ ] 현재 active SSOT에서 LMM 축과 충돌하는 문장/구조가 문서 단위로 식별된다.
- [ ] live 문서 반영 전에 `표면 용어`, `기연 획득 구조`, `성장 단계`, `전투/정치 효용`, `커뮤니티 연동`의 설계 순서가 확정된다.
- [ ] `7색 체계`, `21학파`, `학술원 전공 구조`는 LMM 재설계에 종속된 후행 조정 대상으로 명시된다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0003_onepage_summary.md
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0006_irminsul_infra.md
  - world/live/world_bible/WB-0007_badge_network.md
  - world/live/world_bible/WB-0008_archive_plaza_overview.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0019_platform_spec.md
  - world/live/world_bible/WB-0029_appendix_aptitude_signature_materials.md
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/story_arcs.md
  - world/live/docs/world_bible_index_v2.md
  - docs/handoff/next_steps.md
- impacted_entities:
  - 키리온 렌바렌
  - 각인광장
  - 백지의 그리모어(가칭)
  - 성목 / 특수 지형 노드
  - 정령 계약
  - 픽시 계약(구 live 명칭: 하급 정령 계약)
  - 보존각인학파
  - 7색 체계
  - 21학파(후행 조정 후보)

## 6. 작가 확인 필요 항목
- Q1: 공용 인프라용 정령 접속 마법의 표면 명칭은 `픽시 계약`으로 고정한다. 작가용 구조로는 `픽시군 표준 저위 계약`으로 이해한다.
- Q2: 작중 표면에서는 `LMM`이라는 말을 거의 쓰지 않고, `그리모어 / 광장 / 감각 / 정령 계약` 중심 용어로 갈지 여부

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-15
- note:
  - 대전제 2개는 작가가 직접 승인했다.
  - 현재 단계는 `live 수정 전 설계 헌법과 충돌 지도 고정`까지를 목표로 한다.
