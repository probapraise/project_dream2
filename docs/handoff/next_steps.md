# 다음 작업 목록

최종 업데이트: 2026-03-08 (렌바렌 가족 조형 확장 + 벨쿠란 규정 보강, WORLDBUILD-003~010 반영)
진행 상태 기준: `world/live/docs/master_map.md` recent changes에 `WORLDBUILD-010`까지 반영된 상태

---

## 이 문서의 기준

- 이 문서는 과거 Step 회고가 아니라, **현재 저장소에 실제로 남아 있는 상태와 작가 결정**을 기준으로 다음 작업을 정리한다.
- live SSOT는 `world/live/`다.
- 변경관리 이슈는 `world_ops` 케이스로 처리한다.
- 로컬 감사 결과:
  - `bash scripts/ops/world_ops_audit_bundle.sh`
  - 결과: `errors=0`, `warnings=0`

---

## 현재 실제 상태 요약

### 0. 2026-03-08 세계관 확정분 요약
- 렌바렌 백작가는 표면상 라베르니온 공작가 분가 대귀족이지만, 실체는 비밀 서명귀족이다.
- 렌바렌 가주의 `왕국 최상위 정보기관 수장` 직위는 명예직 성격이 강하고, 실제 정보 수집/분석 실권은 라베르니온 공작가가 쥔다.
- 렌바렌은 식흔(蝕痕) 운용과 잔흔 소거를 제공하는 종속 협력 가문이며, 승계 완료 후 형제자매를 제거하는 `방계 청소` 관행이 존재한다.
- 렌바렌의 현 식흔 후계자는 `여동생`이 아니라 `10세 장남`이다.
  - 장남은 두 달 전 왕도 `계승조회식`을 마친 뒤 가문 비밀과 장래의 방계 청소 의무를 전수받았다.
  - 이 때문에 현재 동생들을 향한 보호 충동, 질투, 공포가 뒤엉켜 심리적으로 흔들리고 있다.
  - 프롤로그 직전 키리온을 목검으로 기절 직전까지 때린 사건도 이런 혼란의 산물로 재해석된다.
  - 장남 이름은 `데리온 렌바렌 (Derion Renbaren)`으로 확정했다.
  - 독자 체감 목표는 `성가신 강압형 형 -> 계속 도움 되는 형 -> 트루 브라더` 전환이다.
  - 데리온은 키리온의 구조 설계/비전투형 재능을 쉽게 신뢰하지 못하고, 연무장 훈련과 실전형 무력을 강요하는 축으로 운용한다.
- 막내딸 이름은 `리리아 렌바렌 (Liria Renbaren)`으로 확정했다.
  - 정식 문장비전 계승자는 아니지만, 그라비온 진위감정 혈통의 `미세한 잔향`이 남아 있어 사람의 표정/말결/분위기를 유난히 잘 읽는다.
  - 키리온과 가장 죽이 잘 맞고, 장차 각인광장 운영에서는 인스타 계열 인싸용 쓰레드 관리자이자 최고 인기 인플루언서 축을 맡는다.
  - 독자 체감 목표는 `집안의 햇빛 -> 건드리면 안 되는 보호 대상 -> 데리온 재평가 장치`다.
- 벨쿠란 왕실은 서명귀족 혈통이 섞인 아동을 추적하며, 10세가 되는 해 왕도 세르비온에서 `계승조회식`을 열어 문장비전 계승 여부를 일괄 검증한다.
- 각 가문이 `계승조회식` 이전에 자체적으로 계승 여부를 사설 검증하는 것은 금지된다.
- 벨쿠란은 `계승조회식` 이전 아동의 체계적 마법 수련도 금지한다.
  - 허용: 마법 이론, 절차, 정형문, 종류 설명
  - 금지: 마나 회로/마나핵 활성화를 도와 실제 시전 가능 상태로 만드는 것
- 조기 수련이 적발되면 부모는 반역죄에 준하는 형을 구형받고, 영지 전체가 특별조사 대상이 된다.
- 이 규정이 가능한 이유는 `마법 사용 경험자`와 `미사용자` 사이에 마나핵/회로 감정 결과 차이가 뚜렷하기 때문이다.
  - 첫 사용 이후의 순환 리듬, 미세 잔향, 회로 개방 흔적이 남는다.
  - 완전 은닉법이 아예 없는 것은 아니지만, 고비용/고난도 감정 기만이 필요하고 일반 귀족가가 안정적으로 쓰기 어렵다.
