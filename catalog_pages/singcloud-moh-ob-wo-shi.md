# SingCLOUD — MOH OB WO SHI

| | |
|---|---|
| **Status** | ⚪ Stub |
| **Profiled on** | 2026-07-23 |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

| # | Object |
|---:|---|
| 1 | `VW_MOH_OB_WO_SHI_F_Export_31-07-2024.csv` |

Under the prefix `common-data/SingCLoud/NonFreeText_Files/`. One object, 2,654,121 rows, 146
columns, unpartitioned.

---

## Read this first

| | Issue | What to do |
|---|---|---|
| 🔴 | **Patient column is `NRIC_X`** | **Confirm whether it is pseudonymised before handling the data** |
| 🔴 | **91.22% of cells are empty** — but the layout is one 4-column block per condition, 36 conditions wide | Most cells may be empty *by design*. Confirm before reading this as a data-quality problem |
| 🟡 | **Schema is completely regular** — 2 identity columns + 36 × (`firstyr_`, `firstdate_X`, `firstdate_Z`, `sc_pattype_`) = 146 | The remaining transcription is just 25 condition names |
| 🟡 | **`cvsypmtoms`** has letters transposed — not `cvsymptoms` — and it propagates through all four columns of that block | Copy as written |
| 🟡 | **72 date columns**, no principal one identified | An empty condition block may mean "never had it" *or* "had it before the data begins" — different facts |
| 📋 | 100 of 146 columns not transcribed | Structure is known; only the last 25 condition names are missing |

---

## Dataset Overview

**Category:** MOH OB WO SHI — taken from the dataset name. Not yet confirmed against a data
dictionary or the data owner. **What `WO SHI` stands for is unknown**, and it is the part of
the name that distinguishes this object from
[MOH OB Operation](singcloud-moh-ob-operation.md) and
[MOH OB Procedure](singcloud-moh-ob-procedure.md).

**Description:** Unknown — to be filled in.

**Data source:** Unknown — to confirm with data owner.

**Population:** Unknown — to confirm with data owner.

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** **Unknown — to confirm with data owner.** The column structure
described below — one block of four columns per condition, 36 conditions wide — is the shape
of one row per *patient* with condition history spread across columns, rather than one row per
condition. That reading is not established and is not adopted here, but it is the first thing
to confirm, because it determines whether 2,654,121 rows is a patient count or something else.

**Rows vs people:** 2,654,121 rows (profiler, 2026-07-23); distinct patients **not counted**.

**What is *not* in it:** Unknown — to be filled in. The column structure is described below;
the full 146-name list is partially transcribed.

### Access

| | |
|---|---|
| **Catalogue alias(es)** | Unknown — to be filled in |
| **Source object(s)** | `common-data/SingCLoud/NonFreeText_Files/VW_MOH_OB_WO_SHI_F_Export_31-07-2024.csv` |
| **Partitions** | 1 object, unpartitioned |
| **Format** | CSV by file extension. Delimiter and encoding unknown |
| **Extract date** | Unknown. The object name contains `_Export_31-07-2024`, matching the two other MOH OB families |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Unknown. This object sits under `NonFreeText_Files/` |

---

## Key Variables

**The schema is highly regular.** After two identity columns, it is 36 repeating blocks of
four columns, one block per named condition:

| Position | Column pattern | Type |
|---|---|---|
| 1 | `DATA_SOURCE` | categorical |
| 2 | `NRIC_X` | id_like |
| 3, 7, 11, … | `firstyr_<condition>` | numeric |
| 4, 8, 12, … | `firstdate_<condition>_X` | date |
| 5, 9, 13, … | `firstdate_<condition>_Z` | date |
| 6, 10, 14, … | `sc_pattype_<condition>` | categorical |

2 + (36 × 4) = 146, which matches the declared column count exactly.

**Within each block, the three `firstyr` / `firstdate_X` / `firstdate_Z` columns always share
an identical missing percentage**, and `sc_pattype` is always slightly emptier. That holds for
every block transcribed.

**Type** is the profiler's label and is provisional until pass 2.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. Every column here is unclassified.

### Columns transcribed so far — 46 of 146

