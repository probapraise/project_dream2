#!/usr/bin/env python3
"""Instantiate 7 core cast profiles from P-slot population.

What this script does:
1) Selects seven P-* slots with deterministic score matching.
2) Marks selected rows as status=named in population_slots.csv.
3) Writes ch_id for selected rows (NC-0001..NC-0007).
4) Ensures selected P-*.yaml files include status/ch_id.
5) Writes core cast cards under population/core_cast/.
6) Writes a summary markdown in docs/.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


WEIGHTS = {
    "DT": 4.0,
    "NFC": 2.2,
    "SM": 2.2,
    "C": 1.8,
    "E": 1.4,
    "A": 1.4,
    "N": 1.2,
    "O": 1.0,
}

TOWER_DORMS = {
    "청탑 기숙사",
    "황탑 기숙사",
    "적탑 기숙사",
    "녹탑 기숙사",
    "백탑 기숙사",
    "보라탑 기숙사",
    "흑탑 기숙사",
}


@dataclass(frozen=True)
class Profile:
    core_id: str
    name: str
    role: str
    background_type: str
    dorm: str
    target: dict[str, float]
    relation_to_mc: str
    world_anchor: str
    desire: str
    fear: str
    flaw: str
    secret: str
    posting_signature: str
    trigger_topics: str
    avoid_topics: str
    anonymity_preference: str
    activity_pattern: str
    lore_rationale: str
    narrative_use: str


PROFILES: tuple[Profile, ...] = (
    Profile(
        core_id="NC-0001",
        name="레비안 루사르트",
        role="비전관 규율 블록의 집행자",
        background_type="signature_noble",
        dorm="비전관",
        target={"O": 0.60, "C": 0.74, "E": 0.56, "A": 0.30, "N": 0.76, "DT": 0.14, "NFC": 0.52, "SM": 0.22},
        relation_to_mc="주인공의 검색/인용 체계를 통제 장치로 묶으려는 1차 라이벌",
        world_anchor="ORG-ARC-HOU-023 루사르트 자작가, 감시선문장(Watch Line)",
        desire="비전관-감찰 라인이 학내 출입권/열람권 규칙을 독점하도록 만드는 것",
        fear="주인공이 로그 인덱싱을 표준화해 감시선 운용 내역의 역추적을 가능하게 만드는 것",
        flaw="모든 관계를 위반 여부와 증거 등급으로 환원해 인간적 완충을 잃는다",
        secret="가문 내부 계승 경쟁에서 밀려 학내 실적만으로 정치적 생존을 시도 중",
        posting_signature="조문/규정 번호와 타임스탬프를 먼저 제시한 뒤 판결문처럼 결론을 낸다",
        trigger_topics="무단 열람, 출입권 우회, 통금 예외, 감찰 로그 누락",
        avoid_topics="사적인 감정 고백형 스레드, 순수 취미 대화",
        anonymity_preference="준실명 계정 선호(권위 확보 목적)",
        activity_pattern="사건 직후보다 1~2시간 뒤 로그가 모인 시점에 강한 글을 올린다",
        lore_rationale="루사르트 가문의 학술원 운용 메모(통금/출입권 충돌 축)와 직접 결합되는 캐릭터",
        narrative_use="초기 시즌의 '규율 vs 공론장' 축을 안정적으로 점화한다",
    ),
    Profile(
        core_id="NC-0002",
        name="이델 그라비온",
        role="증거전 포렌식 브로커",
        background_type="signature_noble",
        dorm="비전관",
        target={"O": 0.74, "C": 0.82, "E": 0.44, "A": 0.62, "N": 0.38, "DT": 0.02, "NFC": 0.80, "SM": 0.28},
        relation_to_mc="주인공의 기술을 '위험하지만 쓸모 있는 공공 도구'로 보는 조건부 동맹",
        world_anchor="ORG-ARC-HOU-007 그라비온 백작가, 저울인장문장(Seal & Scale)",
        desire="진위감정의 표준 절차를 학내 분쟁의 기본 인프라로 고정하는 것",
        fear="감정 결과가 정치적으로 소비되어 가문 신뢰도가 도구화되는 것",
        flaw="중립을 지키려다 결정적 순간에 선택을 미루는 경향",
        secret="일부 고위층의 의뢰를 비공개로 수행한 이력이 있어 약점으로 잡힐 수 있다",
        posting_signature="긴 문장보다 체크리스트와 증거 사슬을 짧게 나열한다",
        trigger_topics="위조 의혹, 발췌 맥락 절단, 출처 미기재 폭로",
        avoid_topics="근거 없는 인신공격형 여론몰이",
        anonymity_preference="반실명(실명 힌트는 두되 직함은 숨김)",
        activity_pattern="초기 루머 단계에는 침묵, 증거가 2개 이상 모이면 개입",
        lore_rationale="그라비온 가문의 '증거가 없으면 없다' 축을 주인공의 LMM 인덱스와 접속한다",
        narrative_use="법적 진실과 여론 진실이 갈라지는 장면에서 축을 잡아준다",
    ),
    Profile(
        core_id="NC-0003",
        name="마엘 렌포드",
        role="각인학파 실험 파트너",
        background_type="common_noble",
        dorm="ANY_TOWER",
        target={"O": 0.80, "C": 0.86, "E": 0.50, "A": 0.56, "N": 0.42, "DT": 0.03, "NFC": 0.82, "SM": 0.30},
        relation_to_mc="주인공의 프로토타입을 현장 실험 가능한 스펙으로 고도화하는 핵심 조력자",
        world_anchor="7탑 기숙사군 공방 라인, 룬공학/아카이브 교차 프로젝트",
        desire="각인학파를 실전 툴체인으로 부활시켜 '쓸모없는 학파' 낙인을 벗기는 것",
        fear="실험 실패가 학파 말소 명분으로 사용되는 것",
        flaw="완성도를 올리려다 릴리즈 타이밍을 놓친다",
        secret="주인공 없이도 성과를 내고 싶다는 경쟁심을 숨기고 있다",
        posting_signature="실험 로그, 변수 표, 재현 절차를 붙인 기술형 글",
        trigger_topics="재현 불가 주장, 조작 의혹, 벤치마크 왜곡",
        avoid_topics="정치 진영 싸움, 인물 중심 흑색선전",
        anonymity_preference="필명 고정(실명 비공개), 로그 서명은 철저히 남김",
        activity_pattern="밤샘 실험 뒤 새벽 시간대에 집중적으로 글을 올린다",
        lore_rationale="주인공의 기술 노선(각인학파 재부상)을 서사적으로 밀어주는 필수 엔지니어 포지션",
        narrative_use="플랫폼 기능이 실제 사건 해결로 연결되는 증거를 만들어낸다",
    ),
    Profile(
        core_id="NC-0004",
        name="리안 벨로크",
        role="학내 여론전 플레이어",
        background_type="common_noble",
        dorm="ANY_NON_VISION",
        target={"O": 0.62, "C": 0.46, "E": 0.84, "A": 0.38, "N": 0.66, "DT": 0.10, "NFC": 0.44, "SM": 0.52},
        relation_to_mc="주인공 이슈를 밈화해 판을 키우지만, 필요하면 즉시 등을 돌리는 가변 동맹",
        world_anchor="학생회 공보 라인 주변 인맥, 기숙사권역 여론 확산 네트워크",
        desire="자신이 만든 프레임이 학내 공식 의제로 승격되는 것",
        fear="관심의 중심에서 밀려 존재감이 소멸되는 것",
        flaw="확산 속도를 우선해 사실 검증을 건너뛴다",
        secret="초기 몇 차례 바이럴은 외부 의뢰를 받고 설계했다",
        posting_signature="짧은 문장, 강한 밈 태그, 캡처 재편집",
        trigger_topics="검열 논란, 특혜 의혹, 상벌 기준의 모순",
        avoid_topics="긴 근거문서 분석, 절차론",
        anonymity_preference="익명 다중 계정 운용",
        activity_pattern="점심/야간 피크 타임에 맞춰 떡밥을 던지고 반응을 리포스트",
        lore_rationale="공론장의 탄생 테마에서 필수인 '확산 엔진' 역할",
        narrative_use="주인공이 설계한 시스템이 군중 심리와 충돌하는 장면을 만든다",
    ),
    Profile(
        core_id="NC-0005",
        name="소하 린데",
        role="학생생활권 대표성 이슈의 얼굴",
        background_type="commoner",
        dorm="ANY_NON_VISION",
        target={"O": 0.70, "C": 0.90, "E": 0.35, "A": 0.72, "N": 0.58, "DT": 0.01, "NFC": 0.78, "SM": 0.18},
        relation_to_mc="주인공 플랫폼의 '현장 증언 레이어'를 가장 신뢰하는 실무형 협력자",
        world_anchor="학생생활권 생활 규율, 생활비/실습비 격차 이슈",
        desire="장학/통금/실습 접근 규칙을 데이터로 공개해 제도 개선을 이끄는 것",
        fear="익명 폭로가 개인 보복으로 돌아와 동료들이 침묵하게 되는 것",
        flaw="정답에 집착해 정치적 타협을 잘 못한다",
        secret="가문이 몰락귀족 출신이라는 사실을 일부러 숨기고 있다",
        posting_signature="비용표, 시간표, 피해 사례를 정리한 문서형 글",
        trigger_topics="장학 박탈, 통금 차별, 실습비 전가",
        avoid_topics="신상털이형 폭로전",
        anonymity_preference="고정 익명(신뢰를 위해 필체와 포맷을 일정하게 유지)",
        activity_pattern="사건 직후 실시간 반응보다 하루 뒤 정리본을 올린다",
        lore_rationale="'평민(몰락귀족 편입)' 축의 현실감을 담당하는 핵심 관찰자",
        narrative_use="상층 정치 갈등을 생활 단위의 체감 고통으로 번역한다",
    ),
    Profile(
        core_id="NC-0006",
        name="타리크 사바르",
        role="조약권/번역권 연결자",
        background_type="foreigner",
        dorm="ANY_NON_VISION",
        target={"O": 0.76, "C": 0.64, "E": 0.60, "A": 0.74, "N": 0.38, "DT": 0.01, "NFC": 0.66, "SM": 0.46},
        relation_to_mc="주인공 시스템을 타문화 문맥으로 번역해 확장하는 국제 연결점",
        world_anchor="교환/조약 파견 라인, 통합 배정 갈등 중재",
        desire="학술원 내부 규칙과 외부 조약 규격을 양립 가능한 문장으로 정리하는 것",
        fear="번역 오류 하나가 외교 분쟁으로 비화하는 것",
        flaw="갈등을 봉합하려다 핵심 쟁점을 흐릴 때가 있다",
        secret="본국 기관의 비공식 보고 의무를 지고 있어 완전한 중립이 불가능",
        posting_signature="원문-번역-해석 주석 3단 구성",
        trigger_topics="호칭/예절 충돌, 조약 해석, 통역 누락",
        avoid_topics="내부 파벌의 순수 권력 다툼",
        anonymity_preference="실명 기반(신뢰 확보 목적)",
        activity_pattern="다툼이 격화되면 중재 요약문을 올리고 댓글에서 조율",
        lore_rationale="외국인 축은 숫자보다 규격 충돌이 핵심이라는 월드바이블 원칙에 부합",
        narrative_use="내부 사건을 국제 이슈로 스케일업할 때 관문 역할",
    ),
    Profile(
        core_id="NC-0007",
        name="브론 키트스톤",
        role="비인간 공방 네트워크 허브",
        background_type="nonhuman",
        dorm="ANY_TOWER",
        target={"O": 0.84, "C": 0.54, "E": 0.78, "A": 0.48, "N": 0.46, "DT": 0.05, "NFC": 0.62, "SM": 0.40},
        relation_to_mc="주인공 프로토콜을 실제 장비/현장 인터페이스로 바꾸는 제작형 동료",
        world_anchor="드워프 공방권 네트워크, 7탑 기숙사군 야간 실습 라인",
        desire="인외 제작 기술이 학내 표준에서 주변화되지 않고 독립 규격으로 인정받는 것",
        fear="사고 발생 시 인외 라인이 일괄적으로 배제되는 것",
        flaw="성급한 실험 욕심 때문에 안전 프로토콜을 우회한다",
        secret="비인가 부품 거래 루트와 접점이 있어 감찰단에 노출되면 치명적",
        posting_signature="도식, 부품 리스트, 실패 로그를 유머 섞어 공유",
        trigger_topics="안전점수 조작, 장비 결함 은폐, 공방 출입 제한",
        avoid_topics="의례/호칭 중심의 귀족 예법 논쟁",
        anonymity_preference="반익명(종족은 공개, 개인 식별정보는 비공개)",
        activity_pattern="실험 직후 바로 결과를 올리고 피드백을 받아 즉시 수정",
        lore_rationale="인외 축의 기술/규격 충돌을 '장비와 로그' 문제로 구현할 수 있는 캐릭터",
        narrative_use="사건의 물증(장비/부품/고장흔) 라인을 만들어 플롯의 증거 밀도를 높인다",
    ),
)


def dorm_matches(dorm_filter: str, dorm: str) -> bool:
    if dorm_filter == "ANY_TOWER":
        return dorm in TOWER_DORMS
    if dorm_filter == "ANY_NON_VISION":
        return dorm != "비전관"
    return dorm == dorm_filter


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    bundle_root = repo_root / "worldbible_refined_bundle_20260303"
    parser = argparse.ArgumentParser(description="Bootstrap 7 core cast profiles from P-* slots")
    parser.add_argument(
        "--csv-path",
        type=Path,
        default=bundle_root / "population" / "population_slots.csv",
        help="Population CSV path",
    )
    parser.add_argument(
        "--population-dir",
        type=Path,
        default=bundle_root / "population",
        help="Population YAML directory",
    )
    parser.add_argument(
        "--card-dir",
        type=Path,
        default=bundle_root / "population" / "core_cast",
        help="Output directory for core cast cards",
    )
    parser.add_argument(
        "--summary-md",
        type=Path,
        default=bundle_root / "docs" / "core_cast_bootstrap_v1.md",
        help="Output markdown summary path",
    )
    return parser.parse_args()


def to_float(row: dict[str, str], key: str) -> float:
    return float(row[key])


def score(row: dict[str, str], target: dict[str, float]) -> float:
    total = 0.0
    for key, t in target.items():
        d = to_float(row, key) - t
        total += WEIGHTS.get(key, 1.0) * (d * d)
    return total


def pick_rows(rows: list[dict[str, str]]) -> dict[str, tuple[Profile, dict[str, str]]]:
    selected: dict[str, tuple[Profile, dict[str, str]]] = {}
    used_ids: set[str] = set()

    for profile in PROFILES:
        candidates = [
            row
            for row in rows
            if row["status"] == "uninstantiated"
            and row["background_type"] == profile.background_type
            and dorm_matches(profile.dorm, row["dorm"])
            and row["id"] not in used_ids
        ]
        if not candidates:
            raise RuntimeError(
                f"No candidate for {profile.core_id} ({profile.background_type}/{profile.dorm})"
            )

        best = min(candidates, key=lambda r: (score(r, profile.target), r["id"]))
        selected[profile.core_id] = (profile, best)
        used_ids.add(best["id"])

    return selected


def update_csv(rows: list[dict[str, str]], selections: dict[str, tuple[Profile, dict[str, str]]]) -> None:
    pid_to_core: dict[str, str] = {}
    for core_id, (_, row) in selections.items():
        pid_to_core[row["id"]] = core_id

    for row in rows:
        core_id = pid_to_core.get(row["id"])
        if not core_id:
            continue
        row["status"] = "named"
        row["ch_id"] = core_id


def write_csv(csv_path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise RuntimeError("No rows in population CSV")
    fieldnames = list(rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def update_yaml_status(yaml_path: Path, core_id: str) -> None:
    if not yaml_path.is_file():
        raise FileNotFoundError(yaml_path)

    lines = yaml_path.read_text(encoding="utf-8").splitlines()
    has_status = False
    has_ch_id = False
    out: list[str] = []

    for line in lines:
        if line.startswith("status:"):
            out.append("status: named")
            has_status = True
            continue
        if line.startswith("ch_id:"):
            out.append(f"ch_id: {core_id}")
            has_ch_id = True
            continue
        out.append(line)

    if not has_status:
        out.append("status: named")
    if not has_ch_id:
        out.append(f"ch_id: {core_id}")

    yaml_path.write_text("\n".join(out) + "\n", encoding="utf-8")


def format_trait_line(row: dict[str, str], keys: tuple[str, ...]) -> str:
    return ", ".join(f"{k} {float(row[k]):.2f}" for k in keys)


def psych_rationale(profile: Profile, row: dict[str, str]) -> str:
    c = float(row["C"])
    e = float(row["E"])
    a = float(row["A"])
    n = float(row["N"])
    dt = float(row["DT"])
    nfc = float(row["NFC"])
    sm = float(row["SM"])

    parts: list[str] = []
    if c >= 0.72:
        parts.append("높은 성실성(C)으로 절차·기한·규율 집착이 강하다")
    elif c <= 0.45:
        parts.append("낮은 성실성(C)으로 즉흥 대응과 우회 전술을 선호한다")

    if e >= 0.70:
        parts.append("높은 외향성(E)으로 공개 반응과 군중 상호작용을 두려워하지 않는다")
    elif e <= 0.40:
        parts.append("낮은 외향성(E)으로 공개 무대보다 기록/문서 채널을 선호한다")

    if a <= 0.40:
        parts.append("낮은 우호성(A) 때문에 갈등 상황에서 타협보다 판정/공격을 택한다")
    elif a >= 0.68:
        parts.append("높은 우호성(A)으로 중재·협업·피해 최소화 지향이 강하다")

    if n >= 0.65:
        parts.append("높은 신경성(N)이 위협 민감도를 올려 조기 경보형 행동을 유도한다")

    if dt >= 0.10:
        parts.append("상대적으로 높은 DT가 프레임 선점/권력적 수읽기를 강화한다")
    elif dt <= 0.02:
        parts.append("낮은 DT로 인해 장기적 신뢰 자본을 우선시한다")

    if nfc >= 0.72:
        parts.append("높은 NFC가 복잡한 자료 해석과 장문 논증을 버티게 한다")

    if sm >= 0.45:
        parts.append("높은 SM으로 맥락에 따라 페르소나를 빠르게 조정한다")
    elif sm <= 0.20:
        parts.append("낮은 SM이라 온라인/오프라인 톤 차이가 작고 일관성이 높다")

    if not parts:
        parts.append("빅5와 파생지표가 중간대에 모여 상황 적응형 행동이 예상된다")

    return "; ".join(parts)


def render_card(profile: Profile, row: dict[str, str]) -> str:
    b5_line = format_trait_line(row, ("O", "C", "E", "A", "N"))
    derived_line = format_trait_line(row, ("DT", "NFC", "SM"))
    psych = psych_rationale(profile, row)

    return f"""---
