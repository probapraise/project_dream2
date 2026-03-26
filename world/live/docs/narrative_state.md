# narrative_state

## Sync metadata
- sync_category: required
- last_synced_episode: ep004
- sync_source: artifacts/writing/episodes/ep004/canon/4화_리라이트_v1.md
- sync_source_sha256: 4b3b443b7e80f44e51636775e8322dbf82d028cdba23febecf38f58b53182a3e
- sync_summary: artifacts/writing/episodes/ep004/summary_v1.md

역할: 작가가 다음 회차 집필 전에 기본 로딩하는 서사 상태 허브. 과거 회차 전체를 다시 읽는 대신, 현재 활성 상태와 다음 진행 방향만 유지한다.

## Current canon frontier
- latest_canon_episode: `ep004` (`artifacts/writing/episodes/ep004/canon/4화_리라이트_v1.md`)
- macro_position: Part 1 오프닝 / 렌바렌 저택 생존 부트스트랩 / 계승조회식 문턱
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
  - latest carry: `ep004`에서 키리온의 게시판 성과가 공식 인정되며 직접 질문은 줄었지만, 칼리온의 관찰은 끝난 것이 아니라 더 조용한 장기 판독으로 이동했다
  - payoff window: pre-academy
- `FS-002`: 셀리아의 돌봄은 안전지대이면서 동시에 주인공의 경계심을 느슨하게 만드는 위험한 이완 장치다.
  - planted: `ep000`
  - latest carry: `ep002`에서 칭찬 직후의 부드러운 꾸지람이 보호와 긴장을 동시에 강화함
  - payoff window: pre-academy recurring beat
- `FS-003`: 렌바렌 저택 행정/정보 흐름에는 집사실 중심의 단일 병목이 있다.
  - planted: `ep001`
  - latest carry: `ep004`에서 키리온은 그 결핍을 `댓글`로 명명하고 리리아와 함께 종이 시뮬레이션까지 해 보지만, 물리적 한계 앞에서 `수정 1회 + 실명 정정`으로 임시 봉합한 채 다음 수를 마법 탐색으로 넘긴다
  - payoff window: pre-academy planning -> academy scale-up
- `FS-004`: `흑색 표준식 입문서`는 선물이 아니라 지속형 심문 장치다.
  - planted: `ep001`
  - latest carry: `ep004`에서 칼리온의 인정 이후 서고 탐색 폭은 넓어졌지만, 무엇을 계속 다시 펼치는가는 여전히 조용한 심문 자료로 남아 있다
  - payoff window: immediate (`ep003` 인접)
- `FS-005`: 치유사의 무해 판정은 "들키지 않았다"이지 "안전하다"가 아니다.
  - planted: `ep001`
  - latest carry: 치유사는 외상/마나 흐름만 확인했고 정체 문제는 판정 대상이 아니었다
  - payoff window: pre-academy
- `FS-006`: 주인공의 장기 목표는 이 세계의 정보 인프라/커뮤니티 구조를 만드는 것이다.
  - planted: `ep000`
  - latest carry: `ep004`에서 `댓글` 욕망이 명시적인 장기 목표가 되었고, 종이 한계 때문에 이를 마법으로 구현해야 한다는 문제의식과 함께 첫 실질 보상까지 지급됐다
  - payoff window: long horizon
- `FS-007`: 데리온은 동생의 마법책 접근과 이상 징후에 유독 예민하게 반응한다.
  - planted: `ep002`
  - latest carry: `ep004`에서 그 루틴은 2년짜리 생활 리듬으로 굳었고, 계승조회식 직전 데리온은 더 말이 적고 단단한 상태로 마지막 압박을 건다
  - payoff window: immediate (`ep003` 인접)

## Character arcs
- `NC-0001 / 키리온 렌바렌`
  - current state: 집사실 앞 종이 게시판의 결핍을 `댓글`로 명명하고 임시 안정화까지 마친 뒤, 첫 실질 보상을 받은 상태에서 계승조회식이라는 더 큰 판정선 앞에 서 있다
  - latest turn: 리리아와 종이 시뮬레이션으로 댓글판 욕망을 장면화했고, 종이 한계 때문에 이를 마법 탐색 과제로 넘겼다. 동시에 2년 누적 운영 끝에 칼리온의 `잘했다.`와 독서 자유 확대를 얻었지만, 화말에서는 `내일도 내가 렌바렌일까?`라는 질문에 닿았다
  - next pressure: 계승조회식에서 성과 가문이 흔들릴 수 있는 상황을 버티면서도, 지금까지 쌓은 유용함과 위장을 한꺼번에 무너뜨리지 않아야 한다
- `칼리온 렌바렌`
  - current state: 유용함을 인정하는 보상을 줄 줄 알지만, 판정을 끝내지 않은 채 더 조용한 관찰로 이동한 감시자
  - latest turn: 게시판이 실제 수치를 만들자 `잘했다.`라고 공식 인정하고 식탁 질문을 줄였지만, 그 완화는 신뢰 확정이 아니라 더 큰 판정선 전의 조정으로 읽힌다
  - next pressure: 계승조회식 전후에도 독자가 `여전히 보고 있다`는 감각을 잃지 않게 해야 한다
