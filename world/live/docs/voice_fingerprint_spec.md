# Voice Fingerprint Specification

## 정의

Voice Fingerprint(VFP)는 instantiated/named 인물의 **개별 말투 지문**이다.
Big5/파생지표가 "왜 이런 성격인가"를 정의한다면, VFP는 "실제로 어떻게 말하는가"를 확정한다.

---

## 핵심 원칙

> 말투는 성격에서 파생되지만, 성격만으로 재현되지 않는다.

- Big5 좌표가 같아도 말투는 다를 수 있다 (어휘 선택, 문장 길이, 말버릇은 좌표 밖의 영역)
- VFP는 인물이 **처음 발화한 시점**에 추출되고, 이후 모든 등장에서 **주입**된다
- `house_rules.md`는 **전역** 문체 규칙의 작성 소스다. `style_selection_vN.md`는 **회차별 선택 패턴**의 작성 소스다. 실제 주입 문서는 둘을 합친 `episode_style_constitution_vN.md`다. VFP는 **개별 인물** 규칙이다
- Layer A/B 문화는 **상황적** 말투 변조이다. VFP는 **기질적** 말투 기저이다

---

## 생성 시점

| 인물 상태 | VFP 존재 여부 | 말투 처리 방식 |
|---|---|---|
| `uninstantiated` | 없음 | Big5 + population_grammar만으로 추론 |
| `instantiated` | **생성** | 첫 발화 후 VFP 추출 → 슬롯에 기록 |
| `named` (core_cast) | **필수** | core_cast 카드에 voice_fingerprint 섹션 포함 |

---

## VFP 레코드 포맷

```yaml
voice_fingerprint:
  version: 1
  extracted_from:
    - "출처1 (예: ep000_prologue/canon/revision_v1)"
    - "출처2 (예: simrun-003)"

  # 1. 문장 구조
  sentence_structure: >
    문장 패턴 기술. 평서문/의문문 비율, 종결 어미 경향,
    접속사 사용 빈도, 체언 종결 여부 등.
  avg_sentence_length: short / medium / long

  # 2. 어휘 레지스터
  register: >
    전반적 톤 기술. 격식/비격식, 건조함/감정적, 은유 체계 등.
  signature_words:
    - "이 인물이 반복적으로 사용하는 단어/표현"
  forbidden_words:
    - "이 인물이 절대 사용하지 않을 단어/표현"

  # 3. 화행 패턴
  speech_acts:
    assertion: "단정/주장 방식"
    question: "질문 방식 (빈도, 수사적 여부)"
    refusal: "거절 방식"
    humor: "유머 방식 (있다면)"
    emotional_leak: "감정이 새어 나올 때의 패턴 (있다면)"

  # 4. 대화 상대별 레지스터 분기
  register_shifts:
    - context: "상황/상대 유형"
      shift: "말투가 어떻게 변하는지"

  # 5. 앵커 대사 (대표 발화 2~4개)
  anchor_lines:
    - "실제 작품/시뮬에서 나온 대표 대사"

  # 6. 내면 서술 톤 (1인칭 시점 인물만 해당)
  inner_voice: >
    내면 독백의 톤과 패턴. 서술자로서의 목소리.
    (3인칭 시점 또는 대화만 있는 인물은 생략)
```

---

## 3단계 운영 파이프라인

### Stage 1: 추출 (Post-Sim / Post-Writing)

인물이 처음 발화한 산출물에서 VFP를 추출한다.

```
[산출물 완료]
  → 등장 인물 목록 추출
  → 각 인물의 발화/서술 분리
  → 오케스트레이터: VFP 초안 생성
  → 작가 검토/수정
  → core_cast 카드 또는 P-* YAML에 voice_fingerprint 섹션 기입
```

**추출 기준:**
- core_cast (named): 오케스트레이터가 초안 → 작가 승인 → 카드에 기록
- instantiated (시뮬 소환): 오케스트레이터가 자동 추출 → 간략 포맷으로 P-* YAML에 기록
- uninstantiated: 추출하지 않음

