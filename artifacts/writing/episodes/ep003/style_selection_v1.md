# 에피소드 스타일 선택 템플릿

- episode_id: `ep003`
- style_selection_version: `v1`
- target_style_constitution: `episode_style_constitution_v1.md`
- target_packet: `prompt_packet_v1.md`
- pov: ``
- narrative_phase: ``
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
| S-01 | Optional | low |  |
| S-02 | Apply | high |  |
| S-03 | Optional | low |  |
| S-04 | Skip | none |  |
| S-05 | Optional | low |  |
| S-06 | Skip | none |  |
| S-07 | Skip | none |  |
| S-08 | Optional | medium |  |
| S-09 | Skip | none |  |
| S-10 | Skip | none |  |
| S-11 | Optional | low |  |
| S-12 | Optional | low |  |
| S-13 | Skip | none |  |
| S-14 | Skip | none |  |
| S-15 | Skip | none |  |
| S-16 | Skip | none |  |
| S-17 | Skip | none |  |
| S-18 | Skip | none |  |

## 이번 화 Apply 요약
- 

## 이번 화 명시적 Skip
- 

## 문체 헌법 컴파일 메모
- `house_rules`의 고정 규약은 `episode_style_constitution_vN.md`에 기본값으로 포함한다.
- 여기에는 이번 화에서 선택한 패턴만 추가해 `어디에 어떻게 쓰는지`가 드러나게 적는다.
- 실제 모델 주입은 `style_selection_vN.md`가 아니라 컴파일된 `episode_style_constitution_vN.md`를 기준으로 한다.

## 후처리 메모
- 실제 수정본에서 효과가 없었던 패턴은 다음 화에서 기본값을 `Skip`으로 돌린다.
- 반복 안정화된 패턴은 `house_rules.md` 승격 검토 대상으로 표시한다.
