# 에피소드 스타일 선택 템플릿

- episode_id: `ep005`
- style_selection_version: `v1`
- target_style_constitution: `episode_style_constitution_v1.md`
- target_packet: `prompt_packet_v1.md`
- pov: `키리온 1인칭`
- narrative_phase: `pre-academy — 계승조회식 현장 + 라베르니온 연회 + 세렌 첫 접속`
- always_load:
  - `artifacts/writing/style/house_rules.md`
  - `world/live/docs/style_bible.md`
  - `artifacts/writing/episodes/lavernion_sisters_character_design_v1.md` (세렌 화법 참조)

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
| S-01 | Apply | medium | 장소가 3회 바뀐다(왕도→검정건물→연회장). 각 착지마다 감각 2~3개를 겹쳐 공기 전환을 찍어야 한다. Beat 1 대기실의 냄새/소리/온도, Beat 2 복도의 발소리/벽 질감, Beat 3 연회장의 소리/음식/조명. |
| S-02 | Apply | high | 전 비트 기본 도구. Beat 2-c 따로 호명 시 긴장(손 떨림, 심장), Beat 2-d 검사 끝 안도(어깨 풀림, 숨), Beat 2-f 데리온의 미세 이완(어깨가 한 번 내려감), Beat 3-d 리리아에게 손목 잡힐 때 저항감. |
| S-03 | Apply | medium | Beat 2-e: 미계승 안도 + 아쉬움이 동시에 올 때 10세 몸의 불수의 반응. Beat 3-e: 세렌과의 대화에서 '별 관심 없다'면서 중간중간 보조하는 행동 — 본인은 모르는 관심의 틈. 2~3회 제한. |
| S-04 | Skip | none | 호칭은 이미 수렴 단계. 이번 화 핵심이 아니다. |
| S-05 | Optional | low | Beat 3-b 계승/미계승 벽 관찰에서 짧게 쓸 수 있지만 강제하지 않음. 이번 화는 설계자 사고보다 관찰자 사고가 중심. |
| S-06 | Skip | none | 셀리아/칼리온 대비가 핵심 장면에 없다. |
| S-07 | Skip | none | 이번 화는 자기 의심이 아니라 외부 판정 긴장과 관찰이 중심. |
| S-08 | Apply | high | Beat 4-c: 세렌의 '하고 싶다'로 화를 닫는 순간. 짧은 압축으로 잠가야 한다. |
| S-09 | Skip | none | IT 레퍼런스 호출 계기가 없다. |
| S-10 | Skip | none | 전생 정보 환기가 핵심이 아니다. |
| S-11 | Apply | medium | Beat 1-b/c 대기실의 정적 공기 — 시간축을 넣으면 대기의 무게가 산다. Beat 3-c 세렌이 홀 한가운데 앉아 있는 정지 장면 — 고립이 선명해진다. |
| S-12 | Apply | medium | Beat 2-b/c: 따로 호명 → 복도 → 검사실 긴장 상승이 이번 화 최대 긴장점. 단문 절단이 가장 효과적인 구간. |
| S-13 | Skip | none | 이번 화에서 분석을 끊는 것보다 순수 관찰 모드가 맞다. |
| S-14 | Optional | low | Beat 1-e 셀리아 옷깃 정리에서 약간 쓸 수 있지만 핵심은 아니다. |
| S-15 | Skip | none | 위장이 핵심 장면에 없다. |
| S-16 | Skip | none | 정보 분류보다 사회 구조 관찰이 이번 화 중심이다. |
| S-17 | Skip | none | 설계 성공 증명 장면이 없다 (게시판은 ep004에서 이미 증명). |
| S-18 | Optional | low | Beat 2-e 이중 감정(안도→칼리온 감시 지속)에서 자연스럽게 스밀 수 있지만 강제하지 않음. |

## 이번 화 Apply 요약 (6개)
- S-01 감각 중첩 (medium) — 장소 3회 전환마다 감각 착지
- S-02 신체 반응으로 감정 (high) — 전 비트 기본 도구
- S-03 감정의 미세한 균열 (medium) — 미계승 안도 + 세렌 대화 중 무의식적 관심
- S-08 압축형 결말 비트 (high) — Beat 4 화말
- S-11 정지 묘사에 시간축 (medium) — 대기실, 세렌 고립 장면
- S-12 긴장 구간 단문 절단 (medium) — Beat 2 따로 호명~검사실

## 이번 화 명시적 Skip
- S-04 호칭 전략 — 수렴 단계
- S-06 대사 대비 — 해당 장면 없음
- S-07 자기 의심 — 외부 판정 긴장 중심
- S-09 VR/IT 레퍼런스 — 호출 계기 없음
- S-10 전생 기억 흐릿함 — 환기 불필요
- S-13 분석 끊기 — 관찰 모드가 맞음
- S-15 위장 보정 — 해당 장면 없음
- S-16 정보 구조화 — 사회 구조 관찰이 중심
- S-17 사용자 반응 증명 — 해당 장면 없음

## 문체 헌법 컴파일 메모
- `house_rules`의 고정 규약은 `episode_style_constitution_vN.md`에 기본값으로 포함한다.
- 여기에는 이번 화에서 선택한 패턴만 추가해 `어디에 어떻게 쓰는지`가 드러나게 적는다.
- 실제 모델 주입은 `style_selection_vN.md`가 아니라 컴파일된 `episode_style_constitution_vN.md`를 기준으로 한다.

## 후처리 메모
- 실제 수정본에서 효과가 없었던 패턴은 다음 화에서 기본값을 `Skip`으로 돌린다.
- 반복 안정화된 패턴은 `house_rules.md` 승격 검토 대상으로 표시한다.
