#!/usr/bin/env python3
"""
sim_runner.py — Layer A Cold Start Simulation Runner
======================================================
시드: 각인광장 베타 오픈 첫날
모드: Cold Start (문화 바이블 없음)
모델: gemini-3.1-flash-lite-preview (global endpoint)
"""

import csv
import json
import random
import sys
from pathlib import Path

from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests

# ── 설정 ──────────────────────────────────────────────────────────────────────
PROJECT_ROOT   = Path(__file__).parent.parent
KEY_PATH       = PROJECT_ROOT / "vertex_key.json"
POPULATION_CSV = PROJECT_ROOT / "worldbible_refined_bundle_20260303/population/population_slots.csv"
OUTPUT_DIR     = PROJECT_ROOT / "worldbible_refined_bundle_20260303/board_states"

PROJECT_ID = "gen-lang-client-0197907947"
MODEL      = "gemini-3.1-flash-lite-preview"
API_URL    = (
    f"https://aiplatform.googleapis.com/v1/projects/{PROJECT_ID}"
    f"/locations/global/publishers/google/models/{MODEL}:generateContent"
)

PROTAGONIST_SLOT = "P-1027"  # NC-0001, 주인공 — 일반 응답자 풀에서 제외

# ── 세계 컨텍스트 (모든 페르소나에 공통 주입) ──────────────────────────────────
WORLD_CONTEXT = """[세계관 기본 상식]
아르케이온 왕립학술원은 마나 기반 세계의 최고 마도 교육기관이다.
학생은 마법사·기사·사제 계열로 나뉘며 총 3600명이 재학 중이다.
배지(학내 표준 단말)로 신분 인증, 정보 입출력, 서명을 수행한다.
귀족(서명귀족·일반귀족), 평민, 외국인, 인외 등 다양한 배경의 학생이 섞여 있다.
계층 간 긴장이 존재하며, 정본(원본 서류)과 열람권이 사회의 권력 자원이다.
"""

SEED_EVENT = """[오늘의 사건 — 각인광장 베타 오픈]
오늘, 키리온 렌바렌(보라탑 1학년 마법사)이 만든 '각인광장(Archive Plaza)'이
처음으로 전 학술원 학생에게 베타 공개되었다.

각인광장은:
- 배지로 텍스트를 입력하면 성목(이르민수) 코어에 영구 각인·저장되는 공론장
- 스레드/댓글/추천/신고/보존권 기능 탑재
- 익명 계정 사용 가능 (단 운영자에게는 신원 노출)
- 검색·인용·증거화가 가능한 최초의 공개 플랫폼

지금 이 순간, 게시판은 완전히 비어 있다. 아무 글도 없다.
아무도 이 플랫폼을 써본 적 없다.
"""

# ── 빅5 수치 → 자연어 성향 변환 ───────────────────────────────────────────────
def b5_to_traits(row: dict) -> str:
    def f(key): return float(row.get(key) or 0.5)
    O, C, E, A, N = f("O"), f("C"), f("E"), f("A"), f("N")
    DT, NFC, SM   = f("DT"), f("NFC"), f("SM")

    traits = []
    traits.append("새로운 것에 강한 호기심, 실험적 사고" if O > 0.65
                  else ("실용적·전통 선호, 검증된 것을 신뢰" if O < 0.40
                  else "적당한 호기심, 실용과 탐구 균형"))
    traits.append("체계적·목표 지향, 계획을 중시" if C > 0.65
                  else ("즉흥적·유연, 흐름에 맡기는 편" if C < 0.40
                  else "상황에 따라 계획적"))
    traits.append("외향적, 의견을 적극적으로 표현" if E > 0.65
                  else ("내향적, 관찰 위주 조용히 행동" if E < 0.40
                  else "상황에 따라 전면에 나섬"))
    traits.append("협력적, 공감 능력 높음, 분위기를 맞춤" if A > 0.65
                  else ("경쟁적·회의적, 손해에 민감" if A < 0.40
                  else "협력과 경쟁 사이 균형"))
    traits.append("감정 반응 예민, 스트레스에 쉽게 반응" if N > 0.65
                  else ("감정적으로 안정적, 웬만해서 흔들리지 않음" if N < 0.40
                  else "보통의 감정 반응"))
    if DT > 0.55:
        traits.append("자기 이익 중심, 전략적 언행 경향")
    if NFC > 0.70:
        traits.append("지적 분석과 탐구를 즐김")
    if SM > 0.70:
        traits.append("상황에 맞게 말투·행동을 능숙하게 조절")
    return "\n".join(f"- {t}" for t in traits)


