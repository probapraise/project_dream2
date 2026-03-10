# Codex Quick Sim 설계안 v1.0

작성일: 2026-03-10
상태: superseded by `simulation_architecture_v2.md`
성격: 초기 제안서 / 역사 문서 (`live SSOT 아님`)

> 2026-03-10 후속 결정:
> 이 문서는 Quick Sim을 실험 트랙으로 제안하던 1차 문서다.
> 현재 채택된 운영 기준은 `docs/design/simulation_architecture_v2.md`이며,
> 거기서 `Quick Sim 기본 / API fallback` 구조로 결정이 갱신되었다.

---

## 1. 개요

### 목적
Codex 멀티 에이전트를 활용해, 기존 API 기반 정식 시뮬레이션보다 훨씬 빠른 탐색형 시뮬레이션(`Quick Sim`) 레인을 추가한다.

### 핵심 판단
- 기존의 `API 직접 호출 = 정식 시뮬레이션` 결정은 유지한다.
- 다만 그 결정이 겨냥했던 문제를 다시 분해하면, 전부가 아니라 일부는 Codex 내부 멀티 에이전트로 대체 가능하다.
- 프로젝트 목적은 "완벽한 역할극" 자체가 아니라, **작가가 건질 만한 창발 아이디어를 빠르고 안전하게 확보하는 것**이다.

### 이번 문서의 결론
- `Quick Sim`은 **정식 시뮬레이션 대체재가 아니다.**
- 대신 `explore only` 성격의 빠른 탐색 레인으로는 충분히 유망하다.
- 따라서 아키텍처는 `API 단일 레인`에서 `Quick Sim + Official Sim` 2트랙으로 확장하는 쪽이 맞다.

---

## 2. 재평가 배경

### 기존 API 분리 결정의 이유
기존 스펙 문서의 판단은 타당했다.

- Codex/Claude Code 서브 에이전트는 시스템 프롬프트 수준에서 코딩 어시스턴트 성격이 강하다.
- 페르소나 역할극만 시키려 해도 개발자 문법으로 회귀하는 경우가 있었다.
- API 직접 호출은 세션 분리, 파라미터 제어, 순정 모델 투입이 가능해 정식 시뮬레이션에 유리했다.

### 새롭게 생긴 변수
최근 Codex 운영 사례를 보면, 프로젝트/에이전트 지시를 세밀하게 설계해 특정 캐릭터성 또는 화행 경향을 꽤 강하게 유도하는 방식이 실사용되고 있다.

이 변화가 뜻하는 것은 다음 하나다.

- `Codex는 절대 역할극을 못 한다`가 아니라
- `Codex는 정식 시뮬레이션 엔진으로 바로 쓰기엔 위험하지만, 제한된 탐색 작업에서는 충분히 쓸 수 있다`

### 문제를 다시 정의하면
이 프로젝트에서 중요한 것은 아래 다섯 가지다.

1. 역할 일관성
2. META/CONFIDENTIAL 격리
3. 반응 다양성과 게시판 그럴듯함
4. 산출물 추적 가능성
5. 작가 입장에서 아이디어가 실제로 건지는가

Codex 멀티 에이전트는 1, 3, 5에서는 승산이 있다.
반면 2, 4는 현재 API 파이프라인이 더 강하다.

따라서 대체가 아니라 분업이 맞다.

---

## 3. 목표와 비목표

### 목표
- Layer B 밈/문법 탐색을 빠르게 돌린다.
- 특정 사건에 어떤 반응군이 붙을지 가설을 빠르게 본다.
- 게시판 톤, 댓글 온도, 프레이밍 후보를 대량 탐색한다.
- 작가가 정식 시뮬레이션 전에 시드 이벤트를 거칠게 다듬을 수 있게 한다.
- 정식 시뮬레이션을 돌릴 가치가 있는 사건만 추려낸다.

### 비목표
- Quick Sim 결과를 바로 canon 또는 live 상태로 승격하지 않는다.
- Quick Sim 결과를 Layer A 문화 확정 근거로 직접 쓰지 않는다.
- Quick Sim으로 META를 다루는 장면을 처리하지 않는다.
- Quick Sim만으로 recurring cast 선정, board_state promote, VFP 확정을 하지 않는다.

---

## 4. 아키텍처 결정

### 4.1 최종 구조

```text
[작가 + 오케스트레이터]
  ├─ Quick Sim (Codex multi-agent, explore only)
  └─ Official Sim (API direct call, official candidate)
```

### 4.2 역할 분리

