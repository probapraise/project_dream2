# SSOT Reflection Audit (2026-03-16)

대상 범위:
- `world_ops/cases/CR-20260315-001/`
- `world_ops/cases/CR-20260315-002/`
- `world_ops/cases/CR-20260316-001/`
- 현재 live SSOT: `world/live/`
- prompt-facing 보조 문서: `docs/handoff/next_steps.md`, `world_ops/world_change_log.md`

판정 기준:
- `반영 완료`: 케이스 문서의 핵심 결정이 live SSOT 문장/구조로 실제 내려와 있음
- `부분 반영`: 핵심선은 들어왔지만 용어, 단계, 세부 운영 규칙, 인덱스/요약 계층이 덜 따라옴
- `미반영`: 케이스 문서에는 있으나 live SSOT에는 아직 없음

## 1. 총평

- `CR-20260315-001` 바닥 재정렬은 live SSOT에 대체로 반영 완료 상태다.
- `CR-20260315-002` LMM/그리모어 재설계는 live SSOT에 핵심 성장선과 플랫폼 구조가 들어왔지만, 용어 치환과 운영 세부는 아직 부분 반영 상태다.
- `CR-20260316-001` 마법 상업 독법 오버홀은 2026-03-18 기준 7탑 21학파 final sync와 전역 규칙 요약까지 live SSOT에 반영 완료 상태다.

## 2. 케이스별 판정

### 2.1 `CR-20260315-001`

판정:
- `대체로 반영 완료`

확인된 반영:
- `WB-0028` 비공개 우주론 SSOT 신설
- `WB-0029` 적성 체계 공통 원리 신설
- `WB-0005/0006/0007` 재작성
- `WB-0016/0017/0026` 바닥 규칙 기준으로 재정렬
- `NC-0001`, `memory_tiers/long_term`의 주인공 정체성 메타를 `외래 기억 잔향 -> 키리온 수렴` 기준으로 정리
- `WB-0009/0010/0011/0013/0025`의 구 기원론 표현을 `심층 마나층 균열 / 잔향역 / 고대 재앙 상흔` 표면 설명으로 치환

잔여 이슈:
- live SSOT보다는 운영 문서 쪽 드리프트가 남아 있다.
- `world_ops/world_change_log.md`에는 `CR-20260315-001` 항목이 없다.
- 케이스 문서 자체도 `phase2=major`, `phase3=minor`, `request=status draft`처럼 절차 메타가 깔끔하게 닫히지 않았다.

### 2.2 `CR-20260315-002`

판정:
- `핵심선 반영, 세부는 부분 반영`

반영 완료로 볼 수 있는 축:
- 각인광장을 `그리모어 -> 성목 분지 -> 배지` 삼층 구조로 재정의
- 하급 과정을 `조회/보충/질문/초기 검색` 축적 구간으로 재배치
- 상급 과정을 `현상 각인 -> 영상 각인술` 및 제도화 확장 구간으로 재배치
- 배지를 `얇은 표준 단말`로 재정의
- `현상 열람실`을 고정식 예외 설비로 반영
- `영상 각인술`을 후행 제도 등록식으로 반영
- `LMM` 공용 상한을 `추천/정렬/의도 색인` 수준으로 후퇴
- narrative/prompt-facing 층에서 `3년 후 점프 기본 전제`를 제거하고 pre-academy와 academy pacing 경계를 보강
- academy snapshot vs current narrative time 혼선을 줄이는 2차 감사 조치를 simulation/population 문서군에 반영

부분 반영 항목:
- `픽시 계약` 표면 명칭 고정안은 live SSOT에 아직 반영되지 않았다.
  - live는 여전히 `하급 정령 계약`을 사용한다.
- `LMM은 판타지 표면 뒤로 후퇴` 원칙은 절반만 반영됐다.
  - 본문은 많이 후퇴했지만 `WB-0008` 제목/엔티티와 일부 요약은 여전히 `LMM`을 전면에 둔다.
- `비공식 운용 -> 감리 허가 -> 시범 운영 -> 드리아드 협약` 상태 기계는 live SSOT에 아직 없다.
  - live는 기능 해금 단계만 적고, 거버넌스 상태 전환은 생략한다.
- `runtime_interface_contract.md`의 패킷/자동 부착 채널 설계는 live SSOT에 고해상도로 내려오지 않았다.
  - `author_signature`, `query_signature`, `runtime_weight`, `정신 서명`, `맥락 가중치`, `연관도 표식` 같은 내부 채널은 live 문서에 거의 없다.
