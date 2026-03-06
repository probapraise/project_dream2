# Phase 2 Report (Collision Scan)

- change_id: CR-20260306-004
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/docs/community_map.md
  - world/live/docs/simulation_playbook.md
  - world/live/board_states/README.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 구조 재작성이나 canon retcon이 아니라, 이미 결정된 동적 커뮤니티 원칙을 운영 규칙으로 구체화하는 작업이다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 보드 생성 시점이 문서마다 암묵적 | 새 보드 추가 시 판단 흔들림 | lifecycle(`concept_only/registered/stateful/retired`) 명시 | dynamic board model | resolved |
| run 결과와 live 보드 생성이 혼동될 수 있음 | smoke/explore 결과 오해 가능 | `simrun-*.json` 기본, BOARD 등록은 별도 승인으로 분리 | `simrun`, `board_state_file`, `promote` | resolved |
| next_steps가 완료 예정 작업을 계속 최우선으로 유지 | 다음 세션 우선순위 왜곡 | handoff 우선순위 재정렬 | `next_steps.md` | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - `board_states/README.md`에도 파일 종류와 legacy ID 은퇴 규칙을 적어 재발 방지.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 보드 lifecycle 규칙은 `community_map`과 `simulation_playbook`이 나눠 갖되, 서로 역할을 분리한다.

## 5. 판단 근거
- world_bible_index 참조: 보드 개별 인덱스가 아니라 운영 문서 레이어 정합 문제다.
- cross-reference 참조: `community_map.md`는 구조 정의, `simulation_playbook.md`는 실행 승격 규칙, `board_states/README.md`는 파일 규칙을 담당하도록 분리한다.

## 6. 분기 결정
- branch: minor
- reason: 설정 추가보다 운영 규칙 명시와 문서 정합화 성격이 강하다.

## 7. 작가 승인
- approved: yes
- note: 사용자 지시로 바로 규칙 문서화 진행.
