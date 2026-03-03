# Phase 2 Report (Collision Scan)

- change_id: CR-20260304-005
- verdict: minor

## 1. 탐색 범위
- files:
  - world_bible/WB-0002_loreops_canon_control.md
  - docs/character_index_v2.md
  - docs/simulation_playbook.md
  - docs/community_map.md
  - docs/master_map.md
  - world_ops/templates/phase2_report.md
  - world_ops/templates/phase3_apply.md

## 2. 충돌 후보
- [ ] 없음
- details:
  - 고정 보드/존/개수 강제 규칙이 잔존하지 않도록 점검
  - 정적 대량 인덱스 재도입 금지

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| scene consistency 규칙 부재 | WB-0002, 집필 검수 루프 | 동적 체크 템플릿 추가 | visibility, evidence_grade, valid_to | resolved |
| 템플릿에 구조화 로그 부재 | world_ops phase2/3 템플릿 | 필수 표 패턴 추가 | collision log, apply log | resolved |
| 동적 운영 가이드 단일 참조점 부재 | docs 탐색 흐름 | docs/dynamic_guide.md 신설 | SSOT/execution view, optional modules | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - 누락으로 판단된 항목은 모두 문서 추가/보강으로 반영.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 기존 quarantine 문서는 참조 링크만 유지하고 본문 복제는 최소화.

## 5. 판단 근거
- 멀티 에이전트 완료 보고 3건 교집합
- quarantine 근거 문서(`WB-0023`, `WB-0027`, `docs/character_index_v2`, `docs/simulation_playbook`, `docs/community_map`)

## 6. 분기 결정
- branch: minor
- reason: 신규 아키텍처 변경 없이 활성 문서와 템플릿 보강으로 해결 가능.

## 7. 작가 승인
- approved: yes
- note: 진행 승인
