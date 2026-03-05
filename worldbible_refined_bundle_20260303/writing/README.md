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
│   │   ├── prompt_v1.md               ← 집필 프롬프트
│   │   ├── draft_v1.md                ← 모델 초안
│   │   ├── revision_v1.md             ← 작가 수정본
│   │   ├── diff_v1.md                 ← 초안↔수정본 비교 분석
│   │   └── prompt_v2.md               ← 재집필 프롬프트 (필요시)
│   ├── ep001/
│   └── ...
```

## 워크플로우

```
1. 기획 대화 (오케스트레이터)
   ↓
2. prompt_vN.md 작성
   ↓
3. 집필 모델에 프롬프트 전달 → draft_vN.md 저장
   ↓
4. 작가 직접 수정 → revision_vN.md 저장
   ↓
5. 초안↔수정본 비교 분석 → diff_vN.md 저장
   ↓
6. diff 누적 → style/style_constitution.md 갱신
   ↓
7. 다음 에피소드 prompt에 문체 헌법 반영
```

## 네이밍 규칙

- 에피소드: `ep000` (프롤로그), `ep001`, `ep002`, ...
- 버전: `_v1`, `_v2`, ... (같은 에피소드 내 재집필 반복 시)
- 파일 종류: `prompt`, `draft`, `revision`, `diff`
