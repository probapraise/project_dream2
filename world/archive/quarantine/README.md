# Quarantine

이 디렉터리는 **데이터 보존용 격리 구역**이다.

## 목적
- SSOT(`docs/history/대화 로그.txt`, `docs/design/spec_sheet_v1.md`)와 충돌 가능성이 높은 레거시 규약/설정을
  즉시 삭제하지 않고 보존한다.
- 활성 문서에서 분리해 오작동을 막고, 필요 시 부분 재사용한다.

## 포함 기준
- 고정 4권역/18보드 강제
- nodes/edges/events/rules/glossary 강제 구조화
- RAG/world_pack 전제 강제
- hard/required 형태의 경직 규칙

## 복원/재사용 원칙
- 파일 통복원 금지
- 필요한 문단만 발췌해 새로운 활성 문서에 반영
- 반영 시 반드시 변경 건(`CR-*`)으로 근거 기록
