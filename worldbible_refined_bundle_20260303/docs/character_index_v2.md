# character_index_v2 (population bootstrap)

- generated_at: 2026-03-04
- source_csv: `/home/dlwhdgus/project_dream2/worldbible_refined_bundle_20260303/population/population_slots.csv`
- total_p_slots: 3600
- ssot: `population/P-*.yaml` + `population/population_slots.csv`
- note: 기존 CH-* 카드/보이스팩 체계는 2026-03-04부로 폐기 완료(영구 삭제). 활성 캐릭터 체계는 `population/P-*`만 사용.

## 1) Status Registry
| status | count |
|---|---:|
| uninstantiated | 3593 |
| instantiated | 0 |
| named | 7 |

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
| 일반동(동관) | 1200 | 33.3% |
| 일반동(서관) | 1140 | 31.7% |
| 장학생동 | 620 | 17.2% |
| 연구·탑동 | 280 | 7.8% |
| 외국·인외동 | 200 | 5.6% |

## 3) Coordinate Occupancy Registry (v0 init)
- 좌표 스키마: `tower x grade_track x background_type x motivation_archetype`
- 현재 초기화 단계에서는 `tower/grade_track/motivation_archetype = UNASSIGNED`로 유지한다.
- 실제 점유는 `instantiated` 이상에서만 증가한다.

| tower | grade_track | background_type | motivation_archetype | slots | occupied(instantiated+) | available(uninstantiated) |
|---|---|---|---|---:|---:|---:|
| UNASSIGNED | UNASSIGNED | `common_noble` | UNASSIGNED | 2870 | 2 | 2868 |
| UNASSIGNED | UNASSIGNED | `commoner` | UNASSIGNED | 200 | 1 | 199 |
| UNASSIGNED | UNASSIGNED | `foreigner` | UNASSIGNED | 120 | 1 | 119 |
| UNASSIGNED | UNASSIGNED | `nonhuman` | UNASSIGNED | 250 | 1 | 249 |
| UNASSIGNED | UNASSIGNED | `signature_noble` | UNASSIGNED | 160 | 2 | 158 |

## 4) Reverse Indexes
### 4.1 Active Index (instantiated 이상만)
- active_count: 7
- pool_file: `docs/character_index_pools/active_instantiated_ids.txt`

### 4.2 Candidate Pools (P-* 전체에서 사전 계산)
- NFC 상위 20%: 720명 (`docs/character_index_pools/nfc_top20_ids.txt`)
- DT 상위 10%: 360명 (`docs/character_index_pools/dt_top10_ids.txt`)
- 인외 풀: 250명 (`docs/character_index_pools/nonhuman_ids.txt`)
- 외국인 풀: 120명 (`docs/character_index_pools/foreigner_ids.txt`)

샘플 ID:
- NFC top20 first 10: P-1160, P-1862, P-0930, P-0296, P-3487, P-2943, P-2277, P-2404, P-0555, P-1215
- DT top10 first 10: P-2093, P-3458, P-2388, P-3382, P-2869, P-3115, P-3373, P-2118, P-3392, P-0357

## 5) Step 5 DoD Check
- [x] 빅5/파생지표 기반 초기 레지스트리 생성
- [x] 좌표 점유 레지스트리 스키마 초기화
- [x] 반응자 선별용 역색인 파일 생성
- [x] 기존 CH-* 162개 + 보이스팩 체계 폐기 완료(2026-03-04, 영구 삭제)

## 6) Rebuild Command
```bash
python3 scripts/rebuild_character_index_v2.py
```
