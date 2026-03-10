# 시뮬레이션 아키텍처 v2

작성일: 2026-03-10  
상태: adopted  
성격: current design authority

---

## 1. 결정 요약

현재 프로젝트의 시뮬레이션 기본 경로는 `Codex Quick Sim`이다.

- 기본값: `Quick Sim`
- fallback: `tuned API Sim`
- 금지: 근거 없이 매번 API부터 돌리는 운영

이 결정의 이유는 단순하다.

- Layer B / 낙서장 / 짧은 반응 / 내부자 유머 계열에서는 Quick Sim이 더 쓸 만했다.
- Quick Sim이 반응 결 다양성, 개념 비틀기, 후처리 속도에서 우세했다.
- API는 격리와 추적성은 강하지만, 기본 상태에서는 게시판 자연스러움이 약했고, 튜닝 후에도 다양성은 Quick Sim보다 좁았다.

따라서 시스템은 `API 기본 + Quick Sim 보조`가 아니라
`Quick Sim 기본 + API fallback`으로 재설계한다.

---

## 2. 새 기본 구조

```text
[작가 + 오케스트레이터]
  ├─ Primary: Quick Sim
  │   ├─ execution packet
  │   ├─ responder agents
  │   ├─ skeptic / combiner
  │   └─ explore artifact
  │
  └─ Fallback: API Sim
      ├─ compile view
      ├─ pre-injection gate
      ├─ gated worker
      ├─ output leak scan
      └─ official candidate artifact
```

핵심은 역할 분리다.

- Quick Sim은 `아이디어 생성기`
- API Sim은 `격리된 검증기`

---

## 3. 트랙 정의

### 3.1 Quick Sim

기본 경로다.

- 엔진: Codex 멀티 에이전트
- 산출물 위치: `artifacts/quick_sims/<run_id>/`
- 반영 등급: `explore only`
- 주용도:
  - Layer B 사건 탐색
  - 게시판 초반 댓글 흐름 샘플
  - 반응자 선발 논리 점검
  - 시드 문장 자극점 검토
  - 밈 후보 / 프레이밍 후보 발굴

### 3.2 API Sim

fallback 경로다.

- 엔진: gated API runner
- 산출물 위치: `artifacts/runs/<run_id>/`
- 반영 등급: `official candidate`
- 주용도:
  - hard isolation이 필요한 run
  - leak scan을 반드시 걸어야 하는 run
  - live board_state 승격 직전 검증
  - Quick Sim 결과가 마음에 들지 않아 재검증이 필요한 run
  - 반복성/추적성이 중요한 run

---

## 4. 기본 의사결정 규칙

### 4.1 시작 규칙

새 사건을 처음 돌릴 때는 무조건 `Quick Sim`부터 간다.

예외는 아래뿐이다.

- META가 강하게 걸린 사건
- CONFIDENTIAL 의존도가 높은 사건
- 처음부터 official candidate가 필요한 사건
- 작가가 직접 API 검증을 먼저 원한 경우

### 4.2 API fallback 트리거

아래 중 하나면 API Sim으로 올린다.

1. Quick Sim 결과가 마음에 들지 않음
2. 댓글 결이 너무 단조롭거나 설명체가 심함
3. leak risk가 의심됨
4. 해당 결과를 board_state promote 후보로 보고 싶음
5. 같은 seed를 격리된 환경에서 한 번 더 보고 싶음

### 4.3 promote 규칙

- Quick Sim 단독 결과는 live에 직접 반영하지 않는다.
- Quick Sim 결과는 작가 판단과 후속 API 검증 또는 수동 승인 루프로 넘긴다.
- live 반영 후보는 `API Sim` 또는 `작가 직접 승인한 Quick Sim 요약물`만 사용한다.

---

## 5. Quick Sim 기본 절차

1. `run_id` 생성
2. `artifacts/quick_sims/<run_id>/` 스캐폴드 생성
3. `inputs/run_brief.md` 작성
4. `inputs/persona_bundles.md` 작성
5. responder agents 실행
6. skeptic / combiner 실행
7. `outputs/thread_sample.md`, `scorecard.md`, `summary.md` 작성
8. 필요 시 API fallback 여부 판단

### Quick Sim 필수 산출물

- `brief.md`
- `inputs/run_brief.md`
- `inputs/persona_bundles.md`
- `outputs/thread_sample.md`
- `outputs/participant_notes.md`
- `scorecard.md`
- `summary.md`

---

## 6. API fallback 절차

1. execution view compile
2. pre-injection gate
3. tuned runner 실행
4. output leak scan
5. 필요 시 official candidate 판정

API는 더 이상 기본 경로가 아니다.  
`실패했을 때 쓰는 예비 수단`도 아니고,  
`격리와 검증이 필요할 때 올리는 상위 레인`으로 본다.

즉, 위상은 낮아졌지만 중요도는 여전히 높다.

---

## 7. 현재 구현 방침

### 7.1 지금 당장 유지

- `artifacts/quick_sims/`를 primary explore registry로 사용
- `artifacts/runs/`를 API fallback registry로 사용
- `simulation_playbook.md`는 Quick Sim 기본 경로를 우선 설명
- `sim_runner.py`는 API fallback worker로 유지

### 7.2 지금 당장 버리는 것

- "시뮬레이션은 기본적으로 API에서 돈다"는 전제
- Quick Sim을 단순 실험 또는 아이디어 메모 수준으로 보는 태도

### 7.3 지금 당장 필요한 것

- Quick Sim scaffold
- Quick Sim scorecard 규격
- tuned API diversity 보정
- Quick Sim용 최소 leak hygiene 규칙

---

## 8. 트랙별 강점

| 항목 | Quick Sim | API Sim |
|---|---|---|
| 속도 | 강함 | 약함 |
| 반응 다양성 | 강함 | 중간 |
| 게시판 자연스러움 | 강함 | 튜닝 시 중상 |
| 격리 | 약함 | 강함 |
| 추적성 | 중간 | 강함 |
| live 승격 전 검증 | 약함 | 강함 |
| 작가와의 인터랙션 | 강함 | 약함 |

---

## 9. 운영 원칙

- 기본은 Quick Sim이다.
- API는 fallback이지만, official candidate로 갈 때는 더 신뢰한다.
- Layer B 탐색은 Quick Sim을 우선한다.
- Layer A culture 승격이나 board_state promote 전에는 API 검증을 우선 고려한다.
- "기본 경로"와 "더 신뢰하는 경로"는 다를 수 있다.

이 시스템에서:

- 더 자주 쓰는 경로 = Quick Sim
- 더 엄격하게 검증하는 경로 = API Sim

---

## 10. 현재 판단

지금 시점의 최종 판단은 아래다.

- `Quick Sim`을 시스템 기본 경로로 채택한다.
- `tuned API Sim`은 fallback이자 검증 레인으로 유지한다.
- 앞으로의 비교는 `Quick Sim vs tuned API`를 기준으로 이어 간다.

## 11. 참조

- `docs/design/codex_quick_sim_v1.md`
- `world/live/docs/simulation_playbook.md`
- `world_ops/SIM_WRITING_ISOLATION.md`
- `artifacts/quick_sims/README.md`

