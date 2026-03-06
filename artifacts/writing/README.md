# writing/

집필 파이프라인 산출물 저장소.

현재 스냅샷 기준 문서이며, 아래 트리는 2026-03-06 시점 실제 파일 구조를 반영한다.

## 폴더 구조

```text
writing/
├── README.md                          ← 이 파일
├── style/
│   └── style_constitution.md          ← 문체 헌법 (에피소드 횡단, 누적)
├── episodes/
│   ├── ep000_prologue/
│   │   ├── prompt_v1.md               ← 집필 프롬프트 (markdown)
│   │   ├── draft_v1.txt               ← 텍스트 초안
│   │   ├── revision_v1.txt            ← 텍스트 리비전
│   │   ├── diff_v1.md                 ← 초안↔수정본 비교 분석
│   │   ├── 프롤로그 초안.docx          ← Word 초안
│   │   └── 프롤로그 리비전.docx        ← Word 리비전
│   ├── ep001/
│   │   ├── prompt_v1.md
│   │   ├── prompt_v2.md
│   │   └── draft_v2.txt
│   └── ...
```

## 워크플로우

```text
1. 기획 대화 (오케스트레이터)
   ↓
2. prompt_vN.md 작성 (markdown)
   ↓
3. 집필 모델에 프롬프트 전달 → 초안 저장 (`draft_vN.txt` 또는 `.docx`)
   ↓
4. 작가 직접 수정 → 수정본 저장 (`revision_vN.txt` 또는 리비전 `.docx`)
   ↓
5. 초안↔수정본 비교 분석 → diff_vN.md 저장
   ↓
6. diff 누적 → style/style_constitution.md 갱신
   ↓
7. 다음 에피소드 prompt에 문체 헌법 반영
```

## 파일 종류별 형식

| 파일 | 형식 | 네이밍 예시 |
|---|---|---|
| 프롬프트 | markdown (.md) | `prompt_v1.md`, `prompt_v2.md` |
| 초안 | text / Word | `draft_v1.txt`, `프롤로그 초안.docx` |
| 수정본 | text / Word | `revision_v1.txt`, `프롤로그 리비전.docx` |
| 비교 분석 | markdown (.md) | `diff_v1.md` |

## 네이밍 규칙

- **폴더**: `ep000` (프롤로그), `ep001` (1화), `ep002` (2화), ...
- **프롬프트/diff**: `_v1`, `_v2`, ... (재집필 반복 시 버전 관리)
- **텍스트 초안/리비전**: `draft_vN.txt`, `revision_vN.txt`
- **Word 초안/수정본**: 한국어 제목 자유 명명 (예: `프롤로그 초안.docx`, `프롤로그 리비전.docx`)
