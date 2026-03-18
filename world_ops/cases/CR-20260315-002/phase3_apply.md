# Phase 3 Apply

- change_id: CR-20260315-002
- branch: minor

## 1. 실제 수정 파일
- `world/live/world_bible/WB-0003_onepage_summary.md`
- `world/live/world_bible/WB-0005_magic_system.md`
- `world/live/world_bible/WB-0006_irminsul_infra.md`
- `world/live/world_bible/WB-0007_badge_network.md`
- `world/live/world_bible/WB-0008_archive_plaza_overview.md`
- `world/live/world_bible/WB-0012_core_conflict_arcs.md`
- `world/live/world_bible/WB-0017_economy_resources.md`
- `world/live/world_bible/WB-0019_platform_spec.md`
- `world/live/world_bible/WB-0029_appendix_aptitude_signature_materials.md`
- `world/live/population/core_cast/NC-0001_P-1027.md`
- `world/live/docs/story_arcs.md`
- `world/live/docs/memory_tiers/long_term.md`
- `world/live/docs/master_map.md`
- `docs/handoff/next_steps.md`
- `world_ops/world_change_log.md`

## 2. 변경 요약 (diff 요약 수준)
- live SSOT의 `하급 정령 계약` 표면 명칭을 `픽시 계약`으로 교체하고, `WB-0006/0007`에 `픽시 -> 요정 -> 드리아드 -> 성목 본체` 정령 위계를 반영했다.
- `WB-0008/0019`에 `색인 -> 주석 -> 실타래` 전반부 성장선, `비공식 운용 -> 감리 허가 -> 시범 운영 -> 드리아드 협약` 상태기계, `조회 전용 -> ... -> 영상 각인 플랫폼` 단계 해금, 공용 패킷/자동 서명 채널 계약을 live 본문으로 내렸다.
- `WB-0003/0012/0017/0029`, `NC-0001`, `story_arcs`, `long_term`, `next_steps`를 같은 기준으로 맞춰 academy pacing과 후행 패턴 학습 표면 규칙까지 정렬했다.

## 2-1. 반영 완료 로그 (필수 표)
| 적용한 해결안 | 반영 파일/섹션 | 관련 ID | 잔여 리스크/후속 작업 |
|---|---|---|---|
| `픽시 계약` 표면 명칭 교체 | `WB-0005`, `WB-0006`, `WB-0007`, `WB-0029` | nomenclature / spirit-ladder | 레거시 설계 문서에는 구 명칭이 역사 기록으로 남음 |
| 그리모어 3단계 + 성목 연계 사다리 반영 | `WB-0003`, `WB-0008`, `NC-0001`, `story_arcs`, `long_term` | growth_architecture_split / irminsul_contract_ladder | 실제 사건 배치는 후속 집필 설계 필요 |
| 운영 상태기계와 패킷 계약 반영 | `WB-0008`, `WB-0019` | runtime_governance_state_machine / runtime_interface_contract | S1->S2 승급 장면 설계는 후속 과제 |
| `관리/정화` 포함 단계 순서 정렬 | `WB-0008`, `WB-0012`, `WB-0019`, `story_arcs`, `long_term` | community_unlock_blueprint | 집필 단계에서 실제 사건 배열 보강 필요 |
| prompt-facing/handoff 동기화 | `NC-0001`, `next_steps`, `world_change_log`, `master_map` | sync follow-up | population/simulation 쪽 추가 사건 설계는 별도 이슈로 가능 |

## 3. 예상 외 영향
- [ ] 없음
- details:
  -

## 4. 미해결 항목
- [ ] 없음
- details:
  - live SSOT 반영 범위 안에서는 추가 미해결 없음. 이후 작업은 사건 설계/집필 단계 과제다.

## 5. 작가 승인
- approved: yes
- note:
  - live SSOT 적용 완료 기준으로 정리
