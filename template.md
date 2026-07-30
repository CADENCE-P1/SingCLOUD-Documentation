<!--
================================================================================
SingCLOUD dataset documentation template  (extended)
================================================================================
Fill one copy per DATASET FAMILY (not per partition file) and save as
datasets/<slug>.md, then add a row to datasets/index.md.

Section order follows docs/00_rationale.md, so that a reader can answer, in order:
  what is in it        → Dataset Overview, Key Variables, Time Coverage
  where did it come from → Provenance & Processing
  can I actually use it  → Dataset Information, Data Quality
  am I allowed to use it → Ownership & Governance

{{PLACEHOLDERS}} are machine-fillable from tools/s3_data_catalog.py output
(dataset_summary.csv / column_summary.csv). Everything else is written by hand.

TWO PASSES
  Pages are built in two passes, and a page is useful after the first.
    Pass 1 — BASE PAGE. Everything the profiler summary establishes: objects,
             sizes, rows, columns, column names, types, missingness. Plus the
             two convention fields below. Everything else marked unknown.
             Status ⚪ Stub.
    Pass 2 — Fill from real analysis of the data and from the data owner:
             descriptions, Class, coding, value domains, date ranges, linkage,
             governance. Status 🟡 Draft, then ✅ Verified.
  A worked pass-1 page is template_sample_singcloud-event-diagnosis_screenshots-only.md.
  Write pass 1 without guessing: an honest unknown is worth more than a plausible
  invention, because the invention is what a later reader will act on.

FILL RULES
  - Unknown is a value. Write:  Unknown — to confirm with data owner
    Never delete a row. A missing row tells the reader nothing; an explicit gap
    tells them who to ask.
  - Keep unknowns SHORT. "Unknown — to confirm with data owner" is the whole
    entry. Do not explain that the profiler summary carries no min/max, no top
    values and no distinct counts — that is a known property of the source, and
    restating it on every field is noise.
  - Two fields are filled by convention, not evidence, on every page:
      Category            -> read from the dataset name
      Primary identifier  -> the patient ID column
    Both are marked at the point of use below. Neither is ever left unknown.
  - Use  n/a — <one-line reason>  when a field genuinely cannot apply.
  - Every number carries (source, date, scope):
    "5,084,554 rows (profiler, 2026-07-23, P1 only)" — never "~5M rows".
  - Exact strings, verbatim: column names, aliases and file names are copied
    character for character, including OCCURENCE, SingCLoud, and the space in
    "COVID Reinfections".
  - Redact infrastructure: no bucket names, object URIs, account IDs or
    credentials. Refer to objects prefix-relative.
  - No patient-level data, no study findings.

Guidance for every field is at the bottom of this file, under
"Appendix D — How to fill this in".

A section-by-section explanation of what each part of this template is for —
read this once before your first dataset page — is in template_intro.md.
================================================================================
-->

# {{DATASET_NAME}}

| | |
|---|---|
| **Status** | ⚪ Stub / 🟡 Draft / ✅ Verified |
| **Documentation tier** | T1 full / T2 short / T3 index-only |
| **Profiled on** | {{PROFILED_AT}} |
| **Last reviewed** | *not yet reviewed* |

**Objects included in this page**

<!-- Every .csv this page was built from, by name, numbered. This is the first thing a reader
checks: does this page describe the files I am holding? Name them even when there are twenty
— a "P1…P8" pattern hides whether P7 was actually profiled. -->

| # | Object |
|---:|---|
| 1 | `{{S3_KEY_BASENAME}}` |

All sit under the prefix `<prefix-relative path>`. <!-- Then one line of totals: n objects,
n rows, n columns each. -->

---

## Dataset Overview

**Category:** <!-- READ IT FROM THE DATASET NAME. VW_EVENT_DIAGNOSIS_F -> "Event diagnosis".
This field only tells a reader what kind of dataset they are looking at; it is not a claim
about clinical content, and it never waits on a data dictionary or the data owner. Say it is
name-derived and unconfirmed, but never leave it unknown. -->

**Description:** <!-- 2–3 sentences. What it records and why it exists. -->

**Data source:** <!-- The upstream system, named: national claims, statutory notification,
clinical system at participating institutions, national registry. -->

**Population:** <!-- Who is IN it. Then a SEPARATE sentence: who is EXCLUDED, and by what
mechanism (only claims-generating care / only confirmed cases / only participating
institutions). The exclusion sentence is the one that changes study designs. -->