def build_system_prompt(char: dict) -> str:
    bg_map = {
        "common_noble":     "일반 귀족",
        "signed_noble":     "서명귀족",
        "commoner":         "평민",
        "foreigner":        "외국인",
        "nonhuman":         "인외",
        "half_signed_noble":"서명귀족 방계",
    }
    bg      = bg_map.get(char.get("background_type", ""), char.get("background_type", "불명"))
    voc     = char.get("vocation", "마법사")
    grade   = char.get("grade", "1학년")
    dorm    = char.get("dorm", "불명")
    mana    = char.get("mana_color", "")
    mana_line = f"- 마나 계열: {mana}탑\n" if mana and voc == "마법사" else ""

    return f"""당신은 아르케이온 왕립학술원의 학생입니다.

[신분]
- 직능: {voc}
- 학년: {grade}
- 기숙사: {dorm}
- 배경: {bg}
{mana_line}
[성격 성향]
{b5_to_traits(char)}

[행동 원칙]
- 당신 자신으로서, 성향에 맞게 자연스럽게 행동하세요.
- 소프트웨어 개발자처럼 행동하지 마세요. 판타지 세계의 학생입니다.
- 한국어로, 이 세계의 언어라고 상상하며 작성하세요.
- 실제 커뮤니티 게시글처럼 짧고 생생하게 (30~150자 권장).
- 글을 쓰지 않을 수도 있습니다. 관망·눈팅도 자연스러운 선택입니다.
"""

# ── API 호출 ──────────────────────────────────────────────────────────────────
def call_llm(creds, system_prompt: str, user_message: str,
             temperature: float = 0.95, max_tokens: int = 400) -> str:
    if not creds.valid:
        creds.refresh(Request())
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
    r = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    return r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()


