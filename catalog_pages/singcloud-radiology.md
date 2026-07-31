# SingCLOUD — Radiology

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_RADIOLOGY_F_Export_06-08-2024.csv` |

Under the prefix `common-data/SingCLoud/FreeText_FTA/`. One object, 6,569,893 rows, 28
columns, unpartitioned.

**This is the largest unpartitioned object in the catalogue** — 2.6 GB in a single file, where
comparable volumes elsewhere are split across 11 to 33 partitions.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **`INVESTIGATION_NAME_ORI_TXT_STD` is 80.75% empty** — against ~52% in Laboratory | Four in five rows unmapped. Anything depending on it is not reproducible until the mapping and failed-match rule are documented |
| 🟡 | **Date columns differ sharply in completeness** — `EXAMINATION_DATE` 0.89% empty, `REPORTED_DATE` 47.9%, `ORDER_DATE` 49.23% | Choose deliberately; two of the four lose half the rows |
| 🟡 | **Schema sits between the two Laboratory families** — 19 columns shared with Laboratory, 5 with Laboratory Item FIL | Suggestive of one investigation model, but no join has been tested |
| 🟡 | **2.6 GB in a single unpartitioned file** — the largest such object in the catalogue | Cannot be processed partition-wise like the billing families |
| 🟡 | Sits under `FreeText_FTA/` but has **no obvious narrative column** | Confirm whether report text was dropped from this view |

---

## Dataset Overview

**Category:** Radiology — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.
`FACILITY_EXTN` is present and 1.55% missing, so the answer is in the data, but it has not
been enumerated here.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established.

**Rows vs people:** 6,569,893 rows (profiler, 2026-07-23, single object); distinct patients
**not counted**.

**What is *not* in it:** Unknown — to be filled in. The 28 column names in *Key Variables* are
the complete column list. What *can* be said exactly: there is no column holding a report
body or narrative text, despite the object sitting under `FreeText_FTA/`.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/FreeText_FTA/VW_RADIOLOGY_F_Export_06-08-2024.csv` |
| **Partitions** | 1 object, unpartitioned |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. The object name contains `_Export_06-08-2024` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. The object sits under a path segment named `FreeText_FTA`, but no column on this page obviously holds narrative text |

---

## Key Variables

All 28 columns, in the order printed in the report, transcribed in full.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

| # | Variable | Type | Missing % | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | | | | |
| 2 | `BATTERY_ACT_ID` | numeric | 0.0 | | | | |
| 3 | `BATTERY_VER_NUM` | numeric | 0.0 | | | | |
| 4 | `BATTERY_ID_ROOT` | id_like | 0.0 | | | | |
| 5 | `INVESTIGATION_NAME_ETS_ID` | categorical | 0.0 | | | | |
| 6 | `INVESTIGATION_NAME_ORI_TXT` | categorical | 0.0 | | | | |
| 7 | `INVESTIGATION_NAME_ORI_TXT_STD` | categorical | 80.75 | | | | |
| 8 | `PATIENT_ID_EXTN_X` | id_like | 0.0 | | | | |
| 9 | `SOURCE_EXTN_TEXT` | categorical | 0.0 | | | | |
| 10 | `FACILITY_EXTN` | categorical | 1.55 | | | | |
| 11 | `INV_RESULT_STATUS_ETS_ID` | categorical | 0.0 | | | | |
| 12 | `INV_TYPE_NAME_ETS_ID` | categorical | 0.0 | | | | |
| 13 | `INV_SUBTYPE_NAME_ETS_ID` | categorical | 0.0 | | | | |
| 14 | `ORDER_DATE_X` | date | 49.23 | | | | |
| 15 | `ORDER_DATE_Z` | date | 49.23 | | | | |
| 16 | `REPORTED_DATE_X` | date | 47.90 | | | | |
| 17 | `REPORTED_DATE_Z` | date | 47.90 | | | | |
| 18 | `EXAMINATION_DATE_X` | date | 0.89 | | | | |
| 19 | `EXAMINATION_DATE_Z` | date | 0.89 | | | | |
| 20 | `DISPLAY_DATE_X` | date | 0.0 | | | | |
| 21 | `DISPLAY_DATE_Z` | date | 0.0 | | | | |
| 22 | `ITEM_NAME_ETS_ID` | categorical | 0.0 | | | | |
| 23 | `ITEM_NAME_ORI_TXT` | categorical | 0.0 | | | | |
| 24 | `ITEM_ABNORMAL_FLAG_ETS_ID` | categorical | 5.27 | | | | |
| 25 | `ITEM_ABNORMAL_FLAG_ORI_TXT` | categorical | 82.43 | | | | |
| 26 | `ITEM_STATUS_ETS_ID` | categorical | 0.0 | | | | |
| 27 | `BATTERY_ID_EXT` | id_like | 0.0 | | | | |
| 28 | `EVENT_EXT` | id_like | 0.69 | | | | |

*(profiler, 2026-07-23)*

