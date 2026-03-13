# writing/

집필 파이프라인 산출물 저장소.

현재 운영 기준 문서이며, 아래 트리는 대표 구조 예시다.

## 폴더 구조

```text
writing/
├── README.md                               ← 이 파일
├── assembly_notes_template.md              ← 멀티 초고 조립 메모 템플릿
├── episode_setting_brief_template.md       ← 이번 화 설정 정리 템플릿
├── episode_style_constitution_template.md  ← 이번 화 문체 헌법 템플릿
├── live_sync_manifest.json                 ← canon -> live 문서 sync 감사 대상 선언
├── long_range_summary_template.md          ← 최근 3회차 이전 장기 맥락 요약 템플릿
├── prompt_packet_template.md               ← 주입 순서/우선순위 패킷 템플릿
├── prompt_template.md                      ← 이번 화 비트 프롬프트 템플릿
├── revision_delta_template.md              ← 멀티 초고↔수정본 비교 템플릿
├── style/
│   ├── style_constitution.md               ← 문체 운영 인덱스
│   ├── house_rules.md                      ← 항상 읽는 고정 집필 규약
│   ├── style_pattern_library.md            ← diff 추출 패턴 라이브러리
│   └── episode_style_selection_template.md ← Apply/Skip/Optional 선택 템플릿
├── episodes/
│   ├── README.md                           ← 에피소드 폴더 규칙 / canon 운영 규칙
│   ├── ep000_prologue/
│   │   ├── canon/
│   │   │   ├── README.md
│   │   │   └── 프롤로그_리라이트_v2.md
│   │   └── ...
│   ├── ep002/
│   │   ├── canon/
│   │   ├── drafts/
│   │   ├── assembled/
│   │   ├── analysis/
│   │   ├── style_selection_v1.md
│   │   ├── episode_style_constitution_v1.md
│   │   ├── setting_brief_v1.md
│   │   ├── long_range_summary_v1.md
│   │   ├── prompt_packet_v1.md
│   │   ├── prompt_v1.md
│   │   └── ...
│   └── ...
```

## canon 폴더 규칙

- 각 에피소드 폴더는 생성 시점부터 반드시 `canon/` 하위 폴더를 포함한다.
- 정식 반영된 최종본은 항상 `canon/` 안에 둔다.
- canon은 고정 불변이 아니다. 새 리비전이나 사후 패치가 채택되면 `canon/` 안에 새 snapshot 파일을 추가하고 `canon/README.md`의 current 항목을 갱신한다.
- superseded canon도 비교와 회고를 위해 `canon/` 안에 남길 수 있다.
- current canon 내용 해시는 `canon/README.md`의 `current_text_canon_sha256`로 관리한다.
- current canon을 나중에 다시 손볼 때는 가능하면 기존 파일을 덮어쓰기보다 `bash scripts/writing/new_canon_patch.sh <episode_id> <new_canon_filename>`로 새 snapshot을 만든 뒤 수정한다.
- 초안, 중간 수정본, 비교 분석, 주입 패킷 문서는 에피소드 루트에 남겨 workflow 흔적과 구분한다.
- canon 파일명은 `revision_vN.*`처럼 버전형이어도 되고, 제목형 파일명이어도 된다. 어떤 파일이 current canon인지는 `canon/README.md`가 결정한다.

## 새 에피소드 폴더 생성

```bash
bash scripts/writing/new_episode_scaffold.sh ep002
```

- 위 스크립트는 에피소드 폴더, `canon/README.md`, `drafts/`, `assembled/`, `analysis/`, `style_selection_v1.md`, `episode_style_constitution_v1.md`, `setting_brief_v1.md`, `long_range_summary_v1.md`, `prompt_packet_v1.md`, `prompt_v1.md`를 함께 생성한다.
- 현재 canon 파일이 아직 없으면 `current_text_canon: none`, `current_word_canon: none` 상태로 시작한다.

## 워크플로우

```text
0. `bash scripts/writing/new_episode_scaffold.sh <episode_id>`
   ↓
1. 기획 대화 (오케스트레이터)
   ↓
2. `house_rules` 확인 + `style_selection_vN.md` 작성
   ↓
3. `episode_style_constitution_vN.md` 컴파일
   ↓
4. `setting_brief_vN.md` + `long_range_summary_vN.md` 작성
   ↓
5. 최근 3회차 raw canon 선정 + `prompt_packet_vN.md` 작성
   ↓
6. `prompt_vN.md` 작성 (이번 화 비트 지시서)
   ↓
7. 외부 집필 모델/코덱스에 패킷 순서대로 전달 → `drafts/draft_<source>_vN.txt` 저장
   ↓
8. 작가가 여러 초고를 조립 → `assembled/assembly_notes_vN.md` + `assembled/revision_assembled_vN.txt`
   ↓
9. 정식 반영본 확정 → `canon/<canon_filename>`으로 이동/저장 + `canon/README.md` current 갱신
   ↓
10. 멀티 초고↔조립본↔캐논 비교 분석 → `analysis/revision_delta_vN.md` 저장
   ↓
11. diff 누적 → style/style_pattern_library.md 갱신
   ↓
12. `bash scripts/writing/post_canon_sync.sh <episode_id>`로 live sync 대상 점검
   ↓
13. `python3 scripts/writing/audit_live_sync.py` 통과 확인
```

