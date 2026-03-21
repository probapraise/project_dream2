# knowledge_state_registry

## Sync metadata
- sync_category: required
- last_synced_episode: ep003
- sync_source: artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md
- sync_source_sha256: 6c65fe6820526e8595010d9a84748edcd285117a70725efe3c08e21d0f338ca7
- sync_summary: artifacts/writing/episodes/ep003/summary_v1.md

역할: 현재 서사에서 중요한 `사실` 단위로 누가 무엇을 알고, 의심하고, 오해하고, 아직 몰라야 하는지를 관리하는 prompt-facing 지식 상태 레지스트리.

## Usage rule
- 이 문서는 인물별 성격 카드가 아니라 `사실/비밀/권한의 의미`를 중심으로 쓴다.
- 각 항목은 가능한 한 `known_by / suspected_by / misread_by / must_not_learn_yet` 구조를 유지한다.
- 장면 하나가 지나며 누군가의 지식 상태가 바뀌면, 인물 카드보다 먼저 이 문서를 갱신한다.

## Knowledge facts

### KS-001 키리온의 이질감과 정체 변조 의심
- canonical statement: 키리온에게는 `원래 8세 차남답지 않은 사고 구조와 어휘`가 있다.
- known_by:
  - 키리온
- strongly_suspected_by:
  - 칼리온
- weakly_suspected_by:
  - 없음. 정체 변조를 직접 의심하는 2차 주체는 아직 본문 전면에 없다.
- misread_by:
  - 셀리아는 이를 정체 변조보다 회복 중 예민함과 이상 반응 쪽으로 읽는다.
- must_not_learn_yet:
  - 리리아
  - 저택 실무선
  - 데리온은 `이상 징후`까지는 감지해도, 정체 핵심을 곧바로 알아버리면 안 된다.
- latest shift:
  - `ep003`에서 서고 첫 선택과 데리온 난입이 겹치며, 칼리온이 읽는 단위가 `행동 이상`에서 `가족 변수 속 반응과 루틴 적응`까지 넓어졌다.
- next volatility:
  - 이후 연무장/야간 독서 루틴이 지속되면, 칼리온의 의심은 `무엇을 고르는가`보다 `어떻게 버티는가` 쪽으로 더 정교해질 수 있다.

### KS-002 서고 접근권과 `첫 책 선택`의 진짜 의미
- canonical statement: `서고 접근권`은 보상처럼 보이지만 실제로는 보상형 통제다. 저번에 몰래 읽다 걸린 `자색 입문서`는 그 안에서 가장 자연스러운 첫 선택지로 떠올라 감시를 더 정교하게 만든다.
- known_by:
  - 키리온
  - 칼리온
- partially_understood_by:
  - 없음. 이 허가를 온전한 감시 장치로 해석하는 인물은 아직 위 둘뿐이다.
- misread_by:
  - 저택 실무선은 이를 `도련님이 특별히 허가받았다`는 표면 사건으로 읽을 가능성이 높다.
  - 독자/모델이 이를 단순 `자유 획득`으로 flatten하면 안 된다.
- must_not_learn_yet:
  - 리리아
  - 셀리아
- latest shift:
  - `ep003`에서 첫 책 선택 시험이 실제로 열렸고, 데리온 개입으로 감시가 사라지지 않은 채 `가족 반응과 생활 루틴` 관찰로 변형됐다.
- next volatility:
  - 이후 독서 시간이 밤 루틴으로 좁아들수록, 이 접근권의 진짜 의미가 `자유`보다 `통제된 관찰` 쪽으로 더 선명해진다.

### KS-003 계승조회식 이전 조기 수련 금지의 실질 위험
- canonical statement: `계승조회식` 이전 아동의 실제 마법 수련은 제도적으로 매우 위험하며, 흔적이 남는 종류의 금지다.
- known_by:
  - 칼리온
  - 셀리아
  - 데리온
- partially_understood_by:
  - 키리온은 `마법책 접근이 민감하다`는 체감은 얻었지만, 제도 전체와 검사 구조를 아직 다 알지는 못한다.
