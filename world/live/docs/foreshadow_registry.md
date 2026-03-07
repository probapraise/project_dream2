# foreshadow_registry

역할: 활성 복선과 장기 서사 약속을 상태 기반으로 관리하는 레지스트리. 회차 요약이 아니라 "무엇이 아직 열려 있는가"를 추적한다.

## Usage rule
- 집필 시 기본 로드는 `status: open` 항목만 한다.
- 복선이 회수되거나 폐기되면 먼저 이 문서 상태를 갱신하고, 그 다음 `narrative_state.md`와 `story_arcs.md`를 맞춘다.
- payoff window는 강한 약속 범위를 뜻하며, 실제 회수 회차는 그 안에서 유동적일 수 있다.

## Open registry

### FS-001 칼리온의 정체 감지 의심
- type: threat
- planted_in: `ep000`
- status: open
- narrative function: 아버지 장면이 단순 권위자 연출이 아니라 상시 검증 시스템이라는 사실을 유지한다.
- latest carry:
  - `ep001`에서 직접 심문 대신 `흑색 표준식 입문서`를 보내 장기 관찰 국면으로 전환
- payoff window: pre-academy
- linked_arcs:
  - `ARC-001`

### FS-002 셀리아의 온기는 위험한 이완 장치
- type: emotional
- planted_in: `ep000`
- status: open
- narrative function: 따뜻한 돌봄이 곧바로 안전 선언이 되지 않게 만들고, 긴장 리듬을 역설적으로 키운다.
- latest carry:
  - `ep001` 복도 산책에서 주인공의 경계가 잠깐 느슨해지는 장면으로 재강조
- payoff window: recurring
- linked_arcs:
  - `ARC-001`
  - `ARC-003`

### FS-003 렌바렌 저택의 정보 병목
- type: system
- planted_in: `ep001`
- status: open
- narrative function: 주인공의 정보 인프라 야망을 추상 포부가 아니라 관찰 가능한 구조 문제와 연결한다.
- latest carry:
  - 집사실에서 질문이 단일 인터페이스를 반복 통과하고, 답 주변에 군집/농담이 자생하는 구조까지 확인
- payoff window: pre-academy -> academy
- linked_arcs:
  - `ARC-002`
  - `ARC-003`

### FS-004 흑색 표준식 입문서 = 지속형 심문 장치
- type: threat
- planted_in: `ep001`
- status: open
- narrative function: 책 읽기 자체를 다음 회차의 긴장 장치로 만든다.
- latest carry:
  - 칼리온의 짧은 메모 `[궁금하다고 했으니.]`
- payoff window: immediate
- linked_arcs:
  - `ARC-001`

### FS-005 치유사 통과는 임시 안전일 뿐
- type: false_relief
- planted_in: `ep001`
- status: open
- narrative function: 독자와 주인공이 "1차 위기를 넘겼다"는 안도에 머무르지 못하게 한다.
- latest carry:
  - 치유사는 외상/마나 흐름만 확인했고, 정체 문제는 판정 대상이 아니었다
- payoff window: pre-academy
- linked_arcs:
  - `ARC-001`

### FS-006 정보 인프라/공동체 집착의 장기 약속
- type: promise
- planted_in: `ep000`
- status: open
- narrative function: 작품의 장기 방향을 정보 인프라/커뮤니티 구축 서사로 고정하되, 당장의 생존 서사와 충돌하지 않게 점진적으로 키운다.
- latest carry:
  - `ep001`에서 집사실 병목과 하인들의 자생적 문답 온도를 보고, 종이 게시판 수준의 첫 골격까지 상상
- payoff window: long horizon
- linked_arcs:
  - `ARC-002`
  - `ARC-003`
