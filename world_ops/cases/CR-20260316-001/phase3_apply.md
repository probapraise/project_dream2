# Phase 3 Apply

- change_id: CR-20260316-001
- branch: major

## 1. 실제 수정 파일
- world/live/world_bible/WB-0015_academy_bible.md
- world/live/world_bible/WB-0007_badge_network.md
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
- `CR-20260316-001` 전체를 한 번에 live로 내리지 않고, 작가 검수가 끝난 `적탑 3학파 + 청탑 3학파 + 녹탑 3학파 + 황탑 3학파 + 자탑 3학파 36식`만 먼저 partial live sync 했다.
- `WB-0015`의 21학파 표, 색역별 요약, 외국/인외 교환학생 로스터 전공명을 적/청/녹/황 신명 기준으로 갱신했다.
- `WB-0015`와 `WB-0007`에 자탑 `보존 / 전달 / 합성` 3축 메모와 배지/체험실/증강현실 구분을 넣어 `교신전심학파 -> 전심공명학파`, `허상연출학파 -> 환영직조학파`, 보존축 `각인연장 / 만상채록 / 만상기록고`, 전달축 `심향채청 / 공명연결 / 전심전이`, 합성축 `환영투사 / 환영극장 / 자색환계` 체계를 live 문장으로 고정했다.
- `WB-0021`에 적/청/녹/황 12학파의 구명 -> 현행명 alias를 추가해 구명 보존 창구를 열어 두었다.
- `WB-0021`에 자탑 구명/구술식 alias까지 추가해 보존축 `발췌색인 / 매체보존막 / 공기서고`, 전달축 `교신전심학파 / 서명채청 / 합창령`, 합성축 `허상연출학파 / 허상막 / 자색대막`의 역참조 창구를 열어 두었다.
- academy current-term snapshot, population CSV, `P-*.yaml`, population 검증/재계산 스크립트를 같은 이름 체계로 맞춰 live/generated layer 드리프트를 제거했다.
- 7탑 전부 점검이 끝난 뒤 수행할 최종 후속 작업을 별도 체크리스트 문서로 고정했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 적탑 3학파 live rename 반영 | `WB-0015` 적탑 표/요약/교환학생 로스터, snapshot, population CSV/YAML, population scripts | `홍련포화학파`, `용철무구학파`, `화연장막학파` | 주문 36식과 독자용 슬롯 문법은 아직 live 미반영 |
| 청탑 3학파 live rename 반영 | `WB-0015` 청탑 표/요약/교환학생 로스터, snapshot, population CSV/YAML, population scripts | `경면수호학파`, `빙쇄구속학파`, `수류유도학파` | 12식 세부와 전투 교리는 아직 케이스 문서 기준 |
| 녹탑 3학파 live rename 반영 | `WB-0015` 녹탑 표/요약/교환학생 로스터, snapshot, population CSV/YAML, population scripts | `생맥약초학파`, `야생교감학파`, `포자영토학파` | 12식 세부와 전투 교리는 아직 케이스 문서 기준 |
| 황탑 3학파 live rename 반영 | `WB-0015` 황탑 표/요약/교환학생 로스터, snapshot, population CSV/YAML, population scripts | `황도유성학파`, `뇌철견인학파`, `결정변성학파` | 황탑 12식 세부와 전투 교리는 아직 케이스 문서 기준 |
| 자탑 3학파 36식 live sync | `WB-0007`, `WB-0012`, `WB-0015`, `WB-0021`, snapshot, population CSV/YAML, population scripts | `보존각인학파`, `전심공명학파`, `환영직조학파`, `각인연장`, `만상기록고`, `심향채청`, `전심전이`, `환영투사`, `자색환계` | 백탑/흑탑 전체 12식과 전역 규칙 문서 반영은 아직 후속 |
| 구명 보존 및 후속 작업 고정 | `WB-0021`, `master_map`, `world_change_log`, `post_7_towers_finalization_checklist.md` | alias 정책, partial live sync 기록 | 남은 백탑/흑탑과 전역 네이밍 규칙은 후속 sync 필요 |

## 3. 예상 외 영향
- [x] 없음
- details:
  - 적탑/청탑/녹탑/황탑 외 학파명, 정원, 직능 분포, 기숙사 규칙은 건드리지 않았다.
  - 자탑은 `보존각인학파 / 전심공명학파 / 환영직조학파` 3축 36식까지 live 등재했고, 백탑/흑탑 live 세부는 그대로 남겨 두었다.

## 4. 미해결 항목
- [ ] 없음
- details:
  - `CR-20260316-001` 전체는 아직 진행 중이다. 이번 반영은 적탑/청탑/녹탑/황탑과 자탑 3학파 36식을 먼저 live SSOT에 canonize한 partial sync다.
  - 백탑/흑탑의 학파명/주문명, 전역 `7색 감정/문화 레지스터`, `교차색 콤보 규칙`, `마법/학파 네이밍 헌법`은 아직 live에 내리지 않았다.
  - `WB-0005`, `WB-0025`, `WB-0029` 수준의 전역 규칙 문서는 7탑 정리가 끝난 뒤 한 번에 닫는 편이 안전하다.

## 5. 작가 승인
- approved: yes
- note:
  - 2026-03-17 작가 지시로 `확정된 탑부터 선반영, 나머지 탑은 후속 점검 후 반영` 전략을 채택했고 현재 live 반영 범위는 적탑/청탑/녹탑/황탑과 자탑 3학파 36식까지다.
