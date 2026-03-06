# simulation_state_index

- last_checked: 2026-03-06
- 이 문서는 bundle-relative 경로를 사용한다.
- 실행 게이트 산출물은 `runs/`(실제 위치: `artifacts/runs/`)에, 시뮬레이션 상태 스냅샷은 `board_states/`에 누적된다.

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

## Board state snapshots

- `board_states/simrun-001_cold_start.json`
- `board_states/simrun-002_pro_cold_start.json`
- `board_states/simrun-003_pro_thinking_cold_start.json`

## Update rule

- 새 RUN이 생성되면 최소 `call_spec`, `manifest`, `view`, 관련 gate/payload 경로를 이 문서에 추가한다.
- 실제 서사 상태 변경이 반영된 경우, 대응하는 `board_states/*.json` 또는 후속 apply 문서도 함께 연결한다.
