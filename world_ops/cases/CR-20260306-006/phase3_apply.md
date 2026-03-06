# Phase 3 Apply

- change_id: CR-20260306-006
- branch: minor

## 1. 실제 수정 파일
- artifacts/writing/README.md
- artifacts/writing/episodes/README.md
- artifacts/writing/episodes/ep000_prologue/canon/README.md
- artifacts/writing/episodes/ep000_prologue/canon/revision_v1.txt
- artifacts/writing/episodes/ep000_prologue/canon/revision_v1.docx
- artifacts/writing/episodes/ep001/canon/README.md
- artifacts/writing/episodes/ep001/canon/revision_v2.txt
- artifacts/writing/episodes/ep001/diff_v2.md
- scripts/README.md
- scripts/writing/new_episode_scaffold.sh
- world/live/docs/narrative_state.md
- world/live/docs/episode_deltas.md
- world/live/docs/voice_fingerprint_spec.md
- world/live/population/core_cast/NC-0001_P-1027.md
- world/live/docs/master_map.md
- docs/handoff/next_steps.md

## 2. 변경 요약 (diff 요약 수준)
- `ep000_prologue`, `ep001`의 current canon 파일을 각 episode의 `canon/` 하위로 이동하고 `canon/README.md`로 current canon을 명시했다.
- `artifacts/writing/README.md`, `artifacts/writing/episodes/README.md`에 새 episode 폴더 표준 구조와 mutable canon 운영 규칙을 추가했다.
- `scripts/writing/new_episode_scaffold.sh`를 추가해 새 episode 폴더 생성 시 `canon/`과 current canon 지시 파일이 자동 생성되도록 했다.
- live 서사 문서와 VFP 출처 경로를 새 canon 경로로 동기화했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| current canon 폴더 분리 | `artifacts/writing/episodes/ep000_prologue/canon/*`, `artifacts/writing/episodes/ep001/canon/*` | `canon/`, `current_text_canon` | 이후 새 canon 채택 시 `canon/README.md` 갱신 습관 필요 |
| episode 구조 문서화 | `artifacts/writing/README.md`, `artifacts/writing/episodes/README.md` | writing episode contract | 향후 Word 작업본 네이밍 세부 규칙은 필요 시 보강 |
| episode scaffold 추가 | `scripts/writing/new_episode_scaffold.sh`, `scripts/README.md` | episode scaffold | 실제 `ep002` 생성 시 한 번 사용 검증 권장 |
| 참조 경로 동기화 | `world/live/docs/narrative_state.md`, `episode_deltas.md`, `docs/handoff/next_steps.md`, `NC-0001` 카드 | `canon/revision_vN` | 과거 케이스/메모에 남은 문자열은 필요 시 추가 정리 |

## 3. 예상 외 영향
- [x] 없음
- details:
  -

## 4. 미해결 항목
- [ ] 실제 `ep002` 생성 시 스캐폴드 사용 검증은 아직 안 함
- details:
  - 스크립트는 추가했지만 새 episode에 실제 적용한 사례는 아직 없다.

## 5. 작가 승인
- approved: yes
- note: episode별 `canon/` 폴더와 current canon 명시 규칙 반영 완료.
