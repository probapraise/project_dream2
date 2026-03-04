# character_index_v2 (population bootstrap)

- generated_at: 2026-03-04
- source_csv: `/home/dlwhdgus/project_dream2/worldbible_refined_bundle_20260303/population/population_slots.csv`
- total_p_slots: 3600
- ssot: `population/P-*.yaml` + `population/population_slots.csv`
- note: 기존 CH-* 카드/보이스팩 체계는 2026-03-04부로 폐기 완료(영구 삭제). 활성 캐릭터 체계는 `population/P-*`만 사용.

## 1) Status Registry
| status | count |
|---|---:|
| uninstantiated | 3599 |
| instantiated | 0 |
| named | 1 |

## 2) Background Distribution
| background_type | label | count | ratio |
|---|---|---:|---:|
| `signature_noble` | 서명귀족 | 160 | 4.4% |
| `common_noble` | 일반귀족 | 2870 | 79.7% |
| `commoner` | 평민(몰락귀족 편입) | 200 | 5.6% |
| `foreigner` | 외국인 | 120 | 3.3% |
| `nonhuman` | 인외 | 250 | 6.9% |

## 2.1 Dorm Distribution
| dorm | count | ratio |
|---|---:|---:|
| 비전관 | 160 | 4.4% |
| 청탑 기숙사 | 521 | 14.5% |
| 황탑 기숙사 | 397 | 11.0% |
| 적탑 기숙사 | 336 | 9.3% |
| 녹탑 기숙사 | 294 | 8.2% |
| 백탑 기숙사 | 278 | 7.7% |
| 보라탑 기숙사 | 245 | 6.8% |
| 흑탑 기숙사 | 43 | 1.2% |
| 기사동 | 980 | 27.2% |
| 신전동군 | 346 | 9.6% |

## 3) Coordinate Occupancy Registry (v1)
- 좌표 스키마: `mana_color x grade x background_type x motivation_archetype`
- 현재 데이터에는 `motivation_archetype` 필드가 없어 `UNASSIGNED`로 고정한다.
- 실제 점유는 `instantiated` 이상에서만 증가한다.

