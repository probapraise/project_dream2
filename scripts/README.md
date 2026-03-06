# Scripts

실제 구현 스크립트는 기능군별 하위 디렉터리에 둔다.

- `population/`: 모집단 생성, 보정, 파생지표, 감사
- `indexes/`: 인덱스 재생성
- `ops/`: world_ops 케이스/게이트/감사
- `sim/`: 게이트 통과 후 호출되는 시뮬레이션 worker

시뮬레이션은 `python3 scripts/sim/sim_runner.py`를 직접 실행하지 않는다.
- 권장 진입점: `bash scripts/ops/world_ops_run_sim.sh ...`
- `sim_runner.py`는 `world_ops_pre_injection_gate.sh`가 만든 gated payload가 없으면 동작하지 않는 하위 실행기다.

루트 `scripts/`의 동일한 파일명은 legacy command 호환용 심볼릭 링크다.
