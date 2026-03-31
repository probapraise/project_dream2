# ep006 pilot source map v1

- target_episode: `ep006`
- pilot_mode: `multisurface_edit_pilot`

## Authority order

1. `artifacts/writing/experiments/ep006_multisurface_edit_pilot/context/anchor_card_v1.md`
2. `artifacts/writing/experiments/ep006_multisurface_edit_pilot/context/draft_brief_v1.md`
3. `artifacts/writing/episodes/ep006/episode_style_constitution_v1.md`
4. `artifacts/writing/style/author_preference_registry.md`
5. `artifacts/writing/style/house_rules.md`
6. `artifacts/writing/episodes/ep006/setting_brief_v1.md`
7. `artifacts/writing/episodes/ep005/canon/5화_리라이트_v1.md`
8. `artifacts/writing/episodes/ep004/canon/4화_리라이트_v1.md`
9. `artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md`
10. 필요한 경우에만 `world/live/docs/*`

## Why this order

- 이번 파일럿은 `editing pipeline experiment`이므로, 회차 특수 목적과 숨김 정보는 실험 폴더의 문서가 먼저 잠근다.
- 공식 회차 입력은 `ep006` 로컬 문서와 recent raw canon이 담당한다.
- 전역 live 문서는 보조층이지만, 현재 `ep005` 캐논 사후 패치로 인해 일부 live 문서가 stale일 수 있다.

## Stale-source warning

- `ep005`는 현재 공식 canon sha가 바뀐 상태지만 live sync가 다시 맞춰지지 않았다.
- 따라서 `world/live/docs/narrative_state.md`, `recent.md` 등에서 `ep005` 후속 해석이 `setting_brief_v1.md`와 충돌하면, 반드시 `setting_brief_v1.md`와 raw canon 쪽을 따른다.
- 이번 파일럿에서는 `setting_brief_v1.md`가 사실상 continuity override다.

## Primary official inputs

- `artifacts/writing/episodes/ep006/setting_brief_v1.md`
- `artifacts/writing/episodes/ep006/episode_style_constitution_v1.md`
- `artifacts/writing/style/author_preference_registry.md`
- `artifacts/writing/style/house_rules.md`
- `artifacts/writing/episodes/ep005/canon/5화_리라이트_v1.md`

## Do not trust over source inputs

- stale `ep005` live summary 해석
- 빈 템플릿 상태의 `ep006/prompt_v1.md`
- 실험 이전의 일반론적 아크 메모가 이번 화 `setting_brief_v1.md`와 직접 충돌하는 경우
