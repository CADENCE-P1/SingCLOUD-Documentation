<!--
Worked example of template.md, filled for one dataset family from the condensed profiler
summary screenshots alone.

This is a BASE PAGE. It records what the summary establishes — object names, sizes, row and
column counts, column names, types and missing percentages — and marks everything else
unknown. It is meant to be filled in later, once the datasets are analysed properly.

Two fields are filled by convention rather than by evidence, and both are catalogue-wide
rules:
  - Category is read from the dataset name.
  - The patient ID column is the primary identifier.

Everything else is transcription and arithmetic. No property of the dataset is deduced from
missingness patterns, column naming or comparison with other datasets.

Contrast with template_sample_singcloud-event-diagnosis.md, which documents the same family
but reasons from the evidence to conclusions about unit of observation, column class and
partition ordering. That page is more useful and more falsifiable. This one is more
defensible. Both are legitimate; know which you are writing.
-->

# SingCLOUD — Event Diagnosis

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Documentation tier** | T2 short |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P1.csv` |
| 2 | `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P2.csv` |
| 3 | `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P3.csv` |
| 4 | `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P4.csv` |
| 5 | `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P5.csv` |
| 6 | `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P6.csv` |

All six sit under the prefix `common-data/SingCLoud/FreeText_FTA/`. Six objects, 32,000,357
rows, 33 columns each.

---

## Dataset Overview

**Category:** Event diagnosis — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner.

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner. Both the inclusion criteria and the
exclusion mechanism are outstanding.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** What one row represents,
and what causes rows to multiply, are not established. Until they are, no row count on this
page can be converted into a count of diagnoses, encounters, admissions or patients.

**Rows vs people:** 32,000,357 rows (profiler, 2026-07-23, P1–P6 summed); distinct patients
**not counted**.

**What is *not* in it:** Unknown — to be filled in. The 33 column names in *Key Variables* are
the complete column list for all six objects, so any variable not named there is not in these
objects.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/FreeText_FTA/VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P{1..6}.csv` |
| **Partitions** | 6 objects, `_P1` through `_P6`. Whether further partitions exist is unknown — to confirm with data owner |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. The object name contains `_Export_31-07-2024_`; what that date denotes is unconfirmed |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. The objects sit under a path segment named `FreeText_FTA` and four column names end in `_TXT`, neither of which confirms free-text content |

---

## Key Variables

All 33 columns, in the order printed in the report, identical in name and order across all six
objects. Row count matches Appendix A.

**Type** is the profiler's label and is provisional — it will be revised when the datasets are
analysed in detail. Three columns were typed differently in different partitions; both
readings are recorded.

**Description, Class, Coding / units, Sensitivity and Notes are outstanding for all 33
columns** and are not guessed here. Class in particular — Raw / Standardised / Derived — is
mandatory under `template.md` and needs a data dictionary or the owner: a suffix such as
`_STD`, `_TXT`, `_X` or `_Z` is a naming convention, not evidence of how a value was produced.
**Every column on this page is unclassified**, and the page cannot reach ✅ Verified until that
is resolved.

