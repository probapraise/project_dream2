# simulation_state_index

- last_checked: 2026-03-10
- 이 문서는 bundle-relative 경로를 사용한다.
- 실행 게이트 산출물은 `runs/`(실제 위치: `artifacts/runs/`)에, Quick Sim 산출물은 `quick_sims/`(실제 위치: `artifacts/quick_sims/`)에, 시뮬레이션 상태 스냅샷은 `board_states/`에 누적된다.

## Quick Sim artifacts (primary explore lane)

- `quick_sims/QSIM-20260310-001_human_backend/`
  - brief: `quick_sims/QSIM-20260310-001_human_backend/brief.md`
  - thread sample: `quick_sims/QSIM-20260310-001_human_backend/outputs/thread_sample.md`
  - scorecard: `quick_sims/QSIM-20260310-001_human_backend/scorecard.md`
  - compare memo: `quick_sims/QSIM-20260310-001_human_backend/comparison_api_vs_quick.md`

## Registered runs

- RUN-PHASE3-SMOKE
  - call_spec: `runs/RUN-PHASE3-SMOKE/calls/SIM-R01-0001.env`
  - manifest: `runs/RUN-PHASE3-SMOKE/manifests/SIM-R01-0001.manifest.md`
  - view: `runs/RUN-PHASE3-SMOKE/views/SIM-R01-0001.view.md`
  - gates:
    - `runs/RUN-PHASE3-SMOKE/gates/SIM-R01-0001_pre_injection_gate.md`
    - `runs/RUN-PHASE3-SMOKE/gates/SIM-R01-0001_output_leak_scan.md`
  - payload: `runs/RUN-PHASE3-SMOKE/payloads/SIM-R01-0001.gated.txt`
- RUN-PHASE3-LEGACY
  - call_spec: `runs/RUN-PHASE3-LEGACY/calls/SIM-R01-0001.env`
  - manifest: `runs/RUN-PHASE3-LEGACY/manifests/SIM-R01-0001.manifest.md`
  - view: `runs/RUN-PHASE3-LEGACY/views/SIM-R01-0001.view.md`
  - gates:
    - `runs/RUN-PHASE3-LEGACY/gates/SIM-R01-0001_pre_injection_gate.md`
    - `runs/RUN-PHASE3-LEGACY/gates/SIM-R01-0001_output_leak_scan.md`
  - payload: `runs/RUN-PHASE3-LEGACY/payloads/SIM-R01-0001.gated.txt`
- RUN-20260304-TEMPLATE-SMOKE
  - call_spec: `runs/RUN-20260304-TEMPLATE-SMOKE/calls/SIM-R01-0001.env`
  - manifest: `runs/RUN-20260304-TEMPLATE-SMOKE/manifests/SIM-R01-0001.manifest.md`
  - view: `runs/RUN-20260304-TEMPLATE-SMOKE/views/SIM-R01-0001.view.md`
- RUN-AUDIT-006
  - call_spec: `runs/RUN-AUDIT-006/calls/SIM-R01-0001.env`
  - manifest: `runs/RUN-AUDIT-006/manifests/SIM-R01-0001.manifest.md`
  - view: `runs/RUN-AUDIT-006/views/SIM-R01-0001.view.md`
- RUN-QSIM-COMPARE-20260310-001
  - call_spec: `runs/RUN-QSIM-COMPARE-20260310-001/calls/SIM-R01-0001.env`
  - manifest: `runs/RUN-QSIM-COMPARE-20260310-001/manifests/SIM-R01-0001.manifest.md`
  - view: `runs/RUN-QSIM-COMPARE-20260310-001/views/SIM-R01-0001.view.md`
  - gates:
    - `runs/RUN-QSIM-COMPARE-20260310-001/gates/SIM-R01-0001_pre_injection_gate.md`
    - `runs/RUN-QSIM-COMPARE-20260310-001/gates/SIM-R01-0001_output_leak_scan.md`
  - payload: `runs/RUN-QSIM-COMPARE-20260310-001/payloads/SIM-R01-0001.gated.txt`
- RUN-QSIM-COMPARE-20260310-002
  - call_spec: `runs/RUN-QSIM-COMPARE-20260310-002/calls/SIM-R01-0001.env`
  - manifest: `runs/RUN-QSIM-COMPARE-20260310-002/manifests/SIM-R01-0001.manifest.md`
  - view: `runs/RUN-QSIM-COMPARE-20260310-002/views/SIM-R01-0001.view.md`
  - gates:
    - `runs/RUN-QSIM-COMPARE-20260310-002/gates/SIM-R01-0001_pre_injection_gate.md`
    - `runs/RUN-QSIM-COMPARE-20260310-002/gates/SIM-R01-0001_output_leak_scan.md`
  - payload: `runs/RUN-QSIM-COMPARE-20260310-002/payloads/SIM-R01-0001.gated.txt`

## Board state snapshots

- `board_states/simrun-001_cold_start.json`
- `board_states/simrun-002_pro_cold_start.json`
- `board_states/simrun-003_pro_thinking_cold_start.json`

## Update rule

- 새 Quick Sim이 생성되면 최소 `brief`, `thread_sample`, `scorecard` 경로를 이 문서에 추가한다.
- 새 RUN이 생성되면 최소 `call_spec`, `manifest`, `view`, 관련 gate/payload 경로를 이 문서에 추가한다.
- 실제 서사 상태 변경이 반영된 경우, 대응하는 `board_states/*.json` 또는 후속 apply 문서도 함께 연결한다.
