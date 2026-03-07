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
    ├── prompt_vN.md
    ├── draft_vN.txt
    ├── revision_vN.txt        (중간 작업본, 선택)
    ├── diff_vN.md
    └── ...
```

## 규칙

- 모든 에피소드 폴더는 생성 시점부터 `canon/` 하위 폴더를 포함한다.
- `canon/`에는 현재 또는 과거에 정식 반영된 canonical snapshot만 둔다.
- `canon/README.md`는 `current_text_canon`, `current_word_canon`을 명시하는 지시 파일이다.
- canon은 수정 가능하다. 새 리비전이 채택되면 `canon/` 안에 새 canon 파일을 추가하고 `canon/README.md` current 항목을 갱신한다.
- 초안, 중간 수정본, diff는 에피소드 루트에 둬서 canon과 작업 흔적을 분리한다.
- canon 파일명은 `revision_vN.*`처럼 기계식 버전명을 써도 되고, `프롤로그_리라이트_v2.md`처럼 제목형 파일명을 써도 된다. 현재 canon 여부는 파일명 패턴이 아니라 `canon/README.md`가 결정한다.

## 생성 커맨드

```bash
bash scripts/writing/new_episode_scaffold.sh ep002
```