**Institutional / geographic coverage:** Unknown — to confirm with data owner.

**Unit of observation:** One row per <!-- patient / encounter / diagnosis event / test result
/ dispensed item -->.
<!-- Then one sentence on what makes rows multiply: "an encounter with four diagnoses yields
four rows". This is the single most misread property of a dataset. -->

**Rows vs people:** {{N_ROWS}} rows; <!-- distinct patients, counted --> distinct patients.
<!-- The profiler does NOT compute distinct patients. If you have not counted them, write
"not counted" — do not let the row count stand in for a headcount. -->

**What is *not* in it:**
- <!-- Variables a reader would reasonably expect and will not find. Highest-value list on the page. -->

### Access

| | |
|---|---|
| **Catalogue alias(es)** | `<exact alias string>` |
| **Source object(s)** | `{{SOURCE_PATH_PATTERN}}` <!-- prefix-relative, e.g. common-data/SingCLoud/FreeText_FTA/... --> |
| **Partitions** | {{N_PARTITIONS}} files — pattern `<...>` |
| **Format** | CSV, delimiter `,`, UTF-8 <!-- casemix is pipe-delimited; state encoding if not UTF-8 --> |
| **Extract date** | <!-- the date in the file name or delivery — a dataset is a snapshot, this says which one --> |
| **Refresh cadence** | Unknown — to confirm with data owner |
| **Free-text content** | Yes / No <!-- objects under FreeText_FTA/ carry free-text clinical fields --> |

---

## Key Variables

<!-- EVERY column, in file order. Row count here must equal Appendix A. If the manifest is
partial (fields used in one analysis rather than the full schema), say so explicitly.

PASS 1 uses the table below: ordinal, name, type, and missing % PER PARTITION. One column
per object, not a single averaged figure — the per-partition spread is evidence in its own
right, and averaging destroys it. State plainly that the remaining fields are outstanding;
do not fill them from column naming.

PASS 2 adds Description, Class, Coding / units and Sensitivity as further columns, or as a
second table if the row gets too wide to read. -->

| # | Variable | Type | P1 | P2 | P3 | … |
|---:|---|---|---:|---:|---:|---:|
| {{ORDINAL}} | `{{COLUMN}}` | {{TYPE}} | {{MISSING_PCT}} | | | |

*(P1…Pn are missing %; profiler, {{PROFILED_AT}})*

**Type** is the profiler's label and is provisional until pass 2. Where the profiler typed a
column differently in different partitions, record BOTH readings rather than picking one —
that disagreement is a real warning about the column's values.

**Outstanding until pass 2, for every column:** Description, Class, Coding / units,
Sensitivity. <!-- Say this explicitly rather than leaving blank cells. A suffix such as _STD,
_TXT, _X or _Z is a naming convention, not evidence of how a value was produced — Class in
particular cannot be read off a column name. -->

**Class** — mandatory for every column by pass 2:

| Class | Meaning | Suitable for | Not suitable for |
|---|---|---|---|
| **Raw** | As entered or measured at source; not transformed | Model training on source signal; audit; re-derivation | Cross-site comparison without your own normalisation |
| **Standardised** | Same information, mapped to a controlled vocabulary or normalised format | Cohort selection; cross-site comparison | Anything depending on distinctions the mapping may collapse |
| **Derived** | Computed or **interpreted** — a human or algorithm made a judgement | Convenience analysis | A substitute for the underlying signal |

<!-- Where the source keeps paired columns (_X/_Z, _TXT/_TXT_STD), document BOTH rows and
say in Notes which to prefer and why. -->

<!-- This template does NOT enumerate the values of categorical columns. The condensed
profiler report carries no top-values block, and transcribing value lists by hand for every
categorical field, for every dataset family, is not sustainable. Where the domain of a field
matters, point the reader at the reference object that defines it (a `VW_*_D_` dimension
table, a published code list) rather than reproducing a sample of it here. -->

> **Value strings drift between extracts** (`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`).
> No page in this catalogue lists the values of a categorical column, so nothing here can be
> copied into a filter. Enumerate the distinct values in your own extract before filtering,
> and re-check them against each new extract — a value string that has drifted returns zero
> rows without raising an error.

---

## Time Coverage

| Date column | Start | End | Source |
|---|---|---|---|
| `<PRINCIPAL_DATE_COLUMN>` | {{DATE_MIN}} | {{DATE_MAX}} | profiler {{PROFILED_AT}} |