- misread_by:
  - 리리아는 이 리스크의 전모보다 집안 분위기와 오빠들의 반응을 먼저 읽는다.
- must_not_dump_to_reader_yet:
  - 검사 절차 전체
  - 법령/기관 세부 명칭
  - 조기 수련 적발 프로토콜 전부
- latest shift:
  - `ep003`에서 데리온 난입과 연무장 교정이 붙으며, 이 규칙은 배경 정보가 아니라 가족 공포와 생활 루틴을 직접 바꾸는 힘으로 올라왔다.
- next volatility:
  - 이후 대련과 독서가 함께 굴러가면, `무엇이 합법적 준비이고 무엇이 금지선인가`가 더 예민한 생활 문제로 바뀔 수 있다.

### KS-004 데리온의 과민 반응 배경
- canonical statement: 데리온의 강압성과 동생의 마법책 접근에 대한 과민 반응은 단순 성격 문제가 아니라, 계승조회식 이후 짊어진 가문 비밀, 타가문 집행 공포, 그리고 키리온을 살아남는 변수로 만들고 싶다는 불가능한 희망과 연결된다.
- known_by:
  - 데리온
  - 칼리온
- partially_suspected_by:
  - 키리온은 `동생의 마법책 접근에 유독 예민하다`는 현상까지는 포착했다.
- misread_by:
  - 리리아는 이를 `성질 급한 형` 쪽으로 더 먼저 읽을 가능성이 높다.
  - 독자는 초반에 `짜증나는 강압형 형`으로 먼저 읽어도 괜찮지만, 거기서 고정되면 안 된다.
- must_not_learn_yet:
  - 리리아
  - 저택 실무선
  - 키리온도 아직 전모를 곧바로 듣지 않는다.
- latest shift:
  - `ep003`에서 데리온이 실제로 서고 문밖까지 들이닥치고, 연무장과 치유를 묶은 새 루틴을 강요하며 이 반응의 실체가 장면으로 드러났다.
- next volatility:
  - 이후 형제 대련이 반복되면 `보호`, `공포`, `통제`, `교정`이 어떻게 섞여 있는지가 더 선명해질 수 있다.

### KS-005 원래 키리온 행동 규칙의 기억 위치
- canonical statement: `원래 키리온답게` 보이는 행동 규칙은 한 사람 머릿속에 완성형으로 있는 게 아니라, 리리아와 가족/생활선의 기억 조각에 분산되어 있다.
- known_by:
  - 리리아
- partially_reconstructed_by:
  - 키리온
- misread_by:
  - 칼리온은 행동의 결과보다 `그 규칙을 어디서 가져왔는가`를 보려 든다.
- must_not_stabilize_yet:
  - 키리온이 `이제 완전히 위장법을 알았다`고 착각하면 안 된다.
- latest shift:
  - `ep003`에서 리리아와 가족 반응을 한 번 더 거치며, 키리온은 `원래 키리온다움`이 장면별로 다르게 호출된다는 사실을 더 체감했다.
- next volatility:
  - 데리온/셀리아/리리아 앞에서 요구되는 자연스러움이 계속 달라지면, 위장 기준도 더 세분화될 수 있다.

### KS-006 칼리온의 최종 판정은 아직 비공개다
- canonical statement: 칼리온이 키리온에 대해 어디까지 결론내렸는지는 아직 주인공과 독자에게 공개되지 않았다.
- known_by:
  - 칼리온
- strongly_hoped_for_by:
  - 없음. 키리온은 아직 확언보다 생존과 관찰 회피를 우선한다.
- misread_by:
  - 독자/모델이 `이미 아들로 받아들였다`고 확정해 쓰면 안 된다.
- must_not_learn_yet:
  - 키리온
  - 독자
- release_rule:
  - pre-academy 구간에서는 `일단은 버틴다`까지만 주고, `그럼에도 내 아들이다` 확언은 더 뒤로 민다.
