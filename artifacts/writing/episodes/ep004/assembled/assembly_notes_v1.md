# assembly_notes_v1

- episode_id: `ep004`
- target_revision: `assembled/revision_assembled_v1.txt`
- packet_source: `prompt_packet_v1.md`
- final_instruction_doc: `prompt_v1.md`
- reconstruction_note: 이번 회차는 최초 canonization이 `draft_codex_v1.txt -> assembled/revision_assembled_v1.txt -> canon` 순서가 아니라, `draft_codex_v1.txt`를 바탕으로 사용자가 `canon/4화_리라이트_v1.md`를 직접 리라이트한 케이스다. 아래 노트는 현재 canon과 `revision_delta_v1.md`를 기준으로 retrospective backfill한 조립 메모다.

## Draft inputs
- `drafts/draft_codex_v1.txt`
- `canon/4화_리라이트_v1.md` (user working tree canonization source, retrospective reconstruction)

## Beat salvage map

| beat | keep? | source | note |
|---|---|---|---|
| 댓글 결핍 명명 오프닝 | refine | `drafts/draft_codex_v1.txt` | 초안의 제목과 도입 설명은 덜고, `빠진 건 하나였다`에서 바로 들어가는 현재 canon의 리듬을 채택한다. |
| 리리아의 물리적 발상과 생활어 반응 | refine | `canon/4화_리라이트_v1.md` | 리리아를 추임새 청자가 아니라 손 먼저 가는 공동 창작자로 세우는 쪽으로 조정됐다. |
| 종이 시뮬레이션과 권한형 편집 붕괴 | keep | `drafts/draft_codex_v1.txt` | `세탁방 vs 부엌`, `집사 한 명의 판단 용량`, `쓸데없는 말의 체류 효과`라는 구조 골격은 초안 쪽이 유지됐다. |
| 2년 압축 보상 패키지 | keep | `drafts/draft_codex_v1.txt` | 숫자 보고 -> `잘했다.` -> 독서 자유 -> 하인 태도 변화의 기능 배치는 그대로 살렸다. |
| 계승조회식 출발과 화말 질문 | refine | `canon/4화_리라이트_v1.md` | 막연한 기대감 대신 `내일도 내가 렌바렌일까?`라는 직접 질문으로 훅을 더 구체화했다. |

## Strong lines to preserve
- `쓰라고 해.`
- `그거 엄청 재밌겠다.`
- `잘했다.`
- `과연 내가 내일도 렌바렌일까?`

## Elements to discard
- 초안 제목 `한 줄`
- 댓글 구조 설명이 추상 시스템 해설로 길어지는 문장
- 리리아를 `질문 받아주는 아이`에 가깝게 만드는 추임새 반응
- 익명성 자체를 감정 클라이맥스로 과하게 밀어 올리는 버전

## Author-added patches
- 오프닝에서 지면 한계 설명을 눌러, 결핍 명명과 리리아의 즉시 반응이 더 빨리 만나게 했다.
- 리리아의 대사를 생활어와 손동작 중심으로 다시 눌러, `논리 설득`보다 `같이 만들고 싶다`는 감정이 먼저 오게 정렬했다.
- 2년 압축 보상 파트는 초안 구조를 유지하되, 사용자 리라이트 기준으로 어휘를 더 생활어화하고 마찰을 줄였다.
- 화말은 `계승조회식이 열린다`는 예고보다 `내일도 내가 렌바렌일까?`라는 직접 질문으로 잠가 ep005의 판정선을 바로 누르게 만들었다.

## Open risks before canon
- 댓글 구조 설명이 다시 길어지면 Beat 2가 설명문처럼 굳어질 위험
- 보상 파트가 너무 만족스럽게 끝나면 계승조회식 전환의 압박이 약해질 위험
- 리리아 톤을 너무 올리면 7세 감각 대신 작위적 통찰처럼 보일 위험
