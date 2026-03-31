# logic_review_v1

- episode_id: `ep006`
- target_raw_draft: `drafts/raw_codex_v1.txt`
- target_user_facing_draft: `drafts/draft_codex_v1.txt`
- review_mode: `raw_draft_discourse_review`
- outcome: `pass` / `rewrite_required`

## Role
- 이 문서는 `raw_codex_v1.txt`를 사용자에게 보여 주기 전에 거치는 내부 논리/담화 검수 기록이다.
- 목적은 `더 잘 쓴다`보다 `사용자가 굳이 잡지 않아도 되는 1차 결함을 먼저 제거한다`에 있다.
- 이 문서는 문장을 바로 고치기보다, 무엇이 왜 문제인지와 어떤 재작성 방향이 필요한지를 먼저 적는다.

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
| F-01 | major |  |  |  |  |

## Blocking summary
- 사용자용 초고로 내보내기 전 반드시 고쳐야 하는 문제
- 

## Release decision
- `pass`: blocker 없음. `drafts/draft_codex_v1.txt` 생성 가능
- `rewrite_required`: blocker 있음. `analysis/logic_patch_brief_v1.md` 작성 후 재작성 필요