| mana_color | grade | background_type | motivation_archetype | slots | occupied(instantiated+) | available(uninstantiated) |
|---|---|---|---|---:|---:|---:|
| 청 | 1학년 | `common_noble` | UNASSIGNED | 187 | 0 | 187 |
| 청 | 1학년 | `commoner` | UNASSIGNED | 8 | 0 | 8 |
| 청 | 1학년 | `foreigner` | UNASSIGNED | 13 | 0 | 13 |
| 청 | 1학년 | `nonhuman` | UNASSIGNED | 26 | 0 | 26 |
| 청 | 1학년 | `signature_noble` | UNASSIGNED | 8 | 0 | 8 |
| 청 | 2학년 | `common_noble` | UNASSIGNED | 174 | 0 | 174 |
| 청 | 2학년 | `commoner` | UNASSIGNED | 9 | 0 | 9 |
| 청 | 2학년 | `foreigner` | UNASSIGNED | 11 | 0 | 11 |
| 청 | 2학년 | `nonhuman` | UNASSIGNED | 18 | 0 | 18 |
| 청 | 2학년 | `signature_noble` | UNASSIGNED | 13 | 0 | 13 |
| 청 | 3학년 | `common_noble` | UNASSIGNED | 160 | 0 | 160 |
| 청 | 3학년 | `commoner` | UNASSIGNED | 19 | 0 | 19 |
| 청 | 3학년 | `foreigner` | UNASSIGNED | 8 | 0 | 8 |
| 청 | 3학년 | `nonhuman` | UNASSIGNED | 8 | 0 | 8 |
| 청 | 3학년 | `signature_noble` | UNASSIGNED | 8 | 0 | 8 |
| 청 | 4학년 | `common_noble` | UNASSIGNED | 165 | 0 | 165 |
| 청 | 4학년 | `commoner` | UNASSIGNED | 3 | 0 | 3 |
| 청 | 4학년 | `foreigner` | UNASSIGNED | 6 | 0 | 6 |
| 청 | 4학년 | `nonhuman` | UNASSIGNED | 12 | 0 | 12 |
| 청 | 4학년 | `signature_noble` | UNASSIGNED | 8 | 0 | 8 |
| 청 | 연구과정 | `common_noble` | UNASSIGNED | 32 | 0 | 32 |
| 청 | 연구과정 | `commoner` | UNASSIGNED | 1 | 0 | 1 |
| 청 | 연구과정 | `nonhuman` | UNASSIGNED | 3 | 0 | 3 |
| 황 | 1학년 | `common_noble` | UNASSIGNED | 139 | 0 | 139 |
| 황 | 1학년 | `commoner` | UNASSIGNED | 10 | 0 | 10 |
| 황 | 1학년 | `foreigner` | UNASSIGNED | 4 | 0 | 4 |
| 황 | 1학년 | `nonhuman` | UNASSIGNED | 9 | 0 | 9 |
| 황 | 1학년 | `signature_noble` | UNASSIGNED | 5 | 0 | 5 |
| 황 | 2학년 | `common_noble` | UNASSIGNED | 118 | 0 | 118 |
| 황 | 2학년 | `commoner` | UNASSIGNED | 13 | 0 | 13 |
| 황 | 2학년 | `foreigner` | UNASSIGNED | 9 | 0 | 9 |
| 황 | 2학년 | `nonhuman` | UNASSIGNED | 13 | 0 | 13 |
| 황 | 2학년 | `signature_noble` | UNASSIGNED | 5 | 0 | 5 |
| 황 | 3학년 | `common_noble` | UNASSIGNED | 111 | 0 | 111 |
| 황 | 3학년 | `commoner` | UNASSIGNED | 12 | 0 | 12 |
| 황 | 3학년 | `foreigner` | UNASSIGNED | 1 | 0 | 1 |
| 황 | 3학년 | `nonhuman` | UNASSIGNED | 10 | 0 | 10 |
| 황 | 3학년 | `signature_noble` | UNASSIGNED | 10 | 0 | 10 |
| 황 | 4학년 | `common_noble` | UNASSIGNED | 122 | 0 | 122 |
| 황 | 4학년 | `commoner` | UNASSIGNED | 11 | 0 | 11 |
| 황 | 4학년 | `foreigner` | UNASSIGNED | 6 | 0 | 6 |
| 황 | 4학년 | `nonhuman` | UNASSIGNED | 9 | 0 | 9 |
| 황 | 4학년 | `signature_noble` | UNASSIGNED | 5 | 0 | 5 |
| 황 | 연구과정 | `common_noble` | UNASSIGNED | 26 | 0 | 26 |
| 황 | 연구과정 | `nonhuman` | UNASSIGNED | 1 | 0 | 1 |
| 황 | 연구과정 | `signature_noble` | UNASSIGNED | 1 | 0 | 1 |
| 적 | 1학년 | `common_noble` | UNASSIGNED | 119 | 0 | 119 |
| 적 | 1학년 | `commoner` | UNASSIGNED | 6 | 0 | 6 |
| 적 | 1학년 | `foreigner` | UNASSIGNED | 4 | 0 | 4 |
| 적 | 1학년 | `nonhuman` | UNASSIGNED | 8 | 0 | 8 |
| 적 | 1학년 | `signature_noble` | UNASSIGNED | 2 | 0 | 2 |
| 적 | 2학년 | `common_noble` | UNASSIGNED | 133 | 0 | 133 |
| 적 | 2학년 | `commoner` | UNASSIGNED | 13 | 0 | 13 |
| 적 | 2학년 | `foreigner` | UNASSIGNED | 1 | 0 | 1 |
| 적 | 2학년 | `nonhuman` | UNASSIGNED | 13 | 0 | 13 |
| 적 | 2학년 | `signature_noble` | UNASSIGNED | 10 | 0 | 10 |
| 적 | 3학년 | `common_noble` | UNASSIGNED | 106 | 0 | 106 |
| 적 | 3학년 | `commoner` | UNASSIGNED | 6 | 0 | 6 |
| 적 | 3학년 | `foreigner` | UNASSIGNED | 8 | 0 | 8 |
| 적 | 3학년 | `nonhuman` | UNASSIGNED | 9 | 0 | 9 |
| 적 | 3학년 | `signature_noble` | UNASSIGNED | 9 | 0 | 9 |
| 적 | 4학년 | `common_noble` | UNASSIGNED | 98 | 0 | 98 |
| 적 | 4학년 | `commoner` | UNASSIGNED | 8 | 0 | 8 |
| 적 | 4학년 | `foreigner` | UNASSIGNED | 6 | 0 | 6 |
| 적 | 4학년 | `nonhuman` | UNASSIGNED | 10 | 0 | 10 |
| 적 | 4학년 | `signature_noble` | UNASSIGNED | 8 | 0 | 8 |
| 적 | 연구과정 | `common_noble` | UNASSIGNED | 17 | 0 | 17 |
| 적 | 연구과정 | `commoner` | UNASSIGNED | 3 | 0 | 3 |
| 적 | 연구과정 | `nonhuman` | UNASSIGNED | 1 | 0 | 1 |
| 적 | 연구과정 | `signature_noble` | UNASSIGNED | 2 | 0 | 2 |
| 녹 | 1학년 | `common_noble` | UNASSIGNED | 95 | 0 | 95 |
| 녹 | 1학년 | `commoner` | UNASSIGNED | 6 | 0 | 6 |
| 녹 | 1학년 | `foreigner` | UNASSIGNED | 3 | 0 | 3 |
| 녹 | 1학년 | `nonhuman` | UNASSIGNED | 10 | 0 | 10 |
| 녹 | 1학년 | `signature_noble` | UNASSIGNED | 5 | 0 | 5 |
| 녹 | 2학년 | `common_noble` | UNASSIGNED | 93 | 0 | 93 |
| 녹 | 2학년 | `commoner` | UNASSIGNED | 11 | 0 | 11 |
| 녹 | 2학년 | `foreigner` | UNASSIGNED | 2 | 0 | 2 |
| 녹 | 2학년 | `nonhuman` | UNASSIGNED | 8 | 0 | 8 |
| 녹 | 2학년 | `signature_noble` | UNASSIGNED | 3 | 0 | 3 |
| 녹 | 3학년 | `common_noble` | UNASSIGNED | 111 | 0 | 111 |
| 녹 | 3학년 | `commoner` | UNASSIGNED | 9 | 0 | 9 |
| 녹 | 3학년 | `foreigner` | UNASSIGNED | 5 | 0 | 5 |
| 녹 | 3학년 | `nonhuman` | UNASSIGNED | 11 | 0 | 11 |
| 녹 | 3학년 | `signature_noble` | UNASSIGNED | 6 | 0 | 6 |
| 녹 | 4학년 | `common_noble` | UNASSIGNED | 97 | 0 | 97 |
| 녹 | 4학년 | `commoner` | UNASSIGNED | 6 | 0 | 6 |
| 녹 | 4학년 | `foreigner` | UNASSIGNED | 5 | 0 | 5 |
| 녹 | 4학년 | `nonhuman` | UNASSIGNED | 6 | 0 | 6 |
| 녹 | 4학년 | `signature_noble` | UNASSIGNED | 4 | 0 | 4 |
| 녹 | 연구과정 | `common_noble` | UNASSIGNED | 14 | 0 | 14 |
| 녹 | 연구과정 | `commoner` | UNASSIGNED | 2 | 0 | 2 |
| 녹 | 연구과정 | `nonhuman` | UNASSIGNED | 2 | 0 | 2 |
| 녹 | 연구과정 | `signature_noble` | UNASSIGNED | 1 | 0 | 1 |
| 백 | 1학년 | `common_noble` | UNASSIGNED | 93 | 0 | 93 |
| 백 | 1학년 | `commoner` | UNASSIGNED | 6 | 0 | 6 |
| 백 | 1학년 | `foreigner` | UNASSIGNED | 4 | 0 | 4 |
| 백 | 1학년 | `nonhuman` | UNASSIGNED | 7 | 0 | 7 |
| 백 | 1학년 | `signature_noble` | UNASSIGNED | 6 | 0 | 6 |
| 백 | 2학년 | `common_noble` | UNASSIGNED | 93 | 0 | 93 |
| 백 | 2학년 | `commoner` | UNASSIGNED | 1 | 0 | 1 |
| 백 | 2학년 | `foreigner` | UNASSIGNED | 4 | 0 | 4 |
| 백 | 2학년 | `nonhuman` | UNASSIGNED | 11 | 0 | 11 |
| 백 | 2학년 | `signature_noble` | UNASSIGNED | 8 | 0 | 8 |
| 백 | 3학년 | `common_noble` | UNASSIGNED | 77 | 0 | 77 |
| 백 | 3학년 | `commoner` | UNASSIGNED | 6 | 0 | 6 |
| 백 | 3학년 | `foreigner` | UNASSIGNED | 2 | 0 | 2 |
| 백 | 3학년 | `nonhuman` | UNASSIGNED | 8 | 0 | 8 |
| 백 | 3학년 | `signature_noble` | UNASSIGNED | 3 | 0 | 3 |
| 백 | 4학년 | `common_noble` | UNASSIGNED | 81 | 0 | 81 |
| 백 | 4학년 | `commoner` | UNASSIGNED | 6 | 0 | 6 |
| 백 | 4학년 | `foreigner` | UNASSIGNED | 1 | 0 | 1 |
| 백 | 4학년 | `nonhuman` | UNASSIGNED | 2 | 0 | 2 |
| 백 | 4학년 | `signature_noble` | UNASSIGNED | 7 | 0 | 7 |
| 백 | 연구과정 | `common_noble` | UNASSIGNED | 14 | 0 | 14 |
| 백 | 연구과정 | `commoner` | UNASSIGNED | 2 | 0 | 2 |
| 백 | 연구과정 | `foreigner` | UNASSIGNED | 1 | 0 | 1 |
| 백 | 연구과정 | `nonhuman` | UNASSIGNED | 3 | 0 | 3 |
| 백 | 연구과정 | `signature_noble` | UNASSIGNED | 4 | 0 | 4 |
| 보라 | 1학년 | `common_noble` | UNASSIGNED | 87 | 1 | 86 |
| 보라 | 1학년 | `commoner` | UNASSIGNED | 4 | 0 | 4 |
| 보라 | 1학년 | `foreigner` | UNASSIGNED | 2 | 0 | 2 |
| 보라 | 1학년 | `nonhuman` | UNASSIGNED | 4 | 0 | 4 |
| 보라 | 1학년 | `signature_noble` | UNASSIGNED | 4 | 0 | 4 |
| 보라 | 2학년 | `common_noble` | UNASSIGNED | 78 | 0 | 78 |
| 보라 | 2학년 | `commoner` | UNASSIGNED | 7 | 0 | 7 |
| 보라 | 2학년 | `foreigner` | UNASSIGNED | 2 | 0 | 2 |
| 보라 | 2학년 | `nonhuman` | UNASSIGNED | 6 | 0 | 6 |
| 보라 | 2학년 | `signature_noble` | UNASSIGNED | 3 | 0 | 3 |
| 보라 | 3학년 | `common_noble` | UNASSIGNED | 100 | 0 | 100 |
| 보라 | 3학년 | `commoner` | UNASSIGNED | 4 | 0 | 4 |
| 보라 | 3학년 | `foreigner` | UNASSIGNED | 3 | 0 | 3 |
| 보라 | 3학년 | `nonhuman` | UNASSIGNED | 7 | 0 | 7 |
| 보라 | 3학년 | `signature_noble` | UNASSIGNED | 2 | 0 | 2 |
| 보라 | 4학년 | `common_noble` | UNASSIGNED | 75 | 0 | 75 |
| 보라 | 4학년 | `commoner` | UNASSIGNED | 4 | 0 | 4 |
| 보라 | 4학년 | `foreigner` | UNASSIGNED | 6 | 0 | 6 |
| 보라 | 4학년 | `nonhuman` | UNASSIGNED | 5 | 0 | 5 |
| 보라 | 4학년 | `signature_noble` | UNASSIGNED | 7 | 0 | 7 |
| 보라 | 연구과정 | `common_noble` | UNASSIGNED | 13 | 0 | 13 |
| 보라 | 연구과정 | `commoner` | UNASSIGNED | 2 | 0 | 2 |
| 보라 | 연구과정 | `nonhuman` | UNASSIGNED | 2 | 0 | 2 |
| 보라 | 연구과정 | `signature_noble` | UNASSIGNED | 1 | 0 | 1 |
| 흑 | 1학년 | `common_noble` | UNASSIGNED | 10 | 0 | 10 |
| 흑 | 1학년 | `foreigner` | UNASSIGNED | 1 | 0 | 1 |
| 흑 | 1학년 | `nonhuman` | UNASSIGNED | 3 | 0 | 3 |
| 흑 | 1학년 | `signature_noble` | UNASSIGNED | 2 | 0 | 2 |
| 흑 | 2학년 | `common_noble` | UNASSIGNED | 15 | 0 | 15 |
| 흑 | 2학년 | `commoner` | UNASSIGNED | 1 | 0 | 1 |
| 흑 | 2학년 | `nonhuman` | UNASSIGNED | 1 | 0 | 1 |
| 흑 | 3학년 | `common_noble` | UNASSIGNED | 6 | 0 | 6 |
| 흑 | 3학년 | `commoner` | UNASSIGNED | 1 | 0 | 1 |
| 흑 | 3학년 | `foreigner` | UNASSIGNED | 1 | 0 | 1 |
| 흑 | 3학년 | `nonhuman` | UNASSIGNED | 3 | 0 | 3 |
| 흑 | 4학년 | `common_noble` | UNASSIGNED | 9 | 0 | 9 |
| 흑 | 4학년 | `foreigner` | UNASSIGNED | 1 | 0 | 1 |
| 흑 | 4학년 | `nonhuman` | UNASSIGNED | 1 | 0 | 1 |
| 흑 | 연구과정 | `common_noble` | UNASSIGNED | 2 | 0 | 2 |