| 트랙 | 엔진 | 주용도 | 반영 등급 |
|---|---|---|---|
| Quick Sim | Codex 멀티 에이전트 | 아이디어 탐색, 반응 가설, 밈 후보 발굴 | explore only |
| Official Sim | API 직접 호출 | 정식 반영 후보, board_state 승격 후보 | official candidate |

### 4.3 왜 2트랙인가
- Quick Sim은 속도와 인터랙션이 강점이다.
- Official Sim은 격리와 추적성이 강점이다.
- 두 레인은 서로 경쟁 관계가 아니라, `선별기`와 `검증기` 관계로 보는 게 맞다.

---

## 5. Quick Sim 사용 범위

### 적합한 작업
- "이 사건이면 어떤 종류의 학생이 먼저 반응하나?" 같은 초기 반응 가설 탐색
- 게시판 초반 5~20댓글 정도의 분위기 샘플
- Layer B 문법과 충돌하는지, 혹은 새 밈 후보가 생기는지 탐색
- 시드 이벤트 문장 자체의 자극 포인트 점검
- named/core cast가 아닌 일반 모집단 반응 샘플링
- 반응자 풀 선발 논리의 대략적 검증

### 부적합한 작업
- META 진실이 걸린 사건
- CONFIDENTIAL 의존도가 높은 사건
- 정식 board_state 갱신 직전 검증
- 반복 재현성이 중요한 평가 run
- 비용을 들여 다수 페르소나를 안정적으로 분산 실행해야 하는 대규모 run

---

## 6. 입력 규칙

### 6.1 가장 중요한 원칙
Quick Sim도 `raw live 문서 던지기`로 돌리면 안 된다.

반드시 아래 원칙을 유지한다.

- 입력은 execution view 기반 요약 패키지로 제한
- agent에게 `world_bible/...` 같은 원본 경로를 직접 열게 하지 않음
- META 문서 직접 주입 금지
- 필요한 CONFIDENTIAL만 명시 허용
- run 목적과 금지 규칙을 별도 명시

### 6.2 persona 구성 방식
`agent.md`, `soul.md` 같은 이름 자체에 의존하지 않는다.

Codex에서 실제로 의미 있는 것은:
- `AGENTS.md` 계열 지시
- agent role config
- turn prompt에 주는 persona bundle

따라서 persona는 다음처럼 다룬다.

1. 글로벌/프로젝트 `AGENTS.md`
  - 작업 규율, 출력 형식, 금지 규칙
2. Quick Sim 공통 지시
  - 게시판 반응자로서 행동하되, 개발 조언/메타 해설 금지
3. 인물별 persona bundle
  - 배경축, 말투, 금기, 이해관계, 현재 노출 정보

즉, `soul.md`는 마법 파일명이 아니라 `persona bundle source text`로 취급한다.

### 6.3 입력 패키지 권장 구조

```text
[run brief]
- sim objective
- board type
- seed event
- allowed knowledge
- forbidden knowledge
- expected output format

[world slice]
- execution view excerpt

[persona bundle]
- slot id
- social position
- likely motive
- speech style
- trigger points

[board grammar]
- relevant Layer A/Layer B hints
```

---

## 7. 에이전트 역할 설계

### 7.1 최소 구성
- `dispatcher`
  - run 목적 제시, 참여자 배치, 결과 수합
- `responders` 3~5명
  - 각자 하나의 반응자 시점 수행
- `skeptic`
  - META 누출, 과도한 설명체, 게시판 톤 이탈 탐지

### 7.2 권장 동작
- responder끼리 긴 대화를 시키기보다, 각자 독립 반응을 먼저 뽑는다.
- dispatcher가 이를 조합해 thread flow를 재구성한다.
- skeptic이 마지막에 "이 반응이 인간 게시판처럼 보이는가"만 검수한다.

### 7.3 이유
Codex 멀티 에이전트는 공식적으로도 read-heavy 병렬 작업에 특히 유리하다.
따라서 "에이전트들이 즉석에서 장시간 상호작용"하는 구조보다, "독립 샘플을 병렬 생성 후 오케스트레이션"하는 구조가 더 안정적이다.

---

## 8. 산출물 규격

### 8.1 저장 위치 제안
정식 run과 섞지 않기 위해 별도 경로를 사용한다.

```text
artifacts/quick_sims/<run_id>/
  brief.md
  inputs/
  outputs/
  scorecard.md
  summary.md
```

### 8.2 필수 산출물
- `brief.md`
  - 목적, seed, 허용 지식, 금지 지식
- `outputs/thread_sample.md`
  - 게시판 샘플 출력
- `outputs/participant_notes.md`
  - 어떤 축의 반응이 나왔는지 요약
