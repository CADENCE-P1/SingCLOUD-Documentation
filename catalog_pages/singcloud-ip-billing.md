# SingCLOUD — IP Billing

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

`VW_IP_BILLING_F_Export_{date}_P{n}.csv`, under the prefix
`common-data/SingCLoud/NonFreeText_Files/`. Thirty-three objects are indexed below.

> ⚠ **The object list is incomplete and the partition count is unconfirmed.** The profiler
> report runs IP Billing continuously from section_13 through section_16 of the screenshots —
> roughly 38 blocks — while only 33 objects could be indexed. Some partitions are therefore
> present in the run but not listed here. **Do not treat the totals below as family totals.**
> Establishing the true partition list is the first open question on this page.

| # | Object | # | Object |
|---:|---|---:|---|
| 1 | `…_05-08-2024_P1.csv` | 18 | `…_06-08-2024_P20.csv` |
| 2 | `…_05-08-2024_P2.csv` | 19 | `…_06-08-2024_P21.csv` |
| 3 | `…_05-08-2024_P3.csv` | 20 | `…_06-08-2024_P22.csv` |
| 4 | `…_05-08-2024_P6.csv` | 21 | `…_06-08-2024_P23.csv` |
| 5 | `…_05-08-2024_P7.csv` | 22 | `…_06-08-2024_P24.csv` |
| 6 | `…_05-08-2024_P10.csv` | 23 | `…_06-08-2024_P25.csv` |
| 7 | `…_05-08-2024_P11.csv` | 24 | `…_06-08-2024_P26.csv` |
| 8 | `…_05-08-2024_P12.csv` | 25 | `…_06-08-2024_P27.csv` |
| 9 | `…_05-08-2024_P13.csv` | 26 | `…_06-08-2024_P28.csv` |
| 10 | `…_05-08-2024_P14.csv` | 27 | `…_06-08-2024_P29.csv` |
| 11 | `…_05-08-2024_P15.csv` | 28 | `…_06-08-2024_P30.csv` |
| 12 | `…_05-08-2024_P16.csv` | 29 | `…_06-08-2024_P31.csv` |
| 13 | `…_05-08-2024_P17.csv` | 30 | `…_06-08-2024_P32.csv` |
| 14 | `…_05-08-2024_P18.csv` | 31 | `…_06-08-2024_P33.csv` |
| 15 | `…_06-08-2024_P19.csv` | 32 | `…_06-08-2024_P34.csv` |
| 16 | `…_06-08-2024_P36.csv` | 33 | `…_06-08-2024_P35.csv` |
| 17 | `…_06-08-2024_P37.csv` | | |

**P4, P5, P8 and P9 are absent** from this list, and the list itself is incomplete — see below.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **The object list is incomplete** — the run spans four screenshot sections (~38 blocks) but only 33 objects could be indexed | Totals here are a lower bound, not a family total. Get a definitive file list before citing any count |
| 🔴 | **Two extract dates** — P1–P18 are `05-08-2024`, P19+ are `06-08-2024` | If these are separate extracts rather than halves of one, rows may be duplicated across them |
| 🟡 | **`SPECIALITY`, not `SPECIALTY`** in `FK_ADMIT_PATIENT_SPECIALITY_ID` and `FK_DISCHARGE_SPECIALITY_ID` | The clinical families use `SPECIALTY`. Easy KeyError |
| 🟡 | **`FK_DISCHARGE_DATE_IDK_X`/`_Z` profile as `categorical`**, not `date` | Do not assume they parse |
| 🟡 | **Patient column is `FK_PATIENT_ID_X`** — OP Billing uses `EXT_PATIENT_CD_X` despite the same prefix and a near-identical schema | Confirm whether it is the same identifier space |
| 📋 | P4, P5, P8, P9 absent from the indexed set | Confirm whether they exist |

---

## Dataset Overview

**Category:** IP billing — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established.

**Rows vs people:** At least 173,000,000 rows across the indexed objects (profiler,
2026-07-23) — a lower bound, since the object list is incomplete. Distinct patients **not
counted**.

