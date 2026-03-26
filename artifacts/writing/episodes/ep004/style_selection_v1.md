# 에피소드 스타일 선택 템플릿

- episode_id: `ep004`
- style_selection_version: `v1`
- target_style_constitution: `episode_style_constitution_v1.md`
- target_packet: `prompt_packet_v1.md`
- pov: `키리온 1인칭`
- narrative_phase: `pre-academy 후반 — 첫 보상 + 욕망 쇼케이스 + 계승조회식 출발`
- always_load:
  - `artifacts/writing/style/house_rules.md`
  - `world/live/docs/style_bible.md`
  - `world/live/docs/voice_fingerprint_spec.md` 또는 해당 인물 카드

## 사용 순서
1. `house_rules.md`를 먼저 읽는다.
2. `style_pattern_library.md`에서 이번 화에 유효한 패턴만 고른다.
3. 선택 결과를 이 문서에 `Apply / Skip / Optional`로 기록한다.
4. `house_rules + Apply 패턴`을 합쳐 `episode_style_constitution_vN.md`를 작성한다.
5. 실제 모델 주입에는 `style_selection_vN.md`가 아니라 `episode_style_constitution_vN.md`를 사용한다.

## 선택 기준
- 이번 화의 중심 갈등을 직접 강화하는가?
- 현재 POV와 인물 조합에 실제로 맞는가?
- 이번 화에서만 의미 있는 패턴을 괜히 전역 규칙처럼 밀어 넣고 있지 않은가?
- 빠지면 분명히 손해가 나는가, 아니면 그냥 있으면 그럴듯한 정도인가?

## 운영 원칙
- Apply는 보통 5~8개 안쪽으로 제한한다.
- `Optional`은 실제 프롬프트 압축본에 넣지 않아도 된다.
- character-specific 패턴은 해당 인물이 안 나오면 기본 `Skip`이다.
- arc-specific 패턴은 서사 국면이 바뀌면 기본 `Skip`이다.

## 패턴 결정표

| 규칙 | 결정 | 강도 | 이유 |
|---|---|---|---|
| S-01 | Apply | medium | Beat 3 몽타주 계절 마커(먼지/땀/서리/입김), Beat 4 첫 외출 마차 감각. 장소와 시간이 빠르게 바뀌는 화라 착지마다 감각 겹침이 필요하다. |
| S-02 | Apply | high | 전 비트 공통. Beat 2에서 키리온이 흥분할 때 몸이 먼저 반응하는 것, Beat 3 칼리온 칭찬 직후 숨통이 트이는 감각, Beat 4 데리온의 긴장이 손과 턱에 스미는 것. |
| S-03 | Apply | medium | Beat 2에서 커뮤니티를 설명하다가 전생 감각이 스며 나오는 균열. Beat 3 칼리온 인정 직후 8세 몸이 허락한 안도. 2~3회 제한. |
| S-04 | Skip | none | 호칭 긴장은 이미 수렴 단계. 이번 화 핵심이 아니다. |
| S-05 | Apply | medium | Beat 2 전체가 키리온의 설계자 사고를 보여주는 장면. 댓글/쓰레드/필터링 같은 개발자 비유가 내면에서 자연스럽게 나와야 한다. 다만 리리아에게 말할 때는 비유를 이 세계 언어로 번역한다. |
| S-06 | Skip | none | 셀리아와 칼리온이 같은 장면에서 대비될 계기가 없다. |
| S-07 | Skip | none | 이번 화는 자기 의심이 아니라 욕망과 확신의 화다. |
| S-08 | Apply | high | Beat 4 화말: 저택 밖이 열리는 감각을 단문 압축으로 잠근다. |
| S-09 | Skip | none | IT 레퍼런스는 S-05의 비유 체계로 충분. 별도 호출 불필요. |
| S-10 | Skip | none | 전생 기억 흐릿함보다 VFP 레지스터 전환이 이번 화 도구다. |
| S-11 | Optional | low | Beat 3 몽타주에서 계절 전환 시 한두 번 쓸 수 있지만, 몽타주 속도가 우선이라 강제하지 않는다. |
| S-12 | Optional | low | ep003만큼 긴장 주도 화가 아니다. Beat 4-c 데리온 침묵에서 한두 번 쓸 수 있는 정도. |
| S-13 | Skip | none | 이번 화에서 키리온은 설계를 리리아에게 적극 설명한다. 끊는 게 아니라 펼치는 화. |
| S-14 | Skip | none | 일상 돌봄의 긴장 역전이 아니라 보상과 전진의 화. |
| S-15 | Skip | none | 위장 보정이 핵심 장면에 없다. |
| S-16 | Apply | medium | Beat 2에서 키리온이 정보의 상태(확정/미정/충돌)를 분류하며 댓글의 필요성을 보여주는 장면. 정보 설계자의 사고를 직접 드러내는 핵심 도구. |
| S-17 | Apply | medium | Beat 3-e: 하인들이 키리온 의견을 실질적 지시로 취급하기 시작하는 장면. 성공은 선언이 아니라 사용자 반응으로 증명해야 한다. |
| S-18 | Optional | low | Beat 3의 보상은 이번에는 진짜 보상이다. 다만 Beat 4의 계승조회식이 새 긴장을 여는 구조이므로, 화 전체로 보면 보상→새 압박의 흐름이 존재한다. 강제하지 않되 Beat 4 전환에서 자연스럽게 스며들 수 있다. |

## 이번 화 Apply 요약 (7개)
- S-01 감각 중첩 (medium) — 몽타주 계절 마커, 첫 외출
- S-02 신체 반응으로 감정 (high) — 전 비트
- S-03 감정의 미세한 균열 (medium) — 커뮤니티 설명 중 전생 감각 스밈, 칼리온 인정 후 안도
- S-05 개발자 화자의 비유 (medium) — Beat 2 설계자 사고
- S-08 압축형 결말 비트 (high) — Beat 4 화말
- S-16 정보 구조화는 상태 분류 (medium) — Beat 2 댓글 필요성 시연
- S-17 작은 승리는 사용자 반응으로 증명 (medium) — Beat 3 하인 태도 변화

## 이번 화 명시적 Skip
- S-04 호칭 전략 — 수렴 단계
- S-06 대사 대비 — 해당 장면 없음
- S-07 자기 의심 — 욕망/확신의 화
- S-09 VR/IT 레퍼런스 — S-05로 충분
- S-10 전생 기억 흐릿함 — VFP 레지스터 전환이 대체
- S-13 분석을 설계 직전에서 끊기 — 이번 화는 펼치는 화
- S-14 일상 돌봄으로 긴장 — 보상 화
- S-15 위장 보정 — 해당 장면 없음

## 문체 헌법 컴파일 메모
- `house_rules`의 고정 규약은 `episode_style_constitution_vN.md`에 기본값으로 포함한다.
- 여기에는 이번 화에서 선택한 패턴만 추가해 `어디에 어떻게 쓰는지`가 드러나게 적는다.
- 실제 모델 주입은 `style_selection_vN.md`가 아니라 컴파일된 `episode_style_constitution_vN.md`를 기준으로 한다.

## 후처리 메모
- 실제 수정본에서 효과가 없었던 패턴은 다음 화에서 기본값을 `Skip`으로 돌린다.
- 반복 안정화된 패턴은 `house_rules.md` 승격 검토 대상으로 표시한다.