- `데리온 렌바렌`
  - current state: 보호 충동과 공포와 통제를 구분 못한 채 휘두르지만, 계승조회식이 다가올수록 그 긴장을 더 눌러 담는 형
  - latest turn: 2년 동안 훈련 루틴을 지속한 끝에, 계승조회식 직전 키리온을 연무장에 한 번 더 세우며 설명 없는 마지막 압박을 줬다
  - next pressure: 단순 폭력성으로 납작해지지 않고, `왜 저렇게까지 굳어 있느냐`가 뒤늦게 재평가될 여지를 계속 남겨야 한다
- `셀리아 그라비온`
  - current state: 주인공에게 유일한 무계산 온기를 제공하는 보호자이자, 동시에 다른 성 가능성을 열어 두는 모계 혈통의 소유자
  - latest turn: 계승조회식 준비 국면에서도 일상 돌봄과 걱정을 붙들며, 키리온이 잠시 긴장을 늦추게 만드는 축으로 남아 있다
  - next pressure: 안전지대이되 완전한 피난처로 보이면 긴장이 죽고, `그라비온` 가능성이 너무 전면에 나오면 서프라이즈가 죽는다
- `리리아 렌바렌`
  - current state: 귀엽기만 한 막내가 아니라, 사람 사이를 뛰어다니며 정보와 분위기를 함께 움직이고 `같이 만드는 판`을 재밌어하는 공동 운영자
  - latest turn: 집사실 앞에서 손 먼저 가는 물리적 해법과 생활어 반응으로 댓글판 욕망 장면을 함께 완성했고, `그거 엄청 재밌겠다.`라는 감정으로 이 구조를 자기 놀이처럼 받아들였다
  - next pressure: 이번 소집 대상에서 빠진 채 저택에 남으므로, 오빠와 떨어진 자리에서도 존재감을 잃지 않는 방식이 필요하다

## Macro structure position
- 현재 구간의 핵심 질문:
  - 주인공은 렌바렌 저택 안에서 얼마나 오래 정체를 숨길 수 있는가
  - 칼리온의 관찰망 아래에서 어디까지 "아이답게" 굴 수 있는가
  - 첫 설계 성공 이후, 저택 내부의 작은 실무 개입을 어디까지 넓히되 자기 사고 방식의 출처는 숨길 수 있는가
  - 계승조회식 이후에도 주인공은 계속 `렌바렌`로 남을 수 있는가
- 현재 구간의 기능:
  - 하급 과정 진입 전, 가문/가정/행정 구조를 독자에게 익히게 하는 준비 구간
  - 코어 캐스트 대량 투입 전, 주인공 1인 시점의 생존 규칙과 장기 공론장 욕망의 씨앗을 먼저 고정하는 구간
  - 저택 내부의 첫 보상을 지급하고, 다음 제도권 판정선인 계승조회식으로 시선을 넘기는 전환 구간
- 현재 배치 목표:
  - 아르케이온 권역 첫 진입(12세 하급 과정 입학식/첫 수업/환경 노출)은 잠정적으로 `ep010` 전후를 목표로 둔다.
  - 하급 과정은 단순 맛보기나 병목 확인 파트가 아니라, `조회/보충/질문/초기 검색` 같은 저단계 기능을 실제로 하나씩 여는 첫 제도권 무대여야 한다.
  - 상급 과정은 `본편 시작점`이라기보다, 하급 과정에서 축적된 기능을 확장/제도화하고 `현상 각인/영상 각인술`과 학파 정치로 가속하는 후행 확장 구간으로 읽어야 한다.
  - 시간 압축이 필요하더라도, 하급 과정의 기능 축적과 생활 리듬이 실제로 지급되기 전에는 `3년 스킵`을 기본 전제로 삼지 않는다.
  - 그 이전에는 칼리온의 `시험을 일단 넘겼다`는 정도의 가벼운 안도만 주인공이 캐치하도록 한다.
  - 칼리온이 키리온 안의 `설명하기 어려운 외래성`과 그 영향을 어느 정도 알고 있으며, 그럼에도 주인공을 아들로 판단했다는 진실은 더 뒤의 가족 이벤트에서 공개한다.

## Next 3-5 episode direction
- `ep005`는 더 이상 게시판 설명 화가 아니라, 왕도 소집과 계승조회식 자체를 전면에 올려야 한다. 핵심 긴장은 `어떤 문장비전이 뜨는가`와 `내일도 렌바렌인가`다.
- 댓글 구조와 마법 탐색은 즉시 구현 파트가 아니라, 저택 파트에서 붙은 장기 욕망으로 배경에 남겨 둔다.
- 칼리온의 `잘했다.` 이후 완화된 공기와, 데리온의 더 눌린 긴장을 동시에 유지해 가족 반응의 온도 차를 써야 한다.
- 저택 내부 보상이 지급됐다고 해서 곧바로 거대한 플랫폼 도약으로 가면 안 된다. 아직은 저택 내부 종이 프로토타입과 색 입문서 탐색 단계다.
- 하급 과정 입학은 여전히 중기 목표로 남기되, 당장은 계승조회식과 그 결과가 가족 내 위치를 어떻게 바꾸는지가 우선이다.
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
