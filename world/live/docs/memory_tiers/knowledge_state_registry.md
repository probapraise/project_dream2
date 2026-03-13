# knowledge_state_registry

## Sync metadata
- sync_category: required
- last_synced_episode: ep002
- sync_source: artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md
- sync_source_sha256: 17673b87624ec2a117ae5776a5ebf816a593199f158942f07badf25f84528203
- sync_summary: artifacts/writing/episodes/ep002/summary_v1.md

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
  - 없음. `ep002` 기준으로는 노골적인 2차 의심 주체가 아직 본문 전면에 없다.
- misread_by:
  - 셀리아는 이를 정체 변조보다 회복 중 예민함과 이상 반응 쪽으로 읽는다.
- must_not_learn_yet:
  - 리리아
  - 저택 실무선
  - 데리온은 `이상 징후`까지는 감지해도, 정체 핵심을 곧바로 알아버리면 안 된다.
- latest shift:
  - `ep002`의 안내판 성공으로, 칼리온이 읽는 대상이 `행동 이상`에서 `사고 방식의 출처` 쪽으로 더 이동했다.
- next volatility:
  - 서고/첫 책 선택, 데리온 개입, 가족 반응이 이 의심을 더 넓힐 수 있다.

### KS-002 서고 접근권과 자색 입문서 열람 허가의 진짜 의미
- canonical statement: `서고 접근권`과 `자색 표준식 입문서 열람 허가`는 보상처럼 보이지만 실제로는 보상형 통제이자 감시 확장이다.
- known_by:
  - 키리온
  - 칼리온
- partially_understood_by:
  - 없음. `ep002` 기준으로 이 허가를 온전한 감시 장치로 해석하는 인물은 위 둘뿐이다.
- misread_by:
  - 저택 실무선은 이를 `도련님이 특별히 허가받았다`는 표면 사건으로 읽을 가능성이 높다.
  - 독자/모델이 이를 단순 `자유 획득`으로 flatten하면 안 된다.
- must_not_learn_yet:
  - 리리아
  - 셀리아
- latest shift:
  - `ep002` 말미에 시험 단위가 `흑색 책을 읽는가`에서 `서고에서 무엇을 먼저 고르는가`로 확장됐다.
- next volatility:
  - 다음 화에서 첫 책 선택과 데리온 변수 개입이 이 허가의 진짜 성격을 더 선명하게 드러낸다.

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
  - `ep002`에서 데리온 민감도와 서고 허가가 동시에 떠오르며, 이 규칙이 단순 배경이 아니라 당장 현재 행동을 제한하는 힘으로 부상했다.
- next volatility:
  - 데리온이 개입하면 이 금지 규칙이 `가문 내부 공포` 차원으로 더 구체화될 수 있다.

### KS-004 데리온의 과민 반응 배경
- canonical statement: 데리온의 강압성과 동생의 마법책 접근에 대한 과민 반응은 단순 성격 문제가 아니라, 계승조회식 이후 짊어진 가문 비밀과 책임 공포와 연결된다.
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
  - `ep002` 종료 시점에서 키리온은 이 과민 반응을 서고 시험장을 비트는 변수로 쓰려는 단계에 들어갔다.
- next volatility:
  - 데리온이 실제로 난입하거나 개입하면 `가족 보호`와 `가문 규율`이 뒤섞인 복합 기능이 드러날 수 있다.

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
  - `ep002`에서 리리아를 통해 첫 묶음을 회수했지만, 여전히 부분 표본 수준이다.
- next volatility:
  - 다른 가족/실무선 반응을 거치면 위장 기준이 더 세밀해질 수 있다.

### KS-006 칼리온의 최종 판정은 아직 비공개다
- canonical statement: 칼리온이 키리온에 대해 어디까지 결론내렸는지는 아직 주인공과 독자에게 공개되지 않았다.
- known_by:
  - 칼리온
- strongly_hoped_for_by:
  - 없음. `ep002` 기준으로 키리온은 아직 확언을 기대하는 단계가 아니다.
- misread_by:
  - 독자/모델이 `이미 아들로 받아들였다`고 확정해 쓰면 안 된다.
- must_not_learn_yet:
  - 키리온
  - 독자
- release_rule:
  - pre-academy 구간에서는 `일단은 버틴다`까지만 주고, `그럼에도 내 아들이다` 확언은 더 뒤로 민다.
