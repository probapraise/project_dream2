# logic_review_v1

- episode_id: `ep005`
- target_raw_draft: `drafts/raw_codex_v1.txt`
- target_user_facing_draft: `drafts/draft_codex_v1.txt`
- review_mode: `raw_draft_discourse_review`
- outcome: `rewrite_required`
- promotion_note: `promoted from ep005_redraft_pilot cycle_02 logic_review_v2`

## Role
- 이 문서는 현재 `drafts/raw_codex_v1.txt`로 승격된 실험 초고에 대해, 사용자에게 보여 주기 전 내부적으로 걸었던 논리/담화 검수 기록이다.
- 목적은 `더 잘 쓴다`보다 `사용자가 굳이 잡지 않아도 되는 1차 결함을 먼저 제거한다`에 있다.
- 이 회차에서는 특히 연회장 진입부와 세렌 첫 접속부가 검수 핵심이었다.

## Review categories
- `contrast`: 공존 가능한 사실을 억지 대비하지 않았는가
- `redundancy`: 이미 보여 준 인상을 다시 요약하지 않았는가
- `inference`: 작은 관찰에서 세계 총평으로 너무 빨리 뛰지 않았는가
- `dialogue`: 기능 설명이 입말보다 앞서지 않는가
- `pov_plausibility`: 그 자리의 화자가 실제로 그렇게까지 생각할 만한가
- `scene_pressure`: 정보는 맞지만 장면 압박이 빠지지 않았는가

## Findings

| id | severity | location | category | issue | rewrite direction |
|---|---|---|---|---|---|
| F-01 | major | Beat 2 말미 연회장 진입 | `scene_pressure` | `아버지가 신세지고 있는 어르신`만으로는 곧바로 `라베르니온 공작가 별채`로 넘어갈 때 장소와 목적 연결이 약했다. | `그 어르신 = 라베르니온 공작`, `오늘은 별채에 인사하러 간다`를 더 분명히 연결한다. |
| F-02 | major | Beat 3 초반 | `contrast` | 연회장 `1층 공개 친교 / 2층 가문별 휴식` 대비가 구조 설명으로만 지나가 장면 기능이 약했다. | 리리아는 1층으로 스며들고, 키리온은 2층 난간으로 물러나는 동선으로 기능 차이를 보여 준다. |
| F-03 | major | Beat 3 초반 | `pov_plausibility` | 키리온 시선이 세렌으로 너무 빨리 이동해, 다른 아이들의 무리와 이미 생긴 계급 분화가 충분히 쌓이지 않았다. | 세렌 전 단계에서 다른 또래 무리와 리리아 움직임을 더 본 뒤 세렌 고립으로 줌인한다. |
| F-04 | major | Beat 3 대화부 | `dialogue` | 리리아/키리온 대사가 기능 설명을 먼저 밀어 실제 아이들 말처럼 들리지 않았다. | 생활어와 즉각 반응 중심으로 대사를 전면 교체한다. |
| F-05 | major | Beat 3 세렌 접속부 | `scene_pressure` | 세렌의 고립이 `특수한 아이` 정보로 먼저 읽히고, `너무 잘 보이는 자리에 혼자 있는 아이`라는 체감이 덜했다. | 고립의 이유를 위압보다 위치와 접근 불가 감각으로 먼저 읽게 한다. |

## Blocking summary
- 연회장 진입부와 세렌 첫 접속부는 그대로 사용자용 초고로 넘기기엔 구조 연결과 대화 결이 약했다.
- 핵심 블로커는 `장소 브리지 선명화`, `1층/2층 기능 분리`, `세렌 전 단계 관찰 확장`, `대사 생활어화`였다.

## Release decision
- `pass`: blocker 없음. `drafts/draft_codex_v1.txt` 생성 가능
- `rewrite_required`: blocker 있음. `analysis/logic_patch_brief_v1.md` 작성 후 재작성 필요
