# 문체 헌법 (Style Constitution)

## 상태
- 2026-03-13부터 이 문서는 `문체 규칙 본문`이 아니라 `운영 인덱스`로 관리한다.
- 이유는 `항상 강제해야 하는 규칙`과 `이번 화에서 골라 써야 하는 패턴`의 안정성이 다르기 때문이다.
- 기존 F 규칙과 S 규칙의 내용은 아래 문서들로 분리 이관했다.

## 현재 구성
- [house_rules.md](./house_rules.md)
  - 표기, 개행, 문장부호, 대사 처리처럼 항상 주입하는 비가변 규칙
- [style_pattern_library.md](./style_pattern_library.md)
  - diff에서 추출한 스타일 패턴 보관소
  - 자동 주입 금지. 회차별 선택 후에만 프롬프트로 들어간다
- [episode_style_selection_template.md](./episode_style_selection_template.md)
  - `episodes/<episode_id>/style_selection_vN.md` 작성용 템플릿

## 운영 원칙
1. `house_rules.md`는 항상 읽는다.
2. diff에서 추출한 규칙은 우선 `style_pattern_library.md`에 후보로만 추가한다.
3. 집필 전에는 반드시 해당 회차의 `style_selection_vN.md`에서 `Apply / Skip / Optional`을 먼저 고른다.
4. 프롬프트에는 `house_rules + 이번 화에서 선택한 패턴`만 압축 주입한다.
5. 개별 인물 화법/호칭 패턴은 반복 안정화 시 VFP 또는 캐릭터 카드로 이동시킨다.

## 승격 규칙
- 3화 이상 반복해도 무리 없이 유지되는 규칙
- 특정 장면, 특정 가족 구도, 특정 아크에 묶이지 않는 규칙
- 개별 인물 말투보다 작품 전반의 엔진 기본값에 가까운 규칙

위 조건을 만족하면 `style_pattern_library.md`의 패턴을 `house_rules.md`로 승격 검토한다.

## 주입 우선순위
1. `house_rules.md`
2. `episodes/<episode_id>/style_selection_vN.md`
3. `voice_fingerprint`
4. `Layer A/B culture`
5. `Big5 + population_grammar`

`style_pattern_library.md`는 참고용 저장소이지, 직접 주입하는 레이어가 아니다.

## 변경 이력

| 날짜 | 변경 내용 |
|---|---|
| 2026-03-13 | 기존 단일 `style_constitution.md`를 `house_rules / pattern_library / episode_style_selection` 3단 구조로 분리하고, 본 문서를 인덱스로 전환 |
