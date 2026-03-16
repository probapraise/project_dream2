# simulation_feedback

## Status
- last_updated: 2026-03-06
- 이 문서는 post-run 관찰/문제/후속 작업 메모를 적는 운영 문서다.
- 실제 run registry와 산출물 위치는 `docs/simulation_state_index.md`를 먼저 본다.
- 기존 `voice_pack`, `character_card 10명 보정` 체크리스트는 폐기되었다.
- run 해석 전에는 반드시 해당 실행의 `temporal_frame`을 확인한다.
- 별도 표기가 없으면 cold-start/board bootstrap run은 current canon 장면이 아니라 academy_sandbox 검증으로 읽는다.

## Current run baseline
- 등록된 cold-start run:
  - `simrun-001_cold_start.json`
  - `simrun-002_pro_cold_start.json`
  - `simrun-003_pro_thinking_cold_start.json`
- 대응 실행 게이트 산출물:
  - `runs/RUN-PHASE3-SMOKE/`
  - `runs/RUN-PHASE3-LEGACY/`
  - `runs/RUN-20260304-TEMPLATE-SMOKE/`

## Common issues to watch
- 게시판 톤과 실제 반응 로그가 어긋나는지
  - Layer A는 board별 창발 경향, Layer B는 낙서장 고정 문법이므로 서로 섞여 보이면 구분 실패다.
- META/CONFIDENTIAL 정보가 출력에 섞여 나오지 않는지
  - 실행 전후 게이트 산출물(`manifest`, `pre_injection_gate`, `output_leak_scan`)을 같이 확인한다.
- 반응자 선발 풀이 과하게 한쪽으로 쏠리지 않는지
  - 직능/배경/기숙사 분포와 실제 sampled participant를 같이 본다.
- board_state 반영이 run 결과와 맞는지
  - artifact output에서 live `board_states/*.json`으로 promote된 결과가 누락/오반영되지 않았는지 확인한다.
- VFP 후속 작업 대상이 생겼는지
  - named/core_cast 또는 반복 등장 instantiated 인물은 `voice_fingerprint` 추출 후보로 올린다.

## Post-run checklist
- [ ] `docs/simulation_state_index.md`에 새 run/call/view/gate/payload 경로 등록
- [ ] `board_states/*.json` 또는 관련 상태 문서에 실제 반영 결과 연결
- [ ] Layer A 창발 패턴이 보이면 `community_grammar_layer_a.md`의 CULTURE 후보로 메모
- [ ] Layer B와 직접 충돌하는 밈/문법이면 `community_grammar_layer_b.md`와 충돌 여부 검토
- [ ] 반복 등장 인물의 말투가 안정적으로 관찰되면 `voice_fingerprint` 추출 후보로 기록
- [ ] `community_memory.md` 또는 후속 world_ops change case 필요 여부 판단

## Follow-up rule
- 이 문서에는 run별 세부 로그를 길게 복붙하지 않는다.
- run별 상세 관찰은 필요 시 날짜/`run_id` 기준의 짧은 메모만 남기고, 원본 경로는 `simulation_state_index`에 연결한다.
- 폐기된 CH-*/voice_pack/persona_state 체계 용어는 사용하지 않는다.