core_id: {profile.core_id}
source_p_id: {row['id']}
status: named
created_at: 2026-03-04
---

# {profile.core_id} {profile.name}

## slot_profile
- source_p_id: {row['id']}
- background_type: {row['background_type']}
- dorm: {row['dorm']}
- b5: {b5_line}
- derived: {derived_line}

## offline_core
- role: {profile.role}
- relation_to_mc: {profile.relation_to_mc}
- world_anchor: {profile.world_anchor}
- desire: {profile.desire}
- fear: {profile.fear}
- flaw: {profile.flaw}
- secret: {profile.secret}

## online_persona
- posting_signature: {profile.posting_signature}
- trigger_topics: {profile.trigger_topics}
- avoid_topics: {profile.avoid_topics}
- anonymity_preference: {profile.anonymity_preference}
- activity_pattern: {profile.activity_pattern}

## rationale
- psych_rationale: {psych}
- lore_rationale: {profile.lore_rationale}
- narrative_use: {profile.narrative_use}
"""


def write_cards(card_dir: Path, selections: dict[str, tuple[Profile, dict[str, str]]]) -> None:
    card_dir.mkdir(parents=True, exist_ok=True)
    for core_id in sorted(selections.keys()):
        profile, row = selections[core_id]
        out_path = card_dir / f"{core_id}_{row['id']}.md"
        out_path.write_text(render_card(profile, row), encoding="utf-8")


def write_summary(summary_md: Path, selections: dict[str, tuple[Profile, dict[str, str]]]) -> None:
    lines: list[str] = []
    lines.append("# core_cast_bootstrap_v1")
    lines.append("")
    lines.append("- generated_at: 2026-03-04")
    lines.append("- source: population/population_slots.csv + population/P-*.yaml")
    lines.append("- count: 7")
    lines.append("- id_policy: CH-* 재사용 없이 `NC-*` 사용")
    lines.append("")
    lines.append("## Selection")
    lines.append("| core_id | source_p_id | name | role | background | dorm |")
    lines.append("|---|---|---|---|---|---|")

    for core_id in sorted(selections.keys()):
        profile, row = selections[core_id]
        lines.append(
            f"| {core_id} | {row['id']} | {profile.name} | {profile.role} | {row['background_type']} | {row['dorm']} |"
        )

    lines.append("")
    lines.append("## Files")
    lines.append("- cards: `population/core_cast/NC-000*_P-*.md`")
    lines.append("- csv status: `population/population_slots.csv`")
    lines.append("- yaml status: `population/P-*.yaml` (선정된 7개만 상태 반영)")

    summary_md.parent.mkdir(parents=True, exist_ok=True)
    summary_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    if not args.csv_path.is_file():
        raise SystemExit(f"CSV not found: {args.csv_path}")

    with args.csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if len(rows) != 3600:
        raise SystemExit(f"Unexpected row count: {len(rows)} (expected 3600)")

    selections = pick_rows(rows)
    update_csv(rows, selections)
    write_csv(args.csv_path, rows)

    for core_id, (_, row) in selections.items():
        update_yaml_status(args.population_dir / f"{row['id']}.yaml", core_id)

    write_cards(args.card_dir, selections)
    write_summary(args.summary_md, selections)

    print("core_cast_selected=7")
    for core_id in sorted(selections.keys()):
        profile, row = selections[core_id]
        print(f"{core_id},{row['id']},{profile.name},{row['background_type']},{row['dorm']}")
    print(f"cards_dir={args.card_dir}")
    print(f"summary_md={args.summary_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