<!-- EVERY date column, one row each, principal one first. A range taken from the wrong column
is a common and invisible error. On a pass-1 page every cell here is Unknown; leave the rows
in, because the list of date columns is itself information. -->

**Date format:** <!-- The format each date column is stored in, or Unknown. This belongs
BEFORE any range is taken: the profiler parses dayfirst=True, so 01/02/2021 reads as
1 February. If a column is month-first, every date derived from it is wrong and nothing
raises. An unambiguous format (YYYY-MM-DD HH:MM:SS) makes the question moot — say so. -->

**Completeness over the period:** <!-- A date range hides holes. Gaps, ramp-up periods, and
truncated tails — a dataset that "runs to 2024-02-28" may just be when the extract was cut.
"Unknown — not yet checked" is acceptable; silence is not. -->

**Variable availability over time:** <!-- Fields absent or largely empty in early records
because the collection tool did not exist yet, with the approximate date each becomes
usable. Detect them by checking missingness by year: a field at 100% missing before some
date is the signature. -->

| Variable | Usable from | Evidence |
|---|---|---|
| | | |

---

## Dataset Information

*Machine-generated from `tools/s3_data_catalog.py`, run {{PROFILED_AT}} — regenerate rather
than hand-edit.*

| Object | Size (MB) | Rows | Cols | Overall missing % |
|---|---:|---:|---:|---:|
| `{{S3_KEY_BASENAME}}` | {{FILE_SIZE_MB}} | {{N_ROWS}} | {{N_COLS}} | {{OVERALL_MISSING_PCT}} |
| **Family total** | | | | |

*Every row count above is a lower bound: the profiler reads with `on_bad_lines="skip"`, so
unparseable lines are dropped silently and never counted.*

| Metric | Value |
|---|---|
| Sample size (distinct patients) | <!-- counted, or "not counted" --> |
| Schema consistent across partitions | Yes / No / not checked |

---

## Provenance & Processing

<!-- Answers "where did each value come from, and what happened to it on the way?"
A field named DIAGNOSIS holding a clinician's interpretation and a field holding the source
waveform are not interchangeable, and a column list alone will not distinguish them. -->

**Collection mechanism:** Unknown — to confirm with data owner.
<!-- How a value physically arrives: clinician entry at point of care, instrument feed,
claims submission, statutory notification, batch extract. -->

**Who enters it, and under what incentive:** Unknown — to confirm with data owner.
<!-- Billing-entered and clinically-entered fields fail differently. -->

**Extract pipeline:** <!-- What happened between the source system and the object you load:
views (VW_* implies a database view), joins, filters, truncation (NIRListtruncated — what
was truncated?). -->

**Processing applied:** <!-- De-identification, pseudonymisation, standardisation mappings,
de-duplication, rounding, small-cell suppression. -->

**Standardisation mappings:** <!-- For every _STD field: what vocabulary, what version, what
rule, what happens on a failed match. If undocumented, SAY SO — results depending on an
undocumented mapping are not reproducible. -->

**Transformations at load:** <!-- Things the platform or loader does that are not in the
file: column lowercasing, dtype inference, delimiter/encoding handling. -->

**Raw vs interpreted — what is lost:** <!-- Where a Derived or Standardised field replaces
something richer: what distinction is gone, and whether the raw value is obtainable
anywhere. -->

**Identifier handling:** Unknown — to confirm with data owner.
<!-- Is the ID a pseudonym? Stable across datasets? Stable across extracts of the SAME
dataset? A pseudonym re-minted per extract makes longitudinal linkage impossible. -->

---

## Data Quality

### Missingness

| Metric | Value |
|---|---|
| Overall missing (share of all cells) | {{OVERALL_MISSING_PCT}}% |
| Columns >50% missing | <!-- count --> |
| Columns 100% missing | <!-- count — these are usually schema placeholders --> |

**Columns that matter** *(full per-column table in Appendix A)*:

| Variable | Missing % | Consequence |
|---|---:|---|
| `<COLUMN>` | {{MISSING_PCT}} | <!-- what a study loses if this column is unusable --> |

**Disguised missing:** <!-- The profiler counts only "", NA, N/A, NULL, null, None, NaN and
"." as missing. Sentinels like UNKNOWN, NIL, 9, 999, 1900-01-01 are counted as PRESENT.
A column reported 0.0% missing can be 40% unusable. The condensed report gives no value
profile, so this CANNOT be answered from the profiler — it needs a value_counts() against the
extract, or the owner. Name the columns most likely to hide a sentinel and say the check is
outstanding; record "checked, none found" only if someone actually ran it. -->

