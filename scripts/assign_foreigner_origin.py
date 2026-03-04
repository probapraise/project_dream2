#!/usr/bin/env python3
"""
foreigner 출신 P-* 슬롯 origin 배정 스크립트

[배정 논리]
  벨쿠란 왕국(ARC 벨라리온 25%+ 강국) 기준 교류 빈도 추론:
  - 메인: ARC 벨라리온 인접 왕국·공국권 → 지리적 근접·외교 협정·학위 상호 인정
  - 나머지: SAH/NOR/ARC 원거리/출신불명 균등 배분

[origin 코드]
  ARC-인접왕국권  : 50명 — ARC 대륙 인접 왕국·공국 (메인)
  SAH-울카자르권  : 18명 — 사막 대륙 상단·도시국가, 면허·학술 인증 목적
  NOR-스카르벨권  : 18명 — 북방 인류권 소왕국
  ARC-원거리소국권: 17명 — ARC 내 원거리 독립 소공국·자유시
  출신불명        : 17명 — 귀화·신원 비공개 (망명·첩보·혼혈 등 서사 여백)

[OST 마사토라 제외]
  관문제국 쇄국 정책 → 유학생 파견 불가. 의도적 배제.

[재현성]
  SEED=42 고정.
"""

import csv
import re
import sys
from pathlib import Path

import numpy as np
import yaml

SEED = 42

ORIGIN_QUOTAS = [
    ("ARC-인접왕국권",   50),
    ("SAH-울카자르권",   18),
    ("NOR-스카르벨권",   18),
    ("ARC-원거리소국권", 17),
    ("출신불명",         17),
]

assert sum(q for _, q in ORIGIN_QUOTAS) == 120, "origin 합계 != 120"


def expand_quotas(quotas: list) -> list:
    result = []
    for label, count in quotas:
        result.extend([label] * count)
    return result


# ---------------------------------------------------------------------------
# YAML 갱신
# ---------------------------------------------------------------------------

_ORIGIN_RE = re.compile(r"^origin: .*$", re.MULTILINE)


def update_yaml_origin(path: Path, origin: str) -> None:
    text = path.read_text(encoding="utf-8")
    new_line = f"origin: {origin}"
    if _ORIGIN_RE.search(text):
        text = _ORIGIN_RE.sub(new_line, text, count=1)
    else:
        # origin 줄이 없으면 vocation 줄 뒤에 삽입
        text = re.sub(
            r"(^vocation: .+$)",
            r"\1\n" + new_line,
            text,
            count=1,
            flags=re.MULTILINE,
        )
    path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# CSV 갱신
# ---------------------------------------------------------------------------

def update_csv(csv_path: Path, origin_map: dict[str, str]) -> None:
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = list(reader.fieldnames or [])

    if "origin" not in fieldnames:
        fieldnames.append("origin")

    updated = 0
    for row in rows:
        pid = row.get("id", "")
        if pid in origin_map:
            row["origin"] = origin_map[pid]
            updated += 1

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"  CSV 갱신: {updated}개")


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    pop_dir   = repo_root / "worldbible_refined_bundle_20260303" / "population"
    csv_path  = pop_dir / "population_slots.csv"

    # foreigner 슬롯 수집
    yaml_files = sorted(pop_dir.glob("P-*.yaml"))
    foreigner_paths: list[Path] = []
    for yf in yaml_files:
        try:
            with yf.open(encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if data and data.get("background_type") == "foreigner":
                foreigner_paths.append(yf)
        except Exception:
            pass

    print(f"foreigner 슬롯: {len(foreigner_paths)}개")
    if len(foreigner_paths) != 120:
        print(f"  경고: 예상 120, 실제 {len(foreigner_paths)}", file=sys.stderr)

    # 이미 배정된 경우 확인
    with foreigner_paths[0].open(encoding="utf-8") as f:
        sample = yaml.safe_load(f)
    if sample.get("origin", "UNASSIGNED") != "UNASSIGNED":
        print("경고: 이미 origin이 배정되어 있습니다.", file=sys.stderr)
        return 1

    rng = np.random.default_rng(SEED)

    # 슬롯 인덱스 셔플 후 origin 배정
    indices = list(range(len(foreigner_paths)))
    rng.shuffle(indices)

    origin_seq = expand_quotas(ORIGIN_QUOTAS)
    assigned: list[tuple[Path, str]] = []
    for rank, i in enumerate(indices):
        assigned.append((foreigner_paths[i], origin_seq[rank]))

    # YAML 갱신
    print("YAML 갱신 중...")
    origin_map: dict[str, str] = {}
    for path, origin in assigned:
        update_yaml_origin(path, origin)
        # id 추출
        pid = path.stem
        origin_map[pid] = origin
    print(f"  완료: {len(assigned)}개")

    # CSV 갱신
    print("CSV 갱신 중...")
    update_csv(csv_path, origin_map)

    # 통계
    from collections import Counter
    counter = Counter(origin for _, origin in assigned)
    print("\n[origin 배정 결과]")
    for label, quota in ORIGIN_QUOTAS:
        actual = counter[label]
        flag = "" if actual == quota else " !"
        print(f"  {label:16s}: {actual:3d} / {quota}{flag}")
    print(f"  {'합계':16s}: {sum(counter.values()):3d} / 120")

    print("\n완료.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
