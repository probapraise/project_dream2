# Phase 2 Report (Collision Scan)

- change_id: CR-20260308-001
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 기존 렌바렌 설정은 `비밀 서명귀족 + 식흔 + 정보기관 수장`까지만 정의돼 있었고, 왜 정체가 유지되는지와 라베르니온 공작가와의 실질 권력관계는 비어 있었다.
  - 이번 변경은 기존 축을 뒤집는 retcon이 아니라, 비밀 유지 메커니즘과 권력 위계를 보강하는 성격이다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 렌바렌 비밀 유지 이유가 약함 | WB-0009, WB-0026 | `방계 청소` 규약을 명시해 혈통 비밀 유지의 구조적 이유를 보강 | 렌바렌, 식흔, 방계 청소 | resolved |
| 렌바렌 정보기관 수장 직함의 실권 위치가 모호함 | WB-0009, WB-0026, EX-0001 | 명예직/실권 분리를 명시하고 라베르니온 공작가를 실권자로 고정 | 라베르니온, 정보기관, 수면거울 | resolved |
| 캐릭터 카드가 새 가문 구조를 반영하지 않음 | EX-0001, NC-0001 | 칼리온/키리온 카드에 후계 구조와 생존 리스크를 반영 | EX-0001, NC-0001 | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - live 참조 인덱스와 master_map recent changes까지 함께 갱신해 검색 경로 누락을 막는다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 동일 설명을 narrative 허브까지 확장하지 않고, 세계관/캐릭터 카드 계층에만 반영해 중복 서술을 피한다.

## 5. 판단 근거
- world_bible_index 참조:
  - world/live/docs/world_bible_index_v2.md
- cross-reference 참조:
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md

## 6. 분기 결정
- branch: minor
- reason: 변경 범위는 세계관 핵심이지만, 실제 수정은 기존 렌바렌 축을 보강하는 국소 문서 갱신이며 외부 재작성 경로가 필요하지 않다.

## 7. 작가 승인
- approved: yes
- note: 사용자가 직접 설정을 확정적으로 제시했고, 별도 확인 질문 없이 반영 가능한 수준으로 명료하다.