| # | Variable | Type | Missing % | Description | Class | Coding / units | Sensitivity |
|---:|---|---|---:|---|---|---|---|
| 1 | `DATA_SOURCE` | categorical | 0.0 | | | | |
| 2 | `NRIC_X` | id_like | 0.0 | | | | |
| 3 | `firstyr_arrhythmia` | numeric | 86.77 | | | | |
| 4 | `firstdate_arrhythmia_X` | date | 86.77 | | | | |
| 5 | `firstdate_arrhythmia_Z` | date | 86.77 | | | | |
| 6 | `sc_pattype_arrhythmia` | categorical | 93.96 | | | | |
| 7 | `firstyr_cad` | numeric | 80.94 | | | | |
| 8 | `firstdate_cad_X` | date | 80.94 | | | | |
| 9 | `firstdate_cad_Z` | date | 80.94 | | | | |
| 10 | `sc_pattype_cad` | categorical | 86.11 | | | | |
| 11 | `firstyr_cvsypmtoms` | numeric | 89.68 | | | | |
| 12 | `firstdate_cvsypmtoms_X` | date | 89.68 | | | | |
| 13 | `firstdate_cvsypmtoms_Z` | date | 89.68 | | | | |
| 14 | `sc_pattype_cvsypmtoms` | categorical | 92.28 | | | | |
| 15 | `firstyr_circulatory` | numeric | 87.49 | | | | |
| 16 | `firstdate_circulatory_X` | date | 87.49 | | | | |
| 17 | `firstdate_circulatory_Z` | date | 87.49 | | | | |
| 18 | `sc_pattype_circulatory` | categorical | 94.08 | | | | |
| 19 | `firstyr_coagdefects` | numeric | 97.47 | | | | |
| 20 | `firstdate_coagdefects_X` | date | 97.47 | | | | |
| 21 | `firstdate_coagdefects_Z` | date | 97.47 | | | | |
| 22 | `sc_pattype_coagdefects` | categorical | 99.65 | | | | |
| 23 | `firstyr_congenitalhd` | numeric | 97.93 | | | | |
| 24 | `firstdate_congenitalhd_X` | date | 97.93 | | | | |
| 25 | `firstdate_congenitalhd_Z` | date | 97.93 | | | | |
| 26 | `sc_pattype_congenitalhd` | categorical | 98.91 | | | | |
| 27 | `firstyr_cx_cvdimplant` | numeric | 98.85 | | | | |
| 28 | `firstdate_cx_cvdimplant_X` | date | 98.85 | | | | |
| 29 | `firstdate_cx_cvdimplant_Z` | date | 98.85 | | | | |
| 30 | `sc_pattype_cx_cvdimplant` | categorical | 99.65 | | | | |
| 31 | `firstyr_dm` | numeric | 73.24 | | | | |
| 32 | `firstdate_dm_X` | date | 73.24 | | | | |
| 33 | `firstdate_dm_Z` | date | 73.24 | | | | |
| 34 | `sc_pattype_dm` | categorical | 79.99 | | | | |
| 35 | `firstyr_deviceadveffect` | numeric | 99.99 | | | | |
| 36 | `firstdate_deviceadveffect_X` | date | 99.99 | | | | |
| 37 | `firstdate_deviceadveffect_Z` | date | 99.99 | | | | |
| 38 | `sc_pattype_deviceadveffect` | categorical | 100.0 | | | | |
| 39 | `firstyr_digestive` | numeric | 98.61 | | | | |
| 40 | `firstdate_digestive_X` | date | 98.61 | | | | |
| 41 | `firstdate_digestive_Z` | date | 98.61 | | | | |
| 42 | `sc_pattype_digestive` | categorical | 99.52 | | | | |
| 43 | `firstyr_drugadveffect` | numeric | 98.05 | | | | |
| 44–146 | *not yet transcribed* | | | | | | |

*(profiler, 2026-07-23)*

**Spelling.** `cvsypmtoms` has the letters transposed — it is not `cvsymptoms`. The
misspelling propagates through all four columns of that block. Copy it character for
character.

**The conditions are cardiovascular and metabolic**, on the evidence of the names read so far:
arrhythmia, CAD, circulatory, coagulation defects, congenital heart disease, cardiovascular
device implant, diabetes, device adverse effect, digestive, drug adverse effect. What the
remaining 25 blocks cover is not yet read.

**`sc_pattype_deviceadveffect` is 100% empty** and its three sibling columns are 99.99% — the
condition is effectively unrecorded.

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> This page lists no values for any column. Enumerate the distinct values in your own extract
> before filtering, and re-check them against each new extract — a value string that has
> drifted returns zero rows without raising an error.

---

## Time Coverage

**Unknown.** No date range is established. The object carries **72 date columns** — a
`firstdate_<condition>_X` and `_Z` for each of the 36 blocks — plus 36 `firstyr_<condition>`
numeric year columns. No principal date column is identified, and with 72 candidates the
question of which to use is not a formality.

