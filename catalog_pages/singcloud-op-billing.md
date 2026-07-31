# SingCLOUD — OP Billing

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

`VW_OP_BILLING_F_Export_14-08-2024_P{n}.csv`, under the prefix
`common-data/SingCLoud/NonFreeText_Files/VW_OP_BILLING_F/` — the family has its own
subdirectory, as MED Billing does.

| # | Object | # | Object | # | Object |
|---:|---|---:|---|---:|---|
| 1 | `…_P1.csv` | 11 | `…_P11.csv` | 21 | `…_P22.csv` |
| 2 | `…_P2.csv` | 12 | `…_P12.csv` | 22 | `…_P23.csv` |
| 3 | `…_P3.csv` | 13 | `…_P13.csv` | 23 | `…_P24.csv` |
| 4 | `…_P4.csv` | 14 | `…_P14.csv` | 24 | `…_P25.csv` |
| 5 | `…_P5.csv` | 15 | `…_P15.csv` | 25 | `…_P26.csv` |
| 6 | `…_P6.csv` | 16 | `…_P16.csv` | 26 | `…_P27.csv` |
| 7 | `…_P7.csv` | 17 | `…_P17.csv` | 27 | `…_P28.csv` |
| 8 | `…_P8.csv` | 18 | `…_P18.csv` | 28 | `…_P29.csv` |
| 9 | `…_P9.csv` | 19 | `…_P20.csv` | | |
| 10 | `…_P10.csv` | 20 | `…_P21.csv` | | |

Twenty-eight objects, 161,122,570 rows, 31 columns each.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **Overall missing falls steadily with partition number** — ~34% at P1–P6 down to ~24% from P10 on | A monotonic gradient, not noise. If partitions are time-ordered, per-partition figures on every billing page become a time series. Ask what the `_P{n}` split is by |
| 🟡 | **`NHC_HOSPTIAL_REMISSION_FUND`** — letters transposed in the source itself | Copy as written; confirmed by two independent reads |
| 🟡 | **Naming differs from IP Billing** despite a shared prefix and most of the schema — `EXT_PATIENT_CD_X` vs `FK_PATIENT_ID_X`, `MEDIFUND_FINASST` vs `MEDIFUND_FNASS` | A query written against one family will not run against the other |
| 🟡 | **Six columns share 49.33% missing, four share 32.09%** | Something links each group; not established |
| ✅ | Cleanest partition set in the catalogue — one extract date, only P19 absent | — |

---

## Dataset Overview

**Category:** OP billing — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established.

**Rows vs people:** 161,122,570 rows (profiler, 2026-07-23, 28 objects summed); distinct
patients **not counted**.

