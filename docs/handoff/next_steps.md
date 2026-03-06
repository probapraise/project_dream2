# 다음 작업 목록

최종 업데이트: 2026-03-06 (경로 표기/Step 8 상태 동기화)
진행 상태 업데이트: 2026-03-06

---

## 세션 핸드오프 (다음 세션 시작점)

- 경로 표기 규칙: 이 문서는 저장소 루트 기준 실제 경로를 사용한다.

- 현재 기준 완료: Step 1~8
- 현재 활성 인물 체계:
  - 기존 CH-* 카드/보이스팩/퍼소나 상태 = 폐기 완료(영구 삭제)
  - 모집단 SSOT = `world/live/population/P-*.yaml` + `world/live/population/population_slots.csv`
  - 코어 캐스트 = NC-0001만 등록 (`world/live/population/core_cast/NC-0001_P-1027.md`)
  - NC-0002~ 조연: 미설계 (다음 작업)
- 인덱스 상태 스냅샷:
  - `uninstantiated=3599`, `named=1`
  - named: `P-1027` (NC-0001, 키리온 렌바렌)
- P-* 슬롯 현재 필드:
  - `id / background_type / crest_vision_holder / dorm / grade / mana_color / major / vocation`
  - 서명귀족만: `noble_house`
  - 비인간만: `race`
  - 외국인만: `origin`
  - `b5 / derived`
  - status/ch_id는 CSV 전용
- 최신 운영 규칙(확정):
  - 문장비전 보유자: 비전관 강제 소속
  - 문장비전 비보유자: 직능 기준 기숙사 배정
  - 외국·인외동 전용동 폐지 (외국인/인외도 동일 배정 규칙 적용)

### 다음 세션 첫 3단계 (권장)
1. **커뮤니티 레이어 B ATOM 누적** — 실제 커뮤니티 글 추가 수집으로 ATOM-002부터 축적
2. **NC-0002~ 조연 코어 캐스트 설계** — 주인공 관계망 기준 (적대/지지/멘토 포지션)
3. **인덱스 재생성** — `python3 scripts/indexes/rebuild_character_index_v2.py` (새 필드 + 최신 기숙사 배정 규칙 반영 확인)

---

## 완료된 스텝

### Step 1. population_grammar.md 작성
- 상태: 완료 (2026-03-04, v0.3 dorm-rule sync 반영)
- 위치: `world/live/docs/population_grammar.md`

### Step 2. P-* 슬롯 생성 스크립트 작성
- 상태: 완료 (2026-03-04)
- 위치: `scripts/population/generate_population_slots.py`
- 출력: `world/live/population/` (P-0001~P-3600)

### Step 3. 파생 지표 산출 배치 프롬프트 설계
- 상태: 완료 (2026-03-04)
- 위치: `world_ops/templates/population_derive_prompt.md`

### Step 4. 파생 지표 산출 실행
- 상태: 완료 (2026-03-04, 멀티 에이전트 6분할 로컬 추론)
- 준비 산출물: `artifacts/batch/` 일체

### Step 5. character_index 좌표 레지스트리 초기화
- 상태: 완료 (2026-03-04)
- 기존 CH-* 162개 폐기 / `world/live/docs/character_index_v2.md` 갱신

### Step 6. 핵심 인물 선제 조형 (구 버전 → 폐기 후 재설계)
- 상태: 완료 후 전면 재설계 (2026-03-04 세션 2)
- 구 NC-0001~NC-0007 (P-0867 등 7명): 전면 삭제, `world/live/docs/core_cast_bootstrap_v1.md` reset
- **현재 상태: NC-0001(주인공)만 신규 등록, 나머지 미설계**

### Step 7. P-* 학생 슬롯 추가 필드 배정
- 상태: 완료 (2026-03-04 세션 2) — 버그 수정 포함
- 실행: `python3 scripts/population/add_student_fields.py` (SEED=42)
- **버그 수정**: 초기 버전은 grade/mana_color/vocation이 동일 셔플 사용 → 완전 상관 문제
  - 수정: 각 필드 배정 직전 독립 `rng.shuffle(idx)` 호출
- 추가 필드: crest_vision_holder / grade / mana_color / major / vocation / noble_house / race / origin
- 배분: 모든 정원 정확히 충족, 1학년~보라탑 등 모든 조합 자연 분포 확인

### Step 7-B. foreigner origin 배정
- 상태: 완료 (2026-03-04 세션 2)
- 점검: `python3 scripts/population/assign_foreigner_origin.py --check`
- 반영: `python3 scripts/population/assign_foreigner_origin.py --apply` (SEED=42)
- 메인: ARC-인접왕국권 50명 / 나머지 4그룹 균등 (SAH·NOR·ARC원거리·출신불명 각 17~18명)
- OST 마사토라(관문제국 쇄국) 의도적 배제

### Step 7-C. 주인공 named 슬롯 지정
- 상태: 완료 (2026-03-04 세션 2)
- 각인학파 유일 슬롯: **P-1027 → NC-0001**
- 주인공: 키리온 렌바렌 / 렌바렌 백작가 차남 / common_noble / 보라탑 1학년 / 마법사
- 렌바렌 백작가: 24 서명귀족 가문 外 일반 백작가 → 비전관 없음 → 플랫폼이 유일한 상승 경로
- 산출물: `world/live/population/core_cast/NC-0001_P-1027.md`
- CSV: P-1027 status=named, ch_id=NC-0001 반영