- 왕가/공작가/일부 2시그니처 이상 가문은 조기 수련 특권을 사실상 누리고 있으며, 이 선행학습 격차가 아카데미 입학 초반 상위권 독식의 한 축으로 고정됐다.
- 키리온은 현재 8세라서 `10세 계승조회식`까지 2년 남았다.
  - 이론 학습은 가능하나, 실제 조기 시전 흔적이 남으면 변명 여지가 급격히 줄어든다.

### 1. 월드/모집단
- 학생 슬롯 SSOT:
  - `world/live/population/P-*.yaml`
  - `world/live/population/population_slots.csv`
- 총 슬롯: `3600`
- 상태 분포:
  - `uninstantiated=3599`
  - `named=1`
- 현재 named 슬롯:
  - `P-1027 -> NC-0001`

### 2. 코어 캐스트
- `world/live/population/core_cast/NC-0001_P-1027.md`만 존재한다.
- `world/live/docs/core_cast_bootstrap_v1.md` 상태는 `partial`이다.
- 다만 **NC-0002 이후 코어 캐스트 추가는 지금 바로 하지 않는다.**
- 작가 결정:
  - 주인공이 학술원에 입학한 뒤
  - 본격적인 시뮬레이션을 돌리면서
  - 그 흐름 속에서 NC를 추가한다.

### 3. 커뮤니티 구조
- 기존 고정 18보드 설정은 폐기됐다.
- 2026-03-06 기준으로 live `board_states/`의 `BOARD-0001_b01.md` ~ `BOARD-0018_b18.md` bootstrap stub은 제거 완료.
- 현재 원칙:
  - 커뮤니티/게시판은 동적 생성
  - `concept_only -> registered -> stateful -> retired` lifecycle로 관리
  - 필요한 보드만 `community_map.md`와 `board_states/`에 추가
  - 선제적으로 18개 보드를 깔아두지 않음
  - 새 ID는 `BOARD-001`, `BOARD-002` 식 3자리 증가형만 사용
- 과거 18보드 역사 자료는 `world/archive/quarantine/`에만 남긴다.

### 4. 시뮬레이션 산출물
- 현재 live에 있는 시뮬레이션 JSON:
  - `world/live/board_states/simrun-001_cold_start.json`
  - `world/live/board_states/simrun-002_pro_cold_start.json`
  - `world/live/board_states/simrun-003_pro_thinking_cold_start.json`
- 작가 결정:
  - 이 산출물들은 **간략 smoke test 결과물**
  - 당분간 정식 Layer A 문화 판단 근거로 쓰지 않음
  - `community_memory.md`나 `community_grammar_layer_a.md`에 승격하지 않음

### 5. Layer B
- `world/live/docs/community_grammar_layer_b.md`에 `ATOM-001~ATOM-006` 누적 완료
- 현재 단계:
  - ATOM 축적 진행 중
  - 상위 `GRAMMAR-*` 합성은 아직 시작 전

### 6. 집필
- 확정 원고:
  - `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v2.md`
  - `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md` (`current canon`)
- `artifacts/writing/style/style_constitution.md`는 리라이트 캐논의 결말 박자에 맞춰 S-07/S-08을 보정했고, live `style_bible.md`도 새 캐논 기준으로 재동기화됨
- 에피소드 폴더 규칙:
  - 각 에피소드 폴더는 생성 시점부터 `canon/` 하위 폴더 포함
  - 정식 반영된 최종본은 `canon/` 안에만 둠
  - `canon/README.md`가 current canon을 명시
  - canon은 수정 가능하며, 새 리비전 채택 시 `canon/` 내부에서 current를 갱신
  - 새 episode 폴더 생성은 `bash scripts/writing/new_episode_scaffold.sh <episode_id>`를 사용
- live 서사 상태 문서:
  - `world/live/docs/narrative_state.md` -> 현재 활성 서사 허브
  - `world/live/docs/story_arcs.md` -> 아크 단위 압축 메모리
  - `world/live/docs/foreshadow_registry.md` -> 활성 복선 레지스트리
  - `world/live/docs/episode_deltas.md` -> 회차별 상태 변화 로그
