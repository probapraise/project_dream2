# 다음 작업 목록

최종 업데이트: 2026-03-10 (Quick Sim 기본 / tuned API fallback 전환 반영 상태)
진행 상태 기준: `ep002` canon 확정, episode summary 추가, Layer B `ATOM-012` 및 `GRAMMAR-001~003` 초안 반영, `Quick Sim` 1차 파일럿/비교 완료 상태

---

## 이 문서의 기준

- 이 문서는 과거 Step 회고가 아니라, **현재 저장소에 실제로 남아 있는 상태와 작가 결정**을 기준으로 다음 작업을 정리한다.
- live SSOT는 `world/live/`다.
- 변경관리 이슈는 `world_ops` 케이스로 처리한다.
- 최근 확인한 git 이력:
  - `753fb27` `worldbuild: normalize color terms and canonize ep002`
  - `5e93929` `writing: add episode summary files`
  - `ea6ffbc` `layerb: add atom batch and grammar drafts`
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
- 혼인 후 성 표기는 현실식 남편 성 추종이 아니라, `출생 가문 성 유지 + 혼인 가문 직위 사용`으로 정리한다.
  - 예: `셀리아 그라비온`, 직위는 `렌바렌 백작부인`
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
- 주인공 정체성의 META 진실은 `완전한 타인 빙의`보다 `적합성 높은 외부 표본의 지식/사고 구조가 덧입혀진 뒤 결국 키리온 렌바렌으로 수렴하는 존재` 쪽으로 고정했다.
  - 상위관찰자들은 빠른 이탈 방지를 위해 이름/부모 같은 자전적 앵커 기억은 지우고, 절차 기억·개념 지식·기질을 남겨 삽입했다.
  - 그래서 장기적으로는 외부인보다 `성숙하게 변형된 키리온 렌바렌`으로 읽히게 된다.
- 서사 배치 기준:
  - 아르케이온 권역 첫 진입(12세 하급 과정 입학식/첫 수업)은 잠정적으로 `10화 전후`를 목표로 둔다.
  - 하급 과정은 `12~14세 기본기 3년`이고, 상급 과정은 `15세 이후 4년`으로 재정의한다.
  - 하급 과정 파트에서는 교수법/환경/수업 내용을 밀도 있게 맛보기로 보여주고, 키리온이 `각인광장` 구현에 필요한 병목과 학습 방향을 파악하게 한다.
  - 이후 `3년 후`로 점프해 `상급 과정 진입성취평가 -> 입학 즉시 전공 선택 우선권 행사 -> 각인술 선택 클리프행어` 구조로 본편을 연다.
  - 하급 과정과 상급 과정은 지리적으로 붙어 있어, 리리아가 하급 과정 재학생일 때도 상급 과정/공동 광장/게시판 서사에 빠르게 접속할 수 있게 한다.
  - 그 이전에는 주인공이 `칼리온의 시험을 일단 통과했다`는 가벼운 안도만 캐치하도록 한다.
  - 칼리온이 실제로 이계 지식과 그 영향을 알고 있었으며, 그럼에도 주인공을 아들로 판단했다는 진실은 학술원 진입 후의 더 큰 가족 이벤트에서 공개한다.

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
- 현재 primary explore 산출물:
  - `artifacts/quick_sims/QSIM-20260310-001_human_backend/`
- 비교용 API run:
  - `artifacts/runs/RUN-QSIM-COMPARE-20260310-001/`
  - `artifacts/runs/RUN-QSIM-COMPARE-20260310-002/`
- 작가 결정:
  - `Quick Sim`을 기본 경로로 사용
  - API run은 fallback이자 검증 레인으로 사용
  - 기존 `simrun-001~003`은 여전히 **간략 smoke test 결과물**
  - 당분간 정식 Layer A 문화 판단 근거로 쓰지 않음
  - `community_memory.md`나 `community_grammar_layer_a.md`에 승격하지 않음

### 5. Layer B
- `world/live/docs/community_grammar_layer_b.md`에 `ATOM-001~ATOM-012` 누적 완료
- 현재 단계:
  - ATOM 축적 12개 도달
  - `GRAMMAR-001~003` 초안 작성 완료

### 6. 집필
- 확정 원고:
  - `artifacts/writing/episodes/ep000_prologue/canon/프롤로그_리라이트_v2.md`
  - `artifacts/writing/episodes/ep001/canon/1화_리라이트_v2.md`
  - `artifacts/writing/episodes/ep002/canon/2화_리라이트_v1.md`
- 회차 요약:
  - `artifacts/writing/episodes/ep000_prologue/summary_v1.md`
  - `artifacts/writing/episodes/ep001/summary_v1.md`
  - `artifacts/writing/episodes/ep002/summary_v1.md`
