# access_control_matrix

## Sync metadata
- sync_category: required
- last_synced_episode: ep002
- sync_source: artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md
- sync_source_sha256: 17673b87624ec2a117ae5776a5ebf816a593199f158942f07badf25f84528203
- sync_summary: artifacts/writing/episodes/ep002/summary_v1.md

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
  - 자유권이 아니라 `첫 선택을 읽기 위한 시험장 개방`이다.

### ACL-003 자색 표준식 입문서 열람
- holder:
  - 키리온
- status: `conditional_allow`
- granted_by:
  - 칼리온
- observed_by:
  - 칼리온
- public justification:
  - 키리온의 주색과 더 자연스럽게 맞는 입문서 허가
- dramatic meaning:
  - 합리적인 허가처럼 보이지만, 어떤 책을 먼저 고르는지 더 정교하게 읽기 위한 미끼다.

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
  - 접근 자체는 허용되지만, 읽는 속도와 멈추는 지점이 곧 진술서가 되는 지속형 심문 장치다.

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
  - 없음. `ep002` 기준 키리온과 리리아 모두 합법적 실제 수련 권한이 없다.
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
  - 공식 권한선은 집사실에 몰려 있지만, 실제 장면을 움직이는 빠른 전달은 비공식 인맥과 발품에서 나온다.
