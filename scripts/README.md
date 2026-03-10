# Scripts

실제 구현 스크립트는 기능군별 하위 디렉터리에 둔다.

- `population/`: 모집단 생성, 보정, 파생지표, 감사
- `indexes/`: 인덱스 재생성
- `ops/`: world_ops 케이스/게이트/감사
- `sim/`: Quick Sim 스캐폴드와 API fallback 시뮬레이션 worker
- `writing/`: 에피소드 집필 폴더 스캐폴드와 집필 보조 스크립트

시뮬레이션 기본 경로는 `Quick Sim`이다.
- 스캐폴드: `bash scripts/sim/new_quick_sim_run.sh <run_id>`
- 산출물 경로: `artifacts/quick_sims/<run_id>/`

API fallback은 `python3 scripts/sim/sim_runner.py`를 직접 실행하지 않는다.
- fallback 진입점: `bash scripts/ops/world_ops_run_sim.sh ...`
- `sim_runner.py`는 `world_ops_pre_injection_gate.sh`가 만든 gated payload가 없으면 동작하지 않는 API 하위 실행기다.

루트 `scripts/`의 동일한 파일명은 legacy command 호환용 심볼릭 링크다.
