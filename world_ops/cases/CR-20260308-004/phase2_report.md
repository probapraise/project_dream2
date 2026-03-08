# Phase 2 Report (Collision Scan)

- change_id: CR-20260308-004
- verdict: minor

## 1. 탐색 범위
- files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/docs/master_map.md
  - world_ops/world_change_log.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 기존 `계승조회식`과 조기 사설 검증 금지 설정은 존재했지만, 왜 10세 이전의 마법 사용 자체가 위험한지와 왕국이 이를 어떻게 귀족 견제에 활용하는지는 비어 있었다.
  - 학술원 서열 편중도 이미 암시돼 있었으나, 왕가/공작가 선행학습 특권과 직접 연결되진 않았다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 아동 마법 금지 규정의 구체성이 없음 | WB-0005, WB-0009, WB-0026 | 이론 교육 허용 / 활성화 보조 금지 / 반역죄급 조사 구조를 명시 | 계승조회식, 마나핵, 마나 회로 | resolved |
| 왕실 귀족 견제 메커니즘이 약함 | WB-0009, WB-0026 | 영지 단위 특별조사와 독학 천재 사례도 조사 명분이 되는 구조 추가 | 특별조사, 귀족 견제 | resolved |
| 학술원 성적 편중의 이유가 비어 있음 | WB-0015 | 왕가/공작가/2시그니처 가문의 선행학습 특권과 초기 성적 독점 연결 | 선행학습, 상위권 독식 | resolved |
| 키리온 현재 시점 위험이 이론/실전으로 분리돼 있지 않음 | NC-0001, EX-0001 | 이론 학습 허용과 실제 시전 금지, 흔적 노출 리스크를 카드에 반영 | NC-0001, EX-0001 | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - 인덱스, master_map, change log까지 함께 갱신해 추적 경로 누락을 막는다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - timeline 문서까지 확장하지 않고, 관련성이 높은 규칙 문서에 우선 반영한다.

## 5. 판단 근거
- world_bible_index 참조:
  - world/live/docs/world_bible_index_v2.md
- cross-reference 참조:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0009_power_structure_factions.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/external/EX-0001.yaml
  - world/live/population/core_cast/NC-0001_P-1027.md

## 6. 분기 결정
- branch: minor
- reason: 세계관 중요도는 높지만 기존 제도와 권력 축을 보강하는 문서 수정 범위이며, 외부 재작성 경로가 필요하지 않다.

## 7. 작가 승인
- approved: yes
- note: 사용자가 규정, 예외, 성적 격차를 함께 명시적으로 제시했다.
