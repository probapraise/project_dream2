#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
usage: new_quick_sim_run.sh <run_id>

example:
  bash scripts/sim/new_quick_sim_run.sh QSIM-20260310-002_board001_followup
EOF
}

if [[ $# -ne 1 ]]; then
  usage
  exit 1
fi

RUN_ID="$1"
if [[ "$RUN_ID" == *"/"* || "$RUN_ID" == *".."* ]]; then
  echo "[fail] invalid run_id: ${RUN_ID}"
  exit 1
fi

SCRIPT_PATH="$(readlink -f "${BASH_SOURCE[0]}")"
ROOT_DIR="$(cd "$(dirname "$SCRIPT_PATH")/../.." && pwd)"
RUN_DIR="${ROOT_DIR}/artifacts/quick_sims/${RUN_ID}"

if [[ -e "$RUN_DIR" ]]; then
  echo "[fail] already exists: ${RUN_DIR}"
  exit 1
fi

mkdir -p "${RUN_DIR}/inputs" "${RUN_DIR}/outputs"

cat > "${RUN_DIR}/brief.md" <<EOF
# ${RUN_ID}

- date: $(date +%F)
- status: drafting
- track: \`Quick Sim\`
- reflection_level: \`explore only\`
- board:
- seed_class:

## Objective
- 

## Success Check
- 
EOF

cat > "${RUN_DIR}/inputs/run_brief.md" <<'EOF'
# Run Brief

## Board
- 

## Seed Event
- 

## Intended Trigger
- 

## Guardrails
- META 금지
- raw live 문서 직접 투입 금지
- live 직접 반영 금지
- explore only
EOF

cat > "${RUN_DIR}/inputs/persona_bundles.md" <<'EOF'
# Persona Bundles

## P-XXXX
- background_type:
- dorm:
- grade:
- major:
- vocation:
- trait cue:
- interpretation:
EOF

cat > "${RUN_DIR}/outputs/thread_sample.md" <<'EOF'
# Thread Sample

주의:
- 이 문서는 explore용 조립본이다.
- 실제 상호 reply log가 아닐 수 있다.

## Seed Post

### 제목

### 본문

## Comment Flow

1. 
EOF

cat > "${RUN_DIR}/outputs/participant_notes.md" <<'EOF'
# Participant Notes

## Raw Outputs

### P-XXXX
- comment_1:
- comment_2:
- reaction_angle:

## Skeptic Review

- fit_score:
- issues:
- keep:
- tweak:
- verdict:
EOF

cat > "${RUN_DIR}/scorecard.md" <<'EOF'
# Scorecard

## Evaluation

| 항목 | 점수 | 메모 |
|---|---:|---|
| 역할 일관성 |  |  |
| 게시판 그럴듯함 |  |  |
| 다양성 |  |  |
| 누출 안전성 |  |  |
| 아이디어 밀도 |  |  |
| 속도 효율 |  |  |

## Aggregate

- average:
- provisional verdict:
EOF

cat > "${RUN_DIR}/summary.md" <<'EOF'
# Summary

## Result

## What We Learned

## Decision
EOF

echo "[ok] scaffolded quick sim run: ${RUN_DIR}"