- `scorecard.md`
  - 평가표
- `summary.md`
  - 작가가 건질 포인트만 압축

### 8.3 반영 규칙
- Quick Sim 산출물은 기본적으로 `explore`
- live 문서 직접 갱신 금지
- 쓸만한 결과가 나오면, 그것을 바탕으로 Official Sim 재실행 또는 작가 승인 루프로 넘긴다

---

## 9. 안전 규칙

### 9.1 hard rule
- META 입력 금지
- live 직접 수정 금지
- Quick Sim 결과의 자동 promote 금지
- named/core cast의 새 정식 앵커를 Quick Sim만으로 확정 금지

### 9.2 운영 rule
- 가능하면 기존 `output_leak_scan` 규칙을 Quick Sim 산출물에도 재사용한다.
- Quick Sim에서 hard leak가 나면 해당 프롬프트 조합은 폐기한다.
- Quick Sim은 `작가 판단 전 탐색 노트`로만 유통한다.

---

## 10. 평가 프로토콜

### 10.1 비교 방식
같은 시드 이벤트를 `Official Sim baseline`과 `Quick Sim`에 모두 넣고 비교한다.

### 10.2 권장 seed 세트
- Layer B 감도가 높은 사건 2개
- 순수 정보 전달형 사건 1개
- 갈등 유발 사건 1개
- 애매한 떡밥형 사건 1개

총 5개 정도면 1차 판단이 가능하다.

### 10.3 점수표

| 항목 | 질문 | 점수 |
|---|---|---|
| 역할 일관성 | 반응자가 개발자/해설자처럼 튀지 않는가 | 1~5 |
| 게시판 그럴듯함 | 실제 커뮤니티 반응처럼 읽히는가 | 1~5 |
| 다양성 | 반응이 한 목소리로 수렴하지 않는가 | 1~5 |
| 누출 안전성 | META/운영 정보가 새지 않는가 | 1~5 |
| 아이디어 밀도 | 작가가 건질 포인트가 있는가 | 1~5 |
| 속도 효율 | API 대비 체감 속도 이득이 큰가 | 1~5 |

### 10.4 통과 기준
- `누출 안전성` 5점이 아닌 run은 탈락
- `아이디어 밀도` 평균 4.0 이상이면 채택 가치 높음
- 전체 평균 3.8 이상이면 Quick Sim 유지
- 전체 평균 4.2 이상이면 운영 레인으로 승격 검토

---

## 11. 도입 원칙

### 11.1 현재 단계에서의 결정
주의:
- 아래 항목은 **초기 제안 당시 판단**이다.
- 현재 운영 기준은 이 섹션이 아니라 `simulation_architecture_v2.md`를 따른다.

- Quick Sim은 즉시 실험해 볼 가치가 있다.
- 하지만 live 플레이북의 정식 기본 경로를 바꾸지는 않는다.

### 11.2 승격 조건
아래가 충족될 때만 live 운영 문서에 편입한다.

- 파일럿 5-run 이상 수행
- hard leak 0건
- 작가 체감상 아이디어 효율이 Official Sim 대비 분명히 높음
- 결과를 official candidate로 넘길 때 손실이 적음

### 11.3 실패 조건
아래 중 하나라도 반복되면 Quick Sim은 보조 수단으로만 남긴다.

- 개발자 말투 회귀가 빈번함
- 반응자 다양성이 낮음
- 게시판보다 회의록처럼 출력됨
- META/운영 정보가 자주 섞임

---

## 12. 구현 우선순위

### Phase 0. 문서화
- 이 설계 문서 작성
- `next_steps.md`에 파일럿 과제 추가

### Phase 1. 수동 파일럿
- seed 5개 선정
- execution view 축약본 수동 생성
- Codex 멀티 에이전트로 각 run 수행
- scorecard 기록

### Phase 2. 반자동화
- Quick Sim 입력 패키지 템플릿 정리
- 산출물 디렉토리 규약 확정
- leak scan 재사용 여부 확인

### Phase 3. 승격 판단
- 점수표 누적
- Official Sim 대비 효용 비교
- 통과 시 live `simulation_playbook`에 보충 규칙 추가

---

## 13. 현재 판단 요약

- API 기반 Official Sim은 유지한다.
- Codex 멀티 에이전트 Quick Sim은 충분히 시도할 가치가 있다.
- 다만 "역할극 엔진 교체"가 아니라 "탐색 속도 향상용 보조 레인"으로 보는 게 정확하다.
- 이 프로젝트에서 중요한 것은 역할극 순도보다, **재미 있는 창발을 빠르고 안전하게 건져내는 운영 구조**다.