- 문체 상태 문서:
  - `world/live/docs/style_bible.md` -> 리라이트 캐논 기준 현재 필체 요약 반영 완료

### 7. VFP
- `world/live/docs/voice_fingerprint_spec.md` 존재
- NC-0001 카드에는 VFP v1 반영 완료
- 하지만 실행 체인에는 아직 주입/검증 코드가 연결되지 않았다.

### 8. 문서/레지스트리 드리프트
- `world/live/docs/simulation_state_index.md`
  - 실제 `artifacts/runs/`와 일부 불일치
- `world/live/docs/character_index_v2.md`
  - 헤더 `source_csv`가 예전 절대 경로를 가리킴
- `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`
  - 대상 루트가 예전 절대 경로로 남아 있음

---

## 우선순위 A: 지금 바로 할 일

### A-1. 왕국 규정 세부 설계 이어가기

이유:
- 이번 세션에서 `계승조회식`, 조기 수련 금지, 감정 차이까지 큰 축은 고정했지만, 제도를 실제 장면과 사건으로 돌릴 수 있는 운영 디테일은 아직 비어 있다.

해야 할 일:
- `계승조회식` 운영기관 명칭 확정
- 조기 수련 금지 법령/칙령의 공식 명칭 확정
- `마법 사용 경험자 vs 미사용자`를 판정하는 감정법/검사의 공식 명칭 확정
- `계승조회식` 당일 실제 절차(호송, 대기, 감정, 판정, 귀가) 설계
- 조기 수련 적발 시 특별조사 프로토콜과 대표 스캔들 사례 설계
- 왕가/공작가/2시그니처 가문의 조기 수련 특권이 어떤 명목으로 합법화되는지 명시

완료 조건:
- 다음 세션에서 제도 설명을 다시 처음부터 복원하지 않고, 바로 장면/사건/인물 갈등 설계로 들어갈 수 있다.

### A-2. `ep002` 집필 입력 정리

이유:
- 장기 연재용 narrative context 허브와 live `style_bible`은 정리됐지만, 리라이트된 캐논을 바탕으로 한 `ep002` 입력 패키지는 아직 미완이다.

해야 할 일:
- `world/live/docs/narrative_state.md`, `story_arcs.md`, `foreshadow_registry.md`, `episode_deltas.md`를 참조해 `ep002` 기획 입력을 정리
  - 책 읽기 = 관찰 장치 구도
  - 렌바렌 저택 정보 병목과 집사실 문답 온도의 후속 관찰 범위
  - 아직 설계/실행으로 점프하지 않는 박자 유지
  - 학술원까지 4년이라는 시간축을 당장 외부 확장 트리거로 쓰지 않는 박자 유지

완료 조건:
- 다음 집필 프롬프트가 live narrative hub와 style 문서를 함께 참조할 수 있다.

### A-3. 실행 레지스트리/경로 드리프트 정리

해야 할 일:
- `world/live/docs/simulation_state_index.md`를 실제 `artifacts/runs/` 구조에 맞게 갱신
- `world/live/docs/character_index_v2.md` 재생성 또는 헤더 정리
- `docs/architecture/PROJECT_ARCHITECTURE_MAP.md` 루트 경로 정정

완료 조건:
- 사람이 읽는 인덱스 문서와 실제 파일 시스템이 다시 일치한다.

### A-4. Layer B ATOM 계속 누적

현재 상태:
- ATOM 6개 누적
- 아직 상위 문법 합성 전

해야 할 일:
- 실제 커뮤니티 사례를 더 수집해 `ATOM-007+` 이어서 추가
- 10~15개 축적 후 상위 `GRAMMAR-*`로 묶을지 판단

---

## 보류/조건부 작업

### 코어 캐스트 확장
- 보류 이유:
  - 지금은 시점이 이름 붙이기보다 입학 이후 시뮬레이션 설계가 먼저다.
- 재개 조건:
  - 주인공 학술원 입학 이후
  - 본격 시뮬레이션에서 반복적으로 포착되는 인물 축이 생길 때

### 현재 simrun 결과의 Layer A 승격
- 보류 이유:
  - 현재 `simrun-001~003`은 smoke test 취급
- 재개 조건:
  - 정식 목적과 참여자 조건을 갖춘 시뮬레이션을 다시 실행했을 때

