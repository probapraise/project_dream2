# Change Request

- change_id: CR-20260316-001
- date: 2026-03-16
- requester: writer
- status: phase4_partial_sync_done
- source_of_truth:
  - primary:
    - world/live/docs/master_map.md
    - world/live/world_bible/WB-0005_magic_system.md
    - world/live/world_bible/WB-0015_academy_bible.md
    - world/live/world_bible/WB-0021_appendix_terms_aliases.md
    - world/live/world_bible/WB-0025_appendix_naming_constitution.md
    - world/live/world_bible/WB-0026_appendix_crest_arcana.md
    - world/live/world_bible/WB-0029_appendix_aptitude_signature_materials.md
    - world/live/population/profiles/current_term_snapshot_v1.yaml
  - secondary:
    - fantasy_magic_casebook.xlsx
    - docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md
    - docs/design/spec_sheet_v1.md
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- `fantasy_magic_casebook.xlsx`를 기준으로 기존 마법 체계를 상업적으로 다시 읽히게 재정렬한다.
- 기존 `7색 × 6형 × 3잔류`, `칠탑 21학파`, `42개 색별 표준 입문 6식`, `문장비전`, `보존각인학파`, 하급/상급 커리큘럼, 주인공 성장선은 유지한다.
- 문제는 메커니즘이 아니라 표면 네이밍과 독자 노출 문법이다. 현재 일부 학파명·주문명이 공학/물리 교과서처럼 읽혀, 장면과 감정 환기가 약하다.
- 리포트가 권장하는 `직관적 슬롯 문법`, `색별 감정/문화 레지스터`, `상태이상-콤보 법칙`, `비전투 활용의 전면화`를 현행 SSOT 위에 덧씌우는 오버홀을 진행한다.

## 2. 정제된 목표 (1문장)
기존 마법 체계의 기계 구조와 서사 자산은 보존하면서도, `학파명/주문명/색별 감정/교차색 콤보/독자용 슬롯 문법`을 상업적으로 다시 설계해 현행 SSOT와 생성 레이어까지 일관되게 갱신한다.

## 3. 변경 유형
- modify | retcon

## 4. 성공 기준 (DoD)
- [ ] 불가침 범위와 검증 방법(해시/라인 범위/무수정 파일)이 케이스 문서로 고정된다.
- [ ] 리포트 권장사항을 Dream2 제약 위로 번역한 `casebook alignment`가 문서화된다.
- [ ] 학파 리네임 대상, 보류 대상, 유지 대상을 분리한 매핑표와 주문 리네임 스켈레톤이 준비된다.
- [ ] 도감 정본, live world bible, population snapshot/scripts, generated population 레이어까지 전파 경로가 분리 설계된다.
- [ ] 불가침 블록, 괄호 표기, 보존각인학파, 문장비전, 주인공 성장선이 훼손되지 않는 검증 게이트가 준비된다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0012_core_conflict_arcs.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0021_appendix_terms_aliases.md
  - world/live/world_bible/WB-0025_appendix_naming_constitution.md
  - world/live/world_bible/WB-0029_appendix_aptitude_signature_materials.md
  - world/live/population/profiles/current_term_snapshot_v1.yaml
  - world/live/population/population_slots.csv
  - world/live/population/P-*.yaml
  - scripts/population/recompute_role_majors.py
  - scripts/population/audit_population_invariants.py
  - world/live/docs/world_bible_index_v2.md
- impacted_entities:
  - 열압포격학파
  - 용융형상학파
  - 결박제어학파
  - 좌표감리학파
  - 탄도관성학파
  - 자계유도학파
  - 군진선도학파
  - 교신전심학파
  - 생명고정학파
  - 서약집행학파
  - 단절추방학파
  - 색별 감정/문화 레지스터
  - 교차색 콤보 규칙
  - 독자용 슬롯 문법

## 6. 작가 확인 필요 항목
- Q1: 최종 학파명은 `장면/감각 우선` 원칙 아래 어느 정도까지 전통 한자어를 남길지 Phase 1에서 승인 필요.
- Q2: 주문명은 `기능어 + 시적어` 혼합을 허용하되, 완전 고유명사화로 읽기 어려워지는 선은 금지하는 가이드가 필요함.

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-16
- note:
  - 작가가 `fantasy_magic_casebook.xlsx` 기준의 오버홀 착수를 승인했다.
  - 현재 상태는 Phase 1 중앙 프레임워크(`독자용 슬롯 문법`, `교차색 콤보`, `마법/학파용 작명 가드레일`) 확정 작업까지 포함한다.
  - 2026-03-17 기준 적탑/청탑/녹탑/황탑 12학파는 live SSOT에 partial sync 완료. 자/백/흑탑과 전역 규칙은 후속 검토 후 반영 예정이다.
