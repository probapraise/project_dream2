# narrative_state

## Sync metadata
- sync_category: required
- last_synced_episode: ep003
- sync_source: artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md
- sync_source_sha256: 340f47e4338f88d9ef3dc38d7a5276e77208fc29dd2ba8ccbd59825178c12e2c
- sync_summary: artifacts/writing/episodes/ep003/summary_v1.md

역할: 작가가 다음 회차 집필 전에 기본 로딩하는 서사 상태 허브. 과거 회차 전체를 다시 읽는 대신, 현재 활성 상태와 다음 진행 방향만 유지한다.

## Current canon frontier
- latest_canon_episode: `ep003` (`artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md`)
- macro_position: Part 1 오프닝 / 렌바렌 저택 생존 부트스트랩 / 하급 과정 진입 전
- default_load_order:
  - 1. `docs/narrative_state.md`
  - 2. `docs/memory_tiers/recent.md`
  - 3. `docs/memory_tiers/current_arc.md`
  - 4. `docs/memory_tiers/entity_registry.md`
  - 5. `docs/memory_tiers/knowledge_state_registry.md`
  - 6. `docs/memory_tiers/access_control_matrix.md`
  - 7. `docs/memory_tiers/long_term.md`
  - 8. `writing/style/house_rules.md` + `docs/style_bible.md`
  - 9. 집필 대상 회차의 `writing/episodes/<episode_id>/episode_style_constitution_vN.md`, `setting_brief_vN.md`, `prompt_packet_vN.md`, `prompt_vN.md` (준비된 경우)
  - 10. 더 깊은 검증이 필요할 때만 `docs/story_arcs.md`, `docs/foreshadow_registry.md`, `docs/episode_deltas.md`, `docs/pre_academy_checkpoint_plan.md`

## Narrative context policy
- 전체 원고 재로딩은 canon 충돌 검증이나 세부 디테일 회수가 필요할 때만 한다.
- `docs/memory_tiers/`는 `story_arcs`, `foreshadow_registry`, `episode_deltas`, core cast 카드에서 뽑아낸 prompt-facing compiled view다.
- `docs/memory_tiers/knowledge_state_registry.md`는 누가 무엇을 알고/의심/오해하는지, `docs/memory_tiers/access_control_matrix.md`는 지금 실제로 열린 권한과 막힌 권한이 무엇인지 별도로 붙잡는다.
- 회차 종료 후에는 사건 요약보다 상태 변화만 `docs/episode_deltas.md`에 추가한다.
- 5~10화 단위로 `docs/story_arcs.md`를 압축 갱신하고, 이 문서에는 활성 항목만 남긴다.
- 복선 회수/폐기 여부는 `docs/foreshadow_registry.md`에서 먼저 처리한 뒤 이 문서를 갱신한다.
- `docs/pre_academy_checkpoint_plan.md`는 집필 입력 기본층이 아니라, academy 진입 전 지급 누락을 막기 위한 pacing companion이다.

## Active foreshadowing
- `FS-001`: 칼리온은 키리온의 말투, 반응 속도, 독서 습관을 통해 정체 변조 여부를 추적 중이다.
  - planted: `ep000`
  - latest carry: `ep003`에서 서고 첫 선택 시험이 실제로 열렸고, 데리온이라는 가족 변수가 끼어들며 관찰 단위가 `책 선택`에서 `가족 반응과 일상 루틴`까지 넓어짐
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
  - latest carry: `ep003`에서 첫 선택 구조가 실제로 열렸지만, 데리온 개입 때문에 감시가 `낮의 서고`에서 `밤 독서까지 포함한 장기 관찰`로 변형됨
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
  - latest carry: `ep003`에서 데리온이 실제로 서고 문밖까지 들이닥쳤고, 그 반응이 `연무장 -> 치유 -> 취침 전 독서` 루틴을 열고 곧바로 며칠짜리 반복으로 굳으며 저택 파트의 새 압력 축이 됨
  - payoff window: immediate (`ep003` 인접)

## Character arcs
- `NC-0001 / 키리온 렌바렌`
  - current state: 서고 첫 선택 시험장을 가족 변수로 한 번 비틀었지만, 그 대가로 `연무장 -> 치유 -> 취침 전 독서`라는 새 루틴이 이미 며칠째 반복 중인 상태
  - latest turn: 자색 입문서를 집은 직후 데리온의 반응을 끌어들여 독서 패턴 감시를 흐렸고, 낮 독서 시간을 잃는 대신 유예를 벌었다. 이제는 드문 데리온 부재일만이 다음 숨통으로 남아 있다
  - next pressure: 이 루틴의 드문 빈틈에서 리리아와 함께 정보/게시판 욕망을 다시 점화하되, 여전히 감시를 키우지 않는 선을 지켜야 한다