### Step 7-D. 커뮤니티 이중 레이어 방법론 설계 토의
- 상태: 방법론 확정 (2026-03-04 세션 2), 구현 대기

### Step 7-E. 기숙사/직능 배정 규칙 합의 반영
- 상태: 완료 (2026-03-04 세션 3)
- 확정 사항:
  - 문장비전 보유자(`crest_vision_holder=true`)는 배경 유형과 무관하게 비전관 강제 소속
  - 문장비전 비보유자는 직능 기준으로 7탑 기숙사군/기사동/신전동군 배정
  - 외국·인외동 전용동 폐지 (외국인/인외도 동일 규칙 적용)
- 반영 문서: `world/live/docs/population_grammar.md` (v0.3)

---

## 진행 중 / 다음 작업

### Step 8. 커뮤니티 레이어 A/B 방법론 구현
- 상태: 완료 (2026-03-04 세션 4)
  - Layer B 문서 생성 및 ATOM-001~003 등록 완료
  - Layer A 문서 생성 및 시뮬레이션 3회 실행 완료

#### 개념 정의
- **레이어 A (시뮬레이션 창발)**: P-* 슬롯 조건 기반 상호작용 누적 → 의도하지 않은 문화·규범 자생
- **레이어 B (작가 투사)**: 주인공(빙의 개발자)이 그리워하는 커뮤니티 문법을 각인광장에 의도적 이식
  - 실제 커뮤니티에서 골때리거나 웃긴 글/사건 → 분해 → ATOM 저장 → 문법 합성

#### 레이어 B 파이프라인
```
입력: 작가가 실제 커뮤니티 글 + 설명 제공
  ↓
분해: 3레이어 추출
  - 사회 동학 (core_pattern)
  - 감정 레지스터 (emotional_register)
  - 커뮤니티 문법 (in_group_mechanics)
  ↓
저장: ATOM-NNN (YAML 형식, `world/live/docs/community_grammar_layer_b.md`)
  ↓
합성: 10~15개 누적 시 → 상위 GRAMMAR-* 규칙으로 통합
  ↓
반영: 캐릭터 빅5/파생지표 조건과 연결 → 시뮬레이션 발동 조건
```

#### ATOM 저장 형식
```yaml
ATOM-NNN:
  source_type: 게시글 / 댓글 / 밈 패턴 / 사건
  core_pattern: 추상 사회 동학
  emotional_register: 감정 온도 (냉소적 쾌감 / 훈훈한 연대 / 집단 조롱 등)
  in_group_mechanics: 집단 내 작동 원리
  trigger_condition: 발동 조건 (캐릭터 타입 + 상황)
  world_translation: 각인광장 표면형 (세계관 언어 번역)
```

#### 적용 범위 (확정 2026-03-04)
- 각인광장 내 **주인공이 직접 관리하는 단일 익명 게시판**에만 적용
- 순수 취미 공간 — 상업성·LMM 고도화 목표와 의도적으로 배치
- 서사 마찰: 조력자들의 폐쇄 압박 vs. 주인공의 고집
- 상세: `world/live/docs/community_grammar_layer_b.md`

#### 저장 위치 (현황)
- `world/live/docs/community_grammar_layer_b.md` (생성 완료, ATOM-001~003 등록)
- `world/live/docs/community_grammar_layer_a.md` (생성 완료, 2026-03-04)

### Step 9. NC-0002~ 조연 코어 캐스트 설계
- 주인공 관계망 기준: 적대 / 지지 / 멘토 포지션 각 1~2명
- 기존 P-* 슬롯 중 선정 (빅5 조건 기반)
- `world/live/docs/core_cast_bootstrap_v1.md` 확장

### Step 10. 인덱스 재생성
- `python3 scripts/indexes/rebuild_character_index_v2.py`
- 새 필드(grade/mana_color/major/vocation 등) 및 최신 기숙사 배정 규칙 반영 점검
- named=1 (NC-0001) 상태 반영

### Step 11. 첫 시뮬레이션 시나리오 확정
- 시나리오 범위 확정 → world_bible 로딩 범위 결정
- `world/live/docs/master_map.md` / `world/live/docs/community_map.md` / `world/live/docs/simulation_playbook.md` 최종 검토

---

## 보류 중

- Voice Pack 템플릿 갱신 (P-* 체계 반영)
- simulation_playbook 온디맨드 생성 흐름 섹션 추가
- ~~레이어 A/B 각인광장 공간 분리 여부 결정~~ → 확정: 단일 익명 게시판에만 적용 (`world/live/docs/community_grammar_layer_b.md`)

---

## 참조 문서

| 문서 | 역할 |
|---|---|
| `docs/design/character_population_methodology.md` | 빅5 배정 + 파생 지표 방법론 |
| `docs/design/spec_sheet_v1.md` (v1.2) | 시스템 전체 설계 원칙 |
| `world_ops/README.md` | 세계관 변경 관리 프로세스 |
| `world/live/docs/core_cast_bootstrap_v1.md` | NC-* 코어 캐스트 현황 |
| `scripts/population/add_student_fields.py` | P-* 추가 필드 배정 (grade/mana_color/major 등) |
| `scripts/population/assign_foreigner_origin.py` | foreigner origin 배정 |
| `scripts/population/generate_nonstudent_slots.py` | NS-* 비학생 655명 생성 |