# ── 응답자 선발 ────────────────────────────────────────────────────────────────
def load_personas(n: int = 12, seed: int = 42) -> list[dict]:
    all_rows = []
    with open(POPULATION_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "named" and row.get("id") != PROTAGONIST_SLOT:
                all_rows.append(row)

    rng = random.Random(seed)

    # 직능별 비율에 맞춰 샘플링 (마법사 7 / 기사 3 / 사제 2)
    by_voc: dict[str, list] = {}
    for r in all_rows:
        by_voc.setdefault(r.get("vocation", "unknown"), []).append(r)

    targets = {"마법사": 7, "기사": 3, "사제": 2}
    sampled = []
    for v, count in targets.items():
        pool = by_voc.get(v, [])
        sampled.extend(rng.sample(pool, min(count, len(pool))))
    return sampled[:n]


# ── 라운드 1: 퍼스트 무버 ──────────────────────────────────────────────────────
def run_round1(creds, personas: list[dict]) -> tuple[list[dict], list[dict]]:
    print("\n" + "─"*60)
    print("ROUND 1 — 퍼스트 무버 (E+O 상위 3명)")
    print("─"*60)

    # E(외향성) + O(개방성) 합산 상위 3명을 퍼스트 무버로 선정
    scored = sorted(
        personas,
        key=lambda r: float(r.get("E") or 0.5) + float(r.get("O") or 0.5),
        reverse=True,
    )
    first_movers = scored[:3]

    posts = []
    for char in first_movers:
        uid   = char["id"]
        label = f"{char.get('vocation')} {char.get('grade')} / {char.get('dorm')} [{char.get('background_type')}]"
        print(f"\n▶ {uid} ({label})")

        user_msg = (
            WORLD_CONTEXT + "\n" + SEED_EVENT +
            "\n[현재 상황]\n"
            "각인광장이 방금 열렸습니다. 게시판은 완전히 비어 있습니다.\n"
            "당신이 원한다면 지금 이 순간 첫 글을 쓸 수 있습니다.\n"
            "당신의 성향에 따라 글을 쓰거나, 아직 관망하거나 선택하세요.\n"
            "글을 쓴다면 실제 게시글 텍스트를 작성하세요.\n"
            "관망한다면 '관망한다' 한 줄로 서술하세요."
        )
        try:
            resp = call_llm(creds, build_system_prompt(char), user_msg, temperature=1.0)
            posts.append({"char": char, "content": resp, "round": 1})
            preview = resp[:100] + "..." if len(resp) > 100 else resp
            print(f"  → {preview}")
        except Exception as e:
            print(f"  → [오류] {e}")

    return posts, first_movers


# ── 라운드 2: 반응자 ───────────────────────────────────────────────────────────
def run_round2(creds, personas: list[dict],
               first_movers: list[dict], r1_posts: list[dict]) -> list[dict]:
    print("\n" + "─"*60)
    print("ROUND 2 — 반응자 (나머지 9명)")
    print("─"*60)

    reactors = [p for p in personas if p not in first_movers]

    # R1 게시판 상태 조립 (같은 라운드 정보 격리 원칙 준수 — R2는 R1만 볼 수 있음)
    board_state = ""
    for i, post in enumerate(r1_posts):
        c = post["char"]
        board_state += (
            f"\n--- 게시글 {i+1} ---\n"
            f"작성자: {c.get('vocation')} {c.get('grade')} ({c.get('dorm')})\n"
            f"{post['content']}\n"
        )

    posts = []
    for char in reactors:
        uid   = char["id"]
        label = f"{char.get('vocation')} {char.get('grade')} / {char.get('dorm')} [{char.get('background_type')}]"
        print(f"\n▶ {uid} ({label})")

        user_msg = (
            WORLD_CONTEXT + "\n" + SEED_EVENT +
            "\n[현재 각인광장 상태 — 방금 올라온 첫 게시물들]\n"
            + board_state +
            "\n[행동 지침]\n"
            "위 글들을 보고 당신 성향대로 반응하세요.\n"
            "댓글을 달거나, 새 글을 쓰거나, 눈팅만 할 수도 있습니다.\n"
            "반응한다면 어느 글에 대한 반응인지 명시하고 실제 텍스트를 쓰세요.\n"
            "눈팅한다면 '눈팅한다' 한 줄로 서술하세요."
        )
        try:
            resp = call_llm(creds, build_system_prompt(char), user_msg, temperature=0.9)
            posts.append({"char": char, "content": resp, "round": 2})
            preview = resp[:100] + "..." if len(resp) > 100 else resp
            print(f"  → {preview}")
        except Exception as e:
            print(f"  → [오류] {e}")

    return posts


# ── 메인 ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("Layer A Cold Start Simulation — simrun-001")
    print(f"Seed   : 각인광장 베타 오픈 첫날")
    print(f"Model  : {MODEL}")
    print(f"Mode   : Cold Start (문화 바이블 없음)")
    print("=" * 60)

    # 인증
    creds = service_account.Credentials.from_service_account_file(
        str(KEY_PATH),
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    creds.refresh(Request())
    print("\n✓ Vertex AI 인증 완료")

    # 응답자 선발
    personas = load_personas(n=12, seed=42)
    print(f"✓ 응답자 {len(personas)}명 선발\n")
    for p in personas:
        print(f"  {p['id']}: {p.get('vocation')} {p.get('grade')} / "
              f"{p.get('dorm')} [{p.get('background_type')}]")

    # 시뮬레이션 실행
    r1_posts, first_movers = run_round1(creds, personas)
    r2_posts = run_round2(creds, personas, first_movers, r1_posts)
    all_posts = r1_posts + r2_posts

    # 결과 저장
    OUTPUT_DIR.mkdir(exist_ok=True)
    result = {
        "sim_id":       "simrun-001",
        "seed":         "각인광장 베타 오픈 첫날",
        "mode":         "cold_start",
        "model":        MODEL,
        "participants": len(personas),
        "rounds":       2,
        "logs": [
            {
                "round":      p["round"],
                "char_id":    p["char"]["id"],
                "vocation":   p["char"].get("vocation"),
                "grade":      p["char"].get("grade"),
                "dorm":       p["char"].get("dorm"),
                "background": p["char"].get("background_type"),
                "content":    p["content"],
            }
            for p in all_posts
        ],
    }

    out_path = OUTPUT_DIR / "simrun-001_cold_start.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 결과 저장: {out_path}")


if __name__ == "__main__":
    main()
