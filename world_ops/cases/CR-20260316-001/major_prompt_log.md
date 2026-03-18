# Major Rewrite Prompt Log

- change_id: CR-20260316-001
- branch: major
- external_model: codex
- submitted_at: 2026-03-16

## 1. 대상 문서
- world_ops/cases/CR-20260316-001/phase1_reader_exposure_framework.md
- world_ops/cases/CR-20260316-001/phase1_color_emotion_registry.md
- world_ops/cases/CR-20260316-001/phase1_red_tower_architecture.md
- world_ops/cases/CR-20260316-001/phase1_blue_tower_architecture.md
- world_ops/cases/CR-20260316-001/phase1_green_tower_architecture.md
- world_ops/cases/CR-20260316-001/phase1_yellow_tower_architecture.md
- world_ops/cases/CR-20260316-001/phase1_purple_tower_architecture.md
- world_ops/cases/CR-20260316-001/phase1_white_tower_architecture.md
- world_ops/cases/CR-20260316-001/phase1_black_tower_architecture.md
- world_ops/cases/CR-20260316-001/phase0_major_rename_map.md
- world_ops/cases/CR-20260316-001/phase0_spell_rename_map.md

## 2. 합의된 프롬프트
- 기존 `7색 × 6형 × 3잔류`, `21학파`, `42개 색별 표준 입문 6식`, `문장비전`, `보존각인학파`, 하급/상급 커리큘럼, 주인공 성장선은 보존한다.
- 이번 단계의 목표는 `메커닉 개편`이 아니라 `독법 개편`이다. 즉 학파명/주문명/색별 정서/슬롯 노출 문법을 상업적으로 다시 설계한다.
- `7색`은 독자 온보딩용 상위 카테고리, `21학파`는 중층 전문화로 유지한다.
- 각 학파 `12전승`은 `기본탄 / 제어 / 방어·이동 / 시그니처 / 궁극기 / 비전투 유틸` 슬롯으로도 읽히게 재태깅한다.
- 네이밍은 `전통 한자어의 격`을 유지하되, `첫 인상은 장면과 감각`이 책임지게 만든다.
- 교차색 콤보는 전체 조합표를 만들지 않고, 기억 가능한 소수의 시그니처 조합만 canonize한다.
- 이번 단계에서는 live SSOT와 generated layer를 직접 치환하지 않고, case 내부 기준 문서와 리네임 초안을 먼저 닫는다.

## 3. 보존 조건 (절대 바꾸면 안 되는 항목)
- `phase0_immutable_checklist.md`에 적힌 불가침 라인 범위와 bracket 표기
- `보존각인학파`의 이름, 전승, 위상
- `문장비전` 블록
- `7색 × 6형 × 3잔류` 기본 프레임
- `42개 색별 표준 입문 6식`
- 하급/상급 커리큘럼 구조
- 주인공 성장선과 narrative read-only 문서

## 4. 변경 조건 (이번에 바꿔야 하는 항목)
- 색별 감정/문화 레지스터를 독자 노출 문법으로 고정
- 학파 리네임 대상 11개와 보류 5개를 축/정서 기준으로 다시 평가
- `독자용 슬롯 문법`, `제한된 교차색 콤보`, `마법/학파용 작명 가드레일`을 중앙 문서로 명문화
- 탑별 architecture 문서를 기준으로 rename-ready / baseline-fixed / redesign-slot 상태를 구분
- `phase0_spell_rename_map.md`에 들어갈 주문 리네임 채우기 기준을 고정

## 5. 수령 산출물
- `phase1_reader_exposure_framework.md`
- 탑별 architecture baseline
- 후속 주문 리네임 작성용 기준 로그
