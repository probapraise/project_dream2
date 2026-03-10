#!/usr/bin/env python3
"""
sim_runner.py — gated simulation worker
=======================================

This runner is no longer a direct-entry simulation script.
It must consume a gated payload produced by:

1) world_ops_compile_execution_views.sh
2) world_ops_pre_injection_gate.sh

The caller is expected to run output leak scan separately and only promote
artifact outputs into `world/live/board_states/` after that scan passes.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_VERTEX_KEY = PROJECT_ROOT / "vertex_key.json"
DEFAULT_BUNDLE_DIR = PROJECT_ROOT / "world/live"

PROJECT_ID = "gen-lang-client-0197907947"
MODEL = "gemini-3.1-flash-lite-preview"
API_URL = (
    f"https://aiplatform.googleapis.com/v1/projects/{PROJECT_ID}"
    f"/locations/global/publishers/google/models/{MODEL}:generateContent"
)

PROTAGONIST_SLOT = "P-1027"  # NC-0001, 주인공 — 일반 응답자 풀에서 제외

DEFAULT_WORLD_CONTEXT = """[세계관 기본 상식]
아르케이온 왕립학술원은 마나 기반 세계의 최고 마도 교육기관이다.
학생은 마법사·기사·사제 계열로 나뉘며 총 3600명이 재학 중이다.
배지(학내 표준 단말)로 신분 인증, 정보 입출력, 서명을 수행한다.
귀족(서명귀족·일반귀족), 평민, 외국인, 인외 등 다양한 배경의 학생이 섞여 있다.
계층 간 긴장이 존재하며, 정본(원본 서류)과 열람권이 사회의 권력 자원이다.
"""

DEFAULT_SEED_EVENT = """[오늘의 사건 — 각인광장 베타 오픈]
오늘, 키리온 렌바렌(자탑 1학년 마법사)이 만든 '각인광장(Archive Plaza)'이
처음으로 전 학술원 학생에게 베타 공개되었다.

각인광장은:
- 배지로 텍스트를 입력하면 성목(이르민수) 코어에 영구 각인·저장되는 공론장
- 스레드/댓글/추천/신고/보존권 기능 탑재
- 익명 계정 사용 가능 (단 운영자에게는 신원 노출)
- 검색·인용·증거화가 가능한 최초의 공개 플랫폼

