# simulation_playbook

## Purpose
- 커뮤니티 시뮬레이션을 "항상 같은 규칙"으로 돌리기 위한 1페이지 운영 규정.
- 시뮬레이션은 **출력(Writer Report)** 을 만들기 위한 도구이며, 세계관/상태 파일의 자동 변경은 "정식 모드(official)"에서만 제안한다.

## Inputs (minimum)
- seed (1~3문장) -> `seed_normalized.json`
- public_lore_pack (PUBLIC만) -> `runs/<RUN>/public_lore_pack.md`
- board scope -> `docs/community_map.md` + `layer_b/*.md`
- persona pool -> `docs/character_index.md` + `characters/*.md`
- (posters에 한해) `voice_packs/*.md`

## Visibility rule (hard)
- world_bible 섹션은 PUBLIC/CONFIDENTIAL/META를 가진다.
- PersonaAgent에게는 원칙적으로 **public_lore_pack만 제공**한다. (META/CONFIDENTIAL 원문 직접 주입 금지)
- Moderator/Orchestrator는 필요 시 CONFIDENTIAL/META를 읽을 수 있으나, 출력에 스포일러를 유출하지 않는다.

## Funnel (awareness -> reaction) (required)
1) awareness_pool: seed 관련성 기반 300~500명(추정) 선별
2) 분류:
   - lurkers: 수치만
   - low_reactors: 그룹 단위 반응(추천/비추천/짧은 코멘트)
   - commenters: 30~50명, 1~3줄
   - posters(first movers 포함): 5~15명, 풀 컨텍스트(+voice_pack)
3) 산출물: `selected_personas.json` (IDs만)

## Round loop (default)
- R1: first movers 2~5명이 게시글 생성
- R2: 댓글/추천 중심 반응
- R3: 토론 심화(대댓글, 교차 보드 유입, 신규 진입)
- R4+: 수렴 감지 시 종료

### Information isolation (hard)
- 같은 라운드의 에이전트들은 서로의 출력을 볼 수 없다.
- 각 에이전트 입력에는 "이전 라운드까지 게시된 내용"만 포함한다.

## Output contract (agent JSON)
- Orchestrator: Simulation Plan JSON 1개
- PersonaAgent: post/comment/reaction JSON 1개
- SummarizerAgent: Writer Report 요약 JSON 1개
- (옵션) ModeratorAgent: actions JSON 1개
- (정식 모드) StateUpdateAgent: proposal JSON 1개

## Stop conditions (default)
- max_rounds 도달
- 신규 논점/갈등이 2라운드 연속 추가되지 않음(수렴)
- Moderator 조치로 스레드가 잠금/중단

## State update policy
- explore 모드: 상태 파일 변경 없음(출력만)
- official 모드:
  - persona_states/, board_states/, docs/community_memory.md 갱신안을 "제안(PR)"으로 생성
  - 작가 승인 후 apply

## Notes
- layer_b는 시뮬 품질의 핵심 레버다. 밈/금기/말투가 어색하면 먼저 layer_b를 수정한다.
- 본 playbook은 부트스트랩 초안이며, 첫 1~3회 시뮬레이션 피드백을 반영해 갱신한다.
