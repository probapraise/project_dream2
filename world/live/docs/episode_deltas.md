# episode_deltas

## Sync metadata
- sync_category: required
- last_synced_episode: ep002
- sync_source: artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md
- sync_source_sha256: 17673b87624ec2a117ae5776a5ebf816a593199f158942f07badf25f84528203
- sync_summary: artifacts/writing/episodes/ep002/summary_v1.md

역할: 회차별 줄거리 요약이 아니라, 캐논 이후 실제로 바뀐 상태만 남기는 로그.

## Usage rule
- 기본 집필 시에는 직전 1~2화만 로딩한다.
- 오래된 회차는 이 문서보다 `story_arcs.md`와 `foreshadow_registry.md`를 우선 참조한다.
- 각 엔트리는 `state_changes`, `activated_refs`, `closed_refs`, `carry_forward`만 남기고 줄거리 재현은 최소화한다.

## DELTA-EP000 `ep000_prologue`
- canon_source: `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v2.md`
- state_changes:
  - 주인공은 8세 `키리온 렌바렌`의 몸에서 깨어났고, 현재 상황을 생존 문제로 인식했다.
  - 칼리온 렌바렌은 질문 구조와 미세한 반응 관찰로 주인공의 정합성을 테스트하는 위협 축으로 설정됐다.
  - 셀리아 그라비온은 계산 없는 온기를 제공하는 보호 축으로 설정됐다.
  - 주인공은 전생의 커뮤니티 유지보수 개발자 감각과 정보 구조 설계 습관을 회수했지만, 당장은 거대한 선언보다 저택 내부 생존을 우선하기로 결론내렸다.
- activated_refs:
  - `ARC-001`
  - `ARC-002`
  - `ARC-003`
  - `FS-001`
  - `FS-002`
  - `FS-006`
- closed_refs:
  - 없음
- carry_forward:
  - 다음 회차에서도 "아버지의 관찰망"과 "어머니의 위험한 이완"을 동시에 유지해야 하며, 장기 공론장 욕망은 아직 생존 우선순위 아래 눌린 상태로 가져간다.

## DELTA-EP001 `ep001`
- canon_source: `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
- state_changes:
  - 주인공은 치유사 검사 전에 반응 속도/어휘/행동을 통제하는 생존 규칙을 자의식적으로 세웠다.
  - 치유사 검사는 통과했지만, 이 결과는 정체 안전 보장이 아니라 즉시 발각만 피한 상태로 남았다.
  - 셀리아와의 복도 산책을 통해 일상적 돌봄이 긴장을 느슨하게 만드는 리듬이 재확인됐고, 학술원 입학까지 4년이 남았다는 외부 시간축이 처음 명시됐다.
  - 집사실 관찰로 렌바렌 저택 행정 체계의 정보 병목이 드러났고, 하인들의 반복 문답과 농담 속에서 주인공이 사랑하던 커뮤니티적 온도가 다시 점화됐다.
  - 주인공은 양피지/분류 체계 기반의 조악한 게시판 구조를 상상했지만, 아직 실행 대신 관찰에 머물렀다.
  - 칼리온이 보낸 `흑색 표준식 입문서`가 다음 회차의 핵심 압박 장치로 추가됐다.
- activated_refs:
  - `FS-003`
  - `FS-004`
  - `FS-005`
- closed_refs:
  - 없음
- carry_forward:
  - `ep002`는 책 자체보다 "읽는 방식이 관찰 대상이 되는 상황"과 "설계 충동을 얼마나 숨길 수 있는가"를 함께 중심축으로 가져가야 한다.

## DELTA-EP002 `ep002`
- canon_source: `artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md`
- state_changes:
  - 키리온은 리리아를 통해 `타인이 기억하는 원래 키리온의 행동 규칙`을 일부 회수했고, 단순 위장이 아니라 타인 기억 기반 보정이 필요하다는 사실을 분명히 인식했다.
  - 집사실 앞 정보 병목을 조악한 안내판으로 정리해, 이 세계에서 처음으로 작은 설계 성공을 실제 사용자의 반응으로 증명했다.
  - 리리아는 정서 자산을 넘어, 정보를 모으고 사람 사이를 오가며 장면을 움직이는 실행 조력자로 자리 잡았다.
  - 칼리온의 시험은 `흑색 입문서를 읽는가`에서 끝나지 않고, `서고에서 무엇을 먼저 고르는가`까지 포함하는 선택 구조 평가로 확장됐다.
  - 보상처럼 보이는 `서고 접근권`과 `자색 표준식 입문서 열람 허가`는 즉시 다음 감시 단계로 재해석됐다.
  - 키리온은 서고 시험을 정면으로 받지 않기 위해 데리온의 예민한 반응을 먼저 끌어들이는 우회 해법을 택했다.
- activated_refs:
  - `FS-007`
- closed_refs:
  - 없음
- carry_forward:
  - `ep003`는 `첫 책 선택` 자체가 시험이 된 상황과, 데리온 개입으로 그 시험장을 비틀려는 키리온의 우회 설계를 함께 중심축으로 가져가야 한다.
