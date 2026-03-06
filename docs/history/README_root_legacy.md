# Project Dream2

## Bootstrap

The first document to load for orchestration is:

- `worldbible_refined_bundle_20260303/docs/master_map.md`

This file is the single routing entrypoint for the live world bundle. Load it first, then open only the linked documents that are needed for the current task.

## Document Roles

- `worldbible_refined_bundle_20260303/docs/master_map.md`
  - First-read bootstrap document for execution and orchestration.
- `spec_sheet_v1.md`
  - High-level design and implementation intent.
- `PROJECT_ARCHITECTURE_MAP.md`
  - Human-oriented architecture snapshot of the current repository state.
- `대화 로그.txt`
  - Historical conversation record used to reconstruct design background.
- `world_ops/README.md`
  - Change-management process and execution gate rules.

## Working Rule

If there is a mismatch between historical/design documents and the live bundle, treat the difference as a change-management issue and resolve it through `world_ops`.