- `artifacts/writing/style/house_rules.md`는 항상 읽는 전역 작성 소스이고, diff 추출 규칙은 `style_pattern_library.md`와 회차별 `style_selection_vN.md`로 분리 운영한다. 실제 모델 주입은 `episode_style_constitution_vN.md`를 기준으로 한다
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
  - 실제 `artifacts/runs/`의 `RUN-AUDIT-TMP`, `RUN-GATE-DRY`가 아직 등록되지 않음
- `artifacts/writing/episodes/*/summary_v1.md`
  - `canon 기준` 링크가 현재 저장소 경로(`/home/dlwhdgus/project_dream2`)가 아니라 예전 절대 경로(`/home/ljhljh/project_dream2`)를 가리킴
- `artifacts/writing/README.md`
  - 스냅샷 기준일이 2026-03-07에 머물러 있고 `ep002` current canon 및 `summary_v1.md` 계열을 아직 반영하지 않음

---

## 우선순위 A: 지금 바로 할 일

### A-1. 아르케이온 구조 개편 후속 정리

이유:
- 오늘 세션에서 `하급 과정 3년 + 15세 상급 과정 진입성취평가` 구조는 고정했지만, 하급 과정의 실제 교수법/생활 리듬/첫 시즌 사건 배치는 아직 문서로 닫히지 않았다.

해야 할 일:
- `WB-0015`에 하급 과정 학년별 운영 규칙과 상급 과정 진입성취평가 후 `입학 즉시 전공 확정` 디테일을 추가 보강
- 입학식/기숙사 배정/첫 수업/첫 시연/첫 서열 충돌 등 `12세 맛보기 시즌`의 대표 이벤트 시퀀스 정리
- `3년 후` 점프 직전 키리온이 파악하는 각인광장 핵심 병목(배지망, 각인술, 중계주, 열람권)을 장면 단위로 정리
- 상급 과정 진입성취평가 상위권-전공 선택-각인술 클리프행어의 장면 설계

완료 조건:
- 다음 세션에서 아카데미 도입부와 15세 점프 시점을 바로 집필 가능한 수준으로 호출할 수 있다.

### A-2. 왕국 규정 세부 설계 이어가기

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

### A-3. `ep003` 집필 입력 패키지 정리

이유:
- `ep002`는 canon과 summary까지 확보됐다. 이제 다음 회차 입력을 `ep000~ep002` 누적 결과 기준으로 묶어야 한다.

해야 할 일:
- `artifacts/writing/episodes/ep000_prologue/summary_v1.md`, `ep001/summary_v1.md`, `ep002/summary_v1.md`와 `ep002` current canon을 묶어 다음 회차 입력 패키지 작성
- `world/live/docs/narrative_state.md`, `story_arcs.md`, `foreshadow_registry.md`, `episode_deltas.md`를 참조해 `ep003` 기획 입력 정리
  - `서고 접근권` 획득 이후 `자색 표준식 입문서`와 서고 열람이 동시에 보상과 감시 장치로 작동하는 구도 유지
  - 칼리온이 `행동`에서 `독서 패턴`으로 감시 해상도를 올린다는 축 명시
  - 아직 학술원/외부 확장으로 점프하지 않고 저택 내부 관찰전의 압력을 유지

완료 조건:
- 다음 집필 프롬프트가 `ep002` canon/summary와 live narrative hub를 함께 참조해 `ep003`로 바로 이어질 수 있다.

### A-4. 실행 레지스트리/경로 드리프트 정리

해야 할 일:
- `world/live/docs/simulation_state_index.md`를 실제 `artifacts/runs/` 구조에 맞게 갱신
- `artifacts/writing/episodes/ep000_prologue/summary_v1.md`, `ep001/summary_v1.md`, `ep002/summary_v1.md`의 절대경로 링크를 현 저장소 기준으로 정정
- `artifacts/writing/README.md` 스냅샷 설명을 현재 파일 구조 기준으로 갱신

완료 조건:
- 사람이 읽는 인덱스 문서와 실제 파일 시스템이 다시 일치한다.

### A-5. Layer B ATOM 계속 누적

현재 상태:
- ATOM 12개 누적
- 상위 `GRAMMAR-001~003` 초안 작성 완료

해야 할 일:
- 실제 커뮤니티 사례를 더 수집해 `ATOM-012+` 이어서 추가
- 12~15개 구간에서 `GRAMMAR-*` 경계와 `synthesis_of` 구성을 재조정
- 필요 시 각 `GRAMMAR-*`를 시뮬레이션 발동 규칙/캐릭터 타입 조건과 직접 연결

