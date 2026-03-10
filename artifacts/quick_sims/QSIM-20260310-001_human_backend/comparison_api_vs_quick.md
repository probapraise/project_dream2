# Comparison — Quick Sim vs API Sim

## Compared Runs

- Quick Sim:
  - [thread_sample.md](/home/dlwhdgus/project_dream2/artifacts/quick_sims/QSIM-20260310-001_human_backend/outputs/thread_sample.md)
  - [scorecard.md](/home/dlwhdgus/project_dream2/artifacts/quick_sims/QSIM-20260310-001_human_backend/scorecard.md)
- API Sim (baseline):
  - [simrun-qsim-compare-001.md](/home/dlwhdgus/project_dream2/artifacts/runs/RUN-QSIM-COMPARE-20260310-001/outputs/simrun-qsim-compare-001.md)
  - [SIM-R01-0001_output_leak_scan.md](/home/dlwhdgus/project_dream2/artifacts/runs/RUN-QSIM-COMPARE-20260310-001/gates/SIM-R01-0001_output_leak_scan.md)
- API Sim (BOARD-001 tuned):
  - [simrun-qsim-compare-002.md](/home/dlwhdgus/project_dream2/artifacts/runs/RUN-QSIM-COMPARE-20260310-002/outputs/simrun-qsim-compare-002.md)
  - [SIM-R01-0001_output_leak_scan.md](/home/dlwhdgus/project_dream2/artifacts/runs/RUN-QSIM-COMPARE-20260310-002/gates/SIM-R01-0001_output_leak_scan.md)

## Important Caveat

이 비교는 세 갈래를 함께 본다.

- Codex Quick Sim
- 현재 공식 API runner baseline
- `BOARD-001 낙서장` 전용으로 prompt/interaction을 튜닝한 API run

즉, 순수 모델 대결이 아니라 다음 세 요소가 함께 섞여 있다.

- 엔진 차이
- 프롬프트/실행 구조 차이
- board-specific tuning 유무

특히 baseline API runner는 본래 `Layer A cold-start` 구조에 더 가깝다.
이번 tuned run은 `scripts/sim/sim_runner.py`에 `thread_reaction` 모드를 추가한 뒤,
같은 4명을 넣고 `낙서장` 반응 전용 지침으로 다시 돌린 결과다.

## Side-by-Side Read

### Quick Sim가 더 좋았던 점
- thread 조립 감각이 더 자연스러웠다.
- 반응 결 차이가 더 또렷했다.
  - 구조 해설형
  - 메타 농담형
  - 짧은 조롱형
  - 분위기 부스터형
- `낙서장 품앗이`, `군중지성 화덕`, `문전박대 감성`, `옆방 선배 말투`처럼
  낙서장식 비틀기가 더 잘 나왔다.
- 산출물을 skeptic이 바로 다듬을 수 있어서 최종 usable sample이 빨리 나온다.

### API Sim baseline가 더 좋았던 점
- 한 캐릭터가 한 번에 더 긴 발화를 뽑아 주어 raw 재료량은 많다.
- 실행뷰, gate, leak scan까지 붙어 있어 추적성과 안전성은 더 강하다.
- 같은 4명을 넣었을 때도 기본 세계관 role 유지 자체는 무너지지 않았다.

### API Sim baseline에서 아쉬웠던 점
- 출력이 게시판 로그보다 `개별 응답 보고서`에 가까웠다.
- 1라운드 3명 반응이 서로 꽤 비슷하게 수렴했다.
- `[게시글 3에 대한 댓글]`, `작성자:` 같은 표식이 출력에 그대로 섞였다.
  - 이는 게시판 자연스러움을 직접 깎는다.
- 문장이 길고 설명적이라 낙서장의 날것 톤은 Quick Sim보다 약했다.

### API Sim tuned가 좋아진 점
- 8개 댓글 흐름이 나와 Quick Sim과 비교 단위가 비슷해졌다.
- `인간 지피티`, `추론 high`, `후만 바셀린 SOTA` 같은 낙서장 표면어는 확실히 더 자연스럽게 붙었다.
- baseline의 포맷 bleed가 사라졌다.
- 짧은 raw comment만 뽑히면서 익명 게시판 느낌은 baseline보다 확실히 강해졌다.

### API Sim tuned의 남은 한계
- 반응이 한 축으로 너무 강하게 수렴했다.
  - 거의 전부 `인간 지피티`
  - `추론 high`
  - `대기열`
- 개별 인물 차이는 살아 있지만, 아이디어의 방향은 Quick Sim보다 덜 벌어진다.
- 낙서장 톤은 더 거칠어졌지만, 개념 비틀기나 구조 읽기 다양성은 오히려 줄었다.

## Score Sketch

| 항목 | Quick Sim | API baseline | API tuned | 메모 |
|---|---:|---:|---:|---|
| 역할 일관성 | 4.0 | 4.0 | 4.2 | tuned API도 학생 role 유지가 안정적이었다. |
| 게시판 그럴듯함 | 4.0 | 3.0 | 4.0 | tuned API는 baseline의 포맷 bleed를 거의 제거했다. |
| 다양성 | 3.5 | 3.0 | 3.0 | tuned API는 톤은 좋아졌지만 반복 밈 수렴이 더 강했다. |
| 누출 안전성 | 5.0 | 5.0 | 5.0 | API 두 run 모두 leak scan 통과. |
| 아이디어 밀도 | 4.0 | 3.5 | 3.7 | tuned API는 표면어는 좋아졌지만 개념 다양성은 Quick Sim이 우세했다. |
| 속도 체감 | 5.0 | 2.5 | 2.5 | API는 여전히 네트워크/실행 체인 비용이 크다. |

## Verdict

이번 비교로 결론이 조금 바뀌었다.

- baseline API는 Quick Sim보다 확실히 밀렸다.
- 하지만 `BOARD-001` 전용으로 prompt와 interaction을 튜닝한 API는
  Quick Sim과 `표면 톤` 면에서는 거의 동급까지 올라왔다.
- 다만 최종적으로는 Quick Sim이 아직도 조금 더 유리했다.
  - 이유: 반응 결 다양성
  - 이유: 개념 비틀기 밀도
  - 이유: 후처리 속도

반대로 tuned API의 강점도 분명하다.

- 격리
- 추적성
- 공식 반영 전 검증 체인
- board-specific tuning 후의 안정적 표면 톤

따라서 현재 판단은 다음이 맞다.

- Layer B 탐색 초안: Quick Sim 우세
- Layer B 톤을 유지한 정식 격리 run: tuned API도 충분히 후보
- 정식 검증/격리: API Sim 우세

## Follow-up

이번 비교로 보인 다음 과제는 명확하다.

1. tuned API에 `rough diversity`를 더 주는 규칙을 넣어 반복 밈 수렴을 줄인다.
2. Quick Sim에는 격리/평가 체인을 조금 더 얹는다.
3. 그 다음 비교부터는 `Quick Sim vs tuned API`를 주력 비교축으로 삼는다.
