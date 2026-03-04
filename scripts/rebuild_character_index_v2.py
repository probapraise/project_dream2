#!/usr/bin/env python3
"""Rebuild character_index_v2 from population slots."""

from __future__ import annotations

import argparse
import csv
import math
from collections import Counter
from datetime import datetime
from pathlib import Path


ACTIVE_STATUSES = {"instantiated", "named"}
BACKGROUND_LABELS = {
    "signature_noble": "서명귀족",
    "common_noble": "일반귀족",
    "commoner": "평민(몰락귀족 편입)",
    "foreigner": "외국인",
    "nonhuman": "인외",
}

DORM_ORDER = (
    "비전관",
    "일반동(동관)",
    "일반동(서관)",
    "장학생동",
    "연구·탑동",
    "외국·인외동",
)


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    bundle_root = repo_root / "worldbible_refined_bundle_20260303"
    parser = argparse.ArgumentParser(description="Rebuild character_index_v2 from P-slot population")
    parser.add_argument(
        "--population-csv",
        type=Path,
        default=bundle_root / "population" / "population_slots.csv",
        help="Input population CSV path",
    )
    parser.add_argument(
        "--index-md",
        type=Path,
        default=bundle_root / "docs" / "character_index_v2.md",
        help="Output character_index_v2 markdown path",
    )
    parser.add_argument(
        "--pool-dir",
        type=Path,
        default=bundle_root / "docs" / "character_index_pools",
        help="Output directory for pool files",
    )
    return parser.parse_args()


def to_float(value: str) -> float:
    return float(value.strip())


def id_sort_key(pid: str) -> int:
    return int(pid.split("-")[1])


def write_id_file(path: Path, ids: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(ids) + ("\n" if ids else ""), encoding="utf-8")


