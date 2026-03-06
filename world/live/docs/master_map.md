# master_map

## What is this
- 이 파일은 오케스트레이터가 항상 로딩하는 유일한 문서다.
- 다른 문서는 필요할 때만 로딩한다.
- 본 저장소는 월드 바이블 + P-* 모집단 슬롯 기반 동적 인물 생성 체계를 운용하는 **부트스트랩 산출물**이다.
- 원문 출처명: `Pramisio_WorldBible_Unified_v1_2_20260302_AcademyCharacterCards.docx` (원본 파일은 현재 저장소에 포함되어 있지 않음)

## Path convention
- 이 문서의 `docs/...`, `world_bible/...`, `population/...`, `writing/...`, `quarantine/...` 표기는 모두 현재 bundle 루트인 `world/live/` 기준 상대경로다.
- 저장소 루트 기준 실제 경로가 필요하면 앞에 `world/live/`를 붙여 해석한다. 예: `docs/master_map.md` -> `world/live/docs/master_map.md`

## Repo layout (quick)
- docs/: 인덱스/상태/워크플로우 문서(항상 가볍게 유지)
- world_bible/: 세계관 섹션(가변 로딩, PUBLIC/CONFIDENTIAL/META 분리)
- population/: P-* 모집단 SSOT + 코어 캐스트 카드(`core_cast/`)
- external/: EX-* 외곽 인물 슬롯(학술원 바깥 서사 인물, 시뮬 필드 포함, 커뮤니티 미투입)
- characters/: deprecated 스텁(archive-linked, 기존 CH-* 체계 폐기)
- layer_b/: 활성 게시판 문화(동적 생성, 현재 비어 있음)
- voice_packs/: deprecated 스텁(archive-linked, 기존 CH-* 체계 폐기)
- persona_states/: deprecated 스텁(archive-linked, 기존 CH-* 상태 폐기)
- board_states/: 시뮬레이션 후 갱신되는 상태
- writing/: 집필 파이프라인 산출물(artifact-linked)
- quarantine/: 충돌 가능성이 있는 레거시 문서 보존 구역(archive-linked)

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
- voice_fingerprint_spec: docs/voice_fingerprint_spec.md
- quarantine_index: quarantine/README.md

## Recent changes (selected)
- 2026-03-06 WRITING-003: ep001 "선물" 2차 개정본을 캐논(revision_v2.txt)으로 확정, diff_v2 작성, style_constitution.md 갱신
- 2026-03-06 LAYERB-004: community_grammar_layer_b에 ATOM-006 추가 — 명명법 질문이 종족 RP/상호 비하 배틀로 번지는 문법 반영
- 2026-03-06 LAYERB-003: community_grammar_layer_b에 ATOM-005 추가 — "지지 철회" 형식의 동일시/방어 서약 문법 반영
- 2026-03-05 VFP-001: Voice Fingerprint 시스템 신설 — voice_fingerprint_spec.md 작성, NC-0001 VFP v1 추출 완료
- 2026-03-05 WRITING-002: ep001 "선물" 집필 프롬프트 v1 작성. 프롤로그 보라→흑색 수정 반영(revision_v1.txt, draft_v1.txt, style_constitution.md)
- 2026-03-05 WRITING-001: writing/ 폴더 계층 신설 — 집필 파이프라인(프롬프트/초안/수정본/diff/문체 헌법) 구조화. 프롤로그 프롬프트 v1 작성 완료
- 2026-03-05 WORLDBUILD-001: WB-0011에 열구 외계 문명 유입 3층 정보 구조 추가 (공공 상식/국가 기밀/마사토라 전략)
- 2026-03-05 WORLDBUILD-002: WB-0009/0026에 렌바렌 백작가 설정 추가 — 비밀 서명귀족, 식흔(蝕痕, 흑 주색, 타인 마법 잔흔 실시간 소거), 왕국 최상위 정보기관 수장
- 2026-03-05 LAYERB-002: community_grammar_layer_b에 ATOM-002(자기비하적 기여 선언), ATOM-003(상호 비열의 서사시화) 추가
- 2026-03-04 PR-BOOTSTRAP-0006: [RESET] NC-* 코어 캐스트 전면 삭제 — 생성 규칙 재설계 진행 중
- 2026-03-04 PR-BOOTSTRAP-0002-RETIRE: 기존 CH-* 캐릭터 카드/보이스팩/퍼소나 상태 체계 폐기(영구 삭제), P-* 동적 생성 체계로 전환
- 2026-03-03 PR-BOOTSTRAP-0003: 커뮤니티 구조(각인광장 B01~B18) -> community_map + layer_b 18개 초안 생성
