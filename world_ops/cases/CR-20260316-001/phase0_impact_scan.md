# Phase 0 Impact Scan

## 요약
- 리네임 1차 대상 11학파 기준 현재 충돌 파일 수는 `1402`개다.
- 이 중 `1394`개가 `world/live/population/P-*.yaml`이라서, 이번 케이스의 실질 난점은 prose보다 generated layer 관리다.
- active direct source는 `도감 정본 1`, `world_bible 3`, `population profile 1`, `population scripts 2`, `population csv 1`로 압축된다.

## 대상 학파별 분포

| term | total_files | total_occurrences | design_magic_system | world_bible | population_yaml | population_profile | scripts_population | other_live_docs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 열압포격학파 | 239 | 474 | 2 | 3 | 467 | 1 | 2 | 0 |
| 용융형상학파 | 99 | 195 | 2 | 4 | 187 | 1 | 2 | 0 |
| 결박제어학파 | 216 | 427 | 2 | 2 | 421 | 1 | 2 | 0 |
| 좌표감리학파 | 23 | 44 | 2 | 5 | 35 | 1 | 2 | 0 |
| 탄도관성학파 | 229 | 454 | 2 | 3 | 447 | 1 | 2 | 0 |
| 자계유도학파 | 101 | 202 | 2 | 7 | 191 | 1 | 2 | 0 |
| 군진선도학파 | 101 | 197 | 3 | 3 | 189 | 1 | 2 | 0 |
| 교신전심학파 | 186 | 370 | 2 | 7 | 359 | 1 | 2 | 0 |
| 생명고정학파 | 244 | 483 | 2 | 2 | 477 | 1 | 2 | 0 |
| 서약집행학파 | 19 | 33 | 3 | 3 | 25 | 1 | 2 | 0 |
| 단절추방학파 | 6 | 9 | 3 | 3 | 1 | 1 | 2 | 0 |

## 직접 수정 레이어

| file | targeted_occurrences | targeted_terms |
|---|---:|---|
| docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | 25 | 열압포격학파 (2), 용융형상학파 (2), 결박제어학파 (2), 좌표감리학파 (2), 탄도관성학파 (2), 자계유도학파 (2), 군진선도학파 (3), 교신전심학파 (2), 생명고정학파 (2), 서약집행학파 (3), 단절추방학파 (3) |
| world/live/world_bible/WB-0015_academy_bible.md | 38 | 열압포격학파 (3), 용융형상학파 (4), 결박제어학파 (2), 좌표감리학파 (5), 탄도관성학파 (3), 자계유도학파 (7), 군진선도학파 (2), 교신전심학파 (6), 생명고정학파 (2), 서약집행학파 (2), 단절추방학파 (2) |
| world/live/world_bible/WB-0012_core_conflict_arcs.md | 1 | 교신전심학파 (1) |
| world/live/world_bible/WB-0021_appendix_terms_aliases.md | 3 | 군진선도학파 (1), 서약집행학파 (1), 단절추방학파 (1) |
| world/live/population/profiles/current_term_snapshot_v1.yaml | 11 | 열압포격학파 (1), 용융형상학파 (1), 결박제어학파 (1), 좌표감리학파 (1), 탄도관성학파 (1), 자계유도학파 (1), 군진선도학파 (1), 교신전심학파 (1), 생명고정학파 (1), 서약집행학파 (1), 단절추방학파 (1) |
| scripts/population/recompute_role_majors.py | 11 | 열압포격학파 (1), 용융형상학파 (1), 결박제어학파 (1), 좌표감리학파 (1), 탄도관성학파 (1), 자계유도학파 (1), 군진선도학파 (1), 교신전심학파 (1), 생명고정학파 (1), 서약집행학파 (1), 단절추방학파 (1) |
| scripts/population/audit_population_invariants.py | 11 | 열압포격학파 (1), 용융형상학파 (1), 결박제어학파 (1), 좌표감리학파 (1), 탄도관성학파 (1), 자계유도학파 (1), 군진선도학파 (1), 교신전심학파 (1), 생명고정학파 (1), 서약집행학파 (1), 단절추방학파 (1) |
| world/live/population/population_slots.csv | 1394 | 열압포격학파 (233), 용융형상학파 (93), 결박제어학파 (210), 좌표감리학파 (17), 탄도관성학파 (223), 자계유도학파 (95), 군진선도학파 (94), 교신전심학파 (179), 생명고정학파 (238), 서약집행학파 (12) |

## 범위 해석
- `world/live/docs/`에는 이번 11학파명이 직접 박힌 현재 direct hit가 없다.
- `WB-0015`가 live prose의 핵심 병목이다.
- `population_slots.csv`와 `P-*.yaml`는 수기 치환 대상이 아니라 regeneration 대상이다.

## 검증 범위 정책
- `구 학파명 0건` 검증은 아래에만 적용한다.
  - docs/design/source_texts/magic_system/
  - world/live/world_bible/
  - world/live/population/profiles/
  - scripts/population/
  - world/live/population/population_slots.csv
  - world/live/population/P-*.yaml
- 아래는 예외 영역으로 둔다.
  - world_ops/cases/ 의 historical 문서
  - docs/history/
  - world/live/world_bible/WB-0021_appendix_terms_aliases.md
