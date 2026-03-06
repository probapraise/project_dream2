# Population Derive Prompt (DT / NFC / SM)

작성일: 2026-03-04
용도: `P-*` 슬롯의 빅5(`O/C/E/A/N`)에서 파생 지표(`DT/NFC/SM`)를 산출하는 배치 실행 템플릿

## 1) 시스템 프롬프트(권장)
아래 문구를 배치 요청의 `system`에 넣는다.

```text
You are a deterministic trait-derivation engine.
Task: derive DT, NFC, SM from Big5 values using the provided formulas.
Rules:
1) Keep all outputs in [0.01, 0.99].
2) Return numeric values with 2 decimals.
3) Include intermediate values (base, residual, clipped) for auditability.
4) Preserve the input id exactly.
5) Output JSON only (no prose).
```

## 2) 사용자 프롬프트(요청 본문 템플릿)
아래 템플릿에서 `${...}`만 치환한다.

```text
[INPUT]
id: ${id}
b5:
  O: ${O}
  C: ${C}
  E: ${E}
  A: ${A}
  N: ${N}

[FORMULAS]
DT_base  = -0.50*A - 0.35*C + 0.25*N + 0.20*E - 0.05*O
NFC_base =  0.45*O + 0.30*C - 0.15*N + 0.05*E + 0.05*A
SM_base  =  0.40*E + 0.15*O + 0.10*A - 0.10*C - 0.20*N

[RESIDUAL POLICY]
- Draw residual-like offsets for diversity, but keep them small:
  eps_DT  in [-0.45, 0.45]  (target sigma ~0.15)
  eps_NFC in [-0.36, 0.36]  (target sigma ~0.12)
  eps_SM  in [-0.39, 0.39]  (target sigma ~0.13)
- If uncertain, use 0.00.

[POST PROCESS]
DT  = clip(DT_base  + eps_DT ,  0.01, 0.99)
NFC = clip(NFC_base + eps_NFC,  0.01, 0.99)
SM  = clip(SM_base  + eps_SM ,  0.01, 0.99)

[OUTPUT SCHEMA]
{
  "id": "P-0001",
  "b5": { "O": 0.65, "C": 0.62, "E": 0.50, "A": 0.58, "N": 0.50 },
  "calc": {
    "DT_base": 0.00,
    "NFC_base": 0.00,
    "SM_base": 0.00,
    "eps_DT": 0.00,
    "eps_NFC": 0.00,
    "eps_SM": 0.00
  },
  "derived": { "DT": 0.01, "NFC": 0.01, "SM": 0.01 }
}
```

## 3) 배치 입력(JSONL) 스펙 예시
벤더별 배치 API 형식에 맞게 필드명은 조정한다.
아래는 `custom_id + 요청 body` 구조 예시다.

```json
{"custom_id":"derive-P-0001","method":"POST","url":"/v1/responses","body":{"model":"gpt-5-mini","input":[{"role":"system","content":[{"type":"input_text","text":"<SYSTEM_PROMPT>"}]},{"role":"user","content":[{"type":"input_text","text":"<USER_PROMPT_WITH_P_0001>"}]}],"response_format":{"type":"json_object"}}}
```

입력 레코드 규칙:
- `custom_id`: `derive-{P-ID}` 고정
- 한 줄(JSON object) = 한 슬롯
- 총 3,600줄

## 4) 배치 실행 절차(운영)
1. `population_slots.csv`를 읽어 JSONL 배치 입력 생성
2. 배치 작업 제출
3. 완료 후 출력 JSONL 다운로드
4. `custom_id` 기준으로 원본 슬롯과 조인
5. 각 `P-*.yaml`의 `derived` 섹션 갱신

실행 커맨드(로컬 자동화):

```bash
# 1) 요청 JSONL 생성 (3,600건)
python3 scripts/population/build_population_derive_batch_jsonl.py --force

# 2) (외부) Batch API 제출/완료 후 결과 JSONL 확보
#    예: artifacts/batch/population_derive_output_from_agents.jsonl

# 3) 결과 반영 (YAML + CSV 동시 갱신)
python3 scripts/population/apply_population_derived_results.py \
  --batch-output-jsonl artifacts/batch/population_derive_output_from_agents.jsonl
```

## 5) 검증 규칙
- 필수:
  - 모든 슬롯 `derived.DT/NFC/SM` 존재
  - 값 범위 `0.01 <= x <= 0.99`
  - 소수점 2자리
- 통계 점검(권장):
  - `DT`, `NFC`, `SM` 평균/표준편차 리포트 생성
  - 극단값(0.01, 0.99) 과다 여부 점검

## 6) 실패/재시도 정책
- JSON 파싱 실패: 해당 `custom_id`만 재요청
- 스키마 누락: 1회 자동 재요청 후 수동 검수 큐 이동
- 범위 위반: 클리핑 후 `adjusted=true` 플래그를 감사 로그에 남김

## 7) 참조
- `docs/design/character_population_methodology.md` (4.2, 4.3)
- `scripts/population/generate_population_slots.py`