**`INVESTIGATION_NAME_ORI_TXT_STD` is 80.75% empty** while its unstandardised partner
`INVESTIGATION_NAME_ORI_TXT` is 0.0%. Four in five rows have an investigation name but no
standardised form. In [Laboratory](singcloud-laboratory.md) the same column is only ~52%
empty, so whatever mapping produces it covers radiology far less well than laboratory.

**`ITEM_ABNORMAL_FLAG_ETS_ID` (5.27%) and `ITEM_ABNORMAL_FLAG_ORI_TXT` (82.43%) are not
populated together**, the same pattern as
[Laboratory Item FIL](singcloud-laboratory-item-fil.md).

### This schema sits between the two Laboratory families

Nineteen of these 28 columns also appear in [Laboratory](singcloud-laboratory.md), five more
appear in [Laboratory Item FIL](singcloud-laboratory-item-fil.md), and four are unique here.

| Group | Columns |
|---|---|
| **Shared with Laboratory** | `DATA_SOURCE`, `BATTERY_ACT_ID`, `BATTERY_VER_NUM`, `BATTERY_ID_ROOT`, `INVESTIGATION_NAME_ETS_ID`, `INVESTIGATION_NAME_ORI_TXT`, `INVESTIGATION_NAME_ORI_TXT_STD`, `PATIENT_ID_EXTN_X`, `SOURCE_EXTN_TEXT`, `FACILITY_EXTN`, `INV_RESULT_STATUS_ETS_ID`, `INV_TYPE_NAME_ETS_ID`, `INV_SUBTYPE_NAME_ETS_ID`, `ORDER_DATE_X`/`_Z`, `DISPLAY_DATE_X`/`_Z`, `BATTERY_ID_EXT`, `EVENT_EXT` |
| **Shared with Laboratory Item FIL** | `ITEM_NAME_ETS_ID`, `ITEM_NAME_ORI_TXT`, `ITEM_ABNORMAL_FLAG_ETS_ID`, `ITEM_ABNORMAL_FLAG_ORI_TXT`, `ITEM_STATUS_ETS_ID` |
| **Unique to Radiology** | `REPORTED_DATE_X`/`_Z`, `EXAMINATION_DATE_X`/`_Z` |
| **In Laboratory but absent here** | `SPECIMEN_COLLECTED_DATE_X`/`_Z`, `SPECIMEN_RECEIVED_DATE_X`/`_Z` |

The specimen columns are gone and examination/reported dates take their place. **This is an
observation about column names, not an established relationship** — no join has been tested
between any of the three families.

**On the `BATTERY_ID_EXT` / `BATTERY_ID_EXTN` discrepancy:** Radiology uses `BATTERY_ID_EXT`,
matching Laboratory. Laboratory Item FIL is the odd one out with `BATTERY_ID_EXTN`. Two of
three families use the shorter form, which makes the FIL spelling worth confirming rather than
assuming it is a synonym.

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
| `EXAMINATION_DATE_X` | Unknown | Unknown | — |
| `EXAMINATION_DATE_Z` | Unknown | Unknown | — |
| `REPORTED_DATE_X` | Unknown | Unknown | — |
| `REPORTED_DATE_Z` | Unknown | Unknown | — |
| `ORDER_DATE_X` | Unknown | Unknown | — |
| `ORDER_DATE_Z` | Unknown | Unknown | — |

Eight date columns, no range established, no principal column identified. **The completeness
ordering is informative and worth recording:** `DISPLAY_DATE` is fully populated,
`EXAMINATION_DATE` is 0.89% empty, `REPORTED_DATE` 47.9% and `ORDER_DATE` 49.23%. A study
needing the date a scan was performed has a near-complete column available; one needing the
date it was ordered or reported loses about half the rows.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If any column is month-first, every date derived from it is wrong and nothing
raises.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown. n/a for partitions — this object is not split.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `VW_RADIOLOGY_F_Export_06-08-2024.csv` | 2,611.79 | 6,569,893 | 28 | 13.10 |
| **Family total** | **2,611.79** | **6,569,893** | 28 | 13.10 |

*The row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | n/a — single object |

**A 2.6 GB single file is a practical constraint, not just a fact.** Every comparable volume
in this catalogue is partitioned; this one is not, so it cannot be processed a partition at a
time the way the billing and laboratory families can.

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Standardisation mappings:** Unknown — to confirm with data owner. One column ends in `_STD`
(`INVESTIGATION_NAME_ORI_TXT_STD`) and it is 80.75% empty. Its vocabulary, version, mapping
rule and failed-match behaviour are unrecorded — and at four in five rows unmapped, the
failed-match behaviour is the pressing question. **Any result depending on this column is not
reproducible until it is answered.**

**Processing applied:** Unknown — to confirm with data owner.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. `ITEM_ABNORMAL_FLAG_*` is a judgement about a result rather than the result itself,
so the Raw / Derived distinction will matter for it.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 13.10% (profiler, 2026-07-23) |
| Columns >50% missing | 2 of 28 (`INVESTIGATION_NAME_ORI_TXT_STD` at 80.75, `ITEM_ABNORMAL_FLAG_ORI_TXT` at 82.43) |
| Columns 100% missing | 0 of 28 |

