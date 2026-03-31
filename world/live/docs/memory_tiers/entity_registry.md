# entity_registry

## Sync metadata
- sync_category: required
- last_synced_episode: ep005
- sync_source: artifacts/writing/episodes/ep005/canon/5화_리라이트_v1.md
- sync_source_sha256: 3f290485186031271b7aeef509a19df278926fa0c30de40ebea5e9fdefc523ff
- sync_summary: artifacts/writing/episodes/ep005/summary_v1.md

역할: 현재 서사에서 중요한 인물들의 `동적 상태값`을 모아 둔 prompt-facing 엔티티 레지스트리. 고정 설정 카드의 대체물이 아니라, 지금 이 시점의 태도/의심/압박/다음 행동만 추적한다.

## Usage rule
- fixed fact는 world bible이나 캐릭터 카드가 우선한다.
- 이 문서는 `지금 이 인물이 무엇을 알고 무엇을 오해하며 얼마나 강하게 움직이는가`만 남긴다.
- 회차 후 캐릭터의 압박 방식, 관계 온도, 감시 밀도가 변하면 먼저 여기서 갱신한다.

## Entity snapshots

### ENT-001 키리온 렌바렌
- surface role: 열 살 직전의 차남, 저택 실무선에 말이 먹히기 시작한 아이
- true state: 외래 기억 잔향을 바탕으로 `현재의 키리온` 행동 규칙을 보정하며 위장 중
- current goal: 별도 검사 라인으로 불린 이유를 들키지 않은 선에서 넘기고, 세렌이 원하는 게시판을 월권 없이 외부 공간에서도 성립시킬 실마리를 잡기
- what he is hiding: 사고 구조의 출처, 과도한 분류 습관, 외래 기억식 문제 해결 방식
- current pressure: `미계승`으로 일단 남았지만 왜 자기만 별도 라인에 섰는지 모르는 채, 라베르니온 별채 같은 외부 권력 공간에서 게시판 욕망을 꺼내도 되는지 가늠해야 한다
- next likely move: 세렌과 리리아가 발견한 외부 실무 병목을 구조 문제로 읽고, `아버지에게 칭찬받고 싶다`는 세렌의 욕망을 `공적 공간에서도 먹히는 도구`로 번역할 방법을 계산한다

### ENT-002 칼리온 렌바렌
- surface role: 절제된 아버지, 허가와 보상을 줄 줄 아는 보호자
- hidden function: 질문 구조와 선택지 설계로 사람의 정합성을 읽는 감시자/판정자
- current read on Kirion: `유용함`은 공식 인정했지만, 이질감과 출처 불명의 사고에 대한 의심을 거둔 것은 아니다
- operating mode now: 공식 행사장에서는 가장 무난한 분기 가문 보호자처럼 보이되, 결과 이후의 반응과 외부 권력선 접속까지 한꺼번에 읽는 장기 관찰자
- current pressure on Kirion: 식탁 심문은 줄었지만, 계승조회식 결과 앞뒤의 반응과 라베르니온 권력선에서의 움직임이 새 판독 자료가 된다
- next likely move: `미계승` 이후에도 키리온을 곁에 둘 이유와 관찰 방식, 외부 실무선에 어느 정도까지 노출시킬지를 다시 조정한다

### ENT-003 셀리아 그라비온
- surface role: 다정한 어머니, 생활 리듬을 붙들어 주는 보호자
- true story function: 안심이 아니라 경계 해제를 부르는 위험한 이완 장치
- current stance toward Kirion: 거의 무조건적인 보호와 애정
- current effect on scene: 대기실과 결과 직후, 연회 이동 중에도 손과 옷매무새 같은 생활적 접촉으로 키리온의 방어를 늦추면서 `그라비온` 가능성을 조용히 그림자처럼 유지한다
- next likely move: 왕도 체류 동안도 걱정과 돌봄을 섞어 보호자 포지션을 유지하되, 미계승 뒤 남은 모호한 감정이 조금씩 새어 나오게 만든다

