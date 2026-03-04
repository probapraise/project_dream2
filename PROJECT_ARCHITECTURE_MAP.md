# Project Dream2 Architecture Map

작성일: 2026-03-04
최종 업데이트: 2026-03-04 (세션 4 — Layer A 문서 완료 + 시뮬레이션 런너 구현)
대상 루트: `/home/dlwhdgus/project_dream2`
조사 방식: 멀티 에이전트 6명 병렬 전수 조사 + 로컬 재검증

## 1. 현재 구현 스냅샷

- 학생 모집단 SSOT: `worldbible_refined_bundle_20260303/population/P-*.yaml` + `population_slots.csv`
- 현재 슬롯 총량: `3600`
- 상태 분포: `uninstantiated=3599`, `named=1` (`P-1027 -> NC-0001`)
- 직능 분포: `마법사 2220 / 기사 1020 / 사제 360`
- 기숙사 상위 분포:
  - `기사동 980`
  - `청탑 기숙사 521`
  - `황탑 기숙사 397`
  - `신전동군 346`
  - `적탑 기숙사 336`
- 진행 상태(문서 기준):
  - Step 1~7-E 완료
  - Step 8(커뮤니티 A/B) **완료** — Layer A/B 문서 + 시뮬레이션 3회 실행
  - Step 9~11 대기
- 시뮬레이션 실행 기록:
  - `simrun-001`: Flash Lite, Cold Start, 12인 2라운드
  - `simrun-002`: Pro (thinking ON, 토큰 부족 → 일부 잘림)
  - `simrun-003`: Pro (thinking ON, maxOutputTokens=8000) — 완전 성공, 문화 후보 3개 창발

## 2. 저장소 상위 구조

```text
project_dream2/
├─ scripts/                          # 데이터 생성/재계산/감사 + world_ops 게이트
├─ world_ops/                        # 변경관리 운영 체계(4-Phase, templates, sessions)
└─ worldbible_refined_bundle_20260303/
   ├─ docs/                          # 인덱스/상태/워크플로우 문서
   ├─ world_bible/                   # 활성 WB 섹션 (PUBLIC/CONFIDENTIAL/META)
   ├─ population/                    # P-* 학생 SSOT + core_cast/
   ├─ nonstudent/                    # NS-* 비학생 슬롯
   ├─ board_states/                  # 시뮬레이션 결과 상태 (simrun-001/002/003 존재)
   ├─ layer_b/                       # 게시판별 문법 산출물(초기)
   ├─ characters/                    # deprecated 스텁
   ├─ voice_packs/                   # deprecated 스텁
   ├─ persona_states/                # deprecated 스텁
   ├─ quarantine/                    # 충돌 가능 레거시 격리 보존
   └─ runs/                          # world_ops 실행 게이트 산출물
```

## 3. 레이어드 아키텍처

### 3.1 오케스트레이션 레이어 (문서 진입점)

- 단일 루트 엔트리: `docs/master_map.md`
- 오케스트레이터는 `master_map`만 상시 로딩, 나머지는 필요 시 로딩
- 인덱스 포인터:
  - `docs/world_bible_index_v2.md` (주)
  - `docs/world_bible_index.md` (legacy)
  - `docs/character_index_v2.md`
  - `docs/community_map.md`
  - `docs/simulation_playbook.md` 등

### 3.2 데이터 레이어 (Population)

- 규범(모델 정의): `docs/population_grammar.md`
- 실데이터 SSOT:
  - `population/P-*.yaml` (개별 슬롯 원본)
  - `population/population_slots.csv` (배치/집계 기준)
- 핵심 필드: `background_type`, `crest_vision_holder`, `dorm`, `grade`, `mana_color`, `major`, `vocation`, Big5, derived

### 3.3 캐릭터 인덱스/명명 레이어

- 슬롯 상태 레지스트리: `docs/character_index_v2.md`
- 코어캐스트 카드: `population/core_cast/*.md`
- 코어캐스트 운영 요약: `docs/core_cast_bootstrap_v1.md`
- named 전환은 CSV/YAML 동시 반영이 원칙

### 3.4 커뮤니티/시뮬레이션 레이어

- Layer A: 창발형 **— 문서 완료, 시뮬레이션 3회 실행**
  - `docs/community_grammar_layer_a.md` (CULTURE 레코드 포맷, 운영 파이프라인, 순응 스펙트럼, 파괴자 감지)
  - 시뮬 결과: `board_states/simrun-001/002/003`
  - 문화 후보 3개 창발 (simrun-003 기준): `fear_of_dark_history`, `teasing_red_tower`, `holy_tree_protection`
  - **아직 CULTURE 레코드 등재 미완료** (작가 승인 대기)
