# revision_delta_v1

- episode_id: `ep005`
- upstream_raw_draft: `drafts/raw_codex_v1.txt`
- base_draft: `drafts/draft_codex_v1.txt`
- compared_revision: `assembled/revision_assembled_v1.txt`
- target_canon: `canon/5화_리라이트_v1.md`
- comparison_mode: `draft_vs_user_revision`
- note: `실험 폴더 cycle_02의 post_review_draft_v2 -> user_revision_v2 차이를 정식 ep005 폴더로 승격한 기록이다.`

## Comparison scope
- 기준 비교축은 `내부 검수 후 사용자용 초고`와 `최신 사용자 형상 텍스트`다.
- 이번 비교는 실험 `post_review_draft_v2`에 대한 직접 사용자 리비전 `user_revision_v2`의 차이를 정식화하는 목적이다.
- continuity 보정과 취향 신호는 분리해서 기록한다.

## Structural delta map

| layer / beat | retained from draft | user rewrite / removal | note |
|---|---|---|---|
| opening | `왕도 도착 -> 검정소 진입 -> 방계 다수/직계 소수` 골격 유지 | `과연 내가 내일도 렌바렌일까` 같은 메타 독백 삭제, 감각과 행동 중심으로 더 빨리 진입 | 초반 박자를 더 즉시적으로 만든 수정 |
| screening | `별도 라인 -> 검사 -> 미계승` 구조 유지 | `살았다 / 길 하나가 닫혔다` 같은 해석을 걷고, `왜 나만 따로 불렸지` 질문을 더 직접 남김 | 결과보다 미해결 질문이 앞으로 나오게 함 |
| party bridge | `라베르니온 별채 이동` 기능 유지 | 세르반 라베르니온 / 공작 / 문경청 수장으로 명시, 방문 이유를 더 직접적으로 설명 | 장소와 권력선을 더 빨리 고정 |
| seren contact | `중앙에 고립된 세렌 -> 리리아가 접근` 골격 유지 | 드레스 칭찬, 주변 시선, 친구 없음, 수련 이야기, 칼리온 칭찬 반응을 추가해 세렌의 결핍을 더 개인화 | 세렌을 추상적 고립보다 구체적 인물로 보정 |
| ending | `세렌이 다음 구조에 호기심을 보인다` 기능 유지 | `익명 구조 호기심`에서 `아버지 칭찬을 받고 싶어서 게시판을 원한다`로 동기 구체화 | 다음 화 엔진이 더 직접적인 욕망으로 잠김 |

## What the user cut
- 오프닝의 메타 질문과 추상적 위기 프레이밍
- 연회장의 1층/2층 기능, 사회 구조를 길게 설명하는 문단
- 화말의 익명 규칙/놀이 구조 설명
- 세렌을 향한 키리온의 장면 내 구조 해석 일부

## What the user concretized
- `아버지가 신세지고 있는 어르신` -> `세르반 라베르니온 / 공작 / 문경청 수장`
- `세렌의 고립` -> `드레스, 시선, 친구 없음, 아버지 칭찬 결핍`
- `게시판 구조` -> `칼리온에게 칭찬받게 만든 도구`

## What the user lowered or sharpened
- 키리온의 분석적 사회 구조 해설은 낮추고, 실제 대화와 즉각 반응을 더 날카롭게 세웠다.
- 세렌 훅을 `흥미롭다`보다 `하고 싶다 / 칭찬받고 싶다`로 압축해 감정 방향을 선명하게 만들었다.

## Character-level corrections
- 세렌은 `고립된 공작가 영애`라는 위치를 유지하되, 최종본에서는 그 고립이 `아버지 칭찬을 원하지만 쉽게 못 받는 아이`라는 욕망으로 연결됐다.
- 리리아는 구조 설명용 도구가 아니라, 세렌의 격식을 무너뜨리고 사건을 열어 버리는 행동 주체로 더 강해졌다.
- 키리온은 구조를 보는 관찰자 역할을 유지하되, 최종본에서는 월권 문제를 먼저 짚는 현실 감각 쪽이 더 전면에 섰다.

## Non-preference edits
- 계승조회식 결과 후 가족 반응의 압축
- 별채 도입부의 권력 정보 명시
- 훅 직전 대화 길이 정리

## Preference extraction candidates

| target | signal | confidence | evidence | next-draft implication |
|---|---|---|---|---|
| `author_preference_registry.md` | 추상 구조 설명은 결국 한 인물의 구체적 결핍/욕망으로 착지시킨다 | medium | 세렌 훅이 `익명 구조 호기심`에서 `아버지 칭찬 욕망`으로 바뀜 | 다음 화에서도 시스템 설명은 사람 한 명의 직접적 바람과 연결하는 편이 맞다 |
| `author_preference_registry.md` | 장면 오프닝에서 메타 독백보다 감각/행동 진입을 선호한다 | medium | 초두의 `과연 내가 내일도 렌바렌일까` 삭제 | 긴장 장면 첫머리는 생각보다 몸과 상황을 먼저 세운다 |
| `style_pattern_library.md` | 고위 신분 인물 첫 접속은 `위치의 어색함 + 사소한 대화 소재 + 숨은 결핍` 순으로 풀면 잘 산다 | medium | 세렌의 드레스, 시선, 친구 없음, 부친 칭찬 욕망 | 신규 인물 첫 만남 장면의 재사용 패턴 후보 |

## Watchlist
- 다음 리비전에서도 구조 설명이 다시 길어지면, 최종 훅을 사람 욕망으로 압축하는 방향이 반복 취향인지 추가 검증할 것

## Next-draft instructions
- 사회 구조나 제도 설명은 그 자체로 끝내지 말고, 장면 안 한 사람의 직접적인 결핍과 연결해 잠근다.
- 신규 인물 첫 등장은 위치와 어색함으로 시작하되, 되도록 빠르게 `그 인물이 실제로 원하는 것`을 한 줄로 드러내는 편이 좋다.
