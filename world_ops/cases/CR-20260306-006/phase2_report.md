# Phase 2 Report (Collision Scan)

- change_id: CR-20260306-006
- verdict: minor

## 1. 탐색 범위
- files:
  - artifacts/writing/README.md
  - artifacts/writing/episodes/ep000_prologue/*
  - artifacts/writing/episodes/ep001/*
  - docs/handoff/next_steps.md
  - world/live/docs/narrative_state.md
  - world/live/docs/episode_deltas.md
  - world/live/population/core_cast/NC-0001_P-1027.md
  - world/live/docs/voice_fingerprint_spec.md

## 2. 충돌 후보
- [x] 없음
- details:
  - 캐논 내용 자체를 바꾸는 작업이 아니라, 캐논 파일의 저장 위치와 명시 방식을 정리하는 구조 개편이다.

## 2-1. 충돌 로그 (필수 표)
| 충돌/변경 포인트 | 영향 범위 | 해결안(후보) | 관련 ID/키워드 | 상태(open/resolved/deferred) |
|---|---|---|---|---|
| 현재 캐논 파일이 episode 루트에 섞여 있어 최종본 식별이 어렵다 | 집필/참조 동선 혼란 | `canon/` 하위 폴더로 분리하고 `canon/README.md`로 current canon 명시 | `canon/`, `current_text_canon` | resolved |
| canon도 추후 수정될 수 있어 "최종본" 이름만으로는 운영이 경직된다 | 추후 revision 승격 시 혼선 | `canon/` 안에 versioned snapshot을 누적하고 current pointer만 갱신 | mutable canon, `revision_vN.*` | resolved |
| 새 episode 폴더를 수동 생성하면 `canon/` 규칙이 다시 빠질 수 있다 | 규칙 재발 누락 | `scripts/writing/new_episode_scaffold.sh` 추가 | episode scaffold | resolved |

## 3. 누락 후보
- [x] 없음
- details:
  - live 서사 문서와 VFP 출처 표기까지 같이 고쳐 경로 드리프트를 남기지 않는다.

## 4. 중복/불필요 정보 후보
- [x] 없음
- details:
  - 작업본(`revision_vN.txt`)과 정식 canon(`canon/revision_vN.txt`)은 역할을 분리해 중복 의미를 줄인다.

## 5. 판단 근거
- artifact reference: `artifacts/writing/README.md`가 episode 저장 구조의 1차 설명 문서다.
- live reference: `world/live/docs/narrative_state.md`, `episode_deltas.md`가 current canon 경로를 직접 참조한다.
- 운영 판단: "정식 canon은 명확해야 하지만 수정 가능해야 한다"는 작가 요구를 만족하려면 폴더 분리 + current pointer 조합이 가장 단순하다.

## 6. 분기 결정
- branch: minor
- reason: 서사 내용 retcon이 아니라 집필 산출물 구조와 경로 참조를 정리하는 운영 규칙 변경이다.

## 7. 작가 승인
- approved: yes
- note: 사용자 요청으로 `canon/` 구조와 mutable canon 규칙 도입 진행.