def main() -> int:
    args = parse_args()
    args.index_md.parent.mkdir(parents=True, exist_ok=True)
    args.pool_dir.mkdir(parents=True, exist_ok=True)

    with args.population_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    total = len(rows)
    status_counts = Counter(row["status"] for row in rows)
    bg_counts = Counter(row["background_type"] for row in rows)
    dorm_counts = Counter(row.get("dorm", "") for row in rows if row.get("dorm"))

    # Provisional coordinate registry (tower/grade/motive are assigned at instantiation time).
    coord_counts = Counter(
        ("UNASSIGNED", "UNASSIGNED", row["background_type"], "UNASSIGNED") for row in rows
    )
    coord_occupied = Counter(
        ("UNASSIGNED", "UNASSIGNED", row["background_type"], "UNASSIGNED")
        for row in rows
        if row["status"] in ACTIVE_STATUSES
    )

    # Active reverse indexes (instantiated+ only)
    active_rows = [r for r in rows if r["status"] in ACTIVE_STATUSES]
    active_ids = sorted((r["id"] for r in active_rows), key=id_sort_key)

    nfc_top_count = math.ceil(total * 0.20)
    dt_top_count = math.ceil(total * 0.10)

    nfc_top = sorted(rows, key=lambda r: (-to_float(r["NFC"]), id_sort_key(r["id"])))[:nfc_top_count]
    dt_top = sorted(rows, key=lambda r: (-to_float(r["DT"]), id_sort_key(r["id"])))[:dt_top_count]

    nfc_top_ids = [r["id"] for r in nfc_top]
    dt_top_ids = [r["id"] for r in dt_top]

    # Small special pools helpful for first simulation.
    nonhuman_ids = sorted(
        (r["id"] for r in rows if r["background_type"] == "nonhuman"),
        key=id_sort_key,
    )
    foreigner_ids = sorted(
        (r["id"] for r in rows if r["background_type"] == "foreigner"),
        key=id_sort_key,
    )

    write_id_file(args.pool_dir / "active_instantiated_ids.txt", active_ids)
    write_id_file(args.pool_dir / "nfc_top20_ids.txt", nfc_top_ids)
    write_id_file(args.pool_dir / "dt_top10_ids.txt", dt_top_ids)
    write_id_file(args.pool_dir / "nonhuman_ids.txt", nonhuman_ids)
    write_id_file(args.pool_dir / "foreigner_ids.txt", foreigner_ids)

    generated_at = datetime.now().strftime("%Y-%m-%d")
    lines: list[str] = []
    lines.append("# character_index_v2 (population bootstrap)")
    lines.append("")
    lines.append(f"- generated_at: {generated_at}")
    lines.append(f"- source_csv: `{args.population_csv}`")
    lines.append("- total_p_slots: 3600")
    lines.append("- ssot: `population/P-*.yaml` + `population/population_slots.csv`")
    lines.append("- note: 기존 CH-* 카드/보이스팩 체계는 2026-03-04부로 폐기 완료(영구 삭제). 활성 캐릭터 체계는 `population/P-*`만 사용.")
    lines.append("")
    lines.append("## 1) Status Registry")
    lines.append("| status | count |")
    lines.append("|---|---:|")
    for status in ("uninstantiated", "instantiated", "named"):
        lines.append(f"| {status} | {status_counts.get(status, 0)} |")
    lines.append("")
    lines.append("## 2) Background Distribution")
    lines.append("| background_type | label | count | ratio |")
    lines.append("|---|---|---:|---:|")
    for key in ("signature_noble", "common_noble", "commoner", "foreigner", "nonhuman"):
        count = bg_counts.get(key, 0)
        ratio = (count / total) * 100 if total else 0.0
        lines.append(f"| `{key}` | {BACKGROUND_LABELS[key]} | {count} | {ratio:.1f}% |")
    lines.append("")
    if dorm_counts:
        lines.append("## 2.1 Dorm Distribution")
        lines.append("| dorm | count | ratio |")
        lines.append("|---|---:|---:|")
        for dorm in DORM_ORDER:
            count = dorm_counts.get(dorm, 0)
            if count == 0:
                continue
            ratio = (count / total) * 100 if total else 0.0
            lines.append(f"| {dorm} | {count} | {ratio:.1f}% |")
        for dorm in sorted(k for k in dorm_counts.keys() if k and k not in DORM_ORDER):
            count = dorm_counts[dorm]
            ratio = (count / total) * 100 if total else 0.0
            lines.append(f"| {dorm} | {count} | {ratio:.1f}% |")
        lines.append("")
    lines.append("## 3) Coordinate Occupancy Registry (v0 init)")
    lines.append("- 좌표 스키마: `tower x grade_track x background_type x motivation_archetype`")
    lines.append("- 현재 초기화 단계에서는 `tower/grade_track/motivation_archetype = UNASSIGNED`로 유지한다.")
    lines.append("- 실제 점유는 `instantiated` 이상에서만 증가한다.")
    lines.append("")
    lines.append("| tower | grade_track | background_type | motivation_archetype | slots | occupied(instantiated+) | available(uninstantiated) |")
    lines.append("|---|---|---|---|---:|---:|---:|")
    for _, _, bg_key, _ in sorted(coord_counts.keys(), key=lambda t: t[2]):
        total_slots = coord_counts[("UNASSIGNED", "UNASSIGNED", bg_key, "UNASSIGNED")]
        occupied = coord_occupied[("UNASSIGNED", "UNASSIGNED", bg_key, "UNASSIGNED")]
        available = total_slots - occupied
        lines.append(
            f"| UNASSIGNED | UNASSIGNED | `{bg_key}` | UNASSIGNED | {total_slots} | {occupied} | {available} |"
        )
    lines.append("")
    lines.append("## 4) Reverse Indexes")
    lines.append("### 4.1 Active Index (instantiated 이상만)")
    lines.append(f"- active_count: {len(active_ids)}")
    lines.append(f"- pool_file: `docs/character_index_pools/active_instantiated_ids.txt`")
    lines.append("")
    lines.append("### 4.2 Candidate Pools (P-* 전체에서 사전 계산)")
    lines.append(f"- NFC 상위 20%: {len(nfc_top_ids)}명 (`docs/character_index_pools/nfc_top20_ids.txt`)")
    lines.append(f"- DT 상위 10%: {len(dt_top_ids)}명 (`docs/character_index_pools/dt_top10_ids.txt`)")
    lines.append(f"- 인외 풀: {len(nonhuman_ids)}명 (`docs/character_index_pools/nonhuman_ids.txt`)")
    lines.append(f"- 외국인 풀: {len(foreigner_ids)}명 (`docs/character_index_pools/foreigner_ids.txt`)")
    lines.append("")
    lines.append("샘플 ID:")
    lines.append(f"- NFC top20 first 10: {', '.join(nfc_top_ids[:10])}")
    lines.append(f"- DT top10 first 10: {', '.join(dt_top_ids[:10])}")
    lines.append("")
    lines.append("## 5) Step 5 DoD Check")
    lines.append("- [x] 빅5/파생지표 기반 초기 레지스트리 생성")
    lines.append("- [x] 좌표 점유 레지스트리 스키마 초기화")
    lines.append("- [x] 반응자 선별용 역색인 파일 생성")
    lines.append("- [x] 기존 CH-* 162개 + 보이스팩 체계 폐기 완료(2026-03-04, 영구 삭제)")
    lines.append("")
    lines.append("## 6) Rebuild Command")
    lines.append("```bash")
    lines.append("python3 scripts/rebuild_character_index_v2.py")
    lines.append("```")

    args.index_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"rows={total}")
    print(f"index_md={args.index_md}")
    print(f"pool_dir={args.pool_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
