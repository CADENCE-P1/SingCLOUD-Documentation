# SingCLOUD — Laboratory Item FIL

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024_P1.csv` |
| 2 | `VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024_P2.csv` |

Both sit under the prefix `common-data/SingCLoud/FreeText_FTA/`. Two objects, 14,392,594 rows,
16 columns each.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **`FIL` is undefined** — the only thing distinguishing this name from `VW_LABORATORY_F` | Ask the owner. It determines whether these are the same investigations at a different grain |
| 🟡 | **`BATTERY_ID_EXTN`** here vs **`BATTERY_ID_EXT`** in Laboratory and Radiology | Two of three families use the short form. Confirm before joining on it |
| 🟡 | **The abnormal-flag pair is not co-populated** — `_ETS_ID` ~10% empty, `_ORI_TXT` ~93% | Do not substitute one for the other |
| ✅ | **Both partitions fully transcribed** — schema consistency is verified, not assumed | — |

---

## Dataset Overview

**Category:** Laboratory item FIL — taken from the dataset name. Not yet confirmed against a
data dictionary or the data owner. **What `FIL` stands for is unknown**, and it is the part of
the name that most needs an answer: it distinguishes this family from
[Laboratory](singcloud-laboratory.md) and nothing here explains how.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.
`FACILITY_EXTN` is present and 0.0% missing, so the answer is in the data, but it has not been
enumerated here.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established. `ITEM_SEQ_NO` exists alongside
`BATTERY_ID_ROOT`, which is the shape a repeating sequence within a battery takes — but that
reading is not established and is not assumed here.

**Rows vs people:** 14,392,594 rows (profiler, 2026-07-23, two objects summed); distinct
patients **not counted**.

**What is *not* in it:** Unknown — to be filled in. The 16 column names in *Key Variables*
are the complete column list for both objects.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/FreeText_FTA/VW_LABORATORY_ITEM_FIL_F_Export_28-07-2024_P{1,2}.csv` |
| **Partitions** | 2 objects, P1 and P2, contiguous |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. Both object names contain `_Export_28-07-2024_` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. The objects sit under a path segment named `FreeText_FTA` |

---

## Key Variables

All 16 columns, in the order printed in the report. Names, order and types verified
**identical in both objects** — the only family in the catalogue so far where every partition
has been transcribed in full.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

| # | Variable | Type | P1 | P2 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | 0.0 | | | | |
| 2 | `BATTERY_ID_ROOT` | id_like | 0.0 | 0.0 | | | | |
| 3 | `FACILITY_EXTN` | categorical | 0.0 | 0.0 | | | | |
| 4 | `PATIENT_ID_EXTN_X` | id_like | 0.0 | 0.0 | | | | |
| 5 | `DISPLAY_DATE_X` | date | 0.0 | 0.0 | | | | |
| 6 | `DISPLAY_DATE_Z` | date | 0.0 | 0.0 | | | | |
| 7 | `ITEM_SEQ_NO` | numeric | 0.0 | 0.0 | | | | |
| 8 | `ITEM_NAME_ETS_ID` | categorical | 0.0 | 0.0 | | | | |
| 9 | `ITEM_NAME_ORI_TXT` | categorical | 0.55 | 0.0 | | | | |
| 10 | `ITEM_NUMERIC_VALUE` | numeric | 2.96 | 2.83 | | | | |
| 11 | `ITEM_NUMERIC_VALUE_UOM` | categorical | 3.04 | 2.88 | | | | |
| 12 | `ITEM_REFERENCE_RANGE` | categorical | 18.02 | 18.02 | | | | |
| 13 | `ITEM_ABNORMAL_FLAG_ETS_ID` | categorical | 10.30 | 10.22 | | | | |
| 14 | `ITEM_ABNORMAL_FLAG_ORI_TXT` | categorical | 92.42 | 94.67 | | | | |
| 15 | `ITEM_STATUS_ETS_ID` | categorical | 0.0 | 0.0 | | | | |
| 16 | `BATTERY_ID_EXTN` | id_like | 0.0 | 0.0 | | | | |

*(P1 and P2 are missing %; profiler, 2026-07-23)*

**`ITEM_ABNORMAL_FLAG_ETS_ID` is ~10% empty while `ITEM_ABNORMAL_FLAG_ORI_TXT` is ~93% empty**,
despite the apparent pairing. Whatever the relationship between the `_ETS_ID` and `_ORI_TXT`
forms, they are not populated together here. Do not substitute one for the other without an
answer.

**`ITEM_REFERENCE_RANGE` is 18.02% empty in both objects** — the same figure to two decimal
places across 14.4 million rows in two separate files.

**Note `BATTERY_ID_EXTN` — with an N.** [Laboratory](singcloud-laboratory.md) carries
`BATTERY_ID_EXT`, without. The two families both carry `BATTERY_ID_ROOT` spelled identically,
so the difference is in one column only. Copy each character for character; this is exactly
the kind of near-match that produces a silent zero-row join.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `DISPLAY_DATE_X` | Unknown | Unknown | — |
| `DISPLAY_DATE_Z` | Unknown | Unknown | — |

Two date columns, both fully populated in both objects. No range is established.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If either column is month-first, every date derived from it is wrong and nothing
raises.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown. The `_P{n}` split is not established as
temporal, so per-partition figures are not a time series.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `…_P1.csv` | 2,189.77 | 8,970,688 | 16 | 7.96 |
| `…_P2.csv` | 1,323.26 | 5,421,906 | 16 | 8.04 |
| **Family total** | **3,513.03** | **14,392,594** | 16 | — |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

