# external_review/

외부 모델 또는 외부 자문자에게 한 번에 넘길 수 있도록 만든 비-SSOT 브리핑 산출물 저장소.

## 목적

- `world/live/`에 흩어진 활성 설정과 현재 서사 위치를 한 번에 설명하는 snapshot 문서를 보관한다.
- 이 폴더의 문서는 집필/시뮬레이션 오케스트레이션용 기본 로딩 문서가 아니다.
- live bundle을 대체하지 않는다. 실제 정본은 계속 `world/live/`와 관련 handoff 문서에 있다.

## 규칙

- 새 브리핑/도감은 날짜가 들어간 파일명으로 저장한다.
  - 예: `world_snapshot_external_review_20260310.md`
  - 예: `world_dossier_external_review_full_20260310.md`
- 문서 상단에 반드시 아래 메타를 적는다.
  - snapshot date
  - git commit
  - source priority
  - known drift
  - visibility policy
- 본문 안의 설정은 가능한 한 `[PUBLIC]`, `[CONFIDENTIAL]`, `[META]`를 유지한다.
- world_ops 절차, quarantine, batch/runs 로그, 원고 전체 텍스트는 기본적으로 제외한다.

## 문서 종류

- `world_snapshot_external_review_YYYYMMDD.md`
  - 짧은 외부 자문용 브리핑.
- `world_dossier_external_review_full_YYYYMMDD.md`
  - world bible 활성 문서와 현재 상태 보조 문서를 거의 전부 싣는 상세판.
  - 고급 모델에게 전수 점검과 아이디어 도출을 맡길 때 우선 사용한다.

## 생성 커맨드

```bash
bash scripts/indexes/build_external_review_dossier.sh
```

- 출력 기본 경로:
  - `artifacts/briefings/external_review/world_dossier_external_review_full_YYYYMMDD.md`
- 필요하면 첫 번째 인자로 출력 파일 경로를 직접 넘길 수 있다.

## 권장 구성

1. 문서 성격 / 스포일러 규칙
2. 포함 소스 manifest
3. world bible full inclusion
4. 현재 상태 보조 문서 full/excerpt inclusion
5. 외부 모델 질문 패키지

## 현재 파일

- `world_snapshot_external_review_20260310.md`
- `world_snapshot_external_review_20260313.md`
- `world_dossier_external_review_full_20260310.md`
