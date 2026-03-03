# character_index_v2 (dynamic)

- generated_at: 2026-03-04
- mode: dynamic
- note: 고정 board/zone 맵핑, 고정 인원수, 고정 ID 대응표를 인덱스 규칙으로 사용하지 않는다.

## SSOT and execution view
- 캐릭터 원본 SSOT는 `characters/*.md`다.
- 본 문서는 실행 시점에 필요한 축만 뽑아 쓰는 경량 파생 뷰다.
- 정적 대량 나열(전원 ID dump)은 금지하고, 요청된 축만 생성한다.

## Dynamic field dictionary
### 최소 필드(권장)
- `id`
- `name`
- `affiliation`
- `role_tags`
- `offline_core`
- `online_persona`
- `rationale`

### 선택 필드(상황별)
- `desire`, `fear`, `flaw`, `secret`
- `relationships`
- `channel_pref`, `avoids`
- `voice`, `psych_rationale`
- `topic_affinity`, `activity_intensity`

## Derived index generation rules
- `frontmatter`를 1순위 입력으로 사용한다.
- `frontmatter` 누락 시 본문 키워드로 약식 추론하되, 추론 필드는 `inferred`로 표시한다.
- 누락 필드는 강제로 채우지 않고 `empty` 상태로 둔다.
- 필드별 개수 제한(예: 관계 2-4개, 주 보드 3개)을 강제하지 않는다.
- 고정 매핑(`B01~B18`, `Zone A~D`, `PA-xxx 1:1`) 규칙을 금지한다.

## Output modes
- quick: `affiliation / role_tags / topic_affinity / activity_intensity` 축만 출력
- deep: 요청된 필드 전체 출력 + 추론 필드 표시

## bootstrap
- 초기 상태에서는 `quick` 모드만 유지한다.
- 정식 리빌드는 `CR-*` 변경 건에서만 수행한다.
