# narrative_state

## Sync metadata
- sync_category: required
- last_synced_episode: ep002
- sync_source: artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md
- sync_source_sha256: 17673b87624ec2a117ae5776a5ebf816a593199f158942f07badf25f84528203
- sync_summary: artifacts/writing/episodes/ep002/summary_v1.md

역할: 작가가 다음 회차 집필 전에 기본 로딩하는 서사 상태 허브. 과거 회차 전체를 다시 읽는 대신, 현재 활성 상태와 다음 진행 방향만 유지한다.

## Current canon frontier
- latest_canon_episode: `ep002` (`artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md`)
- macro_position: Part 1 오프닝 / 렌바렌 저택 생존 부트스트랩 / 하급 과정 진입 전
- default_load_order:
  - 1. `docs/narrative_state.md`
  - 2. `docs/story_arcs.md`에서 `status: active` arc만
  - 3. `docs/foreshadow_registry.md`에서 `status: open` 항목만
  - 4. `docs/episode_deltas.md`에서 직전 1~2화만
  - 5. `writing/style/house_rules.md` + `docs/style_bible.md`
  - 6. 집필 대상 회차의 `writing/episodes/<episode_id>/episode_style_constitution_vN.md`, `setting_brief_vN.md`, `prompt_packet_vN.md`, `prompt_vN.md` (준비된 경우)

## Narrative context policy
- 전체 원고 재로딩은 canon 충돌 검증이나 세부 디테일 회수가 필요할 때만 한다.
- 회차 종료 후에는 사건 요약보다 상태 변화만 `docs/episode_deltas.md`에 추가한다.
- 5~10화 단위로 `docs/story_arcs.md`를 압축 갱신하고, 이 문서에는 활성 항목만 남긴다.
- 복선 회수/폐기 여부는 `docs/foreshadow_registry.md`에서 먼저 처리한 뒤 이 문서를 갱신한다.

## Active foreshadowing
- `FS-001`: 칼리온은 키리온의 말투, 반응 속도, 독서 습관을 통해 정체 변조 여부를 추적 중이다.
  - planted: `ep000`
  - latest carry: `ep002`에서 시험장이 `흑색 입문서를 읽는가`에서 `서고에서 무엇을 먼저 고르는가`로 확장됨
  - payoff window: pre-academy
- `FS-002`: 셀리아의 돌봄은 안전지대이면서 동시에 주인공의 경계심을 느슨하게 만드는 위험한 이완 장치다.
  - planted: `ep000`
  - latest carry: `ep002`에서 칭찬 직후의 부드러운 꾸지람이 보호와 긴장을 동시에 강화함
  - payoff window: pre-academy recurring beat
- `FS-003`: 렌바렌 저택 행정/정보 흐름에는 집사실 중심의 단일 병목이 있다.
  - planted: `ep001`
  - latest carry: `ep002`에서 조악한 안내판만으로도 질문 경로와 실무 동선이 실제로 바뀌는 것이 증명됨
  - payoff window: pre-academy planning -> academy scale-up
- `FS-004`: `흑색 표준식 입문서`는 선물이 아니라 지속형 심문 장치다.
  - planted: `ep001`
  - latest carry: `ep002` 종료 시점에서 책 읽기 자체보다 `첫 선택 구조 전체`가 채점 대상이라는 사실이 확정됨
  - payoff window: immediate (`ep003` 인접)
- `FS-005`: 치유사의 무해 판정은 "들키지 않았다"이지 "안전하다"가 아니다.
  - planted: `ep001`
  - latest carry: 치유사는 외상/마나 흐름만 확인했고 정체 문제는 판정 대상이 아니었다
  - payoff window: pre-academy
- `FS-006`: 주인공의 장기 목표는 이 세계의 정보 인프라/커뮤니티 구조를 만드는 것이다.
  - planted: `ep000`
  - latest carry: `ep002`에서 안내판 실험이 첫 소규모 성공을 거두며 구상이 실제 설계 경험으로 전환됨
  - payoff window: long horizon
- `FS-007`: 데리온은 동생의 마법책 접근과 이상 징후에 유독 예민하게 반응한다.
  - planted: `ep002`
  - latest carry: 키리온이 `첫 책 선택` 시험을 정면으로 받지 않기 위해 데리온 개입을 유도하는 우회 해법을 세움
  - payoff window: immediate (`ep003` 인접)

## Character arcs
- `NC-0001 / 키리온 렌바렌`
  - current state: "원래 키리온답게 보이기"의 일부 규칙을 확보했지만, 그 위장만으로는 칼리온의 관찰을 더 못 버틴다고 판단한 상태
  - latest turn: 리리아를 통해 행동 모델을 회수하고, 집사실 안내판으로 첫 설계 성공을 거둔 뒤, 서고 시험을 데리온 개입으로 비틀려 한다
  - next pressure: 서고 접근권과 첫 책 선택이 모두 진술서가 된 상황에서, 자기 사고 방식의 출처를 얼마나 숨길 수 있는가