### VFP 실행 파이프라인 연결
- 보류 이유:
  - 반복 등장 인물과 본격 시뮬레이션 루프가 아직 충분히 열리지 않았다.
- 재개 조건:
  - 실제 recurring cast와 정식 sim/writing 사이클이 돌기 시작했을 때

---

## 조건부/트리거 작업

### 새 게시판을 live에 추가할 때
- `community_map.md` 먼저 갱신
- 필요 시에만 `board_states/`에 상태 파일 생성
- 변경 건이면 `world_ops` 케이스 기록

### 새 named/core cast를 추가할 때
- `python3 scripts/indexes/rebuild_character_index_v2.py`
- 필요 시 `bash scripts/ops/world_ops_audit_bundle.sh`

### 다음 회차 원고 캐논 확정 직후
- `artifacts/writing/episodes/<episode_id>/canon/`에 정식 반영본 배치
- `artifacts/writing/episodes/<episode_id>/canon/README.md` current 항목 갱신
- `artifacts/writing/style/style_constitution.md` 갱신
- `world/live/docs/style_bible.md` 갱신
- `world/live/docs/narrative_state.md` 갱신
- `world/live/docs/episode_deltas.md`에 상태 변화 추가
- 필요 시 `world/live/docs/story_arcs.md`, `world/live/docs/foreshadow_registry.md` 압축 갱신

### 정식 시뮬레이션 실행 직후
- `world/live/docs/simulation_state_index.md` 갱신
- `community_memory.md` 반영 여부 판단
- recurring 인물 VFP 후보 추출 여부 판단

---

## 지금 당장 다시 돌릴 필요 없는 것

- 모집단 생성 스크립트 전량 재실행
- 파생지표 배치 재생성
- 외국인 origin 재배정
- dorm/major 재계산
- 현재 smoke test simrun을 Layer A 문서로 승격하는 작업
- NC-0002 이후 코어 캐스트 선제 추가

이유:
- 현재 감사(`world_ops_audit_bundle.sh`)는 통과 상태다.
- 작가 판단상 시뮬레이션과 코어 캐스트는 **입학 이후 본격 루프에서 다시 잡는 게 맞다.**

---

## 다음 세션 권장 시작 순서

1. `계승조회식` 운영기관/법령/감정법/당일 절차를 설계해 2026-03-08 세계관 확정분을 사건화 가능한 수준으로 닫는다.
2. 그 다음 `world/live/docs/style_bible.md`를 채우고, 새 narrative hub(`narrative_state`/`story_arcs`/`foreshadow_registry`/`episode_deltas`) 기준으로 `ep002` 기획 입력을 만든다.
3. `world/live/docs/simulation_state_index.md`, `world/live/docs/character_index_v2.md`, `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`의 경로 드리프트를 정리한다.
4. `community_grammar_layer_b.md`의 ATOM을 계속 누적한다.
5. 그 다음에야 입학 이후 정식 시뮬레이션과 NC 코어 캐스트 확장으로 넘어간다.

---

## 참고 문서

- `world/live/docs/master_map.md`
- `world/live/docs/community_map.md`
- `world/live/docs/simulation_playbook.md`
- `world/live/board_states/README.md`
- `world/live/docs/community_grammar_layer_b.md`
- `world/live/docs/narrative_state.md`
- `world/live/docs/story_arcs.md`
- `world/live/docs/foreshadow_registry.md`
- `world/live/docs/episode_deltas.md`
- `world/live/docs/style_bible.md`
- `world/live/docs/voice_fingerprint_spec.md`
- `world/live/docs/simulation_state_index.md`
- `world/live/docs/core_cast_bootstrap_v1.md`
- `world/live/world_bible/WB-0005_magic_system.md`
- `world/live/world_bible/WB-0009_power_structure_factions.md`
- `world/live/world_bible/WB-0015_academy_bible.md`
- `world/live/world_bible/WB-0018_evidence_records_glossary.md`
- `world/live/world_bible/WB-0026_appendix_crest_arcana.md`
- `world/live/external/EX-0001.yaml`
- `world/live/population/core_cast/NC-0001_P-1027.md`
- `artifacts/writing/README.md`
- `artifacts/writing/episodes/README.md`
- `scripts/writing/new_episode_scaffold.sh`
- `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`
