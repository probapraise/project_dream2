# Phase 2 Report (Collision Scan)

- change_id: CR-20260320-002
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/external/EX-0003.yaml
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - world_ops/world_change_log.md

## 2. 충돌 후보
- [x] 없음
- details:
  - `무흔술` 정의 자체는 직전 `CR-20260320-001`에서 이미 canon화되었으므로, 이번 건은 세계 규칙 재수정이 아니라 키리온의 인식과 공개 타이밍, 장기 운용 방식 고정으로 한정한다.
  - 현 canon frontier는 `ep002`라서 입학식/`ep010` 정보를 현재 상태 문서에 과도하게 밀어 넣지 않고, `story_arcs`와 `long_term` 위주로 배치하는 편이 맞다.
  - 키리온의 장기 엔진이 정보 인프라 쪽이라는 큰 축은 유지해야 하므로, 전투력은 `주력`이 아니라 `조커 카드`라는 보조축으로 정리한다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 전투력이 주인공 장기 엔진을 덮어버릴 수 있음 | `NC-0001`, `long_term`, `story_arcs` | `무흔술`은 숨은 자산/조커 카드로 규정하고, 주력 성장선은 여전히 정보 인프라/비전투 마법으로 유지 | 조커 카드, 정보 인프라, 무흔술 | resolved |
| 아직 안 일어난 입학식/`ep010` 내용을 현재 상태 문서에 과투입할 수 있음 | narrative-facing docs | `narrative_state`는 유지하고, 미래 고정 약속은 `story_arcs`와 `long_term`에만 반영 | 입학식, ep010, current frontier | resolved |
| 세렌 등장축이 과하게 커질 수 있음 | academy arc planning | 세렌은 입학식에서 `같은 조 운영 대상` 정도로만 명시하고, 별도 카드 수정은 하지 않음 | 세렌, 모의 탐색전 | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - 데리온의 academy 이후 반복 시험 축까지 `EX-0003`에 함께 넣어, `무흔술` 유지 동력이 빠지지 않게 했다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - `WB-0005/0009/0026` 재수정은 필요 없었다. 직전 case의 세계 규칙을 참조만 하면 충분하다.

## 5. 판단 근거
- world_bible_index 참조: 없음 (활성 파일 추가/삭제 없음)
- cross-reference 참조:
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/external/EX-0003.yaml
  - world/live/docs/story_arcs.md
  - world/live/docs/memory_tiers/long_term.md
  - world_ops/cases/CR-20260320-001/request.md

## 6. 분기 결정
- branch: minor
- reason: 기존 캐릭터 카드/아크/장기 기억 문서의 미래 약속과 운영 로그를 보강하는 작업이며, 신규 파일 구조나 외부 재작성 경로가 필요하지 않다.

## 7. 작가 승인
- approved: yes
- note: writer가 키리온 `무흔술` 공개 타이밍과 academy 이후 전투 자산 운용 방향을 직접 지정
