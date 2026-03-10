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
- story_arcs: docs/story_arcs.md
- foreshadow_registry: docs/foreshadow_registry.md
- episode_deltas: docs/episode_deltas.md
- style_bible: docs/style_bible.md
- community_memory: docs/community_memory.md
- community_grammar_layer_b: docs/community_grammar_layer_b.md
- writing_index: writing/README.md
- style_constitution: writing/style/style_constitution.md
- voice_fingerprint_spec: docs/voice_fingerprint_spec.md
- quarantine_index: quarantine/README.md

## Recent changes (selected)
- 2026-03-10 SIM-ARCH-001: `Quick Sim 기본 / API fallback` 구조를 채택하고 simulation_playbook/simulation_state_index 운영 기준을 재정렬
- 2026-03-10 LAYERB-011: community_grammar_layer_b에 ATOM-012 추가 — AI 자동화 외피 아래 인간 백엔드가 숨어 있는 역자동화 노동 놀이 문법 반영
- 2026-03-09 LAYERB-010: community_grammar_layer_b에 ATOM-011 추가 — 이름 음절 하나로 범주와 장비 체계를 과잉 확장하는 명칭 literal reading 문법 반영
- 2026-03-09 LAYERB-009: community_grammar_layer_b에 `GRAMMAR-001~003` 초안 추가 — 결함 승격형 조롱 / 역설적 지지 합창 / 권위의 바닥화 재해석 축으로 Layer B 상위 규칙 1차 합성
- 2026-03-09 LAYERB-008: community_grammar_layer_b에 ATOM-010 추가 — 악평처럼 시작해 후원/고평점으로 끝나는 애증형 헌정 문법 반영
- 2026-03-09 LAYERB-007: community_grammar_layer_b에 ATOM-009 추가 — 미담/정사를 약탈·수금·조폭 프레임으로 재해석하는 문법 반영
- 2026-03-09 LAYERB-006: community_grammar_layer_b에 ATOM-008 추가 — 황당한 난동 사유를 집단이 정당화 밈으로 승인하는 문법 반영
- 2026-03-09 LAYERB-005: community_grammar_layer_b에 ATOM-007 추가 — 지시문 오독이 음담성 말장난과 인간 우월 밈으로 번지는 문법 반영
- 2026-03-08 WORLDBUILD-016: 마나 주색 체계의 공식 명칭을 `자(紫)` 기준으로 정리하고, 자탑/자계열 표기를 live 문서·생성 스크립트·집필 입력 전반에 반영
- 2026-03-08 WORLDBUILD-015: 아르케이온 단계 명칭을 `하급 과정 / 상급 과정`으로 통일하고, `상급 과정 진입성취평가`를 포함한 서사 허브/hand off/academy bible 표현을 재정렬
- 2026-03-08 WORLDBUILD-014: WB-0015와 서사 허브를 추가 조정해 본과는 `입학 즉시 전공 확정` 구조로 고정하고, 기초 표준식/체술/안전/기록 교육을 하급 아카데미 3년으로 이관
- 2026-03-08 WORLDBUILD-013: WB-0015/narrative_state/story_arcs/NC-0001/handoff에 `12~14세 하급 아카데미 + 15세 본과 진입성취평가` 구조를 반영하고, 3년 스킵 뒤 각인술 선택 클리프행어를 본과 도입선으로 고정
- 2026-03-08 WRITING-008: pre-academy 정체성 축 재조정 — 입학 전에는 `칼리온 시험 통과` 수준의 안도만 주고, `그럼에도 내 아들이다` 확언은 학술원 진입 후로 이연
- 2026-03-08 WRITING-007: `narrative_state`/`story_arcs`/handoff에 학술원 입학 목표 시점(`ep010` 전후)과 그 이전 필수 처리 이벤트(칼리온 확언, 키리온 정체성 수렴) 추가
- 2026-03-08 WORLDBUILD-012: NC-0001과 handoff에 주인공 정체성의 META 진실을 추가 — 자전적 앵커 기억 제거, 지식/사고 구조 이식, 장기적으로 `키리온 렌바렌`으로 수렴
- 2026-03-08 WORLDBUILD-011: 혼인 후 성 표기를 `출생 가문 성 유지 + 혼인 가문 직위` 규칙으로 정리하고 셀리아 표기를 `셀리아 그라비온`으로 교정
- 2026-03-08 WORLDBUILD-010: 리리아 렌바렌(EX-0004) 카드 신설, 그라비온 진위감정 잔향 설정 및 가족/키리온 참조 실명화
- 2026-03-08 WORLDBUILD-009: 데리온 렌바렌(EX-0003) 카드 신설, 부모/키리온 카드 참조 실명화, 장남의 강압적 보호자 성격/말투 앵커 확정
- 2026-03-08 WORLDBUILD-008: WB-0009/0026, EX-0001/0002, NC-0001에 렌바렌 식흔 후계자를 여동생에서 10세 장남으로 교체하고, 장남의 `계승조회식` 이후 혼란/목검 사건 동기를 반영
- 2026-03-08 WORLDBUILD-007: WB-0005/0009/0018/0026, NC-0001에 "마법 사용 경험자와 미사용자의 감정 차이"를 추가해 조기 수련 금지 규정의 실효 근거를 보강
- 2026-03-08 WORLDBUILD-006: WB-0005/0009/0015/0026, EX-0001, NC-0001에 `계승조회식` 이전 아동 마법 수련 금지와 귀족 견제용 특별조사, 선행학습 특권 격차를 반영
- 2026-03-08 WORLDBUILD-005: 서명귀족 혈통 아동 10세 검증 행사 공식 명칭을 `계승조회식`으로 확정하고 live 문서 전반 표현을 통일
- 2026-03-08 WORLDBUILD-004: WB-0009/0026, EX-0001, NC-0001에 서명귀족 혈통 아동 10세 `계승조회식`과 조기 사설 검증 금지 규칙을 반영
- 2026-03-08 WORLDBUILD-003: WB-0009/0026, EX-0001, NC-0001에 렌바렌 가문 방계 청소 규약과 라베르니온 종속 정보권력 구도를 반영
- 2026-03-07 WRITING-006: 프롤로그/1화 리라이트 캐논(`프롤로그_리라이트_v2.md`, `1화_리라이트_v2.md`)을 current canon으로 반영하고 live 서사 허브/NC-0001/집필 인덱스를 새 내용 기준으로 동기화
- 2026-03-06 WRITING-005: episode 폴더에 `canon/` 하위 규칙을 도입하고, current canon은 `canon/README.md`로 명시하도록 집필 산출물 구조를 정리
- 2026-03-06 WRITING-004: `narrative_state`를 활성 허브로 재작성하고 `story_arcs`/`foreshadow_registry`/`episode_deltas`를 추가해 장기 연재용 컨텍스트 압축 체계를 도입
- 2026-03-06 COMMUNITY-RULE-001: community_map/simulation_playbook/board_states README에 동적 게시판 생성/승격/상태 추적 규칙 명시
- 2026-03-06 COMMUNITY-RETIRE-001: live 18보드 bootstrap stub 제거, 커뮤니티 운영 기준을 동적/온디맨드 모델로 재고정
- 2026-03-06 WRITING-003: ep001 "선물" 2차 개정본을 캐논(`canon/revision_v2.txt`)으로 확정, diff_v2 작성, style_constitution.md 갱신
- 2026-03-06 LAYERB-004: community_grammar_layer_b에 ATOM-006 추가 — 명명법 질문이 종족 RP/상호 비하 배틀로 번지는 문법 반영
- 2026-03-06 LAYERB-003: community_grammar_layer_b에 ATOM-005 추가 — "지지 철회" 형식의 동일시/방어 서약 문법 반영
- 2026-03-05 VFP-001: Voice Fingerprint 시스템 신설 — voice_fingerprint_spec.md 작성, NC-0001 VFP v1 추출 완료
- 2026-03-05 WRITING-002: ep001 "선물" 집필 프롬프트 v1 작성. 프롤로그 자→흑색 수정 반영(canon/revision_v1.txt, draft_v1.txt, style_constitution.md)
- 2026-03-05 WRITING-001: writing/ 폴더 계층 신설 — 집필 파이프라인(프롬프트/초안/수정본/diff/문체 헌법) 구조화. 프롤로그 프롬프트 v1 작성 완료
- 2026-03-05 WORLDBUILD-001: WB-0011에 열구 외계 문명 유입 3층 정보 구조 추가 (공공 상식/국가 기밀/마사토라 전략)
- 2026-03-05 WORLDBUILD-002: WB-0009/0026에 렌바렌 백작가 설정 추가 — 비밀 서명귀족, 식흔(蝕痕, 흑 주색, 타인 마법 잔흔 실시간 소거), 왕국 최상위 정보기관 수장
- 2026-03-05 LAYERB-002: community_grammar_layer_b에 ATOM-002(자기비하적 기여 선언), ATOM-003(상호 비열의 서사시화) 추가
- 2026-03-04 PR-BOOTSTRAP-0006: [RESET] NC-* 코어 캐스트 전면 삭제 — 생성 규칙 재설계 진행 중
- 2026-03-04 PR-BOOTSTRAP-0002-RETIRE: 기존 CH-* 캐릭터 카드/보이스팩/퍼소나 상태 체계 폐기(영구 삭제), P-* 동적 생성 체계로 전환
