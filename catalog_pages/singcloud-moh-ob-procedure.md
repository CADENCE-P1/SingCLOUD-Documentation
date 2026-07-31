# SingCLOUD — MOH OB Procedure

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_MOH_OB_PROCEDURE_F_Export_31-07-2024_P1.csv` |
| 2 | `VW_MOH_OB_PROCEDURE_F_Export_31-07-2024_P2.csv` |
| 3 | `VW_MOH_OB_PROCEDURE_F_Export_31-07-2024_P3.csv` |

All sit under the prefix `common-data/SingCLoud/NonFreeText_Files/`. Three objects, 10,723,840
rows, 27 columns each.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **Patient column is `NRIC_X`** | **Confirm whether it is pseudonymised before handling the data** |
| 🔴 | **Every column of every object reports 0.0% missing** — the only multi-object family with none anywhere | A complete dataset and one where every gap was filled with a sentinel look identical here. Run `value_counts()` |
| 🟡 | **Two competing discharge-date pairs** — `dt_dis_X`/`_Z` and `date_dis_X`/`_Z`, all fully populated | Using the wrong one is an invisible error. Establish which is authoritative |
| 🟡 | **`dicd10` profiles as `numeric`** | ICD-10 codes contain letters. Resolve before using it as a diagnosis code |
| 🟡 | Column 12 is **`cp_cpp_p_code_grp`** — `cp_`, where its 16 neighbours use `cs_` | Probably a source typo; two independent reads agree. Copy as written |
| 📋 | Only P1 column-transcribed | Verify P2 and P3 |

---

## Dataset Overview

**Category:** MOH OB procedure — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner. What `MOH` and `OB` denote here is unconfirmed.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.
`cs_cpp_he_facility` is present and 0.0% missing, so the answer is in the data, but it has not
been enumerated here.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established.

**Rows vs people:** 10,723,840 rows (profiler, 2026-07-23, three objects summed); distinct
patients **not counted**.

**What is *not* in it:** Unknown — to be filled in. The 27 column names in *Key Variables*
are the complete column list for the partition read.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/NonFreeText_Files/VW_MOH_OB_PROCEDURE_F_Export_31-07-2024_P{1..3}.csv` |
| **Partitions** | 3 objects, P1–P3, contiguous |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. All three object names contain `_Export_31-07-2024_` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. These objects sit under `NonFreeText_Files/` |

---

## Key Variables

All 27 columns, in the order printed in the report. Transcribed in full from **P1**.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

**Note the casing.** Two upper-case columns (`DATA_SOURCE`, `NRIC_X`) followed by 25
lower-case ones, most carrying a `cs_cpp_` prefix. Copy each character for character.

| # | Variable | Type | P1 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | | | | |
| 2 | `NRIC_X` | id_like | 0.0 | | | | |
| 3 | `cs_cpp_case_type` | categorical | 0.0 | | | | |
| 4 | `cs_cpp_casemix_surrogate_id` | categorical | 0.0 | | | | |
| 5 | `cs_cpp_he_facility` | numeric | 0.0 | | | | |
| 6 | `cs_cpp_mdc` | categorical | 0.0 | | | | |
| 7 | `epi_id` | categorical | 0.0 | | | | |
| 8 | `cs_cpp_patient_surrogate_id` | categorical | 0.0 | | | | |
| 9 | `cs_cpp_are` | categorical | 0.0 | | | | |
| 10 | `cs_cpp_p_block_number` | categorical | 0.0 | | | | |
| 11 | `cs_cpp_p_block_grp` | categorical | 0.0 | | | | |
| 12 | `cp_cpp_p_code_grp` | categorical | 0.0 | | | | |
| 13 | `cs_cpp_procedure_code` | categorical | 0.0 | | | | |
| 14 | `cs_cpp_arcl` | categorical | 0.0 | | | | |
| 15 | `cs_cpp_order_number` | categorical | 0.0 | | | | |
| 16 | `cs_cpp_procedure_type` | categorical | 0.0 | | | | |
| 17 | `cs_cpp_htp` | numeric | 0.0 | | | | |
| 18 | `cs_cpp_ltp` | numeric | 0.0 | | | | |
| 19 | `cs_cpp_drg` | categorical | 0.0 | | | | |
| 20 | `dt_dis_X` | date | 0.0 | | | | |
| 21 | `dt_dis_Z` | date | 0.0 | | | | |
| 22 | `date_dis_X` | date | 0.0 | | | | |
| 23 | `date_dis_Z` | date | 0.0 | | | | |
| 24 | `date_procedure_X` | date | 0.0 | | | | |
| 25 | `date_procedure_Z` | date | 0.0 | | | | |
| 26 | `dicd10` | numeric | 0.0 | | | | |
| 27 | `cpp_tag` | numeric | 0.0 | | | | |