- `칼리온 렌바렌`
  - current state: 직접 추궁보다 허가, 칭찬, 선택지 제공으로 다음 시험장을 여는 감시자
  - latest turn: 서고 접근권을 미끼로 `첫 책 선택`과 독서 습관을 읽는 시험장을 열었고, 그 시험이 데리온 변수와 충돌하면서 관찰망이 더 길게 늘어질 여지를 만들었다
  - next pressure: 직접 등장 없이도, 독자가 여전히 `보고 있다`는 느낌을 잃지 않게 해야 한다
- `데리온 렌바렌`
  - current state: 동생의 마법책 접근에 과민하게 반응하며, 보호 충동과 공포와 통제를 구분 못한 채 휘두르는 형
  - latest turn: 서고 문밖까지 들이닥쳐 키리온을 끌어내고, 실전적으로 압축된 대련과 치유를 묶어 새 일상 루틴을 실제로 반복시키기 시작했다
  - next pressure: 단순 폭력성으로 납작해지지 않고, `왜 저렇게까지 하느냐`가 뒤늦게 재평가될 여지를 계속 남겨야 한다
- `셀리아 그라비온`
  - current state: 주인공에게 유일한 무계산 온기를 제공하는 보호자
  - latest turn: 안내판 사건 뒤 칭찬과 잔소리를 함께 주며 보호자 포지션을 더 선명하게 굳혔다
  - next pressure: 안전지대이되 완전한 피난처로 보이면 긴장이 죽는다
- `리리아 렌바렌`
  - current state: 귀엽기만 한 막내가 아니라, 사람 사이를 뛰어다니며 정보와 분위기를 함께 움직이는 정서적/실무적 조력자
  - latest turn: 키리온의 부탁을 신나서 그대로 실행해 데리온 난입을 촉발했고, 형제 갈등 장면 안에서도 자연스럽게 끼어들어 공기를 바꾸는 가족 엔진으로 기능했다
  - next pressure: 데리온 부재일의 드문 틈에서 집사실 앞을 다시 기웃거리며, 단순 전달자가 아니라 감정과 놀이성으로 구조를 움직이는 인물이어야 한다

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
  - 하급 과정은 단순 맛보기나 병목 확인 파트가 아니라, `조회/보충/질문/초기 검색` 같은 저단계 기능을 실제로 하나씩 여는 첫 제도권 무대여야 한다.
  - 상급 과정은 `본편 시작점`이라기보다, 하급 과정에서 축적된 기능을 확장/제도화하고 `현상 각인/영상 각인술`과 학파 정치로 가속하는 후행 확장 구간으로 읽어야 한다.
  - 시간 압축이 필요하더라도, 하급 과정의 기능 축적과 생활 리듬이 실제로 지급되기 전에는 `3년 스킵`을 기본 전제로 삼지 않는다.
  - 그 이전에는 칼리온의 `시험을 일단 넘겼다`는 정도의 가벼운 안도만 주인공이 캐치하도록 한다.
  - 칼리온이 키리온 안의 `설명하기 어려운 외래성`과 그 영향을 어느 정도 알고 있으며, 그럼에도 주인공을 아들로 판단했다는 진실은 더 뒤의 가족 이벤트에서 공개한다.

## Next 3-5 episode direction
- `ep004` 우선 과제는 이미 반복 중인 `연무장 -> 치유 -> 취침 전 독서` 루틴의 드문 빈틈, 즉 데리온 부재일을 발판으로 리리아와 함께 다음 정보/게시판 프로토타입 욕망을 다시 점화하는 것이다.
- 서고 시험은 끝난 것이 아니라 형태가 바뀐 채 지속 중이므로, 집사실 안내판 성공이 곧바로 더 큰 설계 도약으로 이어지지 않게 해야 한다.
- 데리온의 압박이 `동생을 살리려는 왜곡된 루틴`으로 읽히도록, 단순 체벌 이상의 패턴과 교정성을 유지한다.
- 하급 과정 입학은 멀리 있는 목표로만 남기고, 당장은 저택 내부 생존과 관찰 회피를 우선한다.
- 다만 장기적으로는 `12세 하급 과정에서 제한된 기록 공유와 저단계 기능 해금 축적 -> 15세 이후 상급 과정에서 현상/영상/학파 부흥으로 확장` 구조를 염두에 둔다.
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