**Date format:** Unknown. The profiler parses with `dayfirst=True`, so `01/02/2021` reads as
1 February. If any column is month-first, every date derived from it is wrong and nothing
raises. Note that `firstyr_*` appears to duplicate the year part of `firstdate_*` in a
separate numeric column — if so, comparing the two would be a cheap way to test the parse.

**Completeness over the period:** Unknown — depends on the date range above.

**Variable availability over time:** Unknown.

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Transcribed from the condensed profiler summary, run 2026-07-23.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `VW_MOH_OB_WO_SHI_F_Export_31-07-2024.csv` | 1,531.25 | 2,654,121 | 146 | 91.22 |
| **Family total** | **1,531.25** | **2,654,121** | 146 | 91.22 |

*The row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`
([tools/s3_data_catalog.py](../tools/s3_data_catalog.py)), so unparseable lines are dropped
silently and never counted.*

**91.22% of all cells are empty** — the emptiest object in the catalogue outside the SCDB
`BEFORE` tables. That is the expected consequence of a wide condition-per-column layout where
each patient has few conditions: most cells are empty *by design* rather than by defect. That
reading is not established, but it is the obvious hypothesis to test, and it changes how the
figure should be interpreted.

| Metric | Value |
|---|---|
| Sample size (distinct patients) | **not counted** — the profiler does not compute it |
| Schema consistent across partitions | n/a — single object |

---

## Provenance & Processing

Every field here is owner-only, and none is inferred from column naming.

**Collection mechanism:** Unknown — to confirm with data owner.

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.

**Extract pipeline:** Unknown — to confirm with data owner. The object name begins `VW_`; what
that prefix denotes is not documented in any source available here. A regular 36 × 4 layout is
the signature of a pivot performed somewhere in the pipeline, but nothing establishes that.

**Processing applied:** Unknown — to confirm with data owner.

**Standardisation mappings:** Unknown. No column carries a `_STD` suffix. The condition names
themselves (`cad`, `dm`, `congenitalhd`) are abbreviations from some controlled list; which
one is not established.

**Transformations at load:** Unknown. Inspect `df.columns` after loading — this object's
lower-case names with embedded underscores are the kind a loader that normalises case would
flatten.

**Raw vs interpreted — what is lost:** Unknown. Needs the Class determination this page cannot
yet make. A column named `firstyr_<condition>` is a derived summary — the *first* year a
condition appeared — not a source observation. Where the underlying records are, and whether
they are obtainable, is unknown and worth asking.

**Identifier handling:** Unknown — to confirm with data owner. As with the two other MOH OB
families, the patient column is `NRIC_X`. **Whether it is pseudonymised must be answered
before the data is handled.**

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | 91.22% (profiler, 2026-07-23) |
| Columns >50% missing | **All 144 condition columns** transcribed so far, ranging 73.24% to 100% |
| Columns 100% missing | At least 1 (`sc_pattype_deviceadveffect`); the untranscribed blocks are not yet checked |

Only `DATA_SOURCE` and `NRIC_X` are fully populated.

**Columns that matter:** Unknown — ranking columns by consequence needs their descriptions.
The least-empty conditions are the most-recorded ones: `dm` at 73.24%, `cad` at 80.94%,
`arrhythmia` at 86.77%.

| Variable | Missing % | Consequence if unusable |
|---|---:|---|
| | | |
**Disguised missing:** **Not checked.**

- Profiler counts only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` as missing.
- `UNKNOWN`, `NIL`, `9`, `999`, `1900-01-01` all read as *present* — invisible in these figures.
- On this object the risk runs the other way from most: a `firstyr` column filled with `9999` or a `firstdate` filled with `1900-01-01` would be counted as *present*, making a condition look recorded when it is not.
- Run `value_counts()` before trusting any 0.0% figure.

### Overlap

**Primary identifier:** `NRIC_X`. The patient ID column is the primary identifier for every
dataset in this catalogue. Its dtype as read, leading zeros, casing and padding are unknown —
read it as `str` and inspect before joining. Singapore NRIC values carry a trailing check
letter and leading zeros, both of which a numeric read would destroy.

**Identifier family:** Unknown — to confirm with data owner. `NRIC_X` matches the two other
MOH OB families and the SCDB set; **no join has been tested** between any of them.

**Secondary keys:** None apparent. `NRIC_X` is the only column the profiler typed `id_like`,
and the object carries no case, episode or encounter identifier at all — which is consistent
with one row per patient, and is the strongest available hint about the unit of observation.