- `칼리온 렌바렌`
  - current state: 직접 추궁보다 허가, 칭찬, 선택지 제공으로 다음 시험장을 여는 감시자
  - latest turn: 안내판 효용을 확인한 뒤 서고 접근권과 자색 입문서 열람 허가를 미끼처럼 던져, 시험 단위를 `행동`에서 `선택 구조`로 확장했다
  - next pressure: 친절과 보상을 늘려도 독자가 위협을 더 강하게 느끼게 해야 한다
- `셀리아 그라비온`
  - current state: 주인공에게 유일한 무계산 온기를 제공하는 보호자
  - latest turn: 안내판 사건 뒤 칭찬과 잔소리를 함께 주며 보호자 포지션을 더 선명하게 굳혔다
  - next pressure: 안전지대이되 완전한 피난처로 보이면 긴장이 죽는다
- `리리아 렌바렌`
  - current state: 귀엽기만 한 막내가 아니라, 사람 사이를 뛰어다니며 정보와 분위기를 함께 움직이는 정서적/실무적 조력자
  - latest turn: 키리온이 `원래 키리온` 행동 규칙을 회수하고, 집사실 실험을 굴리는 데 필요한 자연스러운 메신저이자 실행 엔진으로 기능했다
  - next pressure: 장면 편의용 도우미가 아니라, 자기 성격과 자랑 욕구로 움직이는 인물로 계속 유지되어야 한다

## Macro structure position
- 현재 구간의 핵심 질문:
  - 주인공은 렌바렌 저택 안에서 얼마나 오래 정체를 숨길 수 있는가
  - 칼리온의 관찰망 아래에서 어디까지 "아이답게" 굴 수 있는가
  - 첫 설계 성공 이후, 저택 내부의 작은 실무 개입을 어디까지 넓히되 자기 사고 방식의 출처는 숨길 수 있는가
- 현재 구간의 기능:
  - 하급 과정 진입 전, 가문/가정/행정 구조를 독자에게 익히게 하는 준비 구간
  - 코어 캐스트 대량 투입 전, 주인공 1인 시점의 생존 규칙과 장기 공론장 욕망의 씨앗을 먼저 고정하는 구간
- 현재 배치 목표:
  - 아르케이온 권역 첫 진입(12세 하급 과정 입학식/첫 수업/환경 노출)은 잠정적으로 `ep010` 전후를 목표로 둔다.
  - 본격적인 상급 과정 서사는 `15세 상급 과정 진입성취평가 -> 입학 즉시 전공 선택` 시점에서 연다.
  - 그 이전에는 칼리온의 `시험을 일단 넘겼다`는 정도의 가벼운 안도만 주인공이 캐치하도록 한다.
  - 칼리온이 실제로 이계 지식의 존재와 그 영향을 알고 있으며, 그럼에도 주인공을 아들로 판단했다는 진실은 더 뒤의 가족 이벤트에서 공개한다.

## Next 3-5 episode direction
- `ep003` 우선 과제는 `서고 접근권`과 `첫 책 선택`을 둘러싼 관찰전이다.
- 주인공은 서고 시험을 정면으로 받지 않고, 데리온의 개입으로 시험장을 비틀려 한다.
- 렌바렌 저택 내부의 권한 분배, 형제 간 긴장, 서고 접근의 민감도를 함께 노출한다.
- 집사실 안내판 성공이 곧바로 더 큰 설계 도약으로 이어지지는 않는다. 작은 성취가 즉시 더 정교한 감시와 선택 압박으로 돌아오는 흐름을 유지한다.
- 하급 과정 입학은 멀리 있는 목표로만 남기고, 당장은 저택 내부 생존과 관찰 회피를 우선한다.
- 다만 장기적으로는 `12세 하급 과정에서 게시판 설계의 병목 파악 -> 3년 스킵 -> 15세 상급 과정 진입성취평가와 입학 즉시 각인술 선택` 구조를 염두에 둔다.
- 입학 전 저택 파트의 종점은 `완전한 확언`이 아니라 `일단은 버텼다/통과했다`는 안도감이다.
- 최종 정체성 판정과 `그럼에도 내 아들이다` 확언은 학술원 진입 후 한 번 더 무게를 축적한 뒤 회수한다.

## Tone / high-level style notes
- 감각 묘사는 정지 화면보다 시간축 위에서 움직이게 쓴다.
- 긴장 구간은 짧은 문장과 독립 문단으로 박자를 찍는다.
- 돌봄과 일상성은 안심이 아니라 위험한 이완으로 작동해야 한다.
- 건조한 긴장 속에도 하인/집사실 장면처럼 낮은 농담과 생활 소음이 섞여야 세계의 온도가 살아난다.
- 개발자적 분석은 설계 직전에서 끊고, 독자가 다음 판단을 기다리게 만든다.
- "아버지/어머니" 호칭 전환은 관계 온도와 긴장도에 맞춰 유동적으로 운용한다.

## Companion docs
- arc compression: `docs/story_arcs.md`
- foreshadow registry: `docs/foreshadow_registry.md`
- episode state-change log: `docs/episode_deltas.md`
