# board_states

- 이 디렉터리에는 현재 활성 보드의 상태 파일과 실행 결과에서 promote된 상태 스냅샷만 둔다.
- 고정 18보드 bootstrap stub은 2026-03-06부로 live에서 제거했다.
- `simrun-*.json`: 실행 결과 스냅샷. exploratory/smoke run의 기본 형식이다.
- `BOARD-###_<slug>.md`: 반복 보드의 human-readable 상태 요약이 필요할 때만 만드는 선택 파일이다.
- 새 `board_state` 파일은 `world/live/docs/community_map.md`에 보드가 먼저 `registered` 상태로 등록되고, 실제로 추적할 상태가 생겼을 때만 추가한다.
- smoke test나 실험용 run 결과가 여기에 있어도, 별도 승인과 live 문서 반영 전까지는 캐논 상태로 간주하지 않는다.
- legacy `BOARD-0001~BOARD-0018` 형식은 은퇴했으며 다시 사용하지 않는다.
- 과거 고정 보드 모델의 역사 자료는 `world/archive/quarantine/`를 본다.
