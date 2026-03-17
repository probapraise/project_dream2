# Phase 4 Sync

- change_id: CR-20260316-001

## 1. 동기화 대상
- [ ] world_bible_index 업데이트
- [x] master_map 업데이트
- [x] world_change_log 기록

## 2. 반영 내역
- `world/live/world_bible/WB-0015_academy_bible.md`
  - 적탑 3학파를 `홍련포화 / 용철무구 / 화연장막`으로, 청탑 3학파를 `경면수호 / 빙쇄구속 / 수류유도`로, 녹탑 3학파를 `생맥약초 / 야생교감 / 포자영토`로 live 표기 교체
  - 적/청/녹 탑 요약 문장을 최신 판타지 기준으로 재서술
  - 외국/인외 교환학생 로스터 전공명을 동기화
- `world/live/world_bible/WB-0021_appendix_terms_aliases.md`
  - 적/청/녹 9학파의 구명 -> 현행명 alias 추가
- `world/live/population/profiles/current_term_snapshot_v1.yaml`
  - 적/청/녹 탑 major 분포 표기를 새 학파명 기준으로 교체
- `world/live/population/population_slots.csv`, `world/live/population/P-*.yaml`
  - live 모집단 major 필드를 적/청/녹 9학파 신명 기준으로 일괄 치환
- `scripts/population/recompute_role_majors.py`, `scripts/population/audit_population_invariants.py`
  - mage major 허용 집합을 새 학파명 기준으로 교체
- `world/live/docs/master_map.md`, `world_ops/world_change_log.md`
  - partial live sync 이력 기록
- `world_ops/cases/CR-20260316-001/post_7_towers_finalization_checklist.md`
  - 7탑 전체 완료 후 최종 반영 체크리스트 신설

## 3. 일관성 점검
- [x] 참조 경로 정상
- [x] 섹션 ID 정상
- [x] 상태: done

notes:
- 이번 범위는 파일 추가/삭제가 아니라 기존 파일 내용 동기화라 `world_bible_index_v2.md`는 갱신하지 않았다.
- alias 보존 규칙상 `WB-0021`에는 구명을 남겨 두었다.

## 4. 작가 승인
- approved: yes
- note:
  - 2026-03-17 작가가 `적탑+청탑+녹탑만 먼저 live SSOT에 반영`하는 partial sync를 승인했다.
