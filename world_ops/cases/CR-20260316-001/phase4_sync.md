# Phase 4 Sync

- change_id: CR-20260316-001

## 1. 동기화 대상
- [ ] world_bible_index 업데이트
- [x] master_map 업데이트
- [x] world_change_log 기록

## 2. 반영 내역
- `world/live/world_bible/WB-0015_academy_bible.md`
  - 적탑 3학파를 `홍련포화 / 용철무구 / 화연장막`으로, 청탑 3학파를 `경면수호 / 빙쇄구속 / 수류유도`로, 녹탑 3학파를 `생맥약초 / 야생교감 / 포자영토`로, 황탑 3학파를 `황도유성 / 뇌철견인 / 결정변성`으로 live 표기 교체
  - 적/청/녹/황 탑 요약 문장을 최신 판타지 기준으로 재서술
  - 자탑 `교신전심학파 -> 전심공명학파`, `허상연출학파 -> 환영직조학파`를 반영하고 `자탑 현행 3축 전승 메모`를 추가해 보존/전달/합성 36식의 역할과 운용축을 live 문장으로 고정
  - 외국/인외 교환학생 로스터 전공명을 동기화
- `world/live/world_bible/WB-0007_badge_network.md`
  - 학술원 지급 배지 일부 실습형 모델에 자탑 초급식 `환영투사`가 내장된다는 설정과 레퍼런스 의존 패널티를 추가
- `world/live/world_bible/WB-0021_appendix_terms_aliases.md`
  - 적/청/녹/황 12학파의 구명 -> 현행명 alias 추가
  - 자탑 보존/전달/합성 3축의 구명 -> 현행명 alias 추가
- `world/live/population/profiles/current_term_snapshot_v1.yaml`
  - 자탑 major 분포 표기를 `전심공명학파 / 환영직조학파 / 보존각인학파` 기준으로 교체
- `world/live/population/population_slots.csv`, `world/live/population/P-*.yaml`
  - live 모집단 major 필드의 `교신전심학파`를 `전심공명학파`로, `허상연출학파`를 `환영직조학파`로 일괄 치환
- `scripts/population/recompute_role_majors.py`, `scripts/population/audit_population_invariants.py`
  - mage major 허용 집합을 `전심공명학파 / 환영직조학파 / 보존각인학파` 기준으로 교체
- `world/live/docs/master_map.md`, `world_ops/world_change_log.md`
  - 자탑 3학파 36식 full live sync 확장 이력 기록
- `world_ops/cases/CR-20260316-001/post_7_towers_finalization_checklist.md`
  - 7탑 전체 완료 후 최종 반영 체크리스트 신설

## 3. 일관성 점검
- [x] 참조 경로 정상
- [x] 섹션 ID 정상
- [x] 상태: done

notes:
- 이번 범위는 파일 추가/삭제가 아니라 기존 파일 내용 동기화라 `world_bible_index_v2.md`는 갱신하지 않았다.
- alias 보존 규칙상 `WB-0021`에는 구명과 구술식 이름을 남겨 두었다.

## 4. 작가 승인
- approved: yes
- note:
  - 2026-03-17 작가가 `확정된 탑부터 먼저 live SSOT에 반영`하는 partial sync를 승인했고, 현재 반영 범위는 적탑/청탑/녹탑/황탑과 자탑 3학파 36식이다.
