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
- external/: EX-* 외곽 인물 슬롯(학술원 바깥 서사 인물, 시뮬 필드 포함, 커뮤니티 미투입)
- characters/: deprecated 스텁(기존 CH-* 체계 폐기)
- layer_b/: 활성 게시판 문화(동적 생성, 현재 비어 있음)
- voice_packs/: deprecated 스텁(기존 CH-* 체계 폐기)
- persona_states/: deprecated 스텁(기존 CH-* 상태 폐기)
- board_states/: 시뮬레이션 후 갱신되는 상태
- writing/: 집필 파이프라인 산출물(프롬프트/초안/수정본/diff/문체 헌법)
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
- writing_index: writing/README.md
- style_constitution: writing/style/style_constitution.md
- quarantine_index: quarantine/README.md

## Recent changes (last 6)
- 2026-03-05 WRITING-001: writing/ 폴더 계층 신설 — 집필 파이프라인(프롬프트/초안/수정본/diff/문체 헌법) 구조화. 프롤로그 프롬프트 v1 작성 완료
- 2026-03-05 WORLDBUILD-001: WB-0011에 열구 외계 문명 유입 3층 정보 구조 추가 (공공 상식/국가 기밀/마사토라 전략)
- 2026-03-05 WORLDBUILD-002: WB-0009/0026에 렌바렌 백작가 설정 추가 — 비밀 서명귀족, 식흔(蝕痕, 흑 주색, 타인 마법 잔흔 실시간 소거), 왕국 최상위 정보기관 수장
- 2026-03-05 LAYERB-002: community_grammar_layer_b에 ATOM-002(자기비하적 기여 선언), ATOM-003(상호 비열의 서사시화) 추가
- 2026-03-04 PR-BOOTSTRAP-0006: [RESET] NC-* 코어 캐스트 전면 삭제 — 생성 규칙 재설계 진행 중
- 2026-03-04 PR-BOOTSTRAP-0002-RETIRE: 기존 CH-* 캐릭터 카드/보이스팩/퍼소나 상태 체계 폐기(영구 삭제), P-* 동적 생성 체계로 전환
- 2026-03-03 PR-BOOTSTRAP-0003: 커뮤니티 구조(각인광장 B01~B18) -> community_map + layer_b 18개 초안 생성
