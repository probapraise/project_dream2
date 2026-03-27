# episodes/

에피소드별 집필 산출물 저장 구역.

## 표준 구조

```text
episodes/
└── <episode_id>/
    ├── canon/
    │   ├── README.md
    │   └── <current_text_canon>.md
    ├── drafts/
    │   ├── draft_codex_vN.txt
    │   └── draft_<optional_patch_source>_vN.txt
    ├── assembled/
    │   ├── assembly_notes_vN.md
    │   └── revision_assembled_vN.txt
    ├── analysis/
    │   ├── episode_scorecard_vN.md
    │   └── revision_delta_vN.md
    ├── style_selection_vN.md
    ├── episode_style_constitution_vN.md
    ├── setting_brief_vN.md
    ├── long_range_summary_vN.md
    ├── prompt_packet_vN.md
    ├── prompt_vN.md
    └── ...
```

## 규칙

- 모든 에피소드 폴더는 생성 시점부터 `canon/` 하위 폴더를 포함한다.
- `canon/`에는 `README.md`를 제외하고 현재 정식 canon 파일 1개만 둔다.
- `canon/README.md`는 `current_text_canon`과 `current_text_canon_sha256`를 명시하는 지시 파일이며, `current_word_canon`은 단일 파일 원칙 때문에 항상 `none`으로 유지한다.
- canon 사후 수정이 필요하면 새 canon 파일을 추가하지 말고 현재 canon 파일을 직접 수정한 뒤 `canon/README.md` 해시와 downstream 참조를 갱신한다.
- 과거 canon snapshot, patch snapshot, Word 복제본은 `canon/` 안에 두지 않는다. 비교와 회고는 `git history`, `assembled/`, `analysis/`로 처리한다.
- 기준 초고와 선택적 보조 패치는 `drafts/`, 사용자 수정 감사 메모/작업 수정본은 `assembled/`, 초고↔수정본 비교 분석은 `analysis/`에 둔다.
- `analysis/episode_scorecard_vN.md`는 회차 속도계다. 요약문이 아니라 감정/정보/위험/약속/훅 기준으로 독자 체감을 점검한다.
- scorecard는 `assembled/revision_assembled_vN.txt` 또는 현재의 직접 사용자 수정 작업면 기준으로 1차 작성하고, canon 확정 뒤 최종 갱신한다.
- `style_selection_vN.md`는 내부 선택 문서다. 실제 모델에는 `episode_style_constitution_vN.md`를 넣는다.
- `setting_brief_vN.md`는 이번 화에 실제로 필요한 설정만 담는다.
- `long_range_summary_vN.md`는 global `memory_tiers`에 안 들어가는 이번 화 한정 보조 장기 맥락만 담는다.
- `prompt_packet_vN.md`는 주입 순서와 우선순위를 명시하는 패킷 문서다.
- `artifacts/writing/style/author_preference_registry.md`는 회차별 문서가 아니지만, 모든 초고 생성 전에 함께 읽는 전역 취향 레이어다.
- `prompt_vN.md`는 이번 화 비트와 목표만 담당하는 마지막 지시서다.
- `prompt_packet_vN.md`의 `recent_canon_*_path/sha256`는 현재 canon window와 맞아야 한다.
- 실제 기본 주입에는 `world/live/docs/memory_tiers/recent.md`, `current_arc.md`, `entity_registry.md`, `long_term.md`가 함께 들어간다.
- 새 프롬프트 초안은 `artifacts/writing/prompt_packet_template.md`와 `artifacts/writing/prompt_template.md`를 기준으로 작성하고, 과거 단일 `prompt_vN.md`는 히스토리로 취급한다.
- `assembled/assembly_notes_vN.md`는 더 이상 멀티 초고 조립 기록이 아니라, `코덱스 초고 -> 사용자 수정 -> 선택적 AI 보강` 흐름의 수정 의도 로그다.
- canon 확정 뒤에는 `bash scripts/writing/post_canon_sync.sh <episode_id>`로 live sync 대상과 drift 상태를 바로 확인한다.
- 다음 회차가 이미 준비돼 있으면 `python3 scripts/writing/audit_prompt_packet.py <next_episode_id>`로 패킷 stale 여부도 확인한다.
- canon 파일명은 제목형이든 기계식이든 가능하지만, `canon/` 안에는 현재 파일 1개만 남겨 둔다. 어떤 파일이 current canon인지는 `canon/README.md`가 결정한다.

## 생성 커맨드

```bash
bash scripts/writing/new_episode_scaffold.sh ep002
```

- 스캐폴드는 `canon/README.md`, `drafts/`, `assembled/`, `analysis/`, `style_selection_v1.md`, `episode_style_constitution_v1.md`, `setting_brief_v1.md`, `long_range_summary_v1.md`, `prompt_packet_v1.md`, `prompt_v1.md`, `analysis/episode_scorecard_v1.md`, `analysis/revision_delta_v1.md`를 함께 만든다.
