# master_map

## What is this
- 이 파일은 오케스트레이터가 항상 로딩하는 유일한 문서다.
- 다른 문서는 필요할 때만 로딩한다.
- 본 저장소는 기존 월드 바이블(Word) + 캐릭터 카드(구 포맷)를 v2 스펙(분할 섹션 + 2레이어 캐릭터 카드)로 이관한 **부트스트랩 산출물**이다.
- 원문 출처: `Pramisio_WorldBible_Unified_v1_2_20260302_AcademyCharacterCards.docx`

## Repo layout (quick)
- docs/: 인덱스/상태/워크플로우 문서(항상 가볍게 유지)
- world_bible/: 세계관 섹션(가변 로딩, PUBLIC/CONFIDENTIAL/META 분리)
- characters/: 캐릭터 카드(2 레이어, 게시판 비종속)
- layer_b/: 2026-03-04 정리로 초기화됨(재생성 대기)
- voice_packs/: 보이스 유지용(주요 인물 우선, 현재는 전원 초안 생성)
- persona_states/, board_states/: 시뮬레이션 후 갱신되는 상태(초기값 템플릿)

## Index pointers
- world_bible_index: docs/world_bible_index_v2.md
- world_bible_index_legacy: docs/world_bible_index.md
- character_index: docs/character_index_v2.md
- character_index_legacy: docs/character_index.md
- simulation_playbook: docs/simulation_playbook.md
- simulation_feedback: docs/simulation_feedback.md
- simulation_state_index: docs/simulation_state_index.md
- narrative_state: docs/narrative_state.md
- style_bible: docs/style_bible.md
- community_memory: docs/community_memory.md
- cleanup_note: 고정 4x18/스키마 강제 문서 삭제(2026-03-04)

## Recent changes (last 5)
- 2026-03-03 PR-BOOTSTRAP-0002: Appendix G Character Pack 162명 카드 -> characters/*.md (2-layer) 변환 + voice_packs 생성
- 2026-03-03 PR-BOOTSTRAP-0003: 커뮤니티 구조(각인광장 B01~B18) -> community_map + layer_b 18개 초안 생성
- 2026-03-03 PR-BOOTSTRAP-0004: character_index/legacy_id_map 생성
- 2026-03-03 PR-BOOTSTRAP-0005: simulation_playbook 및 상태/피드백 템플릿 파일 생성
- 2026-03-04 PR-CLEANUP-0001: 고정 4x18/스키마 강제 문서 삭제 + world_bible_index 재생성 + Zone.Identifier 정리