*(P1 is missing %; profiler, 2026-07-23)*

**Column 12 is `cp_cpp_p_code_grp` — `cp_`, not `cs_`** — where its 16 neighbours use `cs_`.
Two independent reads of the report (the screenshot and the OCR reconstruction) agree on the
`cp_` prefix, so it is probably a typo in the source rather than a transcription slip. Copy it
as written and confirm with the data owner.

**Two apparently duplicate discharge-date pairs.** `dt_dis_X` / `_Z` and `date_dis_X` / `_Z`
are four separate date columns, all fully populated. What distinguishes `dt_` from `date_` is
unknown and must not be guessed — using the wrong one is the invisible error the Time Coverage
section of `template.md` exists to prevent.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `date_procedure_X` | Unknown | Unknown | — |
| `date_procedure_Z` | Unknown | Unknown | — |
| `dt_dis_X` | Unknown | Unknown | — |
| `dt_dis_Z` | Unknown | Unknown | — |
| `date_dis_X` | Unknown | Unknown | — |
| `date_dis_Z` | Unknown | Unknown | — |

Six date columns, all fully populated in P1. No range is established and no principal date
column is identified — and with two competing discharge-date pairs, identifying the principal
one is more than a formality here.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If any column is month-first, every date derived from it is wrong and nothing
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
| `…_P1.csv` | 1,744.05 | 4,731,825 | 27 | 0.0 |
| `…_P2.csv` | 1,249.98 | 3,325,012 | 27 | 0.0 |
| `…_P3.csv` | 1,002.09 | 2,667,003 | 27 | 0.0 |
| **Family total** | **3,996.12** | **10,723,840** | 27 | 0.0 |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

**Every column of every object is reported 0.0% missing.** This is the only multi-object
family in the catalogue with no missingness anywhere — which makes the disguised-missing check
below more important here than on any other page, not less.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | 27 columns in every object; names, order and types transcribed from P1 only. P2 and P3 are not yet checked column by column |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here. Two columns are named
`*_surrogate_id`, which in some pipelines denotes a key minted during processing rather than
one carried from source — but that reading is not established.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** n/a — no column name on this page carries a `_STD` suffix.

**Transformations at load:** Unknown. Inspect `df.columns` after loading — this family's mixed
casing is the kind a loader that normalises case would flatten.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. The `_X` / `_Z` pairs and the `dt_` / `date_` duplication are both unresolved.

**Identifier handling:** Unknown — to confirm with data owner. As with
[MOH OB Operation](singcloud-moh-ob-operation.md), the patient column is `NRIC_X`.
**Whether it is pseudonymised must be answered before the data is handled.**

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 0.0% in all three objects (profiler, 2026-07-23) |
| Columns >50% missing | 0 of 27 |
| Columns 100% missing | 0 of 27 |

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked, and this is the page where it matters most in the whole catalogue.** Every column of every object reports 0.0% missing.

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `NRIC_X`. The patient ID column is the primary identifier for every
dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are unknown —
read it as `str` and inspect before joining. Singapore NRIC values carry a trailing check
letter and leading zeros, both of which a numeric read would destroy.

