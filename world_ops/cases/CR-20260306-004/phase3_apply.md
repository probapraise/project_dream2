# Phase 3 Apply

- change_id: CR-20260306-004
- branch: minor

## 1. 실제 수정 파일
- world/live/docs/community_map.md
- world/live/docs/simulation_playbook.md
- world/live/board_states/README.md
- world/live/docs/master_map.md
- docs/handoff/next_steps.md

## 2. 변경 요약 (diff 요약 수준)
- `community_map.md`에 보드 lifecycle, 3자리 `BOARD-###` ID 규칙, stateful 승격 조건을 추가했다.
- `simulation_playbook.md`에 기존 보드 사용 / concept_only 후보 / registered-stateful 승격 흐름과 `simrun-*.json` 기본 promote 규칙을 추가했다.
- `board_states/README.md`에 파일 종류(`simrun-*.json`, 선택적 `BOARD-###_<slug>.md`)와 legacy ID 은퇴 규칙을 명시했다.
- `master_map.md` recent changes와 `next_steps.md`를 동기화했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| 보드 lifecycle 명시 | `world/live/docs/community_map.md` | `concept_only`, `registered`, `stateful`, `retired` | 첫 신규 보드 생성 시 실제 적용 검증 필요 |
| 시뮬레이션 승격 규칙 명시 | `world/live/docs/simulation_playbook.md` | `simrun`, `board_state_file`, `promote` | 정식 시뮬레이션 시작 후 run naming 관례 보정 가능 |
| 파일 규칙 정리 | `world/live/board_states/README.md` | `simrun-*.json`, `BOARD-###_<slug>.md` | board summary md 템플릿은 필요 시 후속 추가 |
| handoff 동기화 | `docs/handoff/next_steps.md`, `world/live/docs/master_map.md` | next session priority | narrative/style/state 문서 작업이 다음 우선순위 |

## 3. 예상 외 영향
- [x] 없음
- details:
  -

## 4. 미해결 항목
- [ ] 없음
- details:
  - 첫 정식 신규 보드를 열 때 ID 부여와 stateful 승격 절차를 실제로 한번 검증하면 된다.

## 5. 작가 승인
- approved: yes
- note: 동적 게시판 lifecycle 규칙 live 문서 반영 완료.