지금 이 순간, 게시판은 완전히 비어 있다. 아무 글도 없다.
아무도 이 플랫폼을 써본 적 없다.
"""


@dataclass(frozen=True)
class RunConfig:
    call_id: str
    run_id: str
    sim_id: str
    mode: str
    seed_label: str
    participants: int
    sample_seed: int
    gated_payload: Path
    input_view: Path
    output_json: Path
    output_report: Path | None
    population_csv: Path
    vertex_key: Path
    world_context: str
    seed_event: str
    allowed_view_context: str
    interaction_mode: str
    board_name: str
    board_tone: str
    thread_seed_post: str
    first_movers_count: int
    round2_include_first_movers: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run gated Layer A simulation")
    parser.add_argument(
        "--gated-payload",
        type=Path,
        required=True,
        help="Gated payload file produced by world_ops_pre_injection_gate.sh",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        required=True,
        help="Artifact output JSON path under artifacts/runs/<run_id>/outputs/",
    )
    parser.add_argument(
        "--output-report",
        type=Path,
        help="Optional human-readable markdown report path under artifacts/runs/<run_id>/outputs/",
    )
    parser.add_argument(
        "--population-csv",
        type=Path,
        default=DEFAULT_BUNDLE_DIR / "population" / "population_slots.csv",
        help="Population CSV path (defaults to world/live/population/population_slots.csv)",
    )
    parser.add_argument(
        "--vertex-key",
        type=Path,
        default=DEFAULT_VERTEX_KEY,
        help="Vertex service account JSON path",
    )
    return parser.parse_args()


def fail(message: str) -> "NoReturn":
    raise SystemExit(f"[fail] {message}")


def parse_key_value_file(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def resolve_project_path(raw_path: str) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute():
        resolved = candidate.resolve()
    else:
        resolved = (PROJECT_ROOT / candidate).resolve()
    try:
        resolved.relative_to(PROJECT_ROOT)
    except ValueError as exc:
        fail(f"project root outside path not allowed: {raw_path}")
    return resolved


def require_path_within(path: Path, parent: Path, label: str) -> None:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError:
        fail(f"{label} must live under {parent}")


def require_gated_layout(gated_payload: Path, input_view: Path, output_json: Path) -> tuple[str, str]:
    runs_root = (PROJECT_ROOT / "artifacts" / "runs").resolve()
    payload_dir = gated_payload.resolve().parent
    if payload_dir.name != "payloads":
        fail("gated payload must be inside artifacts/runs/<run_id>/payloads/")
    run_dir = payload_dir.parent
    if run_dir.parent != runs_root:
        fail("gated payload run dir must be under artifacts/runs/")

    views_dir = run_dir / "views"
    outputs_dir = run_dir / "outputs"
    require_path_within(input_view, views_dir, "input_view")
    require_path_within(output_json, outputs_dir, "output_json")

    return run_dir.name, input_view.stem


def build_allowed_view_context(view_path: Path, max_chars: int = 12000) -> str:
    text = view_path.read_text(encoding="utf-8")
    marker = "### source:"
    if marker in text:
        text = text[text.index(marker) :].strip()
    else:
        text = text.strip()
    if len(text) > max_chars:
        text = text[:max_chars].rstrip() + "\n...[truncated]"
    return (
        "[허용된 실행뷰]\n"
        "이번 실행은 아래 execution view에 포함된 문서만 참고할 수 있다.\n\n"
        f"{text}"
    )


def parse_positive_int(raw_value: str, key: str) -> int:
    try:
        value = int(raw_value)
    except ValueError as exc:
        fail(f"{key} must be an integer")
    if value <= 0:
        fail(f"{key} must be > 0")
    return value


def parse_yes_no(raw_value: str, key: str) -> bool:
    value = raw_value.strip().lower()
    if value in {"yes", "true", "1"}:
        return True
    if value in {"no", "false", "0", ""}:
        return False
    fail(f"{key} must be yes/no")


def load_run_config(args: argparse.Namespace) -> RunConfig:
    gated_payload = args.gated_payload.resolve()
    if not gated_payload.is_file():
        fail(f"gated payload not found: {gated_payload}")

    payload = parse_key_value_file(gated_payload)
    input_view_raw = payload.get("input_view")
    if not input_view_raw:
        fail("gated payload missing required key: input_view")
    input_view = resolve_project_path(input_view_raw)
    if not input_view.is_file():
        fail(f"input_view not found: {input_view}")

    output_json = args.output_json.resolve()
    output_json.parent.mkdir(parents=True, exist_ok=True)

    run_id, call_id = require_gated_layout(gated_payload, input_view, output_json)

    output_report: Path | None = None
    if args.output_report:
        output_report = args.output_report.resolve()
        output_report.parent.mkdir(parents=True, exist_ok=True)
        require_path_within(output_report, output_json.parent, "output_report")

    population_csv = args.population_csv.resolve()
    if not population_csv.is_file():
        fail(f"population csv not found: {population_csv}")

    vertex_key = args.vertex_key.resolve()
    if not vertex_key.is_file():
        fail(f"vertex key not found: {vertex_key}")

    sim_id = payload.get("sim_id", call_id.lower())
    mode = payload.get("mode", "cold_start")
    seed_label = payload.get("seed_label", "각인광장 베타 오픈 첫날")
    participants = parse_positive_int(payload.get("participants", "12"), "participants")
    sample_seed = parse_positive_int(payload.get("sample_seed", "42"), "sample_seed")
    world_context = payload.get("world_context", DEFAULT_WORLD_CONTEXT).strip()
    seed_event = payload.get("seed_event", DEFAULT_SEED_EVENT).strip()
    allowed_view_context = build_allowed_view_context(input_view)
    interaction_mode = payload.get("interaction_mode", "cold_start").strip().lower() or "cold_start"
    board_name = payload.get("board_name", "각인광장").strip()
    board_tone = payload.get("board_tone", "").strip()
    thread_seed_post = payload.get("thread_seed_post", "").strip()
    first_movers_count = parse_positive_int(payload.get("first_movers_count", "3"), "first_movers_count")
    round2_include_first_movers = parse_yes_no(
        payload.get("round2_include_first_movers", "no"),
        "round2_include_first_movers",
    )

    if interaction_mode not in {"cold_start", "thread_reaction"}:
        fail("interaction_mode must be one of: cold_start, thread_reaction")
    if interaction_mode == "thread_reaction" and not thread_seed_post:
        fail("thread_reaction mode requires thread_seed_post")

    return RunConfig(
        call_id=call_id,
        run_id=run_id,
        sim_id=sim_id,
        mode=mode,
        seed_label=seed_label,
        participants=participants,
        sample_seed=sample_seed,
        gated_payload=gated_payload,
        input_view=input_view,
        output_json=output_json,
        output_report=output_report,
        population_csv=population_csv,
        vertex_key=vertex_key,
        world_context=world_context,
        seed_event=seed_event,
        allowed_view_context=allowed_view_context,
        interaction_mode=interaction_mode,
        board_name=board_name,
        board_tone=board_tone,
        thread_seed_post=thread_seed_post,
        first_movers_count=first_movers_count,
        round2_include_first_movers=round2_include_first_movers,
    )


def b5_to_traits(row: dict[str, str]) -> str:
    def f(key: str) -> float:
        return float(row.get(key) or 0.5)

    o_val, c_val, e_val, a_val, n_val = (
        f("O"),
        f("C"),
        f("E"),
        f("A"),
        f("N"),
    )
    dt_val, nfc_val, sm_val = f("DT"), f("NFC"), f("SM")

    traits = []
    traits.append(
        "새로운 것에 강한 호기심, 실험적 사고"
        if o_val > 0.65
        else ("실용적·전통 선호, 검증된 것을 신뢰" if o_val < 0.40 else "적당한 호기심, 실용과 탐구 균형")
    )
    traits.append(
        "체계적·목표 지향, 계획을 중시"
        if c_val > 0.65
        else ("즉흥적·유연, 흐름에 맡기는 편" if c_val < 0.40 else "상황에 따라 계획적")
    )
    traits.append(
        "외향적, 의견을 적극적으로 표현"
        if e_val > 0.65
        else ("내향적, 관찰 위주 조용히 행동" if e_val < 0.40 else "상황에 따라 전면에 나섬")
    )
    traits.append(
        "협력적, 공감 능력 높음, 분위기를 맞춤"
        if a_val > 0.65
        else ("경쟁적·회의적, 손해에 민감" if a_val < 0.40 else "협력과 경쟁 사이 균형")
    )
    traits.append(
        "감정 반응 예민, 스트레스에 쉽게 반응"
        if n_val > 0.65
        else ("감정적으로 안정적, 웬만해서 흔들리지 않음" if n_val < 0.40 else "보통의 감정 반응")
    )
    if dt_val > 0.55:
        traits.append("자기 이익 중심, 전략적 언행 경향")
    if nfc_val > 0.70:
        traits.append("지적 분석과 탐구를 즐김")
    if sm_val > 0.70:
        traits.append("상황에 맞게 말투·행동을 능숙하게 조절")
    return "\n".join(f"- {trait}" for trait in traits)


def build_system_prompt(config: RunConfig, char: dict[str, str]) -> str:
    bg_map = {
        "common_noble": "일반 귀족",
        "signature_noble": "서명귀족",
        "commoner": "평민",
        "foreigner": "외국인",
        "nonhuman": "인외",
    }
    bg = bg_map.get(char.get("background_type", ""), char.get("background_type", "불명"))
    voc = char.get("vocation", "마법사")
    grade = char.get("grade", "1학년")
    dorm = char.get("dorm", "불명")
    mana = char.get("mana_color", "")
    mana_line = f"- 마나 계열: {mana}탑\n" if mana and voc == "마법사" else ""
    board_line = ""
    if config.interaction_mode == "thread_reaction":
        tone = config.board_tone or "혼돈, 냉소, 내부자 유머"
        board_line = (
            "[게시판]\n"
            f"- 이름: {config.board_name}\n"
            f"- 분위기: {tone}\n"
            "- 익명성: 완전 익명\n\n"
        )

    base_prompt = f"""당신은 아르케이온 왕립학술원의 학생입니다.