No interpretation of the missingness is offered here.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.
The two `_STD` / `_ORI_TXT` gaps above are the largest, and the date-column ordering noted in
*Time Coverage* is the most consequential for study design.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Fifteen of the 28 columns report 0.0% missing and the check is outstanding for every one of them.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `PATIENT_ID_EXTN_X`. The patient ID column is the primary identifier
for every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. The name matches
[Laboratory](singcloud-laboratory.md),
[Laboratory Item FIL](singcloud-laboratory-item-fil.md),
[Event Diagnosis](singcloud-event-diagnosis.md) and the dispensed-medication families, but
**no join has been tested**.

**Secondary keys:** Unknown. `BATTERY_ID_ROOT`, `BATTERY_ID_EXT` and `EVENT_EXT` also profile
as `id_like`.

**Coding standards:** Unknown — to confirm with data owner.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| [Laboratory](singcloud-laboratory.md) | Unknown | Unknown | Unknown | **no join tested** | Nineteen shared column names, including `BATTERY_ID_ROOT` and `BATTERY_ID_EXT`. The strongest structural similarity in the catalogue — and still untested |
| [Laboratory Item FIL](singcloud-laboratory-item-fil.md) | Unknown | Unknown | Unknown | **no join tested** | Five shared `ITEM_*` columns; note the `BATTERY_ID_EXT` / `BATTERY_ID_EXTN` difference |
| `VW_INV_TYPE_D`, `VW_INV_SUBTYPE_D`, `VW_INV_RESULT_STATUS_D` | Unknown | Unknown | Unknown | **no join tested** | Three `_ETS_ID` columns have same-run dimension objects with matching names — see [the dimension index](singcloud-dimension-tables-index.md) |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner. The near-half emptiness of
  `ORDER_DATE` and `REPORTED_DATE` against a near-complete `EXAMINATION_DATE` is the obvious
  thing to ask about.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked.
- **Schema drift across partitions:** n/a — single object.
- **Value-range anomalies:** Not checked.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Single 2.6 GB file:** cannot be processed partition-wise.
- **Fitness for purpose:** **Cannot be assessed yet.** This page establishes neither what the
  object is nor what one row represents.

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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. The profiler typed `BATTERY_ID_ROOT`, `PATIENT_ID_EXTN_X`, `BATTERY_ID_EXT` and `EVENT_EXT` as `id_like`. The object sits under `FreeText_FTA/` but carries no obvious narrative column — worth confirming whether report text was dropped from this view or lives elsewhere, since that changes the free-text exposure answer entirely. Absence of a classification here is an outstanding task, **not** a finding that the object carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. What is the unit of observation — one row per examination, per item within an examination?
2. What is this dataset, in one paragraph?
3. **What is the relationship between Radiology, `VW_LABORATORY_F` and
   `VW_LABORATORY_ITEM_FIL_F`?** Nineteen column names are shared with the first and five with
   the second. Are they the same underlying investigation model?
4. Does `BATTERY_ID_ROOT` join Radiology to either Laboratory family?
5. Why does Laboratory Item FIL use `BATTERY_ID_EXTN` where Radiology and Laboratory use
   `BATTERY_ID_EXT`?
6. **Why is `INVESTIGATION_NAME_ORI_TXT_STD` 80.75% empty here but ~52% in Laboratory?** What
   vocabulary does it map to, and what happens on a failed match?
7. **Which date should a study use?** `EXAMINATION_DATE` is 0.89% empty, `REPORTED_DATE` 47.9%
   and `ORDER_DATE` 49.23%. Why are two of them half empty?
8. What is the relationship between the `_X` and `_Z` forms of each date?
9. Why is `ITEM_ABNORMAL_FLAG_ORI_TXT` 82.43% empty while `ITEM_ABNORMAL_FLAG_ETS_ID` is
   5.27%? Are they populated by different systems?
10. Who or what assigns `ITEM_ABNORMAL_FLAG`, and against what criteria for an imaging result?
11. **Does this view carry report narrative anywhere?** It sits under `FreeText_FTA/` but no
    column obviously holds it.
12. Is there a data dictionary? All 28 columns are currently undescribed and unclassified.
13. Is `PATIENT_ID_EXTN_X` a pseudonym, and is it stable across datasets and extracts?
14. Do `INV_TYPE_NAME_ETS_ID`, `INV_SUBTYPE_NAME_ETS_ID` and `INV_RESULT_STATUS_ETS_ID` join
    to `VW_INV_TYPE_D`, `VW_INV_SUBTYPE_D` and `VW_INV_RESULT_STATUS_D`?
15. Why is this object unpartitioned at 2.6 GB when comparable families are split?
16. What is the delimiter and file encoding?
17. What date does `06-08-2024` in the object name refer to?
18. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 28 rows, matching the 28 columns declared.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. One object, 6,569,893 rows, 28 columns, all figures transcribed from the screenshots. Category from the dataset name and `PATIENT_ID_EXTN_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — the complete object block, read from
  `source_material/screenshots/mass_columns_screenshots/section_08.png`.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this object.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.
