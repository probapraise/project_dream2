# entity_registry

## Sync metadata
- sync_category: required
- last_synced_episode: ep004
- sync_source: artifacts/writing/episodes/ep004/canon/4화_리라이트_v1.md
- sync_source_sha256: 4b3b443b7e80f44e51636775e8322dbf82d028cdba23febecf38f58b53182a3e
- sync_summary: artifacts/writing/episodes/ep004/summary_v1.md

역할: 현재 서사에서 중요한 인물들의 `동적 상태값`을 모아 둔 prompt-facing 엔티티 레지스트리. 고정 설정 카드의 대체물이 아니라, 지금 이 시점의 태도/의심/압박/다음 행동만 추적한다.

## Usage rule
- fixed fact는 world bible이나 캐릭터 카드가 우선한다.
- 이 문서는 `지금 이 인물이 무엇을 알고 무엇을 오해하며 얼마나 강하게 움직이는가`만 남긴다.
- 회차 후 캐릭터의 압박 방식, 관계 온도, 감시 밀도가 변하면 먼저 여기서 갱신한다.

## Entity snapshots

### ENT-001 키리온 렌바렌
- surface role: 열 살 직전의 차남, 저택 실무선에 말이 먹히기 시작한 아이
- true state: 외래 기억 잔향을 바탕으로 `현재의 키리온` 행동 규칙을 보정하며 위장 중
- current goal: 계승조회식 판정선을 버티고, `댓글` 구조를 마법으로 풀 장기 실마리를 놓치지 않으면서 성이 유지되는지 확인하기
- what he is hiding: 사고 구조의 출처, 과도한 분류 습관, 외래 기억식 문제 해결 방식
- current pressure: 게시판 성공으로 영향력과 시선이 함께 커진 상태에서, 왕도 소집과 계승조회식이 바로 눈앞에 와 있어 결과에 따라 `렌바렌` 성 자체가 흔들릴 수 있다
- next likely move: 왕도에서 의식 절차와 주변 반응을 읽으며, 문장비전 계승 여부와 가문 이동 가능성 앞에서 자기 반응을 최대한 억제한다

### ENT-002 칼리온 렌바렌
- surface role: 절제된 아버지, 허가와 보상을 줄 줄 아는 보호자
- hidden function: 질문 구조와 선택지 설계로 사람의 정합성을 읽는 감시자/판정자
- current read on Kirion: `유용함`은 공식 인정했지만, 이질감과 출처 불명의 사고에 대한 의심을 거둔 것은 아니다
- operating mode now: `잘했다.` 이후 직접 질문은 줄였지만, 허가와 보상을 섞어 더 조용한 장기 관찰로 옮겨 간 감시자
- current pressure on Kirion: 노골적인 식탁 시험은 약해졌어도, 더 큰 공식 판정선인 계승조회식 앞에서 어떻게 반응하는지가 새 판독 자료가 된다
- next likely move: 계승조회식 결과와 그 앞뒤의 가족 반응을 읽고, 키리온에게 줄 자유와 관찰 강도를 다시 조정한다

### ENT-003 셀리아 그라비온
- surface role: 다정한 어머니, 생활 리듬을 붙들어 주는 보호자
- true story function: 안심이 아니라 경계 해제를 부르는 위험한 이완 장치
- current stance toward Kirion: 거의 무조건적인 보호와 애정
- current effect on scene: 키리온의 방어를 잠시 늦추고, 출발 준비와 생활 리듬을 붙드는 완충 역할을 하면서도 `그라비온` 혈통이라는 다른 갈래 가능성을 장면 뒤에 세운다
- next likely move: 계승조회식 전후에도 걱정, 잔소리, 생활 돌봄을 섞어 보호자 포지션을 유지한다

### ENT-004 리리아 렌바렌
- surface role: 밝고 수다스럽고 사람 사이를 뛰어다니는 막내
- current functional role: 손 먼저 가는 공동 운영자 + 판을 재밌게 느끼는 공동 창작자 + 자연스러운 메신저
- stance toward Kirion: 경계 없음, 애정 높음, 오빠와 같이 노는 것을 즐김
- current strength: 사람에게 자연스럽게 말을 걸고 정보를 물어오며, 손 먼저 가는 발상과 생활어 반응으로 장면을 움직인다
- risk if flattened: 귀여운 추임새나 편의용 전달 장치로만 쓰이면 캐릭터성이 죽는다
- next likely move: 저택에 남아 집사실 앞 게시판의 공기를 이어가되, 이번 소집 대상에서 빠진 채 오빠 혼자 떠나는 상황을 받아들여야 한다

### ENT-005 데리온 렌바렌
- surface role: 강압적이고 훈련 집착이 강한 형
- hidden state: 계승조회식 이후 가문 비밀과 방계 청소 구조를 안 채 흔들리고 있음. 실질 공포는 타가문 집행자들이 언젠가 동생들을 죽이러 온다는 점이고, 키리온을 단련시키는 집착은 그 구조를 뒤집을 수 있을지 모른다는 불가능한 희망과 연결된다
- current sensitivity: 동생의 마법책 접근, 이상 징후, 몸상태, 그리고 계승조회식 직전 변수에 과민 반응
- narrative use right now: 2년 동안 지속된 훈련 루틴과 계승조회식 직전의 눌린 긴장을 통해, 설명보다 행동으로 압력을 거는 가족 축
- next likely move: 말수 줄인 채 마지막 대련과 점검을 밀어붙이고, 의식 결과를 기다리며 더 굳어진다

### ENT-006 렌바렌 저택 실무 인력 군집
- surface role: 하인, 하녀, 집사실 실무자
- current state: 반복 질문과 생활 정보 병목 속에서도 농담과 잡담이 살아 있고, 이제는 집사실 앞 종이 게시판을 실제 업무 기준으로 쓰기 시작한 군집
- story function: 장기 공론장 욕망의 원형을 보여주는 `생활형 사용자 집단`
- current stance toward Kirion: `이상하게 정리 잘하는 어린 도련님`을 넘어, 말이 실제로 먹히는 아이로 체감하기 시작함
- next likely move: 안정화된 규칙 아래 게시판을 계속 쓰되, 충돌하는 최신 정보와 댓글 부재의 한계는 여전히 새 구조를 요구하게 된다