- Layer B: 작가 투사형 **— ATOM-001 등록 완료**, BOARD-001 "낙서장" 적용
  - `docs/community_grammar_layer_b.md`
- API 시뮬레이션 런너: `scripts/sim_runner.py`
  - Google Vertex AI (Gemini 3.1) 직접 호출
  - 기본 모델: `gemini-3.1-flash-lite-preview` (global endpoint)
  - 고품질 모델: `gemini-3.1-pro-preview` (thinking ON, maxOutputTokens=8000 권장)
  - Writer Report는 API 미사용 — Claude Code 오케스트레이터가 JSON 직접 분석
- 시뮬레이션 문서 골격:
  - `docs/simulation_playbook.md`
  - `docs/simulation_feedback.md`
  - `docs/simulation_state_index.md`
  - `docs/community_memory.md`

### 3.5 컨트롤 플레인 (world_ops)

- 4-Phase 변경관리 프로세스:
  1. Request 정제
  2. Phase2 충돌 탐색 (minor/major 분기)
  3. Phase3 적용
  4. Phase4 동기화
- 세션 문서 템플릿: `world_ops/templates/*.md`
- 실행 기록: `world_ops/sessions/CR-*.md`
- 실행 격리 게이트:
  - compile execution views
  - pre-injection gate
  - output leak scan
  - delete guard

## 4. 핵심 데이터 파이프라인 맵

### 4.1 학생(P) 파이프라인

```text
generate_population_slots
  -> add_student_fields
  -> (derived 경로 선택)
     -> recompute_derived
     or build_population_derive_batch_jsonl -> apply_population_derived_results
  -> assign_foreigner_origin
  -> (정책 보정)
     -> apply_population_bootstrap_policy
     and/or recompute_dorms
     and/or recompute_role_majors
  -> bootstrap_core_cast
  -> rebuild_character_index_v2
  -> audit_population_invariants
```

### 4.2 단계별 책임

- `generate_population_slots.py`
  - P-0001~P-3600 뼈대 생성
  - 초기 dorm은 `UNASSIGNED`
- `add_student_fields.py`
  - grade/mana_color/major/vocation + 조건부 필드 부여
- `recompute_derived.py` 또는 batch 경로
  - `DT/NFC/SM` 파생값 채움
- `apply_population_bootstrap_policy.py`
  - 배경 재균형 + dorm 정책 일괄 적용
- `recompute_dorms.py`
  - 합의된 dorm 규칙 기준 재산출 + legacy 필드 정리(`tower` 제거)
- `recompute_role_majors.py`
  - 기사/사제 major 정합 보정
- `bootstrap_core_cast.py`
  - 후보 조건 + 성향 거리 점수로 named 슬롯 선정/카드 생성
- `rebuild_character_index_v2.py`
  - 상태/분포/좌표/풀 문서 재생성
- `audit_population_invariants.py`
  - quota, dorm 룰, major 유효성, 조건부 필드 검증

## 5. World Bible/Index/Quarantine 맵

### 5.1 활성 문서 경로

- 본문: `world_bible/WB-*.md`
- 인덱스: `docs/world_bible_index_v2.md`
- 인덱스 재생성: `scripts/rebuild_world_indexes.sh`
- 감사: `scripts/world_ops_audit_bundle.sh`

### 5.2 Quarantine 전략

- 목적: 충돌 가능 레거시를 삭제 대신 격리 보존
- 경로: `quarantine/`
- 원칙:
  - 활성 문서와 분리
  - 필요 시 선별 재흡수
  - 실행 기본 경로에서는 비활성

### 5.3 현재 경계 상태

- `WB-0014/0020/0022/0023/0027` 계열은 활성 인덱스에서 빠져 있고 quarantine에 존재
- 활성 영역 감사는 `docs`, `world_bible`, `next_steps.md` 중심

## 6. World Ops 운영 체인

### 6.1 변경관리 체인

```text
world_ops_new_case
  -> (세션 문서 작성/검토)
  -> (삭제 포함 시) world_ops_delete_guard
  -> world_ops_audit_bundle
  -> world_change_log 갱신
```

### 6.2 시뮬/집필 실행 게이트 체인

```text
world_ops_compile_execution_views
  -> world_ops_pre_injection_gate
  -> (모델 호출)
  -> world_ops_output_leak_scan
```

### 6.3 감사 포인트

- 번들 정합성: index 참조, WB id 일치, 중복 id
- 정본 용어: 금칙어(`role_track`, `탑기숙사` 등) 탐지
- CSV 스키마: 필수 컬럼/레거시 컬럼(`tower`) 검증
- 누출 방지: META/CONFIDENTIAL 패턴 차단

## 7. 구현 완료/진행/미구현 매트릭스

