# 다음 작업 목록

최종 업데이트: 2026-03-04

---

## 즉시 실행 가능 (순서 있음)

### Step 1. population_grammar.md 작성
- 위치: `worldbible_refined_bundle_20260303/docs/population_grammar.md`
- 내용:
  - 탑별 인구 비율 (청탑/보라탑/황탑/백탑/녹탑/적탑/흑탑)
  - 배경 유형 분포 (서명귀족 / 평민 / 몰락귀족 / 외국인 / 인외 등)
  - 학년별 분포
  - 집단 간 구조적 긴장 (비전관 vs 일반동, 탑별 문화 충돌 등)
  - 시드 유형별 반응 민감도 맵 (빅5 좌표 구간 → 반응 예측)
- 참조: `character_population_methodology.md`, `worldbible_refined_bundle_20260303/world_bible/WB-0015_academy_bible.md`

### Step 2. P-* 슬롯 생성 스크립트 작성
- 위치: `scripts/generate_population_slots.py`
- 기능:
  - 정규분포 샘플링으로 P-0001~P-3600 빅5 수치 생성
  - 학술원 보정 적용 (methodology 문서 기준)
  - YAML 형식으로 개별 파일 출력 또는 단일 CSV 출력
- 출력 위치: `worldbible_refined_bundle_20260303/population/` (신규 디렉터리)
- 참조: `character_population_methodology.md` Section 3

### Step 3. 파생 지표 산출 배치 프롬프트 설계
- 위치: `world_ops/templates/population_derive_prompt.md`
- 내용:
  - 입력: P-* ID + 빅5 수치
  - 출력: DT / NFC / SM 수치 (0.01~0.99)
  - 공식 및 잔차 처리 방침 (methodology 문서 기준)
- Batch API 호출 스펙 포함

### Step 4. 파생 지표 산출 실행
- Step 2 산출물을 입력으로 Batch API 병렬 호출
- 토큰 소모 큼 → 별도 세션에서 수행
- 완료 후 각 슬롯 파일에 `derived` 섹션 기입

### Step 5. character_index 좌표 레지스트리 초기화
- 위치: `worldbible_refined_bundle_20260303/docs/character_index_v2.md` 갱신
- Step 4 완료 후 빅5/파생 지표 기반 초기 레지스트리 구성
- 기존 162개 CH-* 카드는 quarantine 처리 또는 삭제

### Step 6. 핵심 인물 5~7명 선제 조형
- 주인공 주변 고정 CH-* 캐릭터
- P-* 슬롯에서 적합한 좌표 선택 후 풀 카드 작성
- 온라인 성향 레이어를 사전 작성하는 유일한 예외 케이스

### Step 7. 첫 시뮬레이션 시나리오 결정 + master_map 갱신
- 시나리오 범위 확정 → world_bible 로딩 범위 결정
- master_map에 P-* 체계 반영
- community_map / layer_b / simulation_playbook 최종 검토

---

## 보류 중 (선행 작업 완료 후)

- 기존 162개 CH-* 카드 최종 처리 (quarantine 이동 또는 삭제)
  - 현재 `worldbible_refined_bundle_20260303/characters/` 에 존재
  - Step 4 완료 후 결정
- Voice Pack 템플릿 갱신 (P-* 체계 반영)
- simulation_playbook에 온디맨드 생성 흐름 섹션 추가

---

## 참조 문서

| 문서 | 역할 |
|---|---|
| `character_population_methodology.md` | 빅5 배정 + 파생 지표 방법론 |
| `spec_sheet_v1.md` (v1.2) | 시스템 전체 설계 원칙 |
| `world_ops/README.md` | 세계관 변경 관리 프로세스 |
