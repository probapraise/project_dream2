# Change Request

- change_id: CR-20260308-016
- date: 2026-03-08
- requester: writer
- status: done
- source_of_truth:
  - primary: world/live/world_bible/WB-0005_magic_system.md + world/live/world_bible/WB-0015_academy_bible.md
  - secondary: world/live/docs/world_bible_index_v2.md + world/live/population/core_cast/NC-0001_P-1027.md + scripts/population/*.py + artifacts/writing/episodes/ep001/*
  - history_only: docs/history/대화 로그.txt

## 1. 원 요청
- 마나 주색 체계에서 `보라`만 2음절이라 리듬이 어긋나므로, 문서 전체를 전수 조사해 `자` 기준으로 정리한다.

## 2. 정제된 목표 (1문장)
- 마나 7색 체계의 공식 명칭을 `적/청/녹/황/자/백/흑`으로 통일하고, 관련 탑/기숙사/계열 표기를 `자탑`, `자계열` 기준으로 재정렬한다.

## 3. 변경 유형
- modify

## 4. 성공 기준 (DoD)
- [x] active live 문서와 생성 스크립트에서 `보라` 주색이 `자(紫)`로 교정된다.
- [x] `보라탑`/`보라탑 기숙사` 표기가 `자탑`/`자탑 기숙사`로 교정된다.
- [x] 현재 집필 입력 산출물과 NC 카드도 같은 용어로 동기화된다.
- [x] history/archive 계열 보존 문서는 건드리지 않는다.

## 5. 예상 영향 범위 (초기)
- impacted_files:
  - world/live/world_bible/WB-0005_magic_system.md
  - world/live/world_bible/WB-0015_academy_bible.md
  - world/live/world_bible/WB-0026_appendix_crest_arcana.md
  - world/live/docs/master_map.md
  - world/live/docs/world_bible_index_v2.md
  - world/live/population/**
  - scripts/population/*.py
  - scripts/indexes/rebuild_character_index_v2.py
  - scripts/sim/sim_runner.py
  - artifacts/writing/episodes/ep001/*
- impacted_entities:
  - 마나 주색 공식 명칭
  - 자탑 기숙사/색역 명칭
  - 키리온의 주색 표기

## 6. 작가 확인 필요 항목
- Q1: 없음
- Q2: 없음

## 7. 승인 기록
- approved: yes
- approved_by: writer
- approved_at: 2026-03-08
- note: 사용자가 `보라` 대신 `자`를 공식 체계어로 쓰도록 active 문서 전체 정리를 직접 요청했다.