### Overlap

**Primary identifier:** `<PATIENT_ID_COLUMN>` — <!-- THE PATIENT ID COLUMN IS ALWAYS THE
PRIMARY IDENTIFIER on a page in this catalogue. Name it directly; never write "not
determined". Then give what is genuinely uncertain: dtype as read, and format — leading
zeros, casing, padding, and whether it is int64 in one partition and object in another. -->

**Identifier family:** <!-- uin / PATIENT_ID_EXTN_X / other / unconfirmed. Cross-family joins
need a crosswalk that may not exist — see docs/03_linkage_guide.md -->

**Secondary keys:** <!-- encounter ID, case number, accession number, order ID -->

| Links to | On | Granularity | Cardinality | Overlap tested? | Notes |
|---|---|---|---|---|---|
| | | 1:1 / 1:N / N:M | | date + figure, or "untested" | |

**Coding standards:** <!-- ICD-10 / SNOMED / local codes / free text. Note version and any
WITHIN-dataset inconsistency — the ICD-10 dot problem (I21.0 vs I210) is the canonical
example. -->

**Known linkage pitfalls:**
- <!-- Only things that have actually bitten someone: zero-row joins, silent all-null merges,
granularity multiplication. -->

### Bias

<!-- The profiler cannot help here at all, and this is usually the field that decides whether
findings are valid. Needs the data owner. -->

- **Coverage / selection:** <!-- who is systematically absent, and why -->
- **Recording practice:** <!-- systematic under-recording; differences between institutions -->
- **Changes over time:** <!-- coding practice, policy, or system changes that create artefactual trends -->
- **Ascertainment:** <!-- free-text fields mean case-finding depends on the keyword list used -->

### Other limitations

- **Duplicates:** <!-- exact duplicate rows; repeated keys. Legitimate (multiple diagnoses per
patient) or a defect? -->
- **Schema drift across partitions:** <!-- same columns, same order, same names? Differing
n_cols in Dataset Information is the tell. -->
- **Value-range anomalies:** <!-- impossible ages, future dates, negative length of stay,
num_min/num_max outside physiological range -->
- **Encoding:** <!-- the profiler falls back from UTF-8 to latin-1 silently — mojibake risk in
text columns -->
- **Fitness for purpose:** <!-- two or three lines: what this dataset supports well, and what
it should not be used for. The part a stakeholder reads first. -->

---

## Ownership & Governance

<!-- Answers "am I allowed to use this, and will approval arrive before my deadline?"
Almost every field here is owner-only. See docs/02_access_and_governance.md. -->

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner <!-- a role, not a person, so the page does not rot --> |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner <!-- ethics/IRB, provider sign-off, additional DUA --> |
| **Typical lead time** | Unknown — to confirm with data owner <!-- stakeholders plan against this number: give a range and its basis --> |
| **Permitted use / conditions** | Unknown — to confirm with data owner <!-- publication limits, small-cell suppression, output review, retention --> |
| **Sensitivity classification** | Unknown — to confirm with data owner |
| **Free-text / PII exposure** | <!-- Columns marked Direct ID / Quasi-ID / Free text in Key Variables. On a pass-1 page Sensitivity is not yet assigned: write "not assessed", list the columns the profiler typed id_like as the place to start, and say plainly that this is an outstanding task and NOT a finding that the dataset carries no PII. --> |
| **Attribution / citation** | Unknown — to confirm with data owner |

**Open questions for the data owner:**
<!-- Every unknown on this page, numbered. Write it so it can be sent as-is — this IS the
meeting agenda. -->
1.

---

## Appendix A — Full column profile

*(profiler, {{PROFILED_AT}} — row count must match Key Variables)*

<!-- The exhaustive per-column table. It exists so Key Variables can be curated and readable
while this stays complete: a mismatch in row count between the two means a column was lost.

Three fields per column, because three is what the condensed report carries. Do not add
distinct counts, ranges or top values unless a run that actually produced them is cited.

ON A PASS-1 PAGE this table is identical to Key Variables character for character. Do not
duplicate it — write one line saying the profile IS the Key Variables table and is not
repeated, and give the row count. Split them at pass 2, when Key Variables gains descriptions
and Class and the two genuinely diverge. -->

