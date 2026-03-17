# Phase 3 Apply

- change_id: CR-20260316-001
- branch: minor

## 1. 실제 수정 파일
- world/live/world_bible/WB-0015_academy_bible.md
- world/live/world_bible/WB-0021_appendix_terms_aliases.md
- world/live/population/profiles/current_term_snapshot_v1.yaml
- world/live/population/population_slots.csv
- world/live/population/P-*.yaml
- scripts/population/recompute_role_majors.py
- scripts/population/audit_population_invariants.py
- world/live/docs/master_map.md
- world_ops/world_change_log.md
- world_ops/cases/CR-20260316-001/phase3_apply.md
- world_ops/cases/CR-20260316-001/phase4_sync.md
- world_ops/cases/CR-20260316-001/post_7_towers_finalization_checklist.md

## 2. 변경 요약 (diff 요약 수준)
- `CR-20260316-001` 전체를 한 번에 live로 내리지 않고, 작가 검수가 끝난 `적탑 3학파 + 청탑 3학파`만 먼저 partial live sync 했다.
- `WB-0015`의 21학파 표, 색역별 요약, 외국/인외 교환학생 로스터 전공명을 적/청 신명 기준으로 갱신했다.
- `WB-0021`에 적/청 6학파의 구명 -> 현행명 alias를 추가해 구명 보존 창구를 열어 두었다.
- academy current-term snapshot, population CSV, `P-*.yaml`, population 검증/재계산 스크립트를 같은 이름 체계로 맞춰 live/generated layer 드리프트를 제거했다.
- 7탑 전부 점검이 끝난 뒤 수행할 최종 후속 작업을 별도 체크리스트 문서로 고정했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 적탑 3학파 live rename 반영 | `WB-0015` 적탑 표/요약/교환학생 로스터, snapshot, population CSV/YAML, population scripts | `홍련포화학파`, `용철무구학파`, `화연장막학파` | 주문 36식과 독자용 슬롯 문법은 아직 live 미반영 |
| 청탑 3학파 live rename 반영 | `WB-0015` 청탑 표/요약/교환학생 로스터, snapshot, population CSV/YAML, population scripts | `경면수호학파`, `빙쇄구속학파`, `수류유도학파` | 12식 세부와 전투 교리는 아직 케이스 문서 기준 |
| 구명 보존 및 후속 작업 고정 | `WB-0021`, `master_map`, `world_change_log`, `post_7_towers_finalization_checklist.md` | alias 정책, partial live sync 기록 | 남은 5탑과 전역 네이밍 규칙은 후속 sync 필요 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 적탑/청탑 외 학파명, 정원, 직능 분포, 기숙사 규칙은 건드리지 않았다.

## 4. 미해결 항목
- [ ] 없음
- details:
  - `CR-20260316-001` 전체는 아직 진행 중이다. 이번 반영은 적탑/청탑만 먼저 live SSOT에 canonize한 partial sync다.
  - 황/녹/자/백/흑탑의 학파명, 주문명, 전역 `7색 감정/문화 레지스터`, `교차색 콤보 규칙`, `마법/학파 네이밍 헌법`은 아직 live에 내리지 않았다.
  - `WB-0005`, `WB-0025`, `WB-0029` 수준의 전역 규칙 문서는 7탑 정리가 끝난 뒤 한 번에 닫는 편이 안전하다.

## 5. 작가 승인
- approved: yes
- note:
  - 2026-03-17 작가 지시로 `적탑+청탑 선반영, 나머지 탑은 후속 점검 후 반영` 전략을 채택했다.