## 파일 종류별 형식

| 파일 | 형식 | 네이밍 예시 |
|---|---|---|
| 스타일 선택지 | markdown (.md) | `style_selection_v1.md` |
| 이번 화 문체 헌법 | markdown (.md) | `episode_style_constitution_v1.md` |
| 이번 화 설정 정리 | markdown (.md) | `setting_brief_v1.md` |
| 장기 맥락 요약 | markdown (.md) | `long_range_summary_v1.md` |
| 주입 패킷 매니페스트 | markdown (.md) | `prompt_packet_v1.md` |
| 이번 화 비트 프롬프트 | markdown (.md) | `prompt_v1.md`, `prompt_v2.md` |
| 병렬 초고 | text / Word | `drafts/draft_codex_v1.txt`, `drafts/draft_external_a_v1.txt` |
| 조립 메모 | markdown (.md) | `assembled/assembly_notes_v1.md` |
| 조립 수정본 | text / Word | `assembled/revision_assembled_v1.txt` |
| 정식 canon | text / Word | `canon/revision_v1.txt`, `canon/프롤로그_리라이트_v2.md` |
| 멀티 초고 비교 분석 | markdown (.md) | `analysis/revision_delta_v1.md` |

## 네이밍 규칙

- **폴더**: `ep000` (프롤로그), `ep001` (1화), `ep002` (2화), ...
- **스타일 선택지**: `style_selection_vN.md`
- **이번 화 문체 헌법**: `episode_style_constitution_vN.md`
- **이번 화 설정 정리**: `setting_brief_vN.md`
- **장기 맥락 요약**: `long_range_summary_vN.md`
- **주입 패킷 매니페스트**: `prompt_packet_vN.md`
- **이번 화 비트 프롬프트**: `prompt_vN.md`
- **병렬 초고**: `drafts/draft_<source>_vN.txt`
- **조립 수정본**: `assembled/revision_assembled_vN.txt`
- **조립 메모**: `assembled/assembly_notes_vN.md`
- **비교 분석**: `analysis/revision_delta_vN.md`
- **정식 canon**: `canon/revision_vN.txt` 또는 `canon/<제목>_vN.md`
- **current canon 지시 파일**: `canon/README.md`

## Prompt Packet 운영 규칙

- 실제 모델 주입 순서는 기본적으로 `episode_style_constitution -> setting_brief -> 최근 3회차 raw canon -> long_range_summary -> prompt_vN`이다.
- `style_selection_vN.md`는 작성용 선택 문서이고, 실제 주입 문서는 `episode_style_constitution_vN.md`다.
- `prompt_vN.md`는 더 이상 단독 컨텍스트 문서가 아니다. 이번 화 비트와 목표만 담당한다.
- 사실 충돌 시 `raw canon > long_range_summary > prompt_vN`을 따른다.
- 문체 충돌 시 `episode_style_constitution_vN.md`가 우선한다.
- 새 프롬프트를 만들 때는 기존 회차 `prompt_vN.md`를 복사하기보다 `prompt_packet_template.md`와 `prompt_template.md`를 출발점으로 사용한다.
- 최근 3회차 raw canon은 기본값이다. 토큰이 빠듯해도 최신 회차 원문부터 유지한다.
- 과거 단일 `prompt_vN.md` 작업본은 히스토리로 취급한다.

## 문체 운영 규칙

- `style/house_rules.md`는 항상 읽는 작성 소스다.
- diff에서 뽑은 문체 규칙은 곧바로 전역 주입하지 않고 `style/style_pattern_library.md`에 후보로만 추가한다.
- 집필 전에는 `episodes/<episode_id>/style_selection_vN.md`에서 이번 화 적용 패턴만 고른다.
- 고른 결과는 `episodes/<episode_id>/episode_style_constitution_vN.md`로 컴파일해 실제 주입한다.
- 조립본은 "초고 하나의 수정본"이 아니라 "여러 초고의 합성본"으로 취급한다.
- `style_pattern_library.md` 반영 판단은 가능하면 단일 초고가 아니라 `analysis/revision_delta_vN.md`의 멀티 초고 비교 기록을 근거로 한다.

## Live Sync Audit

- 선언 파일: `artifacts/writing/live_sync_manifest.json`
- 감사 스크립트: `python3 scripts/writing/audit_live_sync.py`
- post-canon 보조 스크립트: `bash scripts/writing/post_canon_sync.sh <episode_id>`
- canon metadata refresh: `python3 scripts/writing/refresh_canon_metadata.py <episode_id>`
- canon patch snapshot: `bash scripts/writing/new_canon_patch.sh <episode_id> <new_canon_filename>`
- 각 live 문서는 상단 `## Sync metadata` 섹션에 `sync_category`, `last_synced_episode`, `sync_source`, `sync_summary`를 기록한다.
- 각 live 문서는 `sync_source_sha256`도 함께 기록해, 같은 episode 안의 캐논 사후 패치도 감지한다.
- `required` 문서는 최신 current canon과 반드시 같아야 한다.
- `conditional` 문서는 소폭 lag를 허용하지만, manifest 기준을 넘으면 drift 실패로 본다.
- `manual` 문서는 참고용으로 추적하되, audit 실패 대상에는 포함하지 않는다.
