# revision_delta_v1

- episode_id: `<episode_id>`
- upstream_raw_draft: `drafts/raw_codex_v1.txt`
- base_draft: `drafts/draft_codex_v1.txt`
- compared_revision: `assembled/revision_assembled_v1.txt` or `working tree edits on canon/<current_text_canon>`
- target_canon: `canon/<current_text_canon>`
- comparison_mode: `draft_vs_user_revision`
- note: ``

## Comparison scope
- 기준 비교축은 `내부 검수 후 사용자용 초고`와 `최신 사용자 형상 텍스트`다.
- 세계관 보정, 연결성 보정, 오탈자 수정 같은 `비취향 수정`과 반복 취향 신호를 분리해서 적는다.
- 목적은 `무엇이 더 좋아졌나`를 넘어서 `사용자가 어떤 기본값을 반복적으로 거부/선호하나`를 추출하는 것이다.
- 필요하면 `upstream_raw_draft`를 함께 보며 `내부 검수에서 이미 걸러진 것`과 `여전히 사용자 손에서 구조적으로 바뀐 것`을 구분한다.

## Structural delta map

| layer / beat | retained from draft | user rewrite / removal | note |
|---|---|---|---|
| opening |  |  |  |
| middle |  |  |  |
| ending |  |  |  |

## What the user cut
- 반복적으로 걷어낸 설명, 감정 명명, 문어체, 메타 표현
- 

## What the user concretized
- 추상 설명을 장면, 신체 반응, 생활어, 관찰로 바꾼 부분
- 

## What the user lowered or sharpened
- 말투를 낮춘 지점, 압박을 올린 지점, 리듬을 단문으로 끊은 지점
- 

## Character-level corrections
- 특정 인물의 반응, 대사, 존재감을 어떻게 보호했는지
- 

## Non-preference edits
- continuity, 설정 오류, 이름/호칭 정정, 시간축 보정처럼 `취향`으로 일반화하면 안 되는 수정만 분리 기록한다.
- 

## Preference extraction candidates

| target | signal | confidence | evidence | next-draft implication |
|---|---|---|---|---|
| `author_preference_registry.md` |  | low |  |  |
| `style_pattern_library.md` |  | low |  |  |

## Watchlist
- 이번 화에서 한 번 보였지만 아직 전역 기본값으로 승격하기 이른 신호
- 

## Next-draft instructions
- 다음 초고 생성 때 바로 반영할 3~6개 지시를 적는다.
- 
