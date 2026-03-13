# episodes/

에피소드별 집필 산출물 저장 구역.

## 표준 구조

```text
episodes/
└── <episode_id>/
    ├── canon/
    │   ├── README.md
    │   ├── revision_vN.txt
    │   └── revision_vN.docx   (선택)
    ├── drafts/
    │   ├── draft_codex_vN.txt
    │   ├── draft_external_a_vN.txt
    │   └── draft_external_b_vN.txt
    ├── assembled/
    │   ├── assembly_notes_vN.md
    │   └── revision_assembled_vN.txt
    ├── analysis/
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
- `canon/`에는 현재 또는 과거에 정식 반영된 canonical snapshot만 둔다.
- `canon/README.md`는 `current_text_canon`, `current_text_canon_sha256`, `current_word_canon`을 명시하는 지시 파일이다.
- canon은 수정 가능하다. 새 리비전이나 사후 패치가 채택되면 `canon/` 안에 새 canon 파일을 추가하고 `canon/README.md` current 항목을 갱신한다.
- 병렬 초고는 `drafts/`, 조립 메모/수정본은 `assembled/`, 멀티 초고 비교 분석은 `analysis/`에 둔다.
- `style_selection_vN.md`는 내부 선택 문서다. 실제 모델에는 `episode_style_constitution_vN.md`를 넣는다.
- `setting_brief_vN.md`는 이번 화에 실제로 필요한 설정만 담는다.
- `long_range_summary_vN.md`는 최근 3회차 raw canon보다 이전 맥락만 담는다.
- `prompt_packet_vN.md`는 주입 순서와 우선순위를 명시하는 패킷 문서다.
- `prompt_vN.md`는 이번 화 비트와 목표만 담당하는 마지막 지시서다.
- `prompt_packet_vN.md`의 `recent_canon_*_path/sha256`는 현재 canon window와 맞아야 한다.
- 새 프롬프트 초안은 `artifacts/writing/prompt_packet_template.md`와 `artifacts/writing/prompt_template.md`를 기준으로 작성하고, 과거 단일 `prompt_vN.md`는 히스토리로 취급한다.
- canon 확정 뒤에는 `bash scripts/writing/post_canon_sync.sh <episode_id>`로 live sync 대상과 drift 상태를 바로 확인한다.
- 다음 회차가 이미 준비돼 있으면 `python3 scripts/writing/audit_prompt_packet.py <next_episode_id>`로 패킷 stale 여부도 확인한다.
- 캐논 사후 수정은 가능하면 기존 current 파일을 덮어쓰기보다 `bash scripts/writing/new_canon_patch.sh <episode_id> <new_canon_filename>`로 새 snapshot을 만든 뒤 진행한다.
- canon 파일명은 `revision_vN.*`처럼 기계식 버전명을 써도 되고, `프롤로그_리라이트_v2.md`처럼 제목형 파일명을 써도 된다. 현재 canon 여부는 파일명 패턴이 아니라 `canon/README.md`가 결정한다.

## 생성 커맨드

```bash
bash scripts/writing/new_episode_scaffold.sh ep002
```

- 스캐폴드는 `canon/README.md`, `drafts/`, `assembled/`, `analysis/`, `style_selection_v1.md`, `episode_style_constitution_v1.md`, `setting_brief_v1.md`, `long_range_summary_v1.md`, `prompt_packet_v1.md`, `prompt_v1.md`를 함께 만든다.
