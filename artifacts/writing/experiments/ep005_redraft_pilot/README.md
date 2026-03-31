# ep005_redraft_pilot

- status: `pilot`
- base_episode: `artifacts/writing/episodes/ep005`
- current_cycle: `cycle_02`
- created: `2026-03-30`

## Role

- 이 폴더는 `ep005`를 대상으로 `내부 다단계 초고 정제 + 사용자 분기` 구조를 시범 운용하는 격리된 파일럿이다.
- 여기서 사용자가 읽는 산출물도 끝까지 `초고`다.
- 차이는 `사용자 초고`를 바로 1회 생성물로 내보내지 않고, 내부적으로 한 번 더 논리/담화 검수를 거친 뒤 전달한다는 점이다.

## Core loop

1. `raw draft`를 내부 생성한다.
2. `logic review`에서 가짜 대비, 인과 비약, 반복 서술, 작위적 대사, POV 과잉 해석을 잡는다.
3. `rewrite brief`로 문제를 압축한다.
4. `post-review draft`를 다시 쓴다.
5. 사용자는 이 `post-review draft`를 읽고 다음 둘 중 하나를 고른다.
   - 손볼 곳이 적다: `quick_edit`
   - 구조적으로 마음에 안 드는 축이 남아 있다: `rewrite_meeting`
6. `rewrite_meeting`이 열리면 다음 사이클도 다시 `raw -> review -> rewrite -> user` 순서를 돈다.

## Folder map

- `context/`
  - 공통 입력 맵, 이번 실험용 초고 브리프, 내부 논리 리뷰 기준.
- `cycle_02/internal/raw/`
  - 사용자에게 바로 내보내지 않는 1차 초고.
- `cycle_02/internal/review/`
  - raw draft에 대한 내부 논리/담화 검수 결과.
- `cycle_02/internal/rewrite/`
  - logic review를 실제 재작성 지시로 압축한 문서.
- `cycle_02/draft/`
  - 내부 검수 후 사용자에게 보여 줄 기준 초고.
- `cycle_02/quick_edit/`
  - 이 정도면 직접 다듬으면 된다고 판단했을 때 바로 수정하는 경로.
- `cycle_02/rewrite_meeting/`
  - 손볼 축이 많아 재집필 회의를 먼저 열어야 할 때 쓰는 경로.
- `cycle_02/analysis/`
  - 이번 사이클 핸드오프 메모와 다음 분기 판단 메모.
- `archive/round1_contract_flow/`
  - 가장 처음 계약서 중심 실험 보존본.
- `archive/round2_quick_vs_rewrite_flow/`
  - `quick_edit / rewrite_meeting` 2갈래만 먼저 실험했던 이전 구조 보존본.

## Current entrypoint

1. 첫 내부 검수 흐름을 보고 싶으면 [`logic_review_v1.md`](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep005_redraft_pilot/cycle_02/internal/review/logic_review_v1.md) 와 [`rewrite_brief_v1.md`](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep005_redraft_pilot/cycle_02/internal/rewrite/rewrite_brief_v1.md) 를 본다.
2. 사용자 피드백을 반영한 두 번째 내부 검수 흐름은 [`logic_review_v2.md`](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep005_redraft_pilot/cycle_02/internal/review/logic_review_v2.md) 와 [`rewrite_brief_v2.md`](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep005_redraft_pilot/cycle_02/internal/rewrite/rewrite_brief_v2.md) 다.
3. 현재 읽을 초고는 [`post_review_draft_v2.txt`](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep005_redraft_pilot/cycle_02/draft/post_review_draft_v2.txt) 다.
4. 손볼 곳이 적으면 [`user_revision_v2.txt`](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep005_redraft_pilot/cycle_02/quick_edit/user_revision_v2.txt) 를 직접 수정한다.
5. 아직 구조 문제가 크면 [`rewrite_meeting_v1.md`](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep005_redraft_pilot/cycle_02/rewrite_meeting/rewrite_meeting_v1.md) 와 [`redraft_brief_v1.md`](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep005_redraft_pilot/cycle_02/rewrite_meeting/redraft_brief_v1.md) 를 기준으로 다음 라운드로 간다.

## Separation rule

- 메인 `episodes/ep005` 파일은 건드리지 않는다.
- 파일럿에서 검증된 흐름만 나중에 메인 파이프라인으로 승격한다.
