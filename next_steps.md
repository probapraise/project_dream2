# 다음 작업 목록

최종 업데이트: 2026-03-04
진행 상태 업데이트: 2026-03-04

---

## 세션 핸드오프 (다음 세션 시작점)

- 현재 기준 완료: Step 1~6
- 현재 활성 인물 체계:
  - 기존 CH-* 카드/보이스팩/퍼소나 상태 = 폐기 완료(영구 삭제)
  - 모집단 SSOT = `population/P-*.yaml` + `population/population_slots.csv`
  - 코어 캐스트 = `NC-*` 7명 (`population/core_cast/`)
- 인덱스 상태 스냅샷:
  - `uninstantiated=3593`, `instantiated=0`, `named=7`
  - active IDs: `P-0161, P-0203, P-0403, P-0867, P-1097, P-2297, P-3563`

### 다음 세션 첫 3단계 (권장)
1. Step 7 시나리오 1건 확정 (사건 요약 + 공개 범위 + 관련 인물)
2. 시나리오 기준 로딩 범위 고정 (`world_bible_index_v2`, `character_index_v2`, `core_cast_bootstrap_v1`)
3. 첫 탐색 시뮬레이션 1회 실행 후 `official/explore` 분리 기록

---

## 즉시 실행 가능 (순서 있음)

### Step 1. population_grammar.md 작성
- 상태: 완료 (2026-03-04)
- 위치: `worldbible_refined_bundle_20260303/docs/population_grammar.md`
- 내용:
  - 탑별 인구 비율 (청탑/보라탑/황탑/백탑/녹탑/적탑/흑탑)
  - 배경 유형 분포 (서명귀족 / 일반귀족 / 평민(몰락귀족 포함) / 외국인 / 인외)
  - 학년별 분포
  - 집단 간 구조적 긴장 (비전관 vs 일반동, 탑별 문화 충돌 등)
  - 시드 유형별 반응 민감도 맵 (빅5 좌표 구간 → 반응 예측)
- 참조: `character_population_methodology.md`, `worldbible_refined_bundle_20260303/world_bible/WB-0015_academy_bible.md`

### Step 2. P-* 슬롯 생성 스크립트 작성
- 상태: 완료 (2026-03-04)
- 위치: `scripts/generate_population_slots.py`
- 기능:
  - 정규분포 샘플링으로 P-0001~P-3600 빅5 수치 생성
  - `background_type` 배정 (서명귀족/일반귀족/평민/외국인/인외 운영 비율)
  - 학술원 보정 적용 (methodology 문서 기준)
  - YAML 형식으로 개별 파일 출력 또는 단일 CSV 출력
- 출력 위치: `worldbible_refined_bundle_20260303/population/` (신규 디렉터리)
- 참조: `character_population_methodology.md` Section 3

### Step 3. 파생 지표 산출 배치 프롬프트 설계
- 상태: 완료 (2026-03-04)
- 위치: `world_ops/templates/population_derive_prompt.md`
- 내용:
  - 입력: P-* ID + 빅5 수치
  - 출력: DT / NFC / SM 수치 (0.01~0.99)
  - 공식 및 잔차 처리 방침 (methodology 문서 기준)
- Batch API 호출 스펙 포함

### Step 4. 파생 지표 산출 실행
- 상태: 완료 (2026-03-04, 멀티 에이전트 6분할 로컬 추론 반영)
- Step 2 산출물을 입력으로 병렬 처리(600개 x 6 shard)
- 완료 후 각 슬롯 파일에 `derived` 섹션 기입
- 준비 산출물:
  - `world_ops/batch/population_derive_requests.jsonl` (3,600건)
  - `scripts/build_population_derive_batch_jsonl.py`
  - `scripts/apply_population_derived_results.py`
  - `world_ops/batch/agent_shards/derived_01.csv` ~ `derived_06.csv`
  - `world_ops/batch/population_derived_merged.csv`
  - `world_ops/batch/population_derive_output_from_agents.jsonl`

### Step 5. character_index 좌표 레지스트리 초기화
- 상태: 완료 (2026-03-04)
- 위치: `worldbible_refined_bundle_20260303/docs/character_index_v2.md` 갱신
- Step 4 완료 후 빅5/파생 지표 기반 초기 레지스트리 구성
- 기존 162개 CH-* 카드/보이스팩/퍼소나 상태는 폐기 완료(영구 삭제)
- 메모(완료): `python3 scripts/apply_population_bootstrap_policy.py` 실행으로 `population_slots.csv` + `P-*.yaml` 재배치 반영 완료(서명귀족 160 / 일반귀족 2,870 / 평민 200, 비전관 160 전용).

### Step 6. 핵심 인물 5~7명 선제 조형
- 상태: 완료 (2026-03-04)
- 실행:
  - `python3 scripts/bootstrap_core_cast.py`
- 산출물:
  - `worldbible_refined_bundle_20260303/population/core_cast/NC-0001_P-0867.md`
  - `worldbible_refined_bundle_20260303/population/core_cast/NC-0002_P-1097.md`
  - `worldbible_refined_bundle_20260303/population/core_cast/NC-0003_P-0203.md`
  - `worldbible_refined_bundle_20260303/population/core_cast/NC-0004_P-3563.md`
  - `worldbible_refined_bundle_20260303/population/core_cast/NC-0005_P-0161.md`
  - `worldbible_refined_bundle_20260303/population/core_cast/NC-0006_P-2297.md`
  - `worldbible_refined_bundle_20260303/population/core_cast/NC-0007_P-0403.md`
  - `worldbible_refined_bundle_20260303/docs/core_cast_bootstrap_v1.md`
- 반영:
  - `population_slots.csv` 선정 7개 슬롯 `status=named`, `ch_id=NC-*` 반영
  - 대응 `P-*.yaml` 7개에 `status/ch_id` 보강
  - `python3 scripts/rebuild_character_index_v2.py` 재실행으로 `character_index_v2` 상태(3593/0/7) 반영

### Step 7. 첫 시뮬레이션 시나리오 결정 + master_map 갱신
- 시나리오 범위 확정 → world_bible 로딩 범위 결정
- master_map에 P-* 체계 반영
- community_map / layer_b / simulation_playbook 최종 검토

---

## 보류 중 (선행 작업 완료 후)

- Voice Pack 템플릿 갱신 (P-* 체계 반영)
- simulation_playbook에 온디맨드 생성 흐름 섹션 추가

### 처리 완료 메모
- 기존 CH-* 캐릭터 카드/보이스팩 체계 전면 폐기 완료 (2026-03-04)
  - 처리 방식: 혼동 방지를 위해 원본 영구 삭제
  - 활성 경로: `worldbible_refined_bundle_20260303/characters/`, `worldbible_refined_bundle_20260303/voice_packs/` 는 deprecated 스텁만 유지

---

## 참조 문서

| 문서 | 역할 |
|---|---|
| `character_population_methodology.md` | 빅5 배정 + 파생 지표 방법론 |
| `spec_sheet_v1.md` (v1.2) | 시스템 전체 설계 원칙 |
| `world_ops/README.md` | 세계관 변경 관리 프로세스 |
