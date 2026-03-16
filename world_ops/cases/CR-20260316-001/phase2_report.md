# Phase 2 Report (Collision Scan)

- change_id: CR-20260316-001
- verdict: major

## 1. 탐색 범위
- files:
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
  - world/live/docs/narrative_state.md
  - world/live/docs/story_arcs.md
  - world/live/docs/pre_academy_checkpoint_plan.md

## 2. 충돌 후보
- [ ] 없음
- details:
  - 리네임 후보 11학파 기준 현재 저장소 충돌 표면은 `1402`개 파일이며, 이 중 `1394`개가 generated layer인 `world/live/population/P-*.yaml`이다.
  - 따라서 `프로젝트 전체 grep 치환`은 금지하고, `도감 정본 -> live world bible -> snapshot/scripts -> generated population 재생성` 순서로 내려가야 한다.
  - 도감 정본 안에 불가침 블록과 수정 블록이 섞여 있다. 특히 `§0`, `§2`, `§3`, `§4`, `§6-15`, `§7`, `§8`은 해시 검증이 필요한 보호 구간이다.
  - 현재 도감 정본에는 이미 `§8 웹툰화·게임화 밸런스 메모`, `§9 결론`이 있다. 신규 콤보/독자 노출 문법 섹션을 추가하면 재번호 정책을 같이 잡아야 한다.
  - [WB-0015](/home/dlwhdgus/project_dream2/world/live/world_bible/WB-0015_academy_bible.md)는 21학파 요약과 학생 예시를 동시에 가진 최상위 live 요약 문서라서, 도감 정본보다 독자 노출 위험이 높다.
  - [WB-0021](/home/dlwhdgus/project_dream2/world/live/world_bible/WB-0021_appendix_terms_aliases.md)는 구명 보존 창구로 유지되어야 하므로, `구 학파명 0건` 검증 범위에서 제외해야 한다.
  - 주인공 성장선 관련 문서(`narrative_state`, `story_arcs`, `pre_academy_checkpoint_plan`)는 이번 케이스에서 읽기 전용이다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 학파명/주문명 상업화가 도감 정본과 live 요약 문서 양쪽에 동시에 걸려 있음 | 도감 정본, WB-0005, WB-0015, WB-0012 | 도감 정본을 1차 SSOT로 수정한 뒤 live 요약문서를 후행 동기화 | 21학파, 주문명, 색별 감정 | open |
| generated population 레이어가 blast radius 대부분을 차지함 | `population_slots.csv`, `P-*.yaml`, snapshot, scripts | 직접 치환 금지, snapshot/scripts 수정 후 재생성 | 1402 files, 1394 yaml | open |
| 절대 불가침 블록이 동일 파일 내부에 섞여 있어 무차별 편집이 불가 | 도감 정본 §0/§2/§3/§4/§6-15/§7/§8 | 라인 범위 해시와 보호 체크리스트를 먼저 고정 | 표준식, 보존각인학파, 문장비전 | open |
| 케이스북 권장 `4~6 학교` 구조를 현행 21학파에 그대로 적용할 수 없음 | 7색 체계, 21학파 체계 | `7색 = 표면 온보딩`, `21학파 = 중층 전문화`로 번역 | casebook alignment | open |
| 신규 콤보 섹션 삽입 시 기존 섹션 번호가 밀림 | 도감 정본 §8~§9 | 신규 §8 도입 시 기존 §8 -> §9, 기존 §9 -> §10으로 재번호 | 콤보 규칙, 웹툰화 메모, 결론 | open |
| 구명 보존이 필요한 문서와 제거해야 할 문서가 섞여 있음 | alias 문서, closed cases, active SSOT | `active SSOT only zero-old-name` 정책으로 분리 | WB-0021, history, case docs | open |
| 색별 감정/문화 시트를 어디에 canonize할지 아직 정하지 않음 | WB-0005, WB-0029, 도감 정본 | 정본 세부는 도감/ WB-0029, WB-0005는 요약만 유지 | 색별 감정/문화 레지스터 | open |

## 3. 누락 후보
- [ ] 없음
- details:
  - 케이스북 권장사항을 Dream2 제약 위로 번역하는 별도 문서가 없어, 단순 리네임으로 작업이 축소될 위험이 있다.
  - 12전승을 `독자용 슬롯 문법`으로 다시 태깅하는 중앙 문서가 아직 없다.
  - 색별 감정/문화 레지스터와 교차색 콤보 규칙이 현재 live SSOT 어디에도 명시되어 있지 않다.
  - [WB-0025](/home/dlwhdgus/project_dream2/world/live/world_bible/WB-0025_appendix_naming_constitution.md)에 마법/학파용 상업 네이밍 규칙이 아직 없다.

## 4. 중복/불필요 정보 후보
- [ ] 없음
- details:
  - generated population 레이어의 학파명은 canonical prose가 아니라 재생성 가능한 산출물이다. `P-*.yaml` 직접 치환보다 source profile과 script를 수정하는 것이 맞다.
  - 구 학파명은 alias 문서와 historical case에서는 남아도 되며, 이를 강제로 지우는 것은 변경 이력 보존 측면에서 불필요하다.

## 5. 판단 근거
- world_bible_index 참조:
  - `WB-0005`, `WB-0015`, `WB-0021`, `WB-0025`, `WB-0029`가 모두 live bundle 참조축으로 연결되어 있다.
- cross-reference 참조:
  - `fantasy_magic_casebook.xlsx`
  - `world_ops/cases/CR-20260316-001/phase0_casebook_alignment.md`
  - `world_ops/cases/CR-20260316-001/phase0_impact_scan.md`
  - `world_ops/cases/CR-20260316-001/phase0_immutable_checklist.md`

## 6. 분기 결정
- branch: major
- reason:
  - 리네임만 해도 도감 정본, live world bible, naming constitution, population profile, generation scripts, generated population 전체에 걸친다.
  - 보호 블록 해시 검증, alias 정책, generated layer 재생성, 작가 승인 루프가 모두 필요하다.
  - 따라서 이 케이스는 `큰 설계 변경 + 다계층 전파 + 생성 레이어 재생성`이 결합된 major change로 처리한다.

## 7. 작가 승인
- approved: yes
- note:
  - 작가가 오버홀 착수를 승인했다.
  - 현재 승인 범위는 Phase 0 준비 문서와 영향 범위 고정까지다.
