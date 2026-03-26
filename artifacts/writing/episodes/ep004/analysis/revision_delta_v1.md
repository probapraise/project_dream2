# revision_delta_v1

- episode_id: `ep004`
- previous_canon_before_latest_patch: `none`
- previous_canon_before_latest_patch_sha256: `none`
- latest_user_patch_source: `working tree edits on canon/4화_리라이트_v1.md`
- latest_user_patch_source_sha256: `4b3b443b7e80f44e51636775e8322dbf82d028cdba23febecf38f58b53182a3e`
- current_canon: `canon/4화_리라이트_v1.md`
- current_canon_sha256: `4b3b443b7e80f44e51636775e8322dbf82d028cdba23febecf38f58b53182a3e`
- note: 이번 정본 반영은 `draft_codex_v1.txt`를 바탕으로 사용자가 canon 파일 위에서 직접 리라이트하고, 대화 중 리리아 대사와 화말 훅을 반복 미세조정한 첫 canonization이다.

## Canonization outcome
- 사용자 수정본을 현재 정본으로 채택했다.
- 파일명은 참조 안정성을 위해 `canon/4화_리라이트_v1.md`로 고정했다.
- 이번 반영 이후 downstream sync 기준은 위 `current_canon_sha256`를 따른다.

## Compared drafts
- `drafts/draft_codex_v1.txt`
- `working tree edits on canon/4화_리라이트_v1.md`

## Per-source salvage

| source | retained beats/phrases | weakened/removed | note |
|---|---|---|---|
| codex | Beat 1의 `댓글` 결핍 명명, Beat 2의 종이 시뮬레이션 구조, Beat 3의 보상 패키지, Beat 4의 `렌바렌` 질문 훅 | 리리아의 일부 추임새형 반응, 과도하게 추상적인 설명 문장, 초안형 타이틀 `한 줄` | 구조 골격과 핵심 기능은 유지하되, 문장 결은 사용자 리라이트 쪽으로 더 생활어화됐다. |
| user_working_tree | 리리아의 물리적 발상과 생활어 반응, `쓰라고 해`, `그거 엄청 재밌겠다.`, 화말의 직접 질문 | 익명 자체를 감정 클라이맥스로 밀어 올리는 버전 | 캐릭터성 조정과 장면 온도 조정은 대부분 이 층위에서 확정됐다. |

## Author synthesis deltas
- 수정본이 여러 초고를 어떻게 조립했는지 기록한다.
- "초고 하나를 다듬었다"가 아니라 "어떤 재료를 어떤 이유로 합성했는가"가 드러나야 한다.

- 초안의 Beat 배치와 기능 설계는 그대로 유지했다. `댓글 필요성 쇼케이스 -> 2년 압축 보상 -> 계승조회식 출발`의 골격은 변경하지 않았다.
- 대신 장면 어휘는 사용자 리라이트 기준으로 눌렀다. 리리아가 키리온 설명을 받아 적는 추임새형 청자로 내려가지 않게, 손 먼저 가고 생활어로 딴지를 거는 7세 톤을 더 강하게 살렸다.
- 익명성은 장면의 핵심 설계 원리로 남기되, 리리아 감정의 정착점은 `나도 적을 수 있다`보다 `그거 엄청 재밌겠다` 쪽으로 낮춰 자연스럽게 정리했다.
- 화말은 막연한 기대감 대신 `내일도 내가 렌바렌일까?`라는 직접 질문으로 고정해, ep005의 계승조회식을 누르게 만드는 훅으로 정리했다.

## Style learning candidates
- 이번 비교에서 `style_pattern_library.md`로 승격할 가치가 있는 패턴
- 특정 초고 모델이 강했던 장점과 약점

- `아이 캐릭터의 반응은 추상 질문보다 생활 감각의 딴지로 살아난다`는 점을 재확인했다. 리리아 같은 인물은 `왜?`보다 `그럼 맨날 싸우겠다`, `이게 뭐야?` 같은 구체 반응이 훨씬 강하다.
- `커뮤니티 구조 설명`은 논리만 맞는다고 사는 게 아니라, 상대 캐릭터의 손동작과 표정 반응으로 중간중간 끊어 줘야 설명문이 되지 않는다.
- 화말 훅은 `긴장감을 느꼈다`보다 `그래서 내일 뭐가 달라질 수 있지?`라는 구체 질문으로 닫을 때 더 선명하다.
