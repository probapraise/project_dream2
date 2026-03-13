# narrative_state

역할: 작가가 다음 회차 집필 전에 기본 로딩하는 서사 상태 허브. 과거 회차 전체를 다시 읽는 대신, 현재 활성 상태와 다음 진행 방향만 유지한다.

## Current canon frontier
- latest_canon_episode: `ep001` (`artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`)
- macro_position: Part 1 오프닝 / 렌바렌 저택 생존 부트스트랩 / 하급 과정 진입 전
- default_load_order:
  - 1. `docs/narrative_state.md`
  - 2. `docs/story_arcs.md`에서 `status: active` arc만
  - 3. `docs/foreshadow_registry.md`에서 `status: open` 항목만
  - 4. `docs/episode_deltas.md`에서 직전 1~2화만
  - 5. `writing/style/house_rules.md` + `docs/style_bible.md`
  - 6. 집필 대상 회차의 `writing/episodes/<episode_id>/style_selection_vN.md` (준비된 경우)

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
  - latest carry: 집사실에서 동일 문답이 반복되고, 답 주변에 군집/농담이 자생하는 구조 확인
  - payoff window: pre-academy planning -> academy scale-up
- `FS-004`: `흑색 표준식 입문서`는 선물이 아니라 지속형 심문 장치다.
  - planted: `ep001`
  - latest carry: 메모 `[궁금하다고 했으니.]`와 함께 책 읽기 자체가 채점 대상이 되는 구도 확정
  - payoff window: immediate (`ep002` 인접)
- `FS-005`: 치유사의 무해 판정은 "들키지 않았다"이지 "안전하다"가 아니다.
  - planted: `ep001`
  - latest carry: 치유사는 외상/마나 흐름만 확인했고 정체 문제는 판정 대상이 아니었다
  - payoff window: pre-academy
- `FS-006`: 주인공의 장기 목표는 이 세계의 정보 인프라/커뮤니티 구조를 만드는 것이다.
  - planted: `ep000`
  - latest carry: `ep001` 집사실 문답의 자생적 온도와 종이 게시판 구상으로 정서적/구조적 발판 확보
  - payoff window: long horizon

## Character arcs
- `NC-0001 / 키리온 렌바렌`
  - current state: 빙의/전이 사실을 숨긴 채 "정상적인 8세 차남"으로 위장하며, 저택 내부 생존을 1순위로 두는 상태
  - latest turn: 치유사 검사를 통과한 뒤 집사실의 병목과 잡담의 온도를 동시에 목격했고, 곧바로 `흑색 표준식 입문서`라는 새 시험지를 받았다
  - next pressure: 책을 읽는 방식과 지식 반응 속도뿐 아니라, 설계 충동 자체를 얼마나 숨길 수 있는가
- `칼리온 렌바렌`
  - current state: 직접 추궁보다 장기 관찰/검증 장치를 선호하는 감시자
  - latest turn: `흑색 표준식 입문서`를 전달해 읽기 행위 자체를 테스트 환경으로 바꿨다
  - next pressure: 친절과 의도를 분리해서 보여줘야 위협이 유지된다
- `셀리아 그라비온`
  - current state: 주인공에게 유일한 무계산 온기를 제공하는 보호자
  - latest turn: 치유사 호출과 복도 산책으로 심문 국면을 완화했다
  - next pressure: 안전지대이되 완전한 피난처로 보이면 긴장이 죽는다

## Macro structure position
- 현재 구간의 핵심 질문:
  - 주인공은 렌바렌 저택 안에서 얼마나 오래 정체를 숨길 수 있는가
  - 칼리온의 관찰망 아래에서 어디까지 "아이답게" 굴 수 있는가
  - 저택 내부의 정보 병목과 자생적 문답 온도를 본 주인공이 언제, 어떤 규모로 첫 설계 욕망을 행동으로 옮길 것인가
- 현재 구간의 기능:
  - 하급 과정 진입 전, 가문/가정/행정 구조를 독자에게 익히게 하는 준비 구간
  - 코어 캐스트 대량 투입 전, 주인공 1인 시점의 생존 규칙과 장기 공론장 욕망의 씨앗을 먼저 고정하는 구간
- 현재 배치 목표:
  - 아르케이온 권역 첫 진입(12세 하급 과정 입학식/첫 수업/환경 노출)은 잠정적으로 `ep010` 전후를 목표로 둔다.
  - 본격적인 상급 과정 서사는 `15세 상급 과정 진입성취평가 -> 입학 즉시 전공 선택` 시점에서 연다.
  - 그 이전에는 칼리온의 `시험을 일단 넘겼다`는 정도의 가벼운 안도만 주인공이 캐치하도록 한다.
  - 칼리온이 실제로 이계 지식의 존재와 그 영향을 알고 있으며, 그럼에도 주인공을 아들로 판단했다는 진실은 더 뒤의 가족 이벤트에서 공개한다.

## Next 3-5 episode direction
- `ep002` 우선 과제는 `흑색 표준식 입문서`를 둘러싼 관찰전이다.
- 주인공은 책 내용보다 "어떻게 읽는가"를 관리해야 한다.
- 렌바렌 저택 내부의 정보 흐름, 권한 분배, 비공식 전달 경로를 조금 더 구체적으로 포착한다.
- 아직 본격 설계/구축 단계로 점프하지 않는다. 통찰과 충동은 드러나되 실행은 보류하는 긴장을 유지한다.
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