## 4) Reverse Indexes
### 4.1 Active Index (instantiated 이상만)
- active_count: 1
- pool_file: `docs/character_index_pools/active_instantiated_ids.txt`

### 4.2 Candidate Pools (P-* 전체에서 사전 계산)
- NFC 상위 20%: 720명 (`docs/character_index_pools/nfc_top20_ids.txt`)
- DT 상위 10%: 360명 (`docs/character_index_pools/dt_top10_ids.txt`)
- 인외 풀: 250명 (`docs/character_index_pools/nonhuman_ids.txt`)
- 외국인 풀: 120명 (`docs/character_index_pools/foreigner_ids.txt`)

샘플 ID:
- NFC top20 first 10: P-0248, P-0306, P-0542, P-0623, P-0708, P-0930, P-2323, P-2350, P-2795, P-3539
- DT top10 first 10: P-3142, P-0186, P-0140, P-0227, P-1054, P-2000, P-2054, P-2776, P-2167, P-0651

## 5) Step 5 DoD Check
- [x] 빅5/파생지표 기반 초기 레지스트리 생성
- [x] 좌표 점유 레지스트리 스키마 초기화
- [x] 반응자 선별용 역색인 파일 생성
- [x] 기존 CH-* 162개 + 보이스팩 체계 폐기 완료(2026-03-04, 영구 삭제)

## 6) Rebuild Command
```bash
python3 scripts/rebuild_character_index_v2.py
```
