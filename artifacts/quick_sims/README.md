# Quick Sims

Codex 멀티 에이전트 기반 `Quick Sim`의 primary explore 산출물을 보관한다.

## 목적
- 정식 API 시뮬레이션 전에 시드 이벤트와 반응 분포를 빠르게 탐색한다.
- Layer B 문법, 게시판 초반 온도, 반응자 선발 논리를 가볍게 시험한다.
- 작가가 건질 만한 아이디어를 `explore only` 등급으로 압축한다.

## 비목적
- live 상태 직접 반영
- canon 확정
- board_state 자동 승격
- META 진실을 다루는 정식 시뮬레이션 대체

## 권장 구조

```text
artifacts/quick_sims/<run_id>/
  brief.md
  inputs/
  outputs/
  scorecard.md
  summary.md
```

## 운영 규칙
- 현재 기본 시뮬레이션 경로는 `Quick Sim`이다.
- Quick Sim 입력은 가능하면 execution view 기반 요약 패키지로 제한한다.
- Quick Sim 산출물은 기본적으로 `explore only`로 취급한다.
- 쓸만한 결과가 나와도 live 문서를 직접 수정하지 않는다.
- 필요 시 기존 leak scan 규칙을 재사용해 출력물을 검사한다.
- 정식 반영 후보는 별도로 Official Sim 또는 작가 승인 루프로 넘긴다.

## 참조
- 설계 문서: `docs/design/codex_quick_sim_v1.md`
- 정식 시뮬레이션 규칙: `world/live/docs/simulation_playbook.md`
- 격리 원칙: `world_ops/SIM_WRITING_ISOLATION.md`