- 일부 요약/인덱스 계층은 최신 단계표를 끝까지 따라오지 못했다.
  - `관리/정화` 단계가 `world_bible_index*`, `memory_tiers/long_term` 등 일부 요약 계층에서 누락돼 있다.

미반영 항목:
- `색인의 그리모어 -> 주석의 그리모어 -> 실타래의 그리모어` 그리모어 3단계 성장선
- `요정 동행 -> 드리아드 감리 허가 -> 드리아드 협약 -> 성목 본체 공명` 사다리
- `전투 / 협상 / 정치 / 커뮤니티` 효용표의 단계별 explicit SSOT화
- `단계 10~13` 확장선(`다중 성목 연합`, `대륙 간 성목 연방`, `세계수 백본`, `루트 전용 그림자 아카이브`)의 live 문서 반영

보조 문서 드리프트:
- `next_steps.md`의 최상단 상태선은 2026-03-18 기준으로 정리됐지만, `CR-20260315-002` 세부 운영 설계 자체는 여전히 케이스 문서에 더 많이 남아 있다.

### 2.3 `CR-20260316-001`

판정:
- `반영 완료`

근거:
- `phase3_apply`, `phase4_sync`, `world_change_log` 기준으로 7탑 21학파 최종명과 전역 규칙 요약이 live SSOT에 내려왔다.
- `WB-0005`, `WB-0015`, `WB-0021`, `WB-0025`, `WB-0029`, academy current-term snapshot, population CSV/YAML, population scripts, handoff 문서까지 동기화됐다.

반영 완료로 볼 수 있는 축:
- 적탑 3학파 rename live 반영
- 청탑 3학파 rename live 반영
- 녹탑 3학파 rename live 반영
- 황탑 3학파 rename live 반영
- 자탑 3학파 36식 live 반영
- 백탑 3학파 rename 및 요약 반영
- 흑탑 3학파 rename 및 요약 반영
- `7색 감정/문화 레지스터`
- `교차색 콤보 규칙` 상위 요약
- `독자용 슬롯 문법`
- `마법/학파 상업 네이밍 헌법`
- generated layer와 검증 스크립트 동기화

현재 live에 반영된 현행명 기준 위치:
- `WB-0005_magic_system.md`
- `WB-0015_academy_bible.md`
- `WB-0025_appendix_naming_constitution.md`
- `WB-0029_appendix_aptitude_signature_materials.md`
- `WB-0021_appendix_terms_aliases.md`
- `world/live/population/profiles/current_term_snapshot_v1.yaml`
- `scripts/population/recompute_role_majors.py`
- `scripts/population/audit_population_invariants.py`
- `world/live/population/population_slots.csv`
- `world/live/population/P-*.yaml`

현재 live에서 구명이 남아 있어도 되는 위치:
- `WB-0021_appendix_terms_aliases.md`

예외:
- `WB-0021_appendix_terms_aliases.md`는 구명 보존 창구라서 `구명 잔존 = 미반영`으로 판정하면 안 된다.

## 3. 우선순위별 미반영/부분 반영 목록

### P1. 실제 SSOT 드리프트

- `픽시 계약` 표면 명칭 미반영
- `LMM` 전면 노출 후퇴 원칙 부분 반영
- 상태 기계(`비공식 운용 / 감리 허가 / 시범 운영 / 드리아드 협약`) 미반영
- packet/internal channel 설계 미반영

### P2. 요약/인덱스 계층 드리프트

- `관리/정화` 단계가 일부 인덱스/장기 기억 계층에서 누락

### P3. 운영 메타 드리프트

- `world_ops/world_change_log.md`에 `CR-20260315-001` 부재
- `CR-20260315-001`, `CR-20260315-002`는 request/phase 문서 상태값이 완전히 닫히지 않음

## 4. 결론

- 3월 15일 대화 중 `바닥 재정렬`은 SSOT에 거의 반영됐다.
- 3월 15일 대화 중 `LMM/그리모어 재설계`는 SSOT에 핵심 서사 방향만 먼저 들어갔고, 용어 치환/운영 상태/패킷 계층은 아직 케이스 문서에 더 많이 남아 있다.
- 3월 16일 대화 중 `마법 네이밍/상업 독법 오버홀`은 2026-03-18 기준 7탑 21학파 final sync와 전역 규칙 요약까지 live SSOT에 반영 완료됐다.