**추출 소스 우선순위:**
1. 작가 수정본 (revision) — 최우선
2. 시뮬레이션 로그 (simrun) — 보조
3. 모델 초안 (draft) — 참고만 (작가 검수 전이므로 신뢰도 낮음)

### Stage 2: 주입 (Pre-Sim / Pre-Writing)

재등장 시 VFP를 프롬프트에 주입한다.

```
[실행 준비]
  → compile_execution_views (기존)
  → 등장 인물 목록 확정
  → 각 인물의 VFP 존재 여부 확인
      → 있음: VFP를 프롬프트 컨텍스트에 주입
      → 없음: Big5 + population_grammar만 주입 (현행)
  → pre_injection_gate (기존)
  → 모델 호출
```

**주입 포맷 (프롬프트 내):**

```
[VOICE: {인물명} ({ID})]
톤: {register 요약}
문장: {sentence_structure 요약}
서명 어휘: {signature_words}
금지 표현: {forbidden_words}
화행: {speech_acts 요약}
상대별 변화: {register_shifts 요약}
앵커 대사: {anchor_lines}
```

core_cast는 전체 VFP를, instantiated는 축약 VFP를 주입한다.

### Stage 3: 검증 + 갱신 (Post-Output)

산출물에서 Voice Drift를 감지하고, 필요 시 VFP를 갱신한다.

```
[모델 출력 수신]
  → output_leak_scan (기존)
  → voice_consistency_check (신규)
      등장 인물별:
        1. 발화 추출
        2. VFP 대비 이탈 검출
           - forbidden_words 사용 여부
           - sentence_structure 급변 여부
           - signature_words 완전 부재 여부
           - register_shifts 미작동 여부
        3. 판정: PASS / DRIFT_WARNING / DRIFT_CRITICAL
  → 결과 보고
```

**판정 기준:**

| 판정 | 조건 | 조치 |
|---|---|---|
| PASS | 이탈 항목 0~1개, 경미 | 그대로 진행 |
| DRIFT_WARNING | 이탈 항목 2개 이상, 또는 forbidden_word 사용 | 작가에게 플래그, 수정 권고 |
| DRIFT_CRITICAL | 앵커 대사 톤과 정반대, 또는 전면적 레지스터 변경 | 재생성 권고 |

**VFP 갱신 규칙:**
- 작가가 의도적으로 말투를 변경한 경우 → version 올리고 VFP 업데이트
- 모델이 멋대로 변경한 경우 → 기각, 기존 VFP 유지
- 시뮬 반복으로 새로운 패턴이 안정적으로 관찰될 경우 → 작가 승인 후 VFP에 추가

---

## 기존 아키텍처 정합

| 기존 요소 | VFP와의 관계 |
|---|---|
| Big5 + derived | VFP의 **원인**. 왜 이런 말투인지의 심리적 근거 |
| episode_style_constitution | `house_rules`와 `style_selection`을 합쳐 만든 실제 주입 문체 규약. VFP는 **개별** 인물 규칙이며, 충돌 시 `episode_style_constitution`이 우선 |
| population_grammar | uninstantiated 인물의 말투 **예측**. VFP는 instantiated 인물의 말투 **확정** |
| Layer A/B culture | **상황적** 말투 변조. VFP는 **기질적** 말투 기저. 동시 적용 |
| core_cast 카드 | VFP 섹션이 카드 내에 포함됨 |
| P-* YAML | instantiated 전환 시 간략 VFP 필드 추가 |
| simulation_playbook | Stage 2/3이 기존 실행 게이트 체인에 편입 |

---

## 우선순위 적용 순서 (충돌 해소)

프롬프트 주입 시 여러 레이어가 겹칠 때의 우선순위:

```
1. episode_style_constitution (최상위 — 이번 화 문체 헌법)
2. voice_fingerprint (개별 인물 — 기질적 말투)
3. Layer A/B culture (게시판/커뮤니티 — 상황적 변조)
4. Big5 + population_grammar (기저 성격 — VFP 없을 때 폴백)
```

---

## 변경 이력

| 날짜 | 변경 내용 |
|---|---|
| 2026-03-05 | v1.0 최초 작성. NC-0001 키리온 VFP 추출 완료. |
