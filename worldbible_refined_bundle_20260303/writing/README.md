# writing/

집필 파이프라인 산출물 저장소.

## 폴더 구조

```
writing/
├── README.md                          ← 이 파일
├── style/
│   ├── style_constitution.md          ← 문체 헌법 (에피소드 횡단, 누적)
│   └── excerpts/                      ← 레퍼런스 발췌본
├── episodes/
│   ├── ep000_prologue/
│   │   ├── prompt_v1.md               ← 집필 프롬프트 (markdown)
│   │   ├── 프롤로그 초안.docx          ← 모델 초안 (Word)
│   │   ├── 프롤로그 수정본.docx        ← 작가 수정본 (Word)
│   │   ├── diff_v1.md                 ← 초안↔수정본 비교 분석
│   │   └── prompt_v2.md               ← 재집필 프롬프트 (필요시)
│   ├── ep001/
│   │   ├── prompt_v1.md
│   │   ├── 1화 초안.docx
│   │   ├── 1화 수정본.docx
│   │   ├── diff_v1.md
│   │   └── ...
│   └── ...
```

## 워크플로우

```
1. 기획 대화 (오케스트레이터)
   ↓
2. prompt_vN.md 작성 (markdown)
   ↓
3. 집필 모델에 프롬프트 전달 → 초안.docx 저장 (Word)
   ↓
4. 작가 직접 수정 → 수정본.docx 저장 (Word)
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
| 초안 | Word (.docx) | `프롤로그 초안.docx`, `1화 초안.docx` |
| 수정본 | Word (.docx) | `프롤로그 수정본.docx`, `1화 수정본.docx` |
| 비교 분석 | markdown (.md) | `diff_v1.md` |

## 네이밍 규칙

- **폴더**: `ep000` (프롤로그), `ep001` (1화), `ep002` (2화), ...
- **프롬프트/diff**: `_v1`, `_v2`, ... (재집필 반복 시 버전 관리)
- **초안/수정본**: 한국어 제목 (작가가 자유롭게 명명, 예: `프롤로그 초안.docx`, `1화 초안.docx`)
