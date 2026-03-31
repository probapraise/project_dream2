# ep006_multisurface_edit_pilot

- status: `cycle_01_user_review_ready`
- base_episode: `artifacts/writing/episodes/ep006`
- created: `2026-03-31`
- current_cycle: `cycle_01`

## Role

- 이 폴더는 `ep006`를 대상으로 `6면 편집 라우팅 -> 선택 세션 패치 -> 단일 통합 리라이트` 구조를 실제 운용해 보는 격리 실험이다.
- 목적은 새 편집 체계를 정식 스캐폴드에 승격하기 전에, 한 회차를 끝까지 써 보며 문체 평탄화와 문서 증식 리스크를 직접 확인하는 데 있다.
- 메인 `episodes/ep006` 폴더는 공식 입력 저장소로만 쓰고, 실험 중간 산출물은 모두 여기서 관리한다.

## Adapted rule

- 연구안의 `6면`은 고정 6세션이 아니라 `라우터 평가 축`으로 쓴다.
- 실제 실행 세션은 `raw draft -> router -> 필요한 review만 선택 -> approved changes -> single integration -> QA`만 연다.
- 전체 원고 리라이트는 `integration` 단계에서 한 번만 한다.

## Folder map

- `context/`
  - 이번 파일럿 공통 앵커, 입력 맵, 세션 헤더, raw draft 브리프.
- `cycle_01/raw/`
  - 이번 파일럿의 1차 raw draft.
- `cycle_01/review/`
  - 라우터와 선택 review 세션 산출물.
- `cycle_01/integration/`
  - 승인된 변경 목록과 단일 통합 리라이트용 문서.

## Current entrypoint

1. 입력 우선순위와 주의사항은 [source_map_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/context/source_map_v1.md).
2. 작품/회차 앵커는 [anchor_card_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/context/anchor_card_v1.md).
3. raw draft 작성 지시서는 [draft_brief_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/context/draft_brief_v1.md).
4. 현재 1차 원고는 [raw_draft_v1.txt](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/cycle_01/raw/raw_draft_v1.txt).
5. 라우팅 결과는 [router_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/cycle_01/review/router_v1.md).
6. 선택 review 결과는 [structure_review_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/cycle_01/review/structure_review_v1.md), [emotion_dialogue_review_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/cycle_01/review/emotion_dialogue_review_v1.md), [serialization_review_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/cycle_01/review/serialization_review_v1.md).
7. 통합 반영 SSOT는 [approved_changes_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/cycle_01/integration/approved_changes_v1.md).
8. 현재 사용자 리뷰 대상 원고는 [post_review_draft_v1.txt](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/cycle_01/draft/post_review_draft_v1.txt).
9. 최종 회귀 점검은 [final_qa_v1.md](/home/dlwhdgus/project_dream2/artifacts/writing/experiments/ep006_multisurface_edit_pilot/cycle_01/review/final_qa_v1.md).

## Separation rule

- 파일럿이 끝나기 전까지 메인 `episodes/ep006`의 `drafts/`, `analysis/`, `canon/`은 정식 채널로 취급하지 않는다.
- 파일럿에서 채택할 가치가 확인된 산출물만 나중에 메인 파이프라인으로 승격한다.
