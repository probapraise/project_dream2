# Phase 2 Report (Collision Scan)

- change_id: CR-20260306-005
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/docs/narrative_state.md
  - world/live/docs/master_map.md
  - docs/handoff/next_steps.md
  - docs/design/spec_sheet_v1.md
  - artifacts/writing/episodes/ep000_prologue/canon/revision_v1.txt
  - artifacts/writing/episodes/ep001/canon/revision_v2.txt
  - artifacts/writing/episodes/ep001/diff_v2.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 기존 캐논 텍스트를 수정하는 작업이 아니라, 이미 확정된 `ep000`/`ep001` 상태를 압축 로딩 가능한 문서 구조로 재배치하는 작업이다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| `narrative_state`가 비어 있어 장기 연재 시 매번 원고 재탐색 필요 | 집필 입력 컨텍스트 비효율 | 허브 문서 + 압축 레지스트리 문서 분리 | `narrative_state`, `story_arcs`, `episode_deltas` | resolved |
| 복선/아크/회차 요약이 한 문서에 섞이면 재로딩 단위가 커짐 | 100화 이상 진행 시 컨텍스트 과부하 | arc / foreshadow / delta를 별도 문서로 분리 | `foreshadow_registry`, `ARC`, `FS` | resolved |
| 캐논 사실과 문서 요약이 엇갈릴 위험 | 잘못된 서사 상태 고정 | `ep000 canon/revision_v1`, `ep001 canon/revision_v2`, `diff_v2`만 근거로 최소 사실 추출 | `current canon`, `canon/revision_v2` | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - `master_map.md` 인덱스와 `next_steps.md` 운영 지침까지 같이 갱신해 새 문서가 고립되지 않게 한다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 회차 줄거리 요약을 늘리는 대신, `episode_deltas`는 상태 변화만 기록하도록 제한한다.

## 5. 판단 근거
- spec reference: `docs/design/spec_sheet_v1.md` 7.3은 `narrative_state.md`를 활성 복선/아크/구성 위치/다음 3~5화/톤 가이드 문서로 정의한다.
- canon reference: `ep000`은 정체 은폐와 장기 야망, `ep001`은 병목 관찰과 책-심문 장치를 확정했다.
- 운영 판단: 장기 연재에서 중요한 것은 전체 사건 복기가 아니라 "지금 무엇이 열려 있는가"다.

## 6. 분기 결정
- branch: minor
- reason: 세계관 retcon이나 새 canon 추가가 아니라, 집필용 상태 관리 레이어를 정비하는 작업이다.

## 7. 작가 승인
- approved: yes
- note: 사용자가 100화 이상 장기 연재 대비 컨텍스트 관리 구조 설계를 요청해 바로 진행.