**Identifier family:** Unknown — to confirm with data owner. `NRIC_X` matches
[MOH OB Operation](singcloud-moh-ob-operation.md) but differs from every other family in the
catalogue; **no join has been tested**.

**Secondary keys:** Unknown. `NRIC_X` is the only column the profiler typed `id_like`, despite
`epi_id`, `cs_cpp_casemix_surrogate_id`, `cs_cpp_patient_surrogate_id` and
`cs_cpp_order_number` all being identifier-shaped names — all four profile as `categorical`,
which suggests their values are not predominantly long digit strings.

**Coding standards:** Unknown — to confirm with data owner. `dicd10` implies ICD-10 and
`cs_cpp_drg` implies a DRG scheme, but neither is established. Note `dicd10` profiles as
**numeric**, which is not what a column of ICD-10 codes would normally look like — ICD-10
codes contain letters. That is worth resolving before the column is used as a diagnosis code.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| [MOH OB Operation](singcloud-moh-ob-operation.md) | Unknown | Unknown | Unknown | **no join tested** | Both families carry `NRIC_X` and a `date_dis_X` / `_Z` pair, and share a naming stem. **Nothing establishes a relationship** |
| `VW_DRG_D` | Unknown | Unknown | Unknown | **no join tested** | `cs_cpp_drg` and the same-run DRG dimension share naming |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked.
- **Schema drift across partitions:** All three objects report 27 columns. Only P1 has been
  transcribed column by column.
- **Value-range anomalies:** Not checked. `dicd10` typing as numeric is the first thing to look
  at.
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
| **Free-text / PII exposure** | **Not assessed, and the patient column name is a prima facie signal.** `NRIC_X` profiles as `id_like`; if it holds NRIC values rather than a pseudonym, this is direct identifier data and the handling requirements differ sharply from families keyed on a project-minted ID. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. **Is `NRIC_X` a pseudonym or a real NRIC?** This gates everything else on the page.
2. Is the 0.0% missing figure genuine, or does the family use sentinel values?
3. What is the unit of observation — one row per procedure, per episode, per block?
4. What is this dataset, in one paragraph? What do `MOH`, `OB`, `cpp` and `cs_` stand for?
5. **What is the difference between `dt_dis_X` / `_Z` and `date_dis_X` / `_Z`?** Which is the
   discharge date to use?
6. Is column 12 really `cp_cpp_p_code_grp` rather than `cs_cpp_p_code_grp`? If it is a typo,
   will it be corrected in a future extract?
7. Which population is included, and who is excluded by what mechanism?
8. Is there a data dictionary? All 27 columns are currently undescribed and unclassified.
9. `dicd10` profiles as numeric — does it hold ICD-10 codes, and if so how, given ICD-10 codes
   contain letters?
10. What vocabulary do `cs_cpp_procedure_code`, `cs_cpp_mdc` and `cs_cpp_drg` use, and what
    version?
11. What are `cs_cpp_casemix_surrogate_id` and `cs_cpp_patient_surrogate_id`? Are they minted
    during processing, and are they stable across extracts?
12. What are `cs_cpp_are`, `cs_cpp_arcl`, `cs_cpp_htp`, `cs_cpp_ltp` and `cpp_tag`?
13. How does this family relate to `VW_MOH_OB_OPERATION_F` and `VW_MOH_OB_WO_SHI_F`?
14. Is `NRIC_X` linkable to the patient columns in the other families? Does a crosswalk exist?
15. What is the delimiter and file encoding, and are all three objects the same?
16. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 27 rows, matching the 27 columns declared for every object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Three objects, 10,723,840 rows, 27 columns. Column names, types and missing % transcribed from the screenshots for P1; object-level figures for all three. Category from the dataset name and `NRIC_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — the complete P1 block, read from
  `source_material/screenshots/mass_columns_screenshots/section_17.png`. Object-level figures
  for P2 and P3 from the same run.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names. The `cp_`
  prefix on column 12 is the one point where the reconstruction and the screenshot agree on an
  oddity, which is why it is reported here as probable source truth rather than as a misread.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.
