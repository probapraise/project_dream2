# Post 7 Towers Finalization Checklist

## 목적
- `CR-20260316-001`에서 7탑 21학파 전부의 이름/주문/전투 교리 점검이 끝난 뒤, live SSOT에 최종 반영할 때 빠뜨리기 쉬운 후속 작업을 한 번에 닫기 위한 체크리스트다.
- 2026-03-18 기준 이 체크리스트는 실제 실행 완료 상태를 반영한다.

## 실행 트리거
- 아래 조건이 모두 충족되면 이 문서를 실행한다.
  - 7탑 21학파명의 최종안이 확정됨
  - 각 학파 12식의 최종안 또는 live에 올릴 요약본이 확정됨
  - `7색 감정/문화 레지스터`, `교차색 콤보 규칙`, `독자용 슬롯 문법`, `마법/학파 네이밍 헌법`의 live 반영 범위가 확정됨

## 1. live world bible 최종 동기화
- [x] `WB-0015_academy_bible.md`의 21학파 표, 색역별 요약, 샘플 전공 표기를 7탑 최종안 기준으로 전면 갱신
- [x] `WB-0005_magic_system.md`에 7색 감정/문화 레지스터, 독자용 슬롯 문법, 교차색 콤보의 상위 요약 반영
- [x] `WB-0029_appendix_aptitude_signature_materials.md`에 색역 독법/표면 이미지 보강이 필요하면 반영
- [x] `WB-0025_appendix_naming_constitution.md`에 마법/학파 네이밍 헌법 추가
- [x] `WB-0021_appendix_terms_aliases.md`에 구명 -> 최종 현행명 alias 전부 추가

## 2. population / generated layer 최종 동기화
- [x] `world/live/population/profiles/current_term_snapshot_v1.yaml`의 7탑 major 분포 표기를 최종안 기준으로 갱신
- [x] `scripts/population/recompute_role_majors.py`의 mage major 집합을 최종안 기준으로 갱신
- [x] `scripts/population/audit_population_invariants.py`의 mage major 허용 집합을 최종안 기준으로 갱신
- [x] `world/live/population/population_slots.csv` 반영
- [x] `world/live/population/P-*.yaml` 반영
- [x] 필요 시 population 재생성 절차와 검증 절차를 다시 실행

## 3. 케이스/인덱스/로그 정리
- [x] `phase3_apply.md`에 전체 반영 범위와 실제 수정 파일 정리
- [x] `phase4_sync.md`에 최종 동기화 결과 기록
- [x] `world_ops/world_change_log.md`에 최종 반영 로그 추가
- [x] `world/live/docs/master_map.md` recent changes 갱신
- [x] 파일 추가/삭제가 있었으면 `world_bible_index_v2.md`와 관련 인덱스 갱신

## 4. prompt-facing / handoff 드리프트 정리
- [x] `docs/handoff/ssot_reflection_audit_20260316.md` 또는 후속 audit 문서에 `CR-20260316-001` 반영 상태 갱신
- [x] active handoff/next steps 문서에 `partial sync` 흔적이 남아 있으면 `final sync 완료` 상태로 정리
- [x] 독자/집필 프롬프트에 직접 드러나는 구명이 남아 있는지 점검

## 5. 검증 게이트
- [x] active SSOT에서 구명 잔존 검색
- [x] `WB-0021` 같은 alias 보존 문서는 예외 처리
- [x] `git diff --check` 통과
- [x] `scripts/population/audit_population_invariants.py` 통과
- [x] 필요 시 추가 world ops audit 번들 실행

## 6. 완료 조건
- [x] 7탑 최종 명칭과 live SSOT 명칭이 일치함
- [x] generated population layer와 script 허용 집합이 일치함
- [x] alias 문서를 제외한 active SSOT에서 구명 잔존이 관리 가능한 수준으로 정리됨
- [x] 전역 규칙 문서(`WB-0005`, `WB-0025`, `WB-0029`)와 학술원 문서(`WB-0015`)가 서로 충돌하지 않음