### ENT-004 리리아 렌바렌
- surface role: 밝고 수다스럽고 사람 사이를 뛰어다니는 막내
- current functional role: 손 먼저 가는 공동 운영자 + 판을 재밌게 느끼는 공동 창작자 + 공적 공간에서도 장벽을 깨는 사회적 점화기
- stance toward Kirion: 경계 없음, 애정 높음, 오빠와 같이 노는 것을 즐김
- current strength: 사람에게 자연스럽게 말을 걸고 정보를 물어오며, 낯선 또래 무리 속으로도 바로 섞여 들어가 고립된 사람을 판으로 끌어오는 데 강하다
- risk if flattened: 귀여운 추임새나 편의용 전달 장치로만 쓰이면 캐릭터성이 죽는다
- next likely move: 세렌이 `아버지에게 칭찬받을 만한 일`을 실제로 만들 수 있다고 믿고, 외부 공간에서 손댈 병목을 먼저 찾아내 키리온이 구조를 짜도록 판을 계속 밀어붙인다

### ENT-005 데리온 렌바렌
- surface role: 강압적이고 훈련 집착이 강한 형
- hidden state: 계승조회식 이후 가문 비밀과 방계 청소 구조를 안 채 흔들리고 있음. 실질 공포는 타가문 집행자들이 언젠가 동생들을 죽이러 온다는 점이고, 키리온을 단련시키는 집착은 그 구조를 뒤집을 수 있을지 모른다는 불가능한 희망과 연결된다
- current sensitivity: 동생의 마법책 접근, 이상 징후, 몸상태, 그리고 계승조회식 직전 변수에 과민 반응
- narrative use right now: 설명 대신 굳은 몸과 짧은 이완, 그리고 칼리온 쪽으로 다시 붙는 행동으로 사건 무게를 드러내는 가족 축
- next likely move: 공개 공간에서는 더 말을 아끼고, 뒤편 라인에서 칼리온과 함께 다음 조치를 정리하는 쪽으로 움직인다

### ENT-006 렌바렌 저택 실무 인력 군집
- surface role: 하인, 하녀, 집사실 실무자
- current state: 반복 질문과 생활 정보 병목 속에서도 농담과 잡담이 살아 있고, 이제는 집사실 앞 종이 게시판을 실제 업무 기준으로 쓰기 시작한 군집
- story function: 장기 공론장 욕망의 원형을 보여주는 `생활형 사용자 집단`
- current stance toward Kirion: `이상하게 정리 잘하는 어린 도련님`을 넘어, 말이 실제로 먹히는 아이로 체감하기 시작함
- next likely move: 안정화된 규칙 아래 게시판을 계속 쓰되, 충돌하는 최신 정보와 댓글 부재의 한계는 여전히 새 구조를 요구하게 된다

### ENT-007 세렌 라베르니온
- surface role: 라베르니온 공작가 차녀, 이번 계승조회식의 주목받는 승계자
- current functional role: 높은 신분 때문에 또래 세계에서 고립된 채 중심에 앉아 있는 아이, 그리고 `아버지에게 칭찬받고 싶다`는 결핍 때문에 게시판을 원하게 된 첫 외부 협업 접점
- stance toward Kirion and Lyria: 처음엔 격식으로 응답하지만, 둘이 자신을 중앙에서 가장자리로 옮기자 빠르게 호기심과 안도 쪽으로 기운다
- current strength: 타고난 중심성, 이름값, 그리고 `아버지에게 칭찬받고 싶다`는 욕망이 생기면 의외로 빠르게 새로운 구조에 진지하게 붙는 열의
- risk if flattened: 위압적 영애나 로맨스 장식으로만 납작해지면 첫 등장 기능이 죽는다
- next likely move: 게시판을 자기 집에도 두고 싶다는 요청을 더 분명히 하고, 그 과정에서 처음으로 `아버지에게 인정받을지도 모르는 유용한 중심`이 되는 감각을 배우게 된다