| # | Variable | Type | Missing % |
|---:|---|---|---:|
| {{ORDINAL}} | `{{COLUMN}}` | {{INFERRED_TYPE}} | {{MISSING_PCT}} |

## Appendix B — Change log

| Date | Change | By |
|---|---|---|
| | | |

<!-- A re-profile entry should record the delta in rows and columns. A page without a change
log cannot tell a reader whether it describes the extract they are holding. -->

## Appendix C — Sources

- Profiler run {{PROFILED_AT}} — `data_catalog_summary.txt`
- `source_material/screenshots/mass_columns_screenshots/section_<nn>.png`
- `source_material/imported/<file>.md`
- Data owner correspondence — <!-- date, who --> 

---
---

# Appendix D — How to fill this in

*Delete this appendix from the filled copy. It belongs to the template, not to any dataset.*

## D.1 Where each field comes from

Every field is fillable from one of five sources. Knowing which tells you what you can
finish this afternoon and what is blocked on someone else.

| Tag | Source | Fillable now? |
|---|---|---|
| **[P]** | Profiler — `data_catalog_summary.txt`, `dataset_summary.csv`, `column_summary.csv` | Yes, mechanically. Cite the run date |
| **[C]** | Catalogue convention — the answer is fixed by a rule, not by evidence | Yes, always. Never left unknown |
| **[A]** | Analyst observation — inspecting the extract, reading load code, prior project notes | Yes, but label it observed-in-*which*-extract |
| **[O]** | Data owner only — not derivable from the data at all | No. Write the unknown marker and add it to the open-questions list |
| **[D]** | Derived judgement — your interpretation of [P]/[A] evidence | Yes, but show the reasoning so a reader can disagree |

**[P]** and **[C]** together are pass 1. Everything else is pass 2.

| Section | Field | Tag |
|---|---|---|
| Header | Objects included | [P] |
| Overview | Category | **[C]** — from the dataset name |
| | Description | [D] |
| | Data source, Population, Institutional coverage, Refresh cadence | [O] |
| | Unit of observation, Aliases, Extract date | [A] |
| | Rows vs people | [P] rows + [A] patients |
| | Source objects, Partitions, Format, Free-text content | [P] |
| Key Variables | Variable names, Type, Missing % | [P] |
| | Description, Coding / units | [A] + [O] |
| | Class, Sensitivity | [D] |
| Time Coverage | Start / End per date column | [P] |
| | Completeness over the period | [P] + [D] |
| | Variable availability over time | [P] + [O] |
| Dataset Information | Everything except distinct patients | [P] |
| Provenance | Every field except *what is lost* | [O] |
| | Raw vs interpreted — what is lost | [D] |
| Data Quality | Missingness figures, schema drift | [P] |
| | Primary identifier | **[C]** — the patient ID column |
| | Value-range anomalies, disguised missing, duplicates, linkage pitfalls | [A] |
| | Bias, fitness for purpose | [O] + [D] |
| Governance | Everything | [O] |

A page with no **[O]** gaps is either owner-confirmed (✅) or wrong. A 🟡 Draft page is
*expected* to be full of explicit **[O]** unknowns — that is the page doing its job.

## D.2 Choose a documentation tier before you start

There are ~275 profiled objects and a much smaller number of dataset families. Full pages
for all of them is neither achievable nor useful.

| Tier | Applies to | Required |
|---|---|---|
| **T1 — Full page** | Families anyone has asked for, or that carry the primary identifiers | Every field in this template |
| **T2 — Short entry** | Known families with no current demand | Header, Dataset Information, Dataset Overview, Key Variables, primary identifier, data owner. Remaining sections present, marked *Not yet documented — tier T2* |
| **T3 — Index row** | Objects that are partitions or near-duplicates of a documented family | A row in `datasets/index.md` pointing at the family page |

A T3 object must never be silently dropped. "Not documented" is a status; absence is not.

## D.3 Profiler caveats you must not paper over

The generated blocks look authoritative because they are numeric. They are heuristics run
over a sample — every caveat below is a real property of `tools/s3_data_catalog.py`, and
each has a place in the template where it must be disclosed.

