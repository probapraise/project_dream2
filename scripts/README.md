# Scripts

실제 구현 스크립트는 기능군별 하위 디렉터리에 둔다.

- `population/`: 모집단 생성, 보정, 파생지표, 감사
- `indexes/`: 인덱스 재생성
- `ops/`: world_ops 케이스/게이트/감사
- `sim/`: Quick Sim 스캐폴드와 API fallback 시뮬레이션 worker
- `writing/`: 에피소드 집필 폴더 스캐폴드와 집필 보조 스크립트

population 관련 주요 커맨드:
- `python3 scripts/population/add_student_fields.py --dry-run`
- `python3 scripts/population/add_student_fields.py --profile world/live/population/profiles/current_term_snapshot_v1.yaml`
- `python3 scripts/population/audit_population_invariants.py`

population 운영 원칙:
- `add_student_fields.py`는 세계관 정본 빌더가 아니라 `current-term snapshot` 재생성기다.
- 고정 분포는 코드가 아니라 `world/live/population/profiles/current_term_snapshot_v1.yaml`에서 관리한다.
- 장기 설정 변경은 `WB-0015` 같은 SSOT를 먼저 수정한 뒤 snapshot profile을 맞춘다.
- narrative frontier가 pre-academy여도 snapshot은 academy layer를 유지한다. 현재 canon 상태는 `world/live/docs/narrative_state.md`, `world/live/population/core_cast/*.md`에서 읽는다.

집필 관련 주요 커맨드:
- `bash scripts/writing/new_episode_scaffold.sh <episode_id>`
- `bash scripts/writing/new_canon_patch.sh <episode_id> <new_canon_filename>`
- `bash scripts/writing/post_canon_sync.sh <episode_id>`
- `python3 scripts/writing/audit_live_sync.py`
- `python3 scripts/writing/audit_prompt_packet.py <episode_id>`
- `python3 scripts/writing/audit_semantic_continuity.py <episode_id>`
- `python3 scripts/writing/refresh_canon_metadata.py <episode_id>`

semantic audit 운영 원칙:
- 기본 모드: hard contradiction만 실패
- `--strict-warn`: carry 누락/placeholder 같은 경고도 실패 처리
- 주요 semantic source: `memory_tiers/recent.md`, `current_arc.md`, `entity_registry.md`, `knowledge_state_registry.md`, `access_control_matrix.md`

시뮬레이션 기본 경로는 `Quick Sim`이다.
- 스캐폴드: `bash scripts/sim/new_quick_sim_run.sh <run_id>`
- 산출물 경로: `artifacts/quick_sims/<run_id>/`

API fallback은 `python3 scripts/sim/sim_runner.py`를 직접 실행하지 않는다.
- fallback 진입점: `bash scripts/ops/world_ops_run_sim.sh ...`
- `sim_runner.py`는 `world_ops_pre_injection_gate.sh`가 만든 gated payload가 없으면 동작하지 않는 API 하위 실행기다.

루트 `scripts/`의 동일한 파일명은 legacy command 호환용 심볼릭 링크다.