| 영역 | 상태 | 현재 수준 |
|---|---|---|
| P-* 3600 SSOT 전환 | 완료 | YAML+CSV 운용 중 |
| dorm 최신 합의 반영 | 완료 | `crest_vision_holder` 우선 + 직능 배정 |
| role-major 정합 | 완료(보정 스크립트 존재) | 기사/사제 전용 major 셋 반영 |
| character index v2 | 완료 | 상태/분포/좌표/pool 생성 |
| core cast | 부분 완료 | `NC-0001`만 활성 named |
| community Layer B | 부분 완료 | 방법론 + ATOM-001 + BOARD-001 확정 |
| community Layer A | **문서 완료, 시뮬 실행 완료** | 문서 생성 + simrun-001/002/003 실행, CULTURE 등재 대기 |
| API 시뮬레이션 런너 | **완료** | `sim_runner.py` — Vertex AI Gemini 3.1 직접 호출 |
| simulation run 기록 | **부분 완료** | simrun-001/002/003 JSON 저장 완료, state index 미업데이트 |
| world_ops 게이트 체인 | 완료 | compile/pre/output/delete_guard 동작 |

## 8. 리스크/기술부채 레지스트리

- R1. dorm 정책 스크립트 중복
  - `recompute_dorms.py` vs `apply_population_bootstrap_policy.py` 책임 겹침
- R2. major 배정 중복
  - `add_student_fields.py`와 `recompute_role_majors.py` 역할 경계 불명확
- R3. derived 경로 이원화
  - 로컬 재계산 vs 외부 배치 적용 공존
- R4. YAML 스키마 드리프트 위험
  - 일부 스크립트가 `status/ch_id` 취급 방식 상이
- R5. 감사 사각지대
  - quarantine 영역은 기본 감사 범위 밖
- R6. 인덱스 메타 불일치 가능성
  - `world_bible_index_v2`의 summary 라벨과 실제 visibility 간 편차 가능
- R7. 운영 노이즈
  - `Zone.Identifier` 경고가 과다하여 신호 대 잡음비 저하

## 9. 권장 정리 우선순위

1. **CULTURE 레코드 등재** (즉시)
   - simrun-003 창발 후보 3개 작가 검토 후 `community_grammar_layer_a.md`에 등재
   - `fear_of_dark_history` / `teasing_red_tower` / `holy_tree_protection`
2. **NC-0002~ 조연 코어 캐스트 설계** (다음)
   - 시뮬레이션 결과 반영 + 주인공 관계망 기준 (적대/지지/멘토)
3. **인덱스 재생성**
   - `python3 scripts/rebuild_character_index_v2.py`
4. 정책 보정 스크립트 정리
   - dorm canonical 1개로 통일
   - role-major 보정 경로를 단일 파이프라인에 편입
5. 파생지표 경로 모드화
   - `offline(local)` / `batch(llm)` 모드 명확화
6. 스키마 계약서 고정
   - YAML/CSV 필드 계약 문서화 + writer 공통화
7. 코어캐스트 정합 복구
   - `bootstrap_core_cast.py`와 현재 NC-0001 실데이터 불일치 해소

## 10. 부록: 핵심 스크립트 분류

- 생성/초기화:
  - `generate_population_slots.py`
  - `generate_nonstudent_slots.py`
  - `add_student_fields.py`
  - `assign_foreigner_origin.py`
  - `bootstrap_core_cast.py`
- **시뮬레이션 실행**:
  - `sim_runner.py` — Layer A 콜드 스타트 / API 기반 커뮤니티 시뮬레이션
    - 입력: `population_slots.csv` (P-* 슬롯)
    - 출력: `board_states/simrun-NNN_*.json`
    - 모델: `gemini-3.1-flash-lite-preview` (기본) / `gemini-3.1-pro-preview` (고품질)
    - 인증: `vertex_key.json` (서비스 계정, git 제외)
    - Writer Report: API 미사용, Claude Code 오케스트레이터가 직접 분석
- 재계산/보정:
  - `recompute_dorms.py`
  - `recompute_role_majors.py`
  - `recompute_derived.py`
  - `apply_population_bootstrap_policy.py`
  - `apply_population_derived_results.py`
- 인덱스/리빌드:
  - `rebuild_character_index_v2.py`
  - `rebuild_world_indexes.sh`
- 감사/검증:
  - `audit_population_invariants.py`
  - `world_ops_audit_bundle.sh`
- world_ops 운영 게이트:
  - `world_ops_new_case.sh`
  - `world_ops_compile_execution_views.sh`
  - `world_ops_pre_injection_gate.sh`
  - `world_ops_output_leak_scan.sh`
  - `world_ops_delete_guard.sh`
