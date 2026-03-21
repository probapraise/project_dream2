# entity_registry

## Sync metadata
- sync_category: required
- last_synced_episode: ep003
- sync_source: artifacts/writing/episodes/ep003/canon/3화_리라이트_v1.md
- sync_source_sha256: 6c65fe6820526e8595010d9a84748edcd285117a70725efe3c08e21d0f338ca7
- sync_summary: artifacts/writing/episodes/ep003/summary_v1.md

역할: 현재 서사에서 중요한 인물들의 `동적 상태값`을 모아 둔 prompt-facing 엔티티 레지스트리. 고정 설정 카드의 대체물이 아니라, 지금 이 시점의 태도/의심/압박/다음 행동만 추적한다.

## Usage rule
- fixed fact는 world bible이나 캐릭터 카드가 우선한다.
- 이 문서는 `지금 이 인물이 무엇을 알고 무엇을 오해하며 얼마나 강하게 움직이는가`만 남긴다.
- 회차 후 캐릭터의 압박 방식, 관계 온도, 감시 밀도가 변하면 먼저 여기서 갱신한다.

## Entity snapshots

### ENT-001 키리온 렌바렌
- surface role: 회복 중인 8세 차남, 정리벽이 있는 아이
- true state: 외래 기억 잔향을 바탕으로 `현재의 키리온` 행동 규칙을 보정하며 위장 중
- current goal: `연무장 -> 치유 -> 취침 전 독서` 루틴 속에서 감시를 버티며, 줄어든 자유 시간 안에서도 관찰/설계 씨앗을 유지하기
- what he is hiding: 사고 구조의 출처, 과도한 분류 습관, 외래 기억식 문제 해결 방식
- current pressure: 서고 시험을 한 번 비틀었지만, 그 대가로 몸과 시간을 점유하는 새 루틴에 묶인 상태
- next likely move: 리리아와 저택 생활선 틈에서 작은 정보/게시판 프로토타입 욕망을 다시 점화한다

### ENT-002 칼리온 렌바렌
- surface role: 절제된 아버지, 허가와 보상을 줄 줄 아는 보호자
- hidden function: 질문 구조와 선택지 설계로 사람의 정합성을 읽는 감시자/판정자
- current read on Kirion: 노골적 확신은 드러내지 않지만, 분명한 이질감과 출처 불명의 사고를 의심 중
- operating mode now: 직접 심문보다 `허가`, `선택지`, `가족 반응`, `생활 루틴`을 묶어 길게 읽는 감시자
- current pressure on Kirion: `무엇을 먼저 고르는가`에 더해 `가족 변수를 어떻게 쓰고 새 루틴 안에서 어떻게 버티는가`까지 읽는다
- next likely move: 서고, 연무장, 야간 독서를 하나의 장기 관찰선으로 묶는다

### ENT-003 셀리아 그라비온
- surface role: 다정한 어머니, 생활 리듬을 붙들어 주는 보호자
- true story function: 안심이 아니라 경계 해제를 부르는 위험한 이완 장치
- current stance toward Kirion: 거의 무조건적인 보호와 애정
- current effect on scene: 키리온의 방어를 잠시 늦추고, 연무장 이후 회복과 일상 리듬을 붙드는 완충 역할까지 겸한다
- next likely move: 걱정, 잔소리, 생활 돌봄을 섞어 보호자 포지션을 유지한다

### ENT-004 리리아 렌바렌
- surface role: 밝고 수다스럽고 사람 사이를 뛰어다니는 막내
- current functional role: 키리온의 행동 모델 복원자 + 자연스러운 메신저 + 가족 변수이자 현장 실행 엔진
- stance toward Kirion: 경계 없음, 애정 높음, 오빠와 같이 노는 것을 즐김
- current strength: 사람에게 자연스럽게 말을 걸고 정보를 물어오며, 분위기를 망치지 않고 장면을 움직인다
- risk if flattened: 편의용 전달 장치로만 쓰이면 캐릭터성이 죽는다
- next likely move: 새 루틴 사이사이로 파고들어 정보 전달과 놀이 감각을 다시 만든다

### ENT-005 데리온 렌바렌
- surface role: 강압적이고 훈련 집착이 강한 형
- hidden state: 계승조회식 이후 가문 비밀과 방계 청소 구조를 안 채 흔들리고 있음. 실질 공포는 타가문 집행자들이 언젠가 동생들을 죽이러 온다는 점이고, 키리온을 단련시키는 집착은 그 구조를 뒤집을 수 있을지 모른다는 불가능한 희망과 연결된다
- current sensitivity: 동생의 마법책 접근, 이상 징후, 연약함에 과민 반응
- narrative use right now: 서고 시험을 생활 루틴과 형제 대련으로 뒤틀어 버리는 가족 압력 축
- next likely move: 연무장, 교정, 치유를 묶은 왜곡된 보호 루틴을 계속 강요한다

### ENT-006 렌바렌 저택 실무 인력 군집
- surface role: 하인, 하녀, 집사실 실무자
- current state: 반복 질문과 생활 정보 병목 속에서도 농담과 잡담이 살아 있는 군집
- story function: 장기 공론장 욕망의 원형을 보여주는 `생활형 사용자 집단`
- current stance toward Kirion: 안내판 사건 이후 `이상하게 정리 잘하는 어린 도련님` 정도의 체감이 생기기 시작함
- next likely move: 유용한 정리에는 빠르게 반응하지만, 권한과 관성은 여전히 집사실/상층 통제를 따른다
