# narrative_state

역할: 작가가 다음 회차 집필 전에 기본 로딩하는 서사 상태 허브. 과거 회차 전체를 다시 읽는 대신, 현재 활성 상태와 다음 진행 방향만 유지한다.

## Current canon frontier
- latest_canon_episode: `ep001` (`artifacts/writing/episodes/ep001/revision_v2.txt`)
- macro_position: Part 1 오프닝 / 렌바렌 저택 생존 부트스트랩 / 학술원 입학 전
- default_load_order:
  - 1. `docs/narrative_state.md`
  - 2. `docs/story_arcs.md`에서 `status: active` arc만
  - 3. `docs/foreshadow_registry.md`에서 `status: open` 항목만
  - 4. `docs/episode_deltas.md`에서 직전 1~2화만
  - 5. `writing/style/style_constitution.md` + `docs/style_bible.md`

## Narrative context policy
- 전체 원고 재로딩은 canon 충돌 검증이나 세부 디테일 회수가 필요할 때만 한다.
- 회차 종료 후에는 사건 요약보다 상태 변화만 `docs/episode_deltas.md`에 추가한다.
- 5~10화 단위로 `docs/story_arcs.md`를 압축 갱신하고, 이 문서에는 활성 항목만 남긴다.
- 복선 회수/폐기 여부는 `docs/foreshadow_registry.md`에서 먼저 처리한 뒤 이 문서를 갱신한다.

## Active foreshadowing
- `FS-001`: 칼리온은 키리온의 말투, 반응 속도, 독서 습관을 통해 정체 변조 여부를 추적 중이다.
  - planted: `ep000`
  - latest carry: `ep001`의 `흑색 표준식 입문서` 전달
  - payoff window: pre-academy
- `FS-002`: 셀리아의 돌봄은 안전지대이면서 동시에 주인공의 경계심을 느슨하게 만드는 위험한 이완 장치다.
  - planted: `ep000`
  - latest carry: `ep001` 복도 산책 구간
  - payoff window: pre-academy recurring beat
- `FS-003`: 렌바렌 저택 행정/정보 흐름에는 집사실 중심의 단일 병목이 있다.
  - planted: `ep001`
  - latest carry: 없음
  - payoff window: pre-academy planning -> academy scale-up
- `FS-004`: `흑색 표준식 입문서`는 선물이 아니라 지속형 심문 장치다.
  - planted: `ep001`
  - latest carry: 없음
  - payoff window: immediate (`ep002` 인접)
- `FS-005`: 치유사의 무해 판정은 "들키지 않았다"이지 "안전하다"가 아니다.
  - planted: `ep001`
  - latest carry: 없음
  - payoff window: pre-academy
- `FS-006`: 주인공의 장기 목표는 이 세계의 정보 인프라/커뮤니티 구조를 만드는 것이다.
  - planted: `ep000`
  - latest carry: `ep001` 병목 관찰로 현실적 발판 확보
  - payoff window: long horizon

## Character arcs
- `NC-0001 / 키리온 렌바렌`
  - current state: 빙의/전이 사실을 숨긴 채 "정상적인 8세 차남"으로 위장 중
  - latest turn: 치유사 검사를 통과했지만, 칼리온의 관찰은 오히려 장기전으로 이동했다
  - next pressure: 책을 읽는 방식과 지식 반응 속도까지 관리해야 한다
- `칼리온 렌바렌`
  - current state: 직접 추궁보다 장기 관찰/검증 장치를 선호하는 감시자
  - latest turn: `흑색 표준식 입문서`를 전달해 읽기 행위 자체를 테스트 환경으로 바꿨다
  - next pressure: 친절과 의도를 분리해서 보여줘야 위협이 유지된다
- `셀리아 렌바렌`
  - current state: 주인공에게 유일한 무계산 온기를 제공하는 보호자
  - latest turn: 치유사 호출과 복도 산책으로 심문 국면을 완화했다
  - next pressure: 안전지대이되 완전한 피난처로 보이면 긴장이 죽는다

## Macro structure position
- 현재 구간의 핵심 질문:
  - 주인공은 렌바렌 저택 안에서 얼마나 오래 정체를 숨길 수 있는가
  - 칼리온의 관찰망 아래에서 어디까지 "아이답게" 굴 수 있는가
  - 저택 내부의 정보 병목을 발견한 주인공이 언제, 어떤 규모로 첫 설계 욕망을 행동으로 옮길 것인가
- 현재 구간의 기능:
  - 학술원 입학 전, 가문/가정/행정 구조를 독자에게 익히게 하는 준비 구간
  - 코어 캐스트 대량 투입 전, 주인공 1인 시점의 생존 규칙과 장기 야망을 먼저 고정하는 구간

## Next 3-5 episode direction
- `ep002` 우선 과제는 `흑색 표준식 입문서`를 둘러싼 관찰전이다.
- 주인공은 책 내용보다 "어떻게 읽는가"를 관리해야 한다.
- 렌바렌 저택 내부의 정보 흐름, 권한 분배, 비공식 전달 경로를 조금 더 구체적으로 포착한다.
- 아직 본격 설계/구축 단계로 점프하지 않는다. 통찰은 하되 실행은 보류하는 긴장을 유지한다.
- 학술원 입학은 멀리 있는 목표로만 남기고, 당장은 저택 내부 생존과 관찰 회피를 우선한다.

## Tone / high-level style notes
- 감각 묘사는 정지 화면보다 시간축 위에서 움직이게 쓴다.
- 긴장 구간은 짧은 문장과 독립 문단으로 박자를 찍는다.
- 돌봄과 일상성은 안심이 아니라 위험한 이완으로 작동해야 한다.
- 개발자적 분석은 설계 직전에서 끊고, 독자가 다음 판단을 기다리게 만든다.
- "아버지/어머니" 호칭 전환은 관계 온도와 긴장도에 맞춰 유동적으로 운용한다.

## Companion docs
- arc compression: `docs/story_arcs.md`
- foreshadow registry: `docs/foreshadow_registry.md`
- episode state-change log: `docs/episode_deltas.md`
