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
    "청탑 기숙사",
    "황탑 기숙사",
    "적탑 기숙사",
    "녹탑 기숙사",
    "백탑 기숙사",
    "자탑 기숙사",
    "흑탑 기숙사",
    "기사동",
    "신전동군",
)

MANA_COLOR_ORDER = ("청", "황", "적", "녹", "백", "자", "흑", "UNASSIGNED")
GRADE_ORDER = ("1학년", "2학년", "3학년", "4학년", "연구과정", "UNASSIGNED")


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[2]
    bundle_root = repo_root / "world/live"
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


def order_index(value: str, ordered: tuple[str, ...]) -> int:
    try:
        return ordered.index(value)
    except ValueError:
        return len(ordered)


def coord_sort_key(coord: tuple[str, str, str, str]) -> tuple[int, int, str, str]:
    mana_color, grade, background_type, motivation = coord
    return (
        order_index(mana_color, MANA_COLOR_ORDER),
        order_index(grade, GRADE_ORDER),
        background_type,
        motivation,
    )


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

    # Coordinate registry from current slot fields.
    coord_counts = Counter(
        (
            row.get("mana_color", "") or "UNASSIGNED",
            row.get("grade", "") or "UNASSIGNED",
            row["background_type"],
            "UNASSIGNED",
        )
        for row in rows
    )
    coord_occupied = Counter(
        (
            row.get("mana_color", "") or "UNASSIGNED",
            row.get("grade", "") or "UNASSIGNED",
            row["background_type"],
            "UNASSIGNED",
        )
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
    lines.append(f"- total_p_slots: {total}")
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
    lines.append("## 3) Coordinate Occupancy Registry (v1)")
    lines.append("- 좌표 스키마: `mana_color x grade x background_type x motivation_archetype`")
    lines.append("- 현재 데이터에는 `motivation_archetype` 필드가 없어 `UNASSIGNED`로 고정한다.")
    lines.append("- 실제 점유는 `instantiated` 이상에서만 증가한다.")
    lines.append("")
    lines.append("| mana_color | grade | background_type | motivation_archetype | slots | occupied(instantiated+) | available(uninstantiated) |")
    lines.append("|---|---|---|---|---:|---:|---:|")
    for coord in sorted(coord_counts.keys(), key=coord_sort_key):
        mana_color, grade, bg_key, motivation = coord
        total_slots = coord_counts[coord]
        occupied = coord_occupied[coord]
        available = total_slots - occupied
        lines.append(
            f"| {mana_color} | {grade} | `{bg_key}` | {motivation} | {total_slots} | {occupied} | {available} |"
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
    lines.append("python3 scripts/indexes/rebuild_character_index_v2.py")
    lines.append("```")

    args.index_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"rows={total}")
    print(f"index_md={args.index_md}")
    print(f"pool_dir={args.pool_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