| Caveat | Mechanism | Disclose in |
|---|---|---|
| **Types are inferred, not declared** | From the first 2,000 non-null values: numeric if ≥95% parse, date if ≥80% parse (≥50% with a date-like name), `id_like` if >50% of values hold >7 digits | Key Variables — write "profiler inferred numeric", never "the column is numeric" |
| **A column can be mistyped by its first chunk** | The sample is drawn from the first chunk only; a column clean early and messy later keeps the early type | Value-range anomalies |
| **Dates parsed `dayfirst=True`** | `01/02/2021` reads as 1 February. If the source is month-first, every derived range is wrong | Time Coverage |
| **Missingness has a fixed null vocabulary** | Only `""`, `NA`, `N/A`, `NULL`, `null`, `None`, `NaN`, `.` count as missing | Disguised missing — the most important caveat here |
| **Bad rows skipped silently** | `on_bad_lines="skip"` | Dataset Information — row counts are a lower bound |
| **Encoding may have been coerced** | UTF-8 first, silent fall back to latin-1 with `errors="replace"` | Other limitations |
| **No value profile in the condensed report** | The summary carries three fields per column — name, inferred type, missing % — and no top-values, distinct or min/max block | Key Variables; Appendix A — do not write a value list this run cannot support |
| **`id_like` columns are additionally suppressed** | Value profiling is skipped for them by design | Key Variables; PII exposure |
| **Everything is per-object, not per-family** | The profiler does not know `_P1`…`_P8` are one dataset | Dataset Information — give per-object **and** family totals |
| **Distinct patients never computed** | No cross-column or cross-file uniqueness | Rows vs people; Sample size |
| **A profile is a snapshot** | `profiled_at` | Header; Appendix B |

An `id_like` classification is a PII signal, not just a type: the values mostly contain more
than 7 digits, which is prima facie identifier-shaped. Carry it into Ownership & Governance
rather than leaving it as a row in Key Variables.

## D.4 Definition of done — pass 1 (base page)

A base page is finished when it says everything the profiler establishes and claims nothing
more. It is short, and being short is not a defect.

- [ ] Header complete; every `.csv` object named in the objects table
- [ ] Category filled from the dataset name — never unknown
- [ ] Dataset Information transcribed per-object **and** family total, with the lower-bound note
- [ ] Key Variables covers **every** column, with type and missing % per partition
- [ ] Per-partition type disagreements recorded, both readings kept
- [ ] Primary identifier named as the patient ID column — never "not determined"
- [ ] Every remaining field present and marked unknown; none deleted, none guessed
- [ ] Unknowns are one line each — no essays on what the profiler does not carry
- [ ] Open-questions list complete and sendable as-is
- [ ] Change log entry naming the profiler run and the source read
- [ ] No bucket names, object URIs, credentials, patient-level values, or study findings

**The failure mode to watch for is a plausible sentence.** Anything read off a column name —
what a `_STD` suffix means, what an `_X`/`_Z` pair is, whether an `id_like` column identifies
a patient, what the partitions are split by — is invention, and it will be believed.

## D.5 Definition of done — T1 (pass 2, full page)

- [ ] Header complete; row added to `datasets/index.md`
- [ ] Aliases verbatim, with an extract date
- [ ] Dataset Information transcribed from a named profiler run, per-object **and** family total
- [ ] Unit of observation stated, plus what makes rows multiply
- [ ] Rows and distinct patients stated separately
- [ ] Population: inclusion **and** an explicit exclusion sentence
- [ ] Time Coverage attributed to a named date column
- [ ] Key Variables covers **every** column — row count matches Appendix A
- [ ] Every column has a Class and a Sensitivity value
- [ ] No value list anywhere on the page that the cited profiler run did not produce
- [ ] Every `_STD` / derived field either has its mapping documented or is explicitly flagged as undocumented
- [ ] Primary identifier given with dtype and format, not just a name
- [ ] Disguised-missing check done and reported, including "none found"
- [ ] Schema drift across partitions checked
- [ ] Fitness-for-purpose paragraph written
- [ ] Every Governance field present, even if all are unknowns
- [ ] Open-questions list complete and sendable as-is
- [ ] Every number carries (source, date, scope)
- [ ] No bucket names, object URIs, credentials, patient-level values, or study findings
- [ ] Change log entry added

## D.6 The reviewer's three questions

1. **Can I tell what one row is, and how many people that corresponds to?**
2. **Can I tell, for every column I would rely on, whether it is a source value or somebody's interpretation of one?**
3. **Can I tell what I would have to ask, and whom, before I could use this?**

If any answer is no, the page is not done — regardless of how many fields are filled.