**Coding standards:** Unknown — to confirm with data owner.

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| [MOH OB Operation](singcloud-moh-ob-operation.md) | `NRIC_X` | Unknown | Unknown | **no join tested** | Shared identifier column name and extract date only |
| [MOH OB Procedure](singcloud-moh-ob-procedure.md) | `NRIC_X` | Unknown | Unknown | **no join tested** | Same |

**Known linkage pitfalls:** None recorded — no linkage has been attempted. An empty list, not
a clean bill of health.

### Bias

- **Coverage / selection:** Unknown — to confirm with data owner.
- **Recording practice:** Unknown — to confirm with data owner. With a "first year of
  condition" layout, how far back the source reaches determines whether an empty cell means
  "no condition" or "condition predates the data".
- **Changes over time:** Unknown — to confirm with data owner.
- **Ascertainment:** Unknown — to confirm with data owner. Which conditions got a column at
  all is itself a selection decision, and only 36 exist.

### Other limitations

- **Duplicates:** Not checked.
- **Schema drift across partitions:** n/a — single object.
- **Value-range anomalies:** Not checked. The 36 `firstyr_*` columns are numeric years and are
  the obvious place for an impossible value to hide.
- **Encoding:** Unknown. The profiler attempts UTF-8 and falls back to latin-1 with
  `errors="replace"` silently.
- **Column names outstanding:** 100 of 146 columns are not yet transcribed. The structure is
  known, so what is missing is the list of the remaining 25 condition names.
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
| **Free-text / PII exposure** | **Not assessed, and this object warrants particular care.** The patient column is `NRIC_X`, typed `id_like` — if it holds NRIC values rather than a pseudonym, this is direct identifier data. What sits beside it is a per-patient condition history across 36 conditions with first-onset dates: a combination that is highly identifying even without a direct identifier, because a person's specific set of conditions and their onset years is close to unique. Absence of a classification here is an outstanding task, **not** a finding that the object carries no PII |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**

1. **Is `NRIC_X` a pseudonym or a real NRIC?** This gates everything else.
2. **What does `WO SHI` stand for?**
3. Is the unit of observation one row per patient? The object has no case or encounter
   identifier, which points that way but does not establish it.
4. What is this dataset, in one paragraph, and how does it relate to MOH OB Operation and MOH
   OB Procedure?
5. **Is the 91.22% missing figure structural** — most patients having few of the 36
   conditions — or does it indicate incomplete data?
6. What are the remaining 25 conditions, and what determined which 36 got a column?
7. What does `sc_pattype_` denote, and why is it consistently emptier than the three date and
   year columns in the same block?
8. Does `firstyr_<condition>` duplicate the year of `firstdate_<condition>`? If they disagree,
   which is authoritative?
9. What is the relationship between `firstdate_*_X` and `firstdate_*_Z`?
10. **How far back does the source reach?** An empty condition block could mean "never had it"
    or "had it before the data begins" — those are different facts.
11. Is `cvsypmtoms` a misspelling in the source, and will it be corrected in a future extract?
12. `sc_pattype_deviceadveffect` is 100% empty and its siblings 99.99% — is that condition
    deprecated, or genuinely almost never recorded?
13. Where are the underlying records from which these first-onset summaries were derived?
14. Is `NRIC_X` linkable to the patient columns in the other families? Does a crosswalk exist?
15. What is the delimiter and file encoding?
16. Who is the data owner and steward role, what is the approval route, and what lead time
    should a study plan for?

---

## Appendix A — Full column profile

**Partially transcribed.** 46 of 146 columns appear in *Key Variables* above. The schema
structure is established — 2 identity columns plus 36 blocks of 4 — so what remains is the
names of the last 25 condition blocks and their missing percentages.

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| 2026-07-31 | Page created against `template.md` from the profiler run of 2026-07-23. One object, 2,654,121 rows, 146 columns. Column structure established and 46 columns transcribed from the screenshots; 100 outstanding. Category from the dataset name and `NRIC_X` as primary identifier, both by catalogue convention. | CCJX |

## Appendix C — Sources

- **Profiler run 2026-07-23** — object header and the first 46 columns, read from
  `source_material/screenshots/mass_columns_screenshots/section_17.png`.
- `tools/s3_data_catalog.py` — cited only for the profiler's documented behaviour, never for
  any property of this object.
- **Not used for column names:** `source_material/imported/profiler_report_full.txt` and
  `column_summary.csv`, which are OCR reconstructions that corrupt column names.
- **Data owner correspondence — none.** Every governance field on this page is unconfirmed.
