# Project Dream2

## Bootstrap

The first document to load for orchestration is:

- `world/live/docs/master_map.md`

This file is the single routing entrypoint for the live world bundle. Load it first, then open only the linked documents that are needed for the current task.

## Repository Layout

- `docs/`
  - Human-facing design, architecture, handoff, and history documents.
- `artifacts/`
  - Generated batch outputs and other non-SSOT work artifacts.
  - `writing/` and `runs/` live here physically.
- `scripts/`
  - Organized by function: `population/`, `indexes/`, `ops/`, `sim/`.
  - Legacy root-level script paths remain as compatibility symlinks.
  - Simulation entrypoint is `scripts/ops/world_ops_run_sim.sh`; `scripts/sim/sim_runner.py` is a gated worker, not a direct user entrypoint.
- `world/`
  - Stable home for the live bundle and archived world-side assets.
  - `live/` is canonical. `archive/` stores deprecated/quarantined material.
- `world_ops/`
  - Change-management process, templates, and per-change case logs.
- `worldbible_refined_bundle_20260303/`
  - Legacy compatibility symlink that points to `world/live/`.

## Document Roles

- `world/live/docs/master_map.md`
  - First-read bootstrap document for execution and orchestration.
- `docs/design/spec_sheet_v1.md`
  - Secondary design reference for high-level intent. Do not use it as the first routing document when the live bundle says otherwise.
- `docs/architecture/PROJECT_ARCHITECTURE_MAP.md`
  - Human-oriented architecture snapshot of the current repository state.
- `docs/handoff/next_steps.md`
  - Session handoff and queued follow-up work.
- `docs/history/대화 로그.txt`
  - Historical conversation record used to reconstruct design background.
- `world_ops/README.md`
  - Change-management process and execution gate rules.

## Working Rule

If there is a mismatch between historical/design documents and the live bundle, treat the difference as a change-management issue and resolve it through `world_ops`.
