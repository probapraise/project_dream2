# master_map

## What is this
- 이 파일은 오케스트레이터가 항상 로딩하는 유일한 문서다.
- 다른 문서는 필요할 때만 로딩한다.
- 본 저장소는 월드 바이블 + P-* 모집단 슬롯 기반 동적 인물 생성 체계를 운용하는 **부트스트랩 산출물**이다.
- 원문 출처: `Pramisio_WorldBible_Unified_v1_2_20260302_AcademyCharacterCards.docx`

## Repo layout (quick)
- docs/: 인덱스/상태/워크플로우 문서(항상 가볍게 유지)
- world_bible/: 세계관 섹션(가변 로딩, PUBLIC/CONFIDENTIAL/META 분리)
- population/: P-* 모집단 SSOT + 코어 캐스트 카드(`core_cast/`)
- characters/: deprecated 스텁(기존 CH-* 체계 폐기)
- layer_b/: 활성 게시판 문화(동적 생성, 현재 비어 있음)
- voice_packs/: deprecated 스텁(기존 CH-* 체계 폐기)
- persona_states/: deprecated 스텁(기존 CH-* 상태 폐기)
- board_states/: 시뮬레이션 후 갱신되는 상태
- quarantine/: 충돌 가능성이 있는 레거시 문서 보존 구역

## Index pointers
- world_bible_index: docs/world_bible_index_v2.md
- world_bible_index_legacy: docs/world_bible_index.md
- community_map: docs/community_map.md
- character_index: docs/character_index_v2.md
- core_cast_bootstrap: docs/core_cast_bootstrap_v1.md
- character_index_legacy: docs/character_index.md
- simulation_playbook: docs/simulation_playbook.md
- dynamic_guide: docs/dynamic_guide.md
- simulation_feedback: docs/simulation_feedback.md
- simulation_state_index: docs/simulation_state_index.md
- narrative_state: docs/narrative_state.md
- style_bible: docs/style_bible.md
- community_memory: docs/community_memory.md
- community_grammar_layer_b: docs/community_grammar_layer_b.md
- quarantine_index: quarantine/README.md

## Recent changes (last 6)
- 2026-03-04 PR-BOOTSTRAP-0006: [RESET] NC-* 코어 캐스트 전면 삭제 — 생성 규칙 재설계 진행 중
- 2026-03-04 PR-BOOTSTRAP-0002-RETIRE: 기존 CH-* 캐릭터 카드/보이스팩/퍼소나 상태 체계 폐기(영구 삭제), P-* 동적 생성 체계로 전환
- 2026-03-03 PR-BOOTSTRAP-0003: 커뮤니티 구조(각인광장 B01~B18) -> community_map + layer_b 18개 초안 생성
- 2026-03-04 PR-BOOTSTRAP-0004: character_index_v2를 P-* SSOT 기준으로 재정렬
- 2026-03-03 PR-BOOTSTRAP-0005: simulation_playbook 및 상태/피드백 템플릿 파일 생성
- 2026-03-04 PR-CLEANUP-RESTART-0002: quarantine에서 재사용 가능한 동적 규칙만 활성 가이드로 재흡수
