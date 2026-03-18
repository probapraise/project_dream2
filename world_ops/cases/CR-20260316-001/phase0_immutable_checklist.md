# Phase 0 Immutable Checklist

## 목적
- 절대 불가침 범위를 작업 전에 고정한다.
- 도감 정본 내부의 보호 블록과 서사 허브 no-touch 파일을 명시한다.
- 최종 검증 시 `무엇이 바뀌면 안 되는지`를 기계적으로 확인할 수 있게 한다.

## 보호 블록

| 가드레일 | 경로 | 보호 방식 | 검증 앵커 | 상태 |
|---|---|---|---|---|
| 잠금 원칙과 변경 금지 전제 | docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | exact block freeze | lines `9-49`, sha256 `e0635afb43d5cc11be44b97245f7c178051b9643c0472541a46198067c1abb6b` | pending |
| 색×형×잔류 프레임워크 | docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | exact block freeze | lines `65-168`, sha256 `5a2ccb9f83989a7220a80dde74aeb1167f5bb0e79744963aeb733862daa578a0` | pending |
| 42개 색별 표준 입문 6식 | docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | exact block freeze | lines `169-286`, sha256 `295c1efdd2e384ec74df6b7e798fc0bf299562958a71dae7f9de77cc8efe2bca` | pending |
| 하급/상급 커리큘럼 구조 | docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | exact block freeze | lines `287-424`, sha256 `eeab23d8ebaf99d78c9a9828e7b9677b84ebcc4bf943cb71b3c9ba1aacbd89d0` | pending |
| 보존각인학파 학파명/핵심 위상 | docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | selective freeze | anchors `### 6-15`, `학내 이미지`, `추가 주석`, `공용화되어 버린 옛 입문 등록식` | partial_unlock_20260317 |
| 문장비전 23가문 + 왕국 극비 3종 | docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | exact block freeze | lines `1226-1386`, sha256 `b8cbb3453b2a387c6c367d1d85c4c222af264257bdfa012cda997c414f7f2f73` | pending |
| 카운터/밸런스 문법 | docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | exact block freeze | lines `1387-1433`, sha256 `fc5f59350b3b6d20b4eb73b208901b7a414f3cfb6abffb17bb53476b8cac4891` | pending |
| 모든 `[색/형/잔류/태그]` 괄호 표기 | docs/design/source_texts/magic_system/프라미시오_마법도감_정본_3_1_표식탐지_전면재작성_20260313.md | all signature lines freeze | `333` lines, sha256 `7338977c672c3b89ec25f2f5e8785507730deaf57d0a2330c38d99150d49d01b` | pending |
| 주인공 성장선 허브 | world/live/docs/narrative_state.md | no-touch file | sha256 `7539947b5cf80aa64d2b9ec173324459a1028e130d44cc74511479f6a48c08d0` | pending |
| 주인공 장기 아크 허브 | world/live/docs/story_arcs.md | no-touch file | sha256 `d8bb5c5f50a907573370260685ec5d616a5304b60c90f3262dbc6c2d6d2b7cd2` | pending |
| pre-academy 체크포인트 플랜 | world/live/docs/pre_academy_checkpoint_plan.md | no-touch file | sha256 `a296d19548510f428859c72b3db96917b8274210eacf680263786e339210a8c4` | pending |

## 운영 규칙
- 보호 블록이 섞여 있는 파일에서는 `blind replace`를 금지한다.
- 보호 대상이 아닌 학파명/주문명만 선택적으로 교체한다.
- generated layer(`population_slots.csv`, `P-*.yaml`)는 SSOT 반영 이후 재생성으로만 갱신한다.
- alias 문서와 historical case는 `구명 보존 허용 영역`으로 분리한다.
- `보존각인학파`는 2026-03-17 작가 override로 `학파명/핵심 위상은 보호`, `전승 12식은 부분 재점검 가능` 상태로 전환한다.
- 따라서 이 축은 도감 정본 §6-15 전체를 통째로 동결하지 않고, `공용화 전제`, `아카이빙 정체성`, `몰락 서사`, `만상채록(현상 각인)/영상 각인술` 확장선만 고정한 채 주문별 점검을 진행한다.

## 검증 메모
- `§2-5`, `§2-6`, `§4-2`, `§4-4`는 각각 상위 보호 블록(`§2`, `§4`) 안에 포함된다.
- 최종 검증은 `보호 블록 해시`, `괄호 표기 해시`, `no-touch 파일 해시` 세 층으로 나눈다.