**What is *not* in it:** Unknown — to be filled in. The 31 column names in *Key Variables*
are the complete column list for the partitions read.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/NonFreeText_Files/VW_OP_BILLING_F/VW_OP_BILLING_F_Export_14-08-2024_P{n}.csv` |
| **Partitions** | 28 objects, P1–P29 with P19 absent |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. All object names contain `_Export_14-08-2024_` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. These objects sit under `NonFreeText_Files/` |

---

## Key Variables

All 31 columns, in the order printed in the report. Transcribed in full from **P1**; the first
six independently confirmed against **P10**.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

| # | Variable | Type | P1 | P10 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | 0.0 | | | | |
| 2 | `DATA_FORMAT` | categorical | 0.0 | 0.0 | | | | |
| 3 | `FK_INST_ID` | numeric | 0.0 | 0.0 | | | | |
| 4 | `EXT_PATIENT_CD_X` | id_like | 0.0 | 0.0 | | | | |
| 5 | `CASE_NO` | numeric | 0.0 | 0.0 | | | | |
| 6 | `FK_REFERRAL_HCAR_FACILITY_ID` | categorical | 56.54 | 80.27 | | | | |
| 7 | `FK_VISIT_DATE_IDK_X` | date | 0.0 | not read | | | | |
| 8 | `FK_VISIT_DATE_IDK_Z` | date | 0.0 | not read | | | | |
| 9 | `FK_DISCHARGE_CASE_TYPE_ID` | categorical | 49.33 | not read | | | | |
| 10 | `FK_SERVICE_CODE_ID` | numeric | 0.0 | not read | | | | |
| 11 | `SERVICE_DESCRIPTION` | categorical | 71.99 | not read | | | | |
| 12 | `GROSS` | numeric | 4.07 | not read | | | | |
| 13 | `NET_EXCL_GST` | numeric | 21.32 | not read | | | | |
| 14 | `SUBSIDY_EXCL_GST` | numeric | 32.09 | not read | | | | |
| 15 | `TAX_AMOUNT` | numeric | 4.07 | not read | | | | |
| 16 | `FK_BILLING_DATE_IDK_X` | date | 0.0 | not read | | | | |
| 17 | `FK_BILLING_DATE_IDK_Z` | date | 0.0 | not read | | | | |
| 18 | `FK_DRG_ID` | numeric | 49.33 | not read | | | | |
| 19 | `SURCHARGE` | numeric | 32.09 | not read | | | | |
| 20 | `DOCTOR_WAIVER` | numeric | 32.09 | not read | | | | |
| 21 | `NR_SURCHARGE` | numeric | 32.09 | not read | | | | |
| 22 | `CO_INSUR` | numeric | 49.33 | not read | | | | |
| 23 | `MCPS` | numeric | 49.33 | not read | | | | |
| 24 | `MEDISHIELD` | numeric | 49.33 | not read | | | | |
| 25 | `MEDIFUND_FINASST` | numeric | 49.33 | not read | | | | |
| 26 | `MEDISAVE` | numeric | 28.01 | not read | | | | |
| 27 | `OTHERS` | numeric | 49.33 | not read | | | | |
| 28 | `RELATED_COM` | categorical | 92.35 | not read | | | | |
| 29 | `INTER_COM` | categorical | 92.35 | not read | | | | |
| 30 | `NHC_WAIVER_FOR_NR` | categorical | 96.33 | not read | | | | |
| 31 | `NHC_HOSPTIAL_REMISSION_FUND` | categorical | 96.33 | not read | | | | |

*(P1 and P10 are missing %; profiler, 2026-07-23)*

**`NHC_HOSPTIAL_REMISSION_FUND` is spelled with the letters transposed** — `HOSPTIAL`, not
`HOSPITAL`. This is a typo in the source data, not a transcription slip: it appears the same
way in the OCR reconstruction, which is an independent read of the same report. Copy it
character for character.

**Two payer columns differ in spelling from IP Billing.** This family has `MEDIFUND_FINASST`
and `MCPS` typed `numeric`; [IP Billing](singcloud-ip-billing.md) has `MEDIFUND_FNASS` and
`MCPS` typed `categorical`. A query written against one family will not run against the other.

**Six columns share the value 49.33** in P1 (`FK_DISCHARGE_CASE_TYPE_ID`, `FK_DRG_ID`,
`CO_INSUR`, `MCPS`, `MEDISHIELD`, `MEDIFUND_FINASST`, `OTHERS`) and three share 32.09
(`SUBSIDY_EXCL_GST`, `SURCHARGE`, `DOCTOR_WAIVER`, `NR_SURCHARGE`). What links each group is
not established.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `FK_VISIT_DATE_IDK_X` | Unknown | Unknown | — |
| `FK_VISIT_DATE_IDK_Z` | Unknown | Unknown | — |
| `FK_BILLING_DATE_IDK_X` | Unknown | Unknown | — |
| `FK_BILLING_DATE_IDK_Z` | Unknown | Unknown | — |

Four date columns, all fully populated in P1. No range is established. Unlike
[IP Billing](singcloud-ip-billing.md), every date-named column here profiles as `date`.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If any column is month-first, every date derived from it is wrong and nothing
raises. The `_IDK` element in these names is undeciphered and may indicate a date *key* rather
than a date.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown. The `_P{n}` split is not established as
temporal. See the missingness gradient noted below before assuming it is.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `…_P1.csv` | 1,966.13 | 7,003,818 | 31 | 33.45 |
| `…_P2.csv` | 2,133.91 | 7,624,780 | 31 | 34.50 |
| `…_P3.csv` | 2,333.76 | 8,333,018 | 31 | 34.33 |
| `…_P4.csv` | 1,014.32 | 3,618,678 | 31 | 33.99 |
| `…_P5.csv` | 1,289.32 | 4,595,055 | 31 | 33.74 |
| `…_P6.csv` | 1,364.48 | 4,855,493 | 31 | 33.26 |
| `…_P7.csv` | 1,151.99 | 4,061,671 | 31 | 28.71 |
| `…_P8.csv` | 1,188.84 | 4,166,289 | 31 | 26.93 |
| `…_P9.csv` | 1,177.62 | 4,120,140 | 31 | 26.66 |
| `…_P10.csv` | 1,213.93 | 4,238,891 | 31 | 26.12 |
| `…_P11.csv` | 1,214.64 | 4,245,743 | 31 | 26.44 |
| `…_P12.csv` | 1,293.65 | 4,512,759 | 31 | 25.89 |
| `…_P13.csv` | 1,355.14 | 4,724,188 | 31 | 25.48 |
| `…_P14.csv` | 1,479.27 | 5,147,107 | 31 | 25.09 |
| `…_P15.csv` | 1,576.17 | 5,483,201 | 31 | 25.09 |
| `…_P16.csv` | 1,697.11 | 5,899,340 | 31 | 24.88 |
| `…_P17.csv` | 1,696.45 | 5,902,357 | 31 | 25.04 |
| `…_P18.csv` | 1,781.42 | 6,198,253 | 31 | 25.03 |
| `…_P20.csv` | 1,856.57 | 6,460,345 | 31 | 25.06 |
| `…_P21.csv` | 1,915.29 | 6,658,792 | 31 | 24.80 |
| `…_P22.csv` | 1,962.44 | 6,821,950 | 31 | 24.90 |
| `…_P23.csv` | 1,961.79 | 6,816,021 | 31 | 24.72 |
| `…_P24.csv` | 1,784.28 | 6,208,019 | 31 | 25.33 |
| `…_P25.csv` | 2,033.11 | 7,045,239 | 31 | 24.16 |
| `…_P26.csv` | 1,973.86 | 6,836,849 | 31 | 24.09 |
| `…_P27.csv` | 1,918.58 | 6,642,933 | 31 | 23.91 |
| `…_P28.csv` | 1,844.77 | 6,387,893 | 31 | 23.97 |
| `…_P29.csv` | 1,872.11 | 6,513,748 | 31 | 25.62 |
| **Family total** | **46,050.95** | **161,122,570** | 31 | — |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

Family size and rows are sums of the 28 reported figures. Family missing % is left blank
deliberately: the per-object percentages are shares of 28 different denominators and cannot be
averaged.

**Overall missing falls steadily with partition number** — around 33–34% for P1–P6, dropping
through P7–P9, then settling near 24–26% from P10 onward. It is a monotonic-looking gradient
rather than noise, and it is the clearest such pattern in the catalogue. **This is recorded as
an observation, not explained.** It would be consistent with the partitions being ordered by
something (time, institution, case type) that also drives completeness — but nothing in the
profiler output establishes what the `_P{n}` split is by, so no reading is adopted here. It is
worth asking about, because if partitions are time-ordered then the per-partition figures on
every billing page become a time series.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | 31 columns in every object; names and types transcribed from P1, first six confirmed against P10. The remaining 26 are not yet checked column by column |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner. This is a
billing dataset, and `template.md` notes that billing-entered and clinically-entered fields
fail differently.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** n/a — no column name on this page carries a `_STD` suffix.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. `FK_VISIT_DATE_IDK_X` / `_Z` and `FK_BILLING_DATE_IDK_X` / `_Z` form apparent pairs;
no relationship between either pair has been established.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 23.91–34.50% across the 28 objects (profiler, 2026-07-23) |
| Columns >50% missing | 6 of 31 in P1 (`FK_REFERRAL_HCAR_FACILITY_ID`, `SERVICE_DESCRIPTION`, `RELATED_COM`, `INTER_COM`, `NHC_WAIVER_FOR_NR`, `NHC_HOSPTIAL_REMISSION_FUND`) |
| Columns 100% missing | 0 in P1 — no column is entirely empty, unlike every other family documented so far |

No interpretation of the missingness is offered here.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked, and the amount columns are the priority.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- Sixteen columns are numeric amounts or waivers where a recorded `0` and an unrecorded value are different facts that the profiler cannot distinguish. **Do not read "0.0% missing" as "0.0% unusable"** until someone has run `value_counts()`.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `EXT_PATIENT_CD_X`. The patient ID column is the primary identifier for
every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. `EXT_PATIENT_CD_X` is a **fifth**
distinct patient-column name in this catalogue, alongside `FK_PATIENT_ID_X`
([IP Billing](singcloud-ip-billing.md)), `PATIENT_CODE_X`
([MED Billing](singcloud-med-billing.md)), `PATIENT_ID_EXTN_X` (the clinical families) and
`NRIC_X` ([MOH OB Operation](singcloud-moh-ob-operation.md)). Notably IP and OP Billing sit in
the same prefix and share most of their schema, yet name the patient column differently.
**No join has been tested** between any of them.

**Secondary keys:** Unknown. `CASE_NO` is a candidate but profiles as `numeric`, not `id_like`.
`EXT_PATIENT_CD_X` is the only column the profiler typed `id_like`.

**Coding standards:** Unknown — to confirm with data owner. `FK_DRG_ID`,
`FK_SERVICE_CODE_ID`, `FK_DISCHARGE_CASE_TYPE_ID` and `FK_REFERRAL_HCAR_FACILITY_ID` all have
matching `_D` dimension objects in the same run (`VW_DRG_D`, `VW_SERVICE_CODE_D`,
`VW_CASE_TYPE_D`, `VW_REFERRAL_FACILITY_D`), but no join has been tested.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown | **no join tested** | Four `FK_` columns have same-run `_D` objects with matching names, but no linkage has been established |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner. The missingness gradient across
  partitions is the obvious thing to ask about here.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked. Unlike IP and MED Billing, this family has a single extract
  date, so cross-extract duplication is not a concern here.
- **Schema drift across partitions:** All 28 objects report 31 columns. Only P1 has been
  transcribed in full.
- **Value-range anomalies:** Not checked. The amount columns are unbounded numerics with no
  stated units.
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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. `EXT_PATIENT_CD_X` is the only column the profiler typed `id_like`. This is financial data at patient level — payer, subsidy, waiver and amount columns — a distinct sensitivity question from the clinical families that should not be assumed to fall under the same permissions. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. What is the unit of observation — one row per visit, per billed item, per bill?
2. What is this dataset, in one paragraph, and how does it relate to IP, MED, TP and LIP
   Billing? IP and OP Billing share most of their schema — is one derived from the other?
3. **Why does overall missing fall steadily from ~34% at P1 to ~24% at P27?** What determines
   the `_P{n}` split, and are the partitions ordered?
4. **Does partition P19 exist?** If so, why was it not profiled?
5. Which population is included, and who is excluded by what mechanism?
6. Is there a data dictionary? All 31 columns are currently undescribed and unclassified.
7. What do the `FK_` prefix and the `_IDK` element denote?
8. Why is the patient column named `EXT_PATIENT_CD_X` here but `FK_PATIENT_ID_X` in IP
   Billing, when the two families sit in the same prefix and share most of their schema? Are
   they the same identifier space?
9. Do `FK_DRG_ID`, `FK_SERVICE_CODE_ID`, `FK_DISCHARGE_CASE_TYPE_ID` and
   `FK_REFERRAL_HCAR_FACILITY_ID` join to `VW_DRG_D`, `VW_SERVICE_CODE_D`, `VW_CASE_TYPE_D`
   and `VW_REFERRAL_FACILITY_D`?
10. What links the six columns sharing 49.33% missing, and the four sharing 32.09%?
11. What are the units of the amount columns, and how do `GROSS`, `NET_EXCL_GST`,
    `SUBSIDY_EXCL_GST` and `TAX_AMOUNT` relate arithmetically?
12. Is a `0` in an amount or waiver column a real zero or an unrecorded value?
13. What are `RELATED_COM` and `INTER_COM`, absent for ~92% of rows?
14. What are `NHC_WAIVER_FOR_NR` and `NHC_HOSPTIAL_REMISSION_FUND`, and is the `HOSPTIAL`
    spelling stable across extracts or likely to be corrected?
15. What is the delimiter and file encoding?
16. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 31 rows, matching the 31 columns declared for every object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Twenty-eight objects, 161,122,570 rows, 31 columns. Column names and types transcribed from the screenshots for P1, first six confirmed against P10; object-level figures for all 28. Category from the dataset name and `EXT_PATIENT_CD_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — column names, types and per-column missing % read from
  `source_material/screenshots/mass_columns_screenshots/section_18.png` (P1, and the head of
  P10). Object-level figures for all 28 objects from the same run.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names. Its filename
  for P16 reads `14-08-2624`, a digit misread; the object is listed here as `14-08-2024` in
  line with the other 27, which is an assumption worth confirming.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.