### A-6. Quick Sim 기본 레인 후속 구현

이유:
- Quick Sim을 기본 경로로 채택했으므로, 이제는 파일럿 검증 단계가 아니라 운영 루틴으로 굳혀야 한다.

해야 할 일:
- `bash scripts/sim/new_quick_sim_run.sh <run_id>` 스캐폴드를 실제 운영 루틴에 정착
- Layer B / 비-Layer B / 정보 전달형 / 갈등 유발형 seed를 섞어 Quick Sim 5-run 묶음 누적
- Quick Sim 결과의 `skeptic -> scorecard -> summary` 후처리 규격 고정
- Quick Sim에서 API fallback으로 올리는 조건을 케이스 기반으로 더 정교화

완료 조건:
- Quick Sim이 ad hoc 실험이 아니라 저장소의 일상적인 기본 시뮬레이션 레인으로 굳는다.

### A-7. tuned API fallback 다양성 보정

이유:
- `BOARD-001` 전용 프롬프트를 붙인 API run은 표면 톤은 좋아졌지만, 반응이 `인간 지피티 / 추론 high / 대기열` 축으로 과수렴했다.

해야 할 일:
- tuned API용 prompt에 `rough diversity` 규칙을 추가해 반응자 간 밈 수렴을 완화
- 구조 읽기형 / 조롱형 / 분위기 부스터형 / 삐딱한 한 줄형의 분화를 더 강하게 유도
- `Quick Sim vs tuned API` 비교를 다음부터는 주력 기준으로 사용

완료 조건:
- API fallback이 Quick Sim보다 느리더라도, 적어도 "격리된 검증 레인"으로서 별도 가치가 분명해진다.

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
- 필요 시 `bash scripts/writing/new_canon_patch.sh <episode_id> <new_canon_filename>`로 사후 패치 snapshot 생성
- `artifacts/writing/episodes/<episode_id>/summary_v1.md` 작성 또는 최신 상태로 갱신
- `artifacts/writing/style/style_pattern_library.md` 갱신
- `artifacts/writing/episodes/<episode_id>/style_selection_vN.md` 작성 또는 갱신
- `artifacts/writing/episodes/<episode_id>/episode_style_constitution_vN.md` 작성 또는 갱신
- `artifacts/writing/episodes/<episode_id>/setting_brief_vN.md` 작성 또는 갱신
- `artifacts/writing/episodes/<episode_id>/long_range_summary_vN.md` 작성 또는 갱신
- `artifacts/writing/episodes/<episode_id>/prompt_packet_vN.md` 작성 또는 갱신
- `artifacts/writing/episodes/<episode_id>/prompt_vN.md` 작성 또는 갱신
- `artifacts/writing/episodes/<episode_id>/analysis/episode_scorecard_vN.md` 작성 또는 갱신
- `artifacts/writing/episodes/<episode_id>/analysis/revision_delta_vN.md` 작성 또는 갱신
- `world/live/docs/memory_tiers/recent.md`, `current_arc.md`, `entity_registry.md`, `knowledge_state_registry.md`, `access_control_matrix.md`, `long_term.md` 갱신
- pre-academy 구간이면 `world/live/docs/pre_academy_checkpoint_plan.md` 점검
- `world/live/docs/style_bible.md` 갱신
- `world/live/docs/narrative_state.md` 갱신
- `world/live/docs/episode_deltas.md`에 상태 변화 추가
- 필요 시 `world/live/docs/story_arcs.md`, `world/live/docs/foreshadow_registry.md` 압축 갱신
- `bash scripts/writing/post_canon_sync.sh <episode_id>` 실행
- `python3 scripts/writing/audit_live_sync.py --episode-id <episode_id>` 통과 확인
- 다음 회차가 이미 scaffold되어 있으면 `python3 scripts/writing/audit_prompt_packet.py <next_episode_id>` 실행

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
2. 그 다음 `ep000~ep002` canon/summary와 live narrative hub(`narrative_state`/`story_arcs`/`foreshadow_registry`/`episode_deltas`)를 묶어 `ep003` 입력 패키지를 만든다.
3. `world/live/docs/simulation_state_index.md`, `artifacts/writing/episodes/*/summary_v1.md`, `artifacts/writing/README.md`의 드리프트를 정리한다.
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
- `artifacts/writing/episodes/ep000_prologue/summary_v1.md`
- `artifacts/writing/episodes/ep001/summary_v1.md`
- `artifacts/writing/episodes/ep002/summary_v1.md`
- `scripts/writing/new_episode_scaffold.sh`
- `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`