| # | Variable | Type | P1 | P2 | P3 | P4 | P5 | P6 |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | `DATA_SOURCE` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2 | `EVN_ID_EXTN` | id_like | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3 | `PATIENT_ID_EXTN_X` | id_like | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 4 | `VISIT_ADMIN_DATE_X` | date | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 5 | `VISIT_ADMIN_DATE_Z` | date | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 6 | `DISCHARGE_DATE_X` | date | 61.49 | 55.12 | 55.13 | 54.33 | 54.79 | 55.68 |
| 7 | `DISCHARGE_DATE_Z` | date | 61.49 | 55.12 | 55.13 | 54.33 | 54.79 | 55.68 |
| 8 | `PATIENT_TYPE_ETS_ID` | categorical | 0.3 | 0.04 | 0.0 | 0.0 | 0.0 | 0.0 |
| 9 | `EVN_FACILITY_EXTN` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 10 | `EVN_SERVICE_SPECIALTY_ETS_ID` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 11 | `MOV_TYPE_ETS_ID` | categorical | 17.02 | 13.93 | 13.71 | 12.7 | 12.11 | 12.45 |
| 12 | `MOV_CAT_ETS_ID` | categorical | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 13 | `DISCHARGE_OUTCOME` | categorical | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| 14 | `DISCHARGE_DISPOSITION_ETS_ID` | categorical | 59.6 | 60.72 | 60.46 | 60.19 | 59.21 | 58.56 |
| 15 | `DOC_TYPE_CODE` | categorical | 77.77 | 70.01 | 74.33 | 74.5 | 73.01 | 72.13 |
| 16 | `DOC_TYPE_ETS_ID` | categorical | 77.77 | 70.01 | 74.33 | 74.5 | 73.01 | 72.13 |
| 17 | `DIAG_SERVICE_SPECIALTY_ETS_ID` | categorical; **id_like in P4** | 77.77 | 70.01 | 74.33 | 74.5 | 73.01 | 72.13 |
| 18 | `DIAGNOSIS_NAME_ETS_ID` | **categorical P1; id_like P2–P3; numeric P4–P6** | 78.66 | 70.02 | 74.35 | 74.66 | 73.21 | 72.32 |
| 19 | `DIAGNOSIS_TYPE_ETS_ID` | categorical | 77.77 | 70.01 | 74.33 | 74.5 | 73.01 | 72.13 |
| 20 | `DIAGNOSIS_TYPE_TXT` | categorical | 91.05 | 78.09 | 81.75 | 81.39 | 79.74 | 79.25 |
| 21 | `DIAG_STATUS_ETS_ID` | categorical | 96.3 | 86.23 | 89.19 | 87.99 | 87.18 | 86.94 |
| 22 | `DIAG_ONSET_DATE_X` | date | 98.22 | 92.71 | 94.7 | 94.78 | 93.88 | 84.86 |
| 23 | `DIAG_ONSET_DATE_Z` | date | 98.22 | 92.71 | 94.7 | 94.78 | 93.88 | 84.86 |
| 24 | `DIAG_OCCURENCE_DATE_X` | **date P1–P4; categorical P5–P6** | 89.01 | 91.92 | 92.59 | 96.36 | 100.0 | 100.0 |
| 25 | `DIAG_OCCURENCE_DATE_Z` | **date P1–P4; categorical P5–P6** | 89.01 | 91.92 | 92.59 | 96.36 | 100.0 | 100.0 |
| 26 | `EVN_SERVICE_SPECIALTY_TXT` | categorical | 94.84 | 93.73 | 92.74 | 90.48 | 89.72 | 89.22 |
| 27 | `DIAG_SERVICE_SPECIALTY_TXT` | categorical | 83.19 | 75.52 | 80.91 | 83.22 | 82.39 | 79.48 |
| 28 | `EVN_SERVICE_SPECIALTY_TXT_STD` | categorical | 0.74 | 0.81 | 0.9 | 1.0 | 1.12 | 0.96 |
| 29 | `DIAG_SERVICE_SPECIALTY_TXT_STD` | categorical | 77.92 | 70.24 | 74.59 | 74.53 | 73.06 | 70.78 |
| 30 | `ICD_CODE_PMH_STD` | categorical | 94.95 | 93.92 | 92.95 | 90.48 | 89.73 | 90.08 |
| 31 | `ICD_CODE_OUTCOME_STD` | categorical | 99.29 | 99.08 | 99.06 | 99.06 | 98.96 | 98.73 |
| 32 | `DIAGNOSIS_NAME_TXT` | categorical | 84.21 | 76.27 | 81.58 | 83.99 | 83.26 | 80.66 |
| 33 | `DIAGNOSIS_NAME_TXT_STD` | categorical | 78.61 | 70.94 | 75.29 | 75.43 | 74.05 | 71.68 |

*(P1–P6 are missing %; profiler, 2026-07-23)*

**Spelling.** `DIAG_OCCURENCE_DATE_X` / `_Z` is spelled `OCCURENCE`, with one `R`, in all six
partitions. Copy it character for character.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `VISIT_ADMIN_DATE_X` | Unknown | Unknown | — |
| `VISIT_ADMIN_DATE_Z` | Unknown | Unknown | — |
| `DISCHARGE_DATE_X` | Unknown | Unknown | — |
| `DISCHARGE_DATE_Z` | Unknown | Unknown | — |
| `DIAG_ONSET_DATE_X` | Unknown | Unknown | — |
| `DIAG_ONSET_DATE_Z` | Unknown | Unknown | — |
| `DIAG_OCCURENCE_DATE_X` | Unknown | Unknown | — |
| `DIAG_OCCURENCE_DATE_Z` | Unknown | Unknown | — |

No date range is established and no principal date column is identified. Obtaining this needs
only a `min()` / `max()` per date column, and it is the highest-value gap on the page.

