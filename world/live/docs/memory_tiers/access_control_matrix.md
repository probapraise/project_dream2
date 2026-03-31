# access_control_matrix

## Sync metadata
- sync_category: required
- last_synced_episode: ep005
- sync_source: artifacts/writing/episodes/ep005/canon/5화_리라이트_v1.md
- sync_source_sha256: 3f290485186031271b7aeef509a19df278926fa0c30de40ebea5e9fdefc523ff
- sync_summary: artifacts/writing/episodes/ep005/summary_v1.md

역할: 현재 서사에서 중요한 `접근 권한 / 금지 / 허가 / 통제` 상태를 resource 중심으로 추적하는 prompt-facing 접근 권한 매트릭스.

## Usage rule
- 이 문서는 법률집이 아니라, 지금 장면 설계에서 실제로 긴장을 만드는 권한선만 적는다.
- 각 항목은 `holder / status / granted_by / observed_by / dramatic meaning` 정도를 유지한다.
- 새로운 허가가 열리거나, 막힌 권한을 우회하는 순간이 나오면 회차 종료 후 먼저 이 문서를 갱신한다.

## Access rows

### ACL-001 키리온의 방 밖 이동
- holder:
  - 키리온
- status: `conditional_allow`
- granted_by:
  - 셀리아와 저택 회복 동선
- observed_by:
  - 저택 실무선
  - 가족선
- trigger_condition:
  - 회복 명분, 짧은 동선, 보호자 시야 안에 있다는 전제가 붙을 때
- dramatic meaning:
  - 완전한 감금은 아니지만, `왜 방 밖에 있었는가`가 설명되지 않으면 바로 시선이 붙는다.

### ACL-002 서고 출입
- holder:
  - 키리온
- status: `conditional_allow`
- granted_by:
  - 칼리온
- observed_by:
  - 칼리온
  - 저택 실무선
- public justification:
  - 회복 중 차남에게 내려진 이례적 배려/학습 허가
- dramatic meaning:
  - 자유권이 아니라 `첫 선택을 읽기 위한 시험장 개방`이었고, `ep004` 시점에는 첫 보상 이후 겉보기 자유도가 약간 늘어났어도 여전히 조용한 관찰전 안에 있다.

### ACL-003 서고 내 `자색 입문서` 접근
- holder:
  - 키리온
- status: `available_within_acl_002`
- granted_by:
  - `ACL-002`의 서고 출입 허가
- observed_by:
  - 칼리온
  - 서고 동행 실무선
- public justification:
  - 키리온의 주색이 자색이라면 그 계열 입문서를 먼저 집는 것이 가장 자연스럽다.
- dramatic meaning:
  - 별도 명시 허가가 없어도, 이 책은 `가장 무난해 보이는 첫 선택`이라 현장 관찰의 핵심 센서가 된다.

### ACL-004 흑색 표준식 입문서 접근
- holder:
  - 키리온
- status: `physically_allowed_but_high_risk`
- granted_by:
  - 칼리온
- observed_by:
  - 칼리온
- public justification:
  - `궁금하다고 했으니.`라는 메모가 붙은 선물 형태
- dramatic meaning:
  - 접근 자체는 허용되지만, 읽는 속도와 멈추는 지점이 곧 진술서가 되는 지속형 심문 장치다. `ep004` 이후에는 다른 색 입문서 탐색 폭도 넓어졌지만, 무엇을 계속 다시 펼치는가는 여전히 조용한 판독 자료다.

### ACL-005 집사실 원문 지침 열람
- holder:
  - 집사
  - 제한된 실무 책임선
- status: `restricted`
- blocked_for:
  - 일반 하인/하녀 다수
  - 질문하러 오는 생활 실무선
- observed_by:
  - 집사실 행정선
- dramatic meaning:
  - 답은 존재하지만 직접 닿는 인터페이스가 좁아, 반복 질문과 실무 병목이 발생한다.

### ACL-006 계승조회식 이전 실제 마법 수련
- holder:
  - 없음. 키리온과 리리아 모두 합법적 실제 수련 권한이 없다.
- status: `blocked`
- enforced_by:
  - 왕국 규정
  - 가문 리스크 관리
- observed_by:
  - 가족 보호자선
  - 향후 감정/검사 체계
- dramatic meaning:
  - 이론 학습과 실제 시전 사이에 큰 단절이 있으며, 선을 넘는 순간 저택 내부 긴장이 곧바로 제도 리스크로 바뀐다.

### ACL-007 저택 실무 정보의 비공식 전달 경로
- holder:
  - 리리아
  - 하인/하녀 군집