Family size and rows are sums of the two reported figures. Family missing % is left blank
deliberately: the per-object percentages are shares of two different denominators and cannot
be averaged.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | **Yes, fully verified** — 16 columns, same names in the same order with the same types, in both objects |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** Unknown — to confirm with data owner. No column carries a `_STD`
suffix, but `ITEM_NAME_ETS_ID` / `ITEM_NAME_ORI_TXT` and
`ITEM_ABNORMAL_FLAG_ETS_ID` / `ITEM_ABNORMAL_FLAG_ORI_TXT` form apparent code-and-text pairs.
What either suffix denotes is unconfirmed.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. Given that `ITEM_ABNORMAL_FLAG` is a judgement about a result rather than the result
itself, this is a field where the Raw / Derived distinction will matter.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 7.96% (P1) and 8.04% (P2) (profiler, 2026-07-23) |
| Columns >50% missing | 1 of 16 in both objects (`ITEM_ABNORMAL_FLAG_ORI_TXT`) |
| Columns 100% missing | 0 of 16 |

No interpretation of the missingness is offered here.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.
`ITEM_NUMERIC_VALUE` at ~3% empty is the obvious candidate for a result-value column, but that
reading is not established.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Eight columns report 0.0% missing in both objects and the check is outstanding for every one of them. `ITEM_NUMERIC_VALUE` is the priority: on a numeric result column, a recorded `0` and an unrecorded value are different facts that the profiler cannot distinguish.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `PATIENT_ID_EXTN_X`. The patient ID column is the primary identifier
for every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. The name matches the identifier
column in [Laboratory](singcloud-laboratory.md),
[Event Diagnosis](singcloud-event-diagnosis.md) and the dispensed-medication families, but
**no join has been tested**.

**Secondary keys:** Unknown. `BATTERY_ID_ROOT` and `BATTERY_ID_EXTN` also profile as
`id_like`.

**Coding standards:** Unknown — to confirm with data owner.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| [Laboratory](singcloud-laboratory.md) | Unknown | Unknown | Unknown | **no join tested** | The two families share `BATTERY_ID_ROOT`, `PATIENT_ID_EXTN_X`, `FACILITY_EXTN`, `DISPLAY_DATE_X` and `_Z` by name, and the naming suggests a battery-to-item relationship. **Nothing establishes that.** Note the `BATTERY_ID_EXT` / `BATTERY_ID_EXTN` discrepancy before attempting a join on that column |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked.
- **Schema drift across partitions:** None — both objects fully verified identical. This is the
  only family in the catalogue where that can be said.
- **Value-range anomalies:** Not checked. `ITEM_NUMERIC_VALUE` is an unbounded numeric holding
  results across an unknown range of analytes, so a single global range check would not be
  meaningful; it needs checking per item.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Fitness for purpose:** **Cannot be assessed yet.** This page establishes neither what the
  dataset is nor what one row represents.

---

## Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |
| **Sensitivity classification** | Unknown — to confirm with data owner |
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. The profiler typed `BATTERY_ID_ROOT`, `PATIENT_ID_EXTN_X` and `BATTERY_ID_EXTN` as `id_like`. `ITEM_NAME_ORI_TXT` and `ITEM_ABNORMAL_FLAG_ORI_TXT` carry the `_ORI_TXT` suffix that elsewhere in the catalogue accompanies as-entered text, so they are the candidates for free-text content — unconfirmed. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. **What does `FIL` stand for?** It is the only thing distinguishing this family's name from
   `VW_LABORATORY_F`.
2. **What is the relationship between this family and `VW_LABORATORY_F`?** Does
   `BATTERY_ID_ROOT` join them, and at what cardinality?
3. Why does Laboratory carry `BATTERY_ID_EXT` and this family `BATTERY_ID_EXTN`? Are they the
   same thing?
4. What is the unit of observation — one row per result item within a battery?
5. What is this dataset, in one paragraph?
6. Which population is included, and who is excluded by what mechanism?
7. Is there a data dictionary? All 16 columns are currently undescribed and unclassified.
8. What do the `_ETS_ID` and `_ORI_TXT` suffixes denote, and which of a pair should be
   preferred?
9. Why is `ITEM_ABNORMAL_FLAG_ORI_TXT` ~93% empty while `ITEM_ABNORMAL_FLAG_ETS_ID` is ~10%
   empty? Are they populated by different systems?
10. `ITEM_ABNORMAL_FLAG` is a judgement about a result. Who or what assigns it, and against
    which reference range?
11. Is `ITEM_REFERENCE_RANGE` a free-text string or a structured value?
12. Is `ITEM_NUMERIC_VALUE` comparable across items, or does it need `ITEM_NUMERIC_VALUE_UOM`
    to be interpreted? Are units consistent per item?
13. Is a `0` in `ITEM_NUMERIC_VALUE` a real result or an unrecorded value?
14. Is `PATIENT_ID_EXTN_X` a pseudonym, and is it stable across datasets and across successive
    extracts of this one?
15. What is the delimiter and file encoding, and are both objects the same?
16. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 16 rows, matching the 16 columns declared for both objects.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Two objects, 14,392,594 rows, 16 columns. Both objects transcribed in full from the screenshots. Category from the dataset name and `PATIENT_ID_EXTN_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — the complete P1 and P2 blocks, read from
  `source_material/screenshots/mass_columns_screenshots/section_04.png`.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names. For this
  family the reconstruction is badly wrong — it recovers 159 distinct column names for a
  16-column object, having read across a block boundary.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.