**No date format is established for any column either**, which matters before any range is
taken: the profiler parses with `dayfirst=True`, so `01/02/2021` is read as 1 February. If any
of these columns is month-first, every date derived from it is wrong and nothing raises.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown. The per-partition missing percentages in *Key
Variables* are **not** a time series: what the `_P{n}` split is by, and whether the partitions
are ordered, are both unknown.

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P1.csv` | 1,213.37 | 5,084,554 | 33 | 56.52 |
| `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P2.csv` | 1,562.11 | 6,102,154 | 33 | 53.00 |
| `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P3.csv` | 1,599.10 | 6,421,452 | 33 | 54.53 |
| `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P4.csv` | 1,759.08 | 7,056,689 | 33 | 54.67 |
| `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P5.csv` | 947.86 | 3,763,418 | 33 | 54.34 |
| `VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P6.csv` | 904.57 | 3,572,090 | 33 | 54.09 |
| **Family total** | **7,986.09** | **32,000,357** | 33 | — |

Family size and rows are sums of the six reported figures. Family missing % is left blank
deliberately: the per-object percentages are shares of six different denominators and cannot
be averaged.

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted. The gap cannot be measured from this output.*

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | **Names, order and count: yes** — 33 columns, same names in the same order in all six objects. **Types: no** — three columns differ, recorded in *Key Variables* |

---

## Provenance & Processing

Every field in this section is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes in this platform is not documented in any source available here.

**Processing applied:** Unknown — to confirm with data owner. De-identification,
pseudonymisation, de-duplication, rounding and small-cell suppression are all outstanding.

**Standardisation mappings:** Unknown — to confirm with data owner. Five column names end in
`_STD`; for each, the vocabulary, version, mapping rule and failed-match behaviour are
unrecorded, and whether the suffix denotes standardisation at all is unconfirmed. **Any result
depending on one of these columns is not reproducible until this is answered.**

**Transformations at load:** Unknown. Inspect `df.columns` after loading rather than assuming
the uppercase names transcribed on this page survive the load.

**Raw vs interpreted — what is lost:** Unknown. This needs the Class determination the page
cannot yet make. Several column names form apparent pairs (`_X`/`_Z`, `_TXT`/`_TXT_STD`); no
relationship between any pair has been established, and none is assumed here.

**Identifier handling:** Unknown — to confirm with data owner. Whether `PATIENT_ID_EXTN_X` is
a pseudonym, and whether it is stable across datasets and across successive extracts of this
one, is outstanding.

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 53.00–56.52% across the six objects (profiler, 2026-07-23) |
| Columns >50% missing | **22 of 33** in every partition |
| Columns 100% missing | **1** in P1–P4 (`DISCHARGE_OUTCOME`); **3** in P5–P6 (`DISCHARGE_OUTCOME`, `DIAG_OCCURENCE_DATE_X`, `DIAG_OCCURENCE_DATE_Z`) |

No interpretation of the missingness is offered here — not what causes it, not what it implies
about the unit of observation, and not whether it is a defect.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.
Full per-column figures are in *Key Variables*.

**Disguised missing:** **Not checked.** Sentinels such as `UNKNOWN`, `NIL`, `9`, `999` or
`1900-01-01` are counted as *present* by the profiler, whose null vocabulary is fixed: only
`""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN` and `.` count as missing. **Do not read "0.0%
missing" on this page as "0.0% unusable"** — eight columns are reported 0.0% missing in all
six partitions and the check is outstanding for every one of them.

### Overlap

**Primary identifier:** `PATIENT_ID_EXTN_X`. The patient ID column is the primary identifier
for every dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are
unknown — read it as `str` and inspect before joining, since an ID that loads as `int64` in
one partition and `object` in another produces a silent zero-row join.

**Identifier family:** Unknown — to confirm with data owner.

**Secondary keys:** Unknown. `EVN_ID_EXTN` is the other column the profiler typed `id_like`.

**Coding standards:** Unknown — to confirm with data owner. Two column names contain `ICD`;
whether either holds ICD codes, in what version, and under what dot convention, is unchecked.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| Unknown | Unknown | Unknown | Unknown | **no join tested** | No linkage to any other dataset has been established. Column-name similarity is not treated here as evidence of a shared key |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner.
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner.

This section needs the data owner and has no substitute. It is the one most likely to decide
whether a finding is valid, and it is entirely empty.

### Other limitations

- **Duplicates:** Not checked — neither exact duplicate rows nor repeated key values.
- **Schema drift across partitions:** Names, order and count are identical across all six
  objects (33 each). Types differ for three columns — `DIAGNOSIS_NAME_ETS_ID`
  (categorical / id_like / numeric), `DIAG_SERVICE_SPECIALTY_ETS_ID` (id_like in P4 only), and
  `DIAG_OCCURENCE_DATE_X` / `_Z` (date in P1–P4, categorical in P5–P6). The cause is unknown.
  **One consequence follows regardless of cause:** pandas performs its own per-file type
  inference, so these columns may load as different dtypes from different partitions. Read
  them as `str` explicitly.
- **Value-range anomalies:** Not checked.
- **Encoding:** Unknown. `tools/s3_data_catalog.py` attempts UTF-8 and falls back to latin-1
  with `errors="replace"` silently, so an object that needed the fallback is indistinguishable
  from one that did not.
- **Fitness for purpose:** **Cannot be assessed yet.** Fitness is a judgement about a dataset
  against a purpose, and this page establishes neither what the dataset is nor what one row
  represents. Treat the family as undocumented for the purpose of study design.

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
| **Free-text / PII exposure** | **Not assessed.** No column is classified Direct ID, Quasi-ID or Free text yet. The profiler typed `EVN_ID_EXTN` and `PATIENT_ID_EXTN_X` as `id_like` in all six partitions, plus `DIAGNOSIS_NAME_ETS_ID` (P2–P3) and `DIAG_SERVICE_SPECIALTY_ETS_ID` (P4) — digit-heavy values worth inspecting first. Absence of a classification here is an outstanding task, **not** a finding that the dataset carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. What is the unit of observation — what does one row represent, and what causes rows to
   multiply?
2. What is this dataset, in one paragraph: what does it record, and why does it exist?
3. What is the source system, and what does the `VW_` prefix denote?
4. Which population is included, and who is excluded by what mechanism?
5. Which institutions contribute, and from what date did each begin?
6. Is there a data dictionary? All 33 columns are currently undescribed and unclassified.
7. For each column: is it a source value, a mapped value, or a computed/interpreted one?
   (Class is mandatory and cannot be filled without this.)
8. For each of the five `_STD` columns: what vocabulary, what version, what mapping rule, and
   what happens on a failed match?
9. What is the relationship between the apparent `_X` / `_Z` pairs, and which should be
   preferred?
10. Which columns are coded, and against which reference tables?
11. What ICD version do `ICD_CODE_PMH_STD` and `ICD_CODE_OUTCOME_STD` use, and are codes
    dotted, undotted, or both?
12. Is `DISCHARGE_OUTCOME` — 100% empty in all six objects — deprecated, or populated in a
    source not delivered here?
13. `DIAG_OCCURENCE_DATE_X` / `_Z` are 100% empty in P5 and P6 but populated in P1–P4. Why?
14. What determines the `_P{n}` split, and are the partitions ordered in any way?
15. Are there partitions beyond P6? This run profiled six.
16. Is `PATIENT_ID_EXTN_X` a pseudonym, and is it stable across datasets and across successive
    extracts of this one?
17. Does a crosswalk exist to the identifiers used by other families in this catalogue?
18. What is the delimiter and file encoding, and are all six objects the same?
19. What date does `31-07-2024` in the object name refer to?
20. Which fields are mandatory at entry, and for whom?
21. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

The per-column profile is the *Key Variables* table above and is not repeated here: with
Description, Class, Coding and Sensitivity still outstanding, the two tables would be
identical. Both carry 33 rows, matching the 33 columns declared for every object.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-30 | Page created against `template.md` from the profiler run of 2026-07-23, using the condensed summary screenshots only. Six objects, 32,000,357 rows, 33 columns. Category taken from the dataset name and `PATIENT_ID_EXTN_X` named as primary identifier, both by catalogue convention; every other field either transcribed or left unknown. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — read from
  `source_material/screenshots/mass_columns_screenshots/section_03.png` (report header;
  partitions P1–P5) and `section_04.png` (P5 tail and P6). The report header reads
  `S3 DATA CATALOG - CONDENSED SUMMARY`, `Rebuilt 2026-07-23 05:49:02 - 275 datasets`. It also
  prints the source bucket URI, **redacted here** under the no-infrastructure rule in
  `template.md`.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour (type
  inference, null vocabulary, `on_bad_lines="skip"`, encoding fallback), never for any property
  of this dataset.
- **Deliberately not used:** `source_material/imported/profiler_report_full.txt`,
  `dataset_summary.csv`, `column_summary.csv`, `data_context_extract.md`,
  `hf_diagnosis_data_context.md`, `catalogue_config_snapshot.md`, and
  `datasets/full_inventory.md`. These carry additional material — analyst notes, catalogue
  aliases, an eight-partition claim, dimension-table candidates — and several are OCR
  reconstructions with known transcription errors. Excluding them is the point of this
  version, not an oversight. `template_sample_singcloud-event-diagnosis.md` uses them.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.