- status: `informal_only`
- granted_by:
  - 제도적 허가가 아니라 생활 관성과 친밀도
- observed_by:
  - 거의 기록되지 않음
- dramatic meaning:
  - 공식 권한선은 집사실에 몰려 있지만, 실제 장면을 움직이는 빠른 전달은 비공식 인맥과 발품에서 나온다. `ep004` 시점에는 이 비공식 전달이 집사실 앞 종이 게시판이라는 임시 인터페이스로 더 또렷이 응결되어, 실무선이 실제로 기대는 생활형 회로가 됐다.

### ACL-008 `연무장 -> 치유 -> 취침 전 독서` 루틴
- holder:
  - 키리온
- status: `conditionally_open_but_family_enforced`
- granted_by:
  - 칼리온의 서고 허가
  - 회복 이후 저택 생활 리듬
- enforced_by:
  - 데리온
- constrained_by:
  - 연무장 소모
  - 치유 이후 남는 체력
- observed_by:
  - 데리온
  - 가족선
  - 저택 생활선
- dramatic meaning:
  - 서고 시험을 한 번 유예하는 대가로 생긴 통제선이다. 이 루틴은 `ep004` 시점에 2년 가까이 생활 리듬으로 굳었고, 독서 시간은 몸과 시간을 점유당한 뒤에야 열리는 좁은 자유로 남는다.

### ACL-009 집사실 앞 종이 게시판 수정/보충 참여
- holder:
  - 키리온
  - 리리아
  - 일부 하인/하녀
- status: `informal_participatory_with_named_corrections`
- granted_by:
  - 집사실 앞 생활 관성
  - 리리아의 자연스러운 개입
  - 키리온의 설계와 묵시적 허용
  - 2년 누적 운영으로 쌓인 실무 신뢰
- constrained_by:
  - 수정 횟수는 1회로 제한된다
  - 고칠 때는 누가 고쳤는지 이름을 남겨야 한다
  - 공식 최신 정보 판정 권한은 여전히 집사실/상층에 있다
  - `아닌데?`를 덧붙일 댓글/의견 레이어가 아직 없다
  - 충돌이 생기면 결국 사람을 찾아가 말로 풀어야 한다
- observed_by:
  - 집사실 앞 실무선
  - 키리온
  - 리리아
- dramatic meaning:
  - 이 판은 더 이상 일방향 안내문이 아니라 사용자 직접 수정/보충이 가능한 참여형 프로토타입이 됐고, 실제 비용 절감까지 만들어 냈다. 다만 종이의 물리적 한계 때문에 정정 충돌을 수용할 구조는 여전히 없어, 다음 단계 욕망은 `읽는 판`의 확대가 아니라 `말을 붙일 자리`의 발명으로 이동한다.

### ACL-010 계승조회식 참석
- holder:
  - 키리온
- status: `resolved_current_cycle`
- granted_by:
  - 왕실 소집 규정
  - 서명귀족 혈통 판정 체계
- observed_by:
  - 칼리온
  - 셀리아
  - 데리온
  - 의식 실무선
- trigger_condition:
  - 만 열 살 전후의 대상 아동으로 분류될 때
- dramatic meaning:
  - 선택권이 붙은 허가가 아니라 빠질 수 없는 공식 판정선이다. `ep005`에서 키리온은 실제로 이 호출을 이행해 `미계승`으로 남았지만, 별도 검사 라인 배정과 그 기준의 불투명성까지 함께 확인했다.

### ACL-011 저택 밖 게시판 구조 반출
- holder:
  - 키리온
  - 리리아
  - 세렌
- status: `socially_blocked_but_imminent_experiment`
- granted_by:
  - 공식 허가 없음
  - 리리아의 추진력
  - 세렌의 요청과 아버지 칭찬 욕망
- observed_by:
  - 라베르니온 별채 실무선
  - 귀족 손님 시선
  - 키리온
- constrained_by:
  - 공작가 별채는 저택 내부보다 정치적 시선이 훨씬 촘촘하다
  - 세렌의 요청만으로 충분하지 않고, 가주 또는 실무 책임선 허락 없이 설치하면 곧바로 월권으로 읽힐 수 있다
  - 누가 중심에서 제안하고 누가 써도 되는지가 곧 권한 문제가 된다
- dramatic meaning:
  - 저택 안에서는 실험으로 버티던 구조가, 외부 귀족 공간에선 곧바로 `누가 허락하고 누가 책임지는가`의 문제로 바뀐다. 화말의 훅은 세렌의 인정 욕망과 이 금지선이 처음 맞부딪히는 순간이다.