[신분]
- 직능: {voc}
- 학년: {grade}
- 기숙사: {dorm}
- 배경: {bg}
{mana_line}
[board_line]
[성격 성향]
{b5_to_traits(char)}

[행동 원칙]
- 당신 자신으로서, 성향에 맞게 자연스럽게 행동하세요.
- 소프트웨어 개발자처럼 행동하지 마세요. 판타지 세계의 학생입니다.
- 한국어로, 이 세계의 언어라고 상상하며 작성하세요.
- 실제 커뮤니티 게시글처럼 짧고 생생하게 (30~150자 권장).
- 글을 쓰지 않을 수도 있습니다. 관망·눈팅도 자연스러운 선택입니다.
"""
    base_prompt = base_prompt.replace("[board_line]\n", board_line)
    if config.interaction_mode != "thread_reaction":
        return base_prompt

    return (
        base_prompt
        + """
- 지금 하는 일은 익명 게시판 반응 작성이다. 분석 보고서를 쓰는 것이 아니다.
- 제목, 설명, 서문, 각주, 괄호 해설, '작성자:' 같은 라벨을 붙이지 마세요.
- 실제 댓글 또는 짧은 게시글 원문만 출력하세요.
- 반말 위주로, 짧고 날것처럼 작성하세요.
- 너무 친절하게 정리하지 말고, 실제 학생이 툭 던진 말처럼 쓰세요.
- 아무 말도 안 할 거면 정확히 '눈팅함'만 출력하세요.
"""
    )


def load_credentials(key_path: Path):
    try:
        from google.auth.transport.requests import Request
        from google.oauth2 import service_account
    except ImportError as exc:
        fail("google-auth is required to run sim_runner.py")
    creds = service_account.Credentials.from_service_account_file(
        str(key_path),
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    return creds, Request


def call_llm(creds, request_cls, system_prompt: str, user_message: str,
             temperature: float = 0.95, max_tokens: int = 400) -> str:
    try:
        import requests
    except ImportError as exc:
        fail("requests is required to run sim_runner.py")

    if not creds.valid:
        creds.refresh(request_cls())
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
    }
    payload = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": user_message}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens,
        },
    }
    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()


def load_personas(population_csv: Path, n: int, seed: int) -> list[dict[str, str]]:
    all_rows: list[dict[str, str]] = []
    with population_csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("id") == PROTAGONIST_SLOT:
                continue
            if row.get("status") == "named":
                continue
            all_rows.append(row)

    rng = random.Random(seed)

    by_vocation: dict[str, list[dict[str, str]]] = {}
    for row in all_rows:
        by_vocation.setdefault(row.get("vocation", "unknown"), []).append(row)

    targets = {"마법사": 7, "기사": 3, "사제": 2}
    sampled: list[dict[str, str]] = []
    for vocation, count in targets.items():
        pool = by_vocation.get(vocation, [])
        sampled.extend(rng.sample(pool, min(count, len(pool))))
    return sampled[:n]


def build_base_user_context(config: RunConfig) -> str:
    return "\n\n".join(
        [
            config.allowed_view_context,
            config.world_context,
            config.seed_event,
        ]
    )


def build_thread_state(posts: list[dict[str, object]]) -> str:
    chunks = []
    for index, post in enumerate(posts, start=1):
        chunks.append(f"댓글 {index}: {post['content']}")
    return "\n".join(chunks)


def run_round1(
    config: RunConfig,
    creds,
    request_cls,
    personas: list[dict[str, str]],
    base_context: str,
) -> tuple[list[dict[str, object]], list[dict[str, str]]]:
    print("\n" + "─" * 60)
    print(f"ROUND 1 — 퍼스트 무버 (E+O 상위 {config.first_movers_count}명)")
    print("─" * 60)

    scored = sorted(
        personas,
        key=lambda row: float(row.get("E") or 0.5) + float(row.get("O") or 0.5),
        reverse=True,
    )
    first_movers = scored[: min(len(scored), config.first_movers_count)]

    posts: list[dict[str, object]] = []
    for char in first_movers:
        uid = char["id"]
        label = f"{char.get('vocation')} {char.get('grade')} / {char.get('dorm')} [{char.get('background_type')}]"
        print(f"\n▶ {uid} ({label})")

        if config.interaction_mode == "thread_reaction":
            user_msg = (
                base_context
                + "\n\n[시드 글]\n"
                + config.thread_seed_post
                + "\n\n[행동 지침]\n"
                + f"위 시드 글을 방금 본 {config.board_name} 이용자라고 생각하고 짧은 댓글 하나만 작성하세요.\n"
                + "설명, 라벨, 제목, 메타 해설 없이 실제 댓글 원문만 출력하세요.\n"
                + "시드 글의 허접함, 구조, 답변 말투, 분위기 중 하나를 물고 늘어져도 됩니다.\n"
                + "안 쓰고 넘어가려면 정확히 '눈팅함'만 출력하세요."
            )
        else:
            user_msg = (
                base_context
                + "\n\n[현재 상황]\n"
                + "각인광장이 방금 열렸습니다. 게시판은 완전히 비어 있습니다.\n"
                + "당신이 원한다면 지금 이 순간 첫 글을 쓸 수 있습니다.\n"
                + "당신의 성향에 따라 글을 쓰거나, 아직 관망하거나 선택하세요.\n"
                + "글을 쓴다면 실제 게시글 텍스트를 작성하세요.\n"
                + "관망한다면 '관망한다' 한 줄로 서술하세요."
            )
        try:
            resp = call_llm(
                creds,
                request_cls,
                build_system_prompt(config, char),
                user_msg,
                temperature=1.0,
            )
            posts.append({"char": char, "content": resp, "round": 1})
            preview = resp[:100] + "..." if len(resp) > 100 else resp
            print(f"  → {preview}")
        except Exception as exc:  # pragma: no cover - network/runtime path
            print(f"  → [오류] {exc}")

    return posts, first_movers


def run_round2(
    config: RunConfig,
    creds,
    request_cls,
    personas: list[dict[str, str]],
    first_movers: list[dict[str, str]],
    round1_posts: list[dict[str, object]],
    base_context: str,
) -> list[dict[str, object]]:
    print("\n" + "─" * 60)
    print("ROUND 2 — 반응자 (나머지)")
    print("─" * 60)

    if config.round2_include_first_movers:
        reactors = list(personas)
    else:
        reactors = [persona for persona in personas if persona not in first_movers]

    if config.interaction_mode == "thread_reaction":
        board_state = build_thread_state(round1_posts)
    else:
        board_state = ""
        for index, post in enumerate(round1_posts, start=1):
            char = post["char"]
            board_state += (
                f"\n--- 게시글 {index} ---\n"
                f"작성자: {char.get('vocation')} {char.get('grade')} ({char.get('dorm')})\n"
                f"{post['content']}\n"
            )

    posts: list[dict[str, object]] = []
    for char in reactors:
        uid = char["id"]
        label = f"{char.get('vocation')} {char.get('grade')} / {char.get('dorm')} [{char.get('background_type')}]"
        print(f"\n▶ {uid} ({label})")

        if config.interaction_mode == "thread_reaction":
            user_msg = (
                base_context
                + "\n\n[시드 글]\n"
                + config.thread_seed_post
                + "\n\n[현재 댓글 흐름]\n"
                + board_state
                + "\n\n[행동 지침]\n"
                + f"위 흐름을 본 {config.board_name} 이용자라고 생각하고 후속 댓글 하나만 작성하세요.\n"
                + "누군가를 받거나, 다른 댓글을 비틀거나, 새 웃음 포인트를 추가해도 됩니다.\n"
                + "설명, 라벨, 제목 없이 실제 댓글 원문만 출력하세요.\n"
                + "안 쓰고 넘어가려면 정확히 '눈팅함'만 출력하세요."
            )
        else:
            user_msg = (
                base_context
                + "\n\n[현재 각인광장 상태 — 방금 올라온 첫 게시물들]\n"
                + board_state
                + "\n[행동 지침]\n"
                + "위 글들을 보고 당신 성향대로 반응하세요.\n"
                + "댓글을 달거나, 새 글을 쓰거나, 눈팅만 할 수도 있습니다.\n"
                + "반응한다면 어느 글에 대한 반응인지 명시하고 실제 텍스트를 쓰세요.\n"
                + "눈팅한다면 '눈팅한다' 한 줄로 서술하세요."
            )
        try:
            resp = call_llm(
                creds,
                request_cls,
                build_system_prompt(config, char),
                user_msg,
                temperature=0.9,
            )
            posts.append({"char": char, "content": resp, "round": 2})
            preview = resp[:100] + "..." if len(resp) > 100 else resp
            print(f"  → {preview}")
        except Exception as exc:  # pragma: no cover - network/runtime path
            print(f"  → [오류] {exc}")

    return posts


def build_result(config: RunConfig, personas: list[dict[str, str]], posts: list[dict[str, object]]) -> dict[str, object]:
    return {
        "run_id": config.run_id,
        "call_id": config.call_id,
        "sim_id": config.sim_id,
        "seed": config.seed_label,
        "mode": config.mode,
        "model": MODEL,
        "participants": len(personas),
        "rounds": 2,
        "source_view": str(config.input_view.relative_to(PROJECT_ROOT)),
        "logs": [
            {
                "round": post["round"],
                "char_id": post["char"]["id"],
                "vocation": post["char"].get("vocation"),
                "grade": post["char"].get("grade"),
                "dorm": post["char"].get("dorm"),
                "background": post["char"].get("background_type"),
                "content": post["content"],
            }
            for post in posts
        ],
    }


def write_markdown_report(path: Path, result: dict[str, object]) -> None:
    lines = [
        "# sim_runner_report",
        "",
        f"- run_id: {result['run_id']}",
        f"- call_id: {result['call_id']}",
        f"- sim_id: {result['sim_id']}",
        f"- seed: {result['seed']}",
        f"- mode: {result['mode']}",
        f"- model: {result['model']}",
        f"- source_view: {result['source_view']}",
        "",
        "## logs",
    ]
    for log in result["logs"]:
        lines.extend(
            [
                f"### round {log['round']} / {log['char_id']}",
                f"- vocation: {log['vocation']}",
                f"- grade: {log['grade']}",
                f"- dorm: {log['dorm']}",
                f"- background: {log['background']}",
                "",
                str(log["content"]),
                "",
            ]
        )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    config = load_run_config(args)

    print("=" * 60)
    print("Layer A Simulation — gated runner")
    print(f"Run ID : {config.run_id}")
    print(f"Call ID: {config.call_id}")
    print(f"Sim ID : {config.sim_id}")
    print(f"Mode   : {config.mode}")
    print(f"Interact: {config.interaction_mode}")
    print(f"Seed   : {config.seed_label}")
    print("=" * 60)

    creds, request_cls = load_credentials(config.vertex_key)
    creds.refresh(request_cls())
    print("\n✓ Vertex AI 인증 완료")

    personas = load_personas(
        population_csv=config.population_csv,
        n=config.participants,
        seed=config.sample_seed,
    )
    print(f"✓ 응답자 {len(personas)}명 선발\n")
    for persona in personas:
        print(
            f"  {persona['id']}: {persona.get('vocation')} {persona.get('grade')} / "
            f"{persona.get('dorm')} [{persona.get('background_type')}]"
        )

    base_context = build_base_user_context(config)
    round1_posts, first_movers = run_round1(config, creds, request_cls, personas, base_context)
    round2_posts = run_round2(config, creds, request_cls, personas, first_movers, round1_posts, base_context)
    all_posts = round1_posts + round2_posts

    result = build_result(config, personas, all_posts)
    config.output_json.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\n✓ artifact json 저장: {config.output_json}")

    if config.output_report:
        write_markdown_report(config.output_report, result)
        print(f"✓ artifact report 저장: {config.output_report}")

    print("\n다음 단계: world_ops_output_leak_scan.sh 통과 후에만 live board_states 로 promote 하십시오.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