**What is *not* in it:** Unknown — to be filled in. The 37 column names in *Key Variables*
are the complete column list for the partitions read.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/NonFreeText_Files/VW_IP_BILLING_F_Export_{date}_P{n}.csv` |
| **Partitions** | **Unconfirmed** — 33 indexed, run appears longer. See warning above |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Two dates in the object names: `05-08-2024` and `06-08-2024` |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. Unlike the clinical families, these objects sit under `NonFreeText_Files/` |

---

## Key Variables

All 37 columns, in the order printed in the report. Names, order and types verified **identical
in P10 and P35** — two partitions from different extract dates, which is the stronger check.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

| # | Variable | Type | P10 | P35 | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | 0.0 | | | | |
| 2 | `DATA_FORMAT` | categorical | 0.0 | 0.0 | | | | |
| 3 | `FK_INST_ID` | numeric | 0.0 | 0.0 | | | | |
| 4 | `FK_PATIENT_ID_X` | id_like | 0.0 | 0.0 | | | | |
| 5 | `CASE_NO` | numeric | 0.0 | 0.0 | | | | |
| 6 | `FK_DRG_ID` | numeric | 0.0 | 0.0 | | | | |
| 7 | `LOS_DAYS` | categorical | 49.63 | 34.06 | | | | |
| 8 | `FK_ADMIT_TYPE_ID` | numeric | 0.0 | 0.0 | | | | |
| 9 | `ADMIT_TYPE_CODE` | categorical | 45.88 | 33.11 | | | | |
| 10 | `ADMIT_TYPE_DESC` | categorical | 0.0 | 0.0 | | | | |
| 11 | `FK_ADMIT_PATIENT_CLASS_ID` | numeric | 0.0 | 0.0 | | | | |
| 12 | `FK_DISCHARGE_PAT_CLASS_ID` | numeric | 0.0 | 0.0 | | | | |
| 13 | `FK_DISCHARGE_DATE_IDK_X` | categorical | 45.88 | 33.17 | | | | |
| 14 | `FK_DISCHARGE_DATE_IDK_Z` | categorical | 45.88 | 33.17 | | | | |
| 15 | `FK_DISCHARGE_CASE_TYPE_ID` | categorical | 0.0 | 0.0 | | | | |
| 16 | `FK_SERVICE_CODE_ID` | numeric | 0.0 | 0.0 | | | | |
| 17 | `SERVICE_DESCRIPTION` | categorical | 45.88 | 33.11 | | | | |
| 18 | `FK_ADMIT_DATE_IDK_X` | date | 0.0 | 0.0 | | | | |
| 19 | `FK_ADMIT_DATE_IDK_Z` | date | 0.0 | 0.0 | | | | |
| 20 | `FK_ADMIT_PATIENT_SPECIALITY_ID` | numeric | 0.0 | 0.0 | | | | |
| 21 | `FK_DISCHARGE_SPECIALITY_ID` | numeric | 0.0 | 0.0 | | | | |
| 22 | `GROSS` | numeric | 0.0 | 0.0 | | | | |
| 23 | `SUBSIDY` | numeric | 0.0 | 0.0 | | | | |
| 24 | `NET` | numeric | 0.0 | 0.0 | | | | |
| 25 | `FK_BILLING_DATE_IDK_X` | date | 0.0 | 0.0 | | | | |
| 26 | `FK_BILLING_DATE_IDK_Z` | date | 0.0 | 0.0 | | | | |
| 27 | `GST` | numeric | 0.0 | 0.0 | | | | |
| 28 | `ZPHS` | numeric | 0.0 | 0.0 | | | | |
| 29 | `ZWAV` | numeric | 0.0 | 0.0 | | | | |
| 30 | `NR_SURCHARGE_AMT` | numeric | 0.0 | 0.55 | | | | |
| 31 | `SELF_PAYER` | numeric | 54.12 | 66.89 | | | | |
| 32 | `MCPS` | categorical | 100.0 | 100.0 | | | | |
| 33 | `CO_INSUR` | numeric | 54.12 | 66.89 | | | | |
| 34 | `MEDISAVE` | numeric | 54.12 | 66.89 | | | | |
| 35 | `MEDISHIELD` | numeric | 54.12 | 66.89 | | | | |
| 36 | `MEDIFUND_FNASS` | numeric | 54.12 | 66.89 | | | | |
| 37 | `OTHERS` | categorical | 100.0 | 100.0 | | | | |

*(P10 and P35 are missing %; profiler, 2026-07-23)*

**Spelling.** `FK_ADMIT_PATIENT_SPECIALITY_ID` and `FK_DISCHARGE_SPECIALITY_ID` use
**SPECIALITY**, not SPECIALTY. The clinical families use `SPECIALTY`
(see [singcloud-event-diagnosis.md](singcloud-event-diagnosis.md)). Copy each character for
character.

**`MCPS` and `OTHERS` are 100% empty in both partitions read.** The five payer columns
(`SELF_PAYER`, `CO_INSUR`, `MEDISAVE`, `MEDISHIELD`, `MEDIFUND_FNASS`) share an identical
missing percentage within each partition — 54.12 in P10, 66.89 in P35. What that means is not
established here.

**Three date-named columns are not typed as dates.** `FK_DISCHARGE_DATE_IDK_X` / `_Z` profile
as `categorical` while `FK_ADMIT_DATE_IDK_X` / `_Z` and `FK_BILLING_DATE_IDK_X` / `_Z` profile
as `date`. The cause is unknown; do not assume the discharge columns parse.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `FK_ADMIT_DATE_IDK_X` | Unknown | Unknown | — |
| `FK_ADMIT_DATE_IDK_Z` | Unknown | Unknown | — |
| `FK_BILLING_DATE_IDK_X` | Unknown | Unknown | — |
| `FK_BILLING_DATE_IDK_Z` | Unknown | Unknown | — |
| `FK_DISCHARGE_DATE_IDK_X` | Unknown | Unknown | — |
| `FK_DISCHARGE_DATE_IDK_Z` | Unknown | Unknown | — |

No date range is established and no principal date column is identified. The two discharge
columns are typed `categorical`, so they may not be dates in the form the name suggests.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If any column is month-first, every date derived from it is wrong and nothing
raises. The `_IDK` element in these names is undeciphered and may indicate a date *key* rather
than a date.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown. The `_P{n}` split is not established as
temporal, so per-partition figures are not a time series.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23. **Incomplete** — see the
warning at the top of this page.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `…_05-08-2024_P1.csv` | 1,524.35 | 4,754,230 | 37 | 19.01 |
| `…_05-08-2024_P2.csv` | 1,544.37 | 4,806,705 | 37 | 19.02 |
| `…_05-08-2024_P3.csv` | 1,695.30 | 5,269,642 | 37 | 19.01 |
| `…_05-08-2024_P6.csv` | 1,286.51 | 3,972,234 | 37 | 18.99 |
| `…_05-08-2024_P7.csv` | 1,373.82 | 4,263,554 | 37 | 18.99 |
| `…_05-08-2024_P10.csv` | 1,471.74 | 4,560,956 | 37 | 19.02 |
| `…_05-08-2024_P11.csv` | 1,848.32 | 5,661,909 | 37 | 18.98 |
| `…_05-08-2024_P12.csv` | 2,053.53 | 6,269,176 | 37 | 19.01 |
| `…_05-08-2024_P13.csv` | 2,228.36 | 6,804,777 | 37 | 19.00 |
| `…_05-08-2024_P14.csv` | 2,248.85 | 6,887,095 | 37 | 19.00 |
| `…_05-08-2024_P15.csv` | 1,606.98 | 4,926,182 | 37 | 19.00 |
| `…_05-08-2024_P16.csv` | 1,689.86 | 5,170,972 | 37 | 19.00 |
| `…_05-08-2024_P17.csv` | 1,651.05 | 5,048,694 | 37 | 19.00 |
| `…_05-08-2024_P18.csv` | 1,736.80 | 5,320,883 | 37 | 19.00 |
| `…_06-08-2024_P19.csv` | 1,829.06 | 5,603,762 | 37 | 19.00 |
| `…_06-08-2024_P20.csv` | 1,738.72 | 5,320,699 | 37 | 19.00 |
| `…_06-08-2024_P21.csv` | 1,845.58 | 5,655,943 | 37 | 18.98 |
| `…_06-08-2024_P22.csv` | 1,888.16 | 5,786,580 | 37 | 18.99 |
| `…_06-08-2024_P23.csv` | 1,938.02 | 5,916,678 | 37 | 18.99 |
| `…_06-08-2024_P24.csv` | 2,008.02 | 6,138,965 | 37 | 19.00 |
| `…_06-08-2024_P25.csv` | 2,051.15 | 6,254,820 | 37 | 18.99 |
| `…_06-08-2024_P27.csv` | 1,852.47 | 5,643,354 | 37 | 18.98 |
| `…_06-08-2024_P28.csv` | 2,074.26 | 6,304,264 | 37 | 18.97 |
| `…_06-08-2024_P29.csv` | 2,193.82 | 6,670,998 | 37 | 18.97 |
| `…_06-08-2024_P30.csv` | 1,697.03 | 5,157,608 | 37 | 18.96 |
| `…_06-08-2024_P31.csv` | 1,601.99 | 4,859,928 | 37 | 18.95 |
| `…_06-08-2024_P32.csv` | 1,625.31 | 4,944,880 | 37 | 18.95 |
| `…_06-08-2024_P33.csv` | 1,587.15 | 4,808,681 | 37 | 18.96 |
| `…_06-08-2024_P34.csv` | 1,665.16 | 5,042,933 | 37 | 18.96 |
| `…_06-08-2024_P35.csv` | 1,630.91 | 4,939,721 | 37 | 18.96 |
| `…_06-08-2024_P36.csv` | 1,662.53 | 5,030,501 | 37 | 18.96 |
| `…_06-08-2024_P37.csv` | 1,583.22 | 4,776,279 | 37 | 18.97 |
| **Sum over indexed objects** | **56,432.40** | **172,573,603** | 37 | — |

*The sum is a **lower bound in two ways**: the object list above is incomplete, and every row
count is itself a lower bound because the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), dropping unparseable lines
silently. It is not a family total.*

Overall missing sits in a very narrow band — 18.95% to 19.02% across all 32 indexed objects,
a spread of 0.07 percentage points. This is much tighter than any other family in the
catalogue.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | 37 columns in every indexed object; names, order and types verified identical in P10 and P35, which come from different extract dates |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner. This is a
billing dataset, and `template.md` notes that billing-entered and clinically-entered fields
fail differently — but which this is, and what the incentive is, is not established here.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** n/a — no column name on this page carries a `_STD` suffix.

**Transformations at load:** Unknown. Inspect `df.columns` after loading.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. The `FK_` prefix on fifteen columns, and the `_IDK` element on six, are undeciphered;
no meaning is assumed for either.

**Identifier handling:** Unknown — to confirm with data owner.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 18.95–19.02% across the 32 indexed objects (profiler, 2026-07-23) |
| Columns >50% missing | 5 of 37 in P10, 6 in P35 |
| Columns 100% missing | 2 in both partitions read (`MCPS`, `OTHERS`) |

No interpretation of the missingness is offered here.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- **Do not read "0.0% missing" as "0.0% unusable"** — 25 of the 37 columns are reported 0.0% missing in both partitions read and the check is outstanding for every one of them. On a billing dataset with many numeric amount columns, a zero-versus-missing distinction is exactly the kind of thing this check exists to catch.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `FK_PATIENT_ID_X`. The patient ID column is the primary identifier for
every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining.

**Identifier family:** Unknown — to confirm with data owner. The name differs from the
`PATIENT_ID_EXTN_X` used by the clinical families under `FreeText_FTA/`, which is a reason to
check rather than assume; **no join has been tested**.

**Secondary keys:** Unknown. `CASE_NO` is a candidate but profiles as `numeric`, not `id_like`.
`FK_PATIENT_ID_X` is the only column the profiler typed `id_like`.

**Coding standards:** Unknown — to confirm with data owner. `FK_DRG_ID` suggests a DRG coding
scheme and a dimension object named `VW_DRG_D` exists in the same run, but no join has been
tested and the relationship is not established.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown | **no join tested** | Several `FK_` columns and same-run `_D` dimension objects share naming, but no linkage has been established |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

### Other limitations

- **Duplicates:** Not checked. The two extract dates make this more pressing than usual: if
  `05-08-2024` and `06-08-2024` are separate extracts rather than two halves of one, rows may
  be duplicated across them.
- **Schema drift across partitions:** All indexed objects report 37 columns. Names, order and
  types verified identical in P10 and P35; the rest are not yet checked column by column.
- **Value-range anomalies:** Not checked. `LOS_DAYS` profiles as `categorical` rather than
  numeric, which is worth understanding before any length-of-stay calculation.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Incomplete object list:** The most consequential limitation on this page. Any count
  computed from the table above is a count over an unknown fraction of the family.
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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. `FK_PATIENT_ID_X` is the only column the profiler typed `id_like`. This is financial data at patient level — payer, subsidy and amount columns — which is a distinct sensitivity question from the clinical families and should not be assumed to fall under the same permissions. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. **How many partitions does this family have, and what are they?** The run appears to hold
   more objects than could be indexed. A definitive file list is needed before any count from
   this page is used.
2. Are `_Export_05-08-2024_` and `_Export_06-08-2024_` two halves of one extract, or two
   separate extracts? If separate, can rows appear in both?
3. **Do partitions P4, P5, P8 and P9 exist?**
4. What is the unit of observation — what does one row represent, and what causes rows to
   multiply?
5. What is this dataset, in one paragraph, and how does it relate to OP Billing, MED Billing,
   TP Billing and LIP Billing?
6. Which population is included, and who is excluded by what mechanism?
7. Is there a data dictionary? All 37 columns are currently undescribed and unclassified.
8. What do the `FK_` prefix and the `_IDK` element denote?
9. Why are `FK_DISCHARGE_DATE_IDK_X` / `_Z` typed `categorical` when the admit and billing
   date columns type as `date`?
10. `MCPS` and `OTHERS` are 100% empty in both partitions read — deprecated, or populated in a
    source not delivered here?
11. Why do the five payer columns share an identical missing percentage within each partition?
12. What are `ZPHS` and `ZWAV`?
13. Is `LOS_DAYS` a number, and why does it profile as `categorical`?
14. Is `FK_PATIENT_ID_X` the same identifier space as `PATIENT_ID_EXTN_X` in the clinical
    families? Does a crosswalk exist?
15. Does `FK_DRG_ID` join to `VW_DRG_D`, and do the other `FK_` columns join to the matching
    `_D` objects?
16. What is the delimiter and file encoding?
17. Are the amount columns in dollars, cents, or something else, and are they gross of GST?
18. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 37 rows, matching the 37 columns declared for every indexed object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. Column names and types transcribed from the screenshots for P10 and P35; object-level figures for 32 indexed objects. Object list flagged incomplete — the screenshot run is longer than the index. Category from the dataset name and `FK_PATIENT_ID_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — column names, types and per-column missing % read from
  `source_material/screenshots/mass_columns_screenshots/section_13.png` (P10) and
  `section_15.png` (P35). The family's blocks run continuously from section_13 to at least
  section_16. Object-level figures for the indexed objects from the same run.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this dataset.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names. For this
  family the reconstruction also under-counts objects and mangles filenames
  (`VW_IP_BILLING_F_Export:_05-08-2024_P14.c5v`, `VW_IP_BILLING_F-_Export_06-08-2024_P26.csv`),
  which is why the partition count here is marked unconfirmed rather than taken from it.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.
