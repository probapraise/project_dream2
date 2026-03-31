# assembly_notes_v1

- episode_id: `ep005`
- upstream_raw_draft: `drafts/raw_codex_v1.txt`
- base_draft: `drafts/draft_codex_v1.txt`
- working_revision: `assembled/revision_assembled_v1.txt`
- target_canon: `canon/5화_리라이트_v1.md`
- edit_mode: `user_rewrite_plus_selective_ai_polish`
- packet_source: `prompt_packet_v1.md`
- final_instruction_doc: `prompt_v1.md`

## Role
- 이 문서는 `ep005`에서 내부 검수 후 초고가 실험 폴더의 `quick_edit` 사용자 수정본을 거치며 어떻게 정리됐는지 기록하는 작업 로그다.
- 현재 canon은 `ep005_redraft_pilot/cycle_02/quick_edit/user_revision_v2.txt`를 정식 폴더로 승격한 결과다.

## Edit pass map

| pass | actor | source span | purpose | note |
|---|---|---|---|---|
| 1 | codex | `drafts/raw_codex_v1.txt` | `왕도 도착 -> 계승조회식 -> 라베르니온 별채 연회 -> 세렌 첫 접속` 기본 골격 초안화 | 정식 폴더의 raw는 실험 `raw_draft_v2`를 승격했다. |
| 2 | internal review + rewrite | `analysis/logic_review_v1.md` -> `analysis/logic_patch_brief_v1.md` | 연회장 브리지, 1층/2층 대비, 세렌 전 단계 관찰, 대사 생활어를 보강 | 결과가 현재 `drafts/draft_codex_v1.txt`다. |
| 3 | user quick edit | `drafts/draft_codex_v1.txt` -> `assembled/revision_assembled_v1.txt` | 설명층을 줄이고, 세렌 훅을 `아버지 칭찬 욕망 + 게시판 요청`으로 더 직접 잠근다 | 이 버전이 현재 canon으로 승격됐다. |

## Draft strengths kept
- `왕도 도착 -> 검사 대기 -> 미계승 결과 -> 연회 -> 세렌 첫 접속`의 큰 비트 연결
- 검사 구간의 단문 절단과 관찰자 모드
- 세렌의 첫 등장을 `권위`보다 `고립`으로 먼저 읽게 하는 방향
- 리리아가 관계와 사건을 동시에 여는 돌격형 실행 엔진이라는 점

## Repeated cuts
- 오프닝의 메타 독백 (`과연 내가 내일도 렌바렌일까`)을 걷어내고 왕도 도착 장면으로 바로 들어간다.
- 연회장의 `1층/2층 기능 설명`, `사회 구조 분석`, `익명 구조 규칙 설명` 같은 설명층을 최종본에서 더 짧게 줄인다.
- 세렌 훅을 구조 호기심 단독 축보다 더 직접적인 인간 욕망으로 정리한다.

## Repeated concretizations
- `아버지가 신세지고 있는 어르신`을 `세르반 라베르니온 / 공작 / 문경청 수장`으로 구체화했다.
- 세렌 첫 접속에서 `드레스`, `주변 시선`, `친구 없음`, `아버지에게 칭찬받고 싶다`를 붙여 인물 결핍을 더 직접적으로 드러냈다.
- 게시판을 추상 구조가 아니라 `칼리온에게 칭찬받게 만든 도구`로 재정의해 화말 동기를 구체화했다.

## Tone corrections
- 사회 구조 해석을 길게 끌기보다, 키리온의 짧은 관찰과 리리아/세렌 대화로 장면을 더 직접적으로 굴렸다.
- 격식 장면에서도 아이들 말투가 실제로 맞부딪히는 느낌을 살리도록 생활어 반응을 늘렸다.

## Character protection edits
- 세렌을 `위압적인 공작가 영애`보다 `중앙에 고립돼 있고 칭찬을 갈망하는 아이`로 보정했다.
- 키리온이 세렌에게 너무 빨리 감정적으로 기울지 않게, 관찰과 제동의 역할을 유지했다.
- 리리아는 단순 귀여운 막내가 아니라, 타인의 결핍에 바로 뛰어드는 실행 엔진으로 더 선명해졌다.

## Hook and end-beat corrections
- 초고의 `익명 구조 자체가 재밌다` 쪽 훅을, 최종본에서는 `세렌이 아버지 칭찬을 받고 싶어서 게시판을 원한다`는 더 직접적인 욕망 훅으로 교체했다.

## Selective AI patch log
- 사용자 지시: 연회장 브리지, 층별 기능 대비, 세렌 전 단계 관찰, 대사 생활어화를 보강
- 반영 위치: 현재 `drafts/draft_codex_v1.txt`로 승격된 실험 `post_review_draft_v2`

## Open risks after canon
- `왜 키리온만 별도 검사 라인이었는가`는 의도적으로 미해결이라, 다음 화에서 무의미하게 방치되지 않게 low-burn 관리가 필요하다.
- 세렌의 `아버지 칭찬 욕망`이 다음 화에서 바로 실무 사건과 연결되지 않으면 훅의 동력이 약해질 수 있다.
