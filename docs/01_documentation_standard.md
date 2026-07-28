# The documentation standard

Every dataset page in `datasets/` must contain these four sections, in this order, with
these field names. Uniformity is the point: it is what makes datasets *comparable* rather
than merely *described*.

If a field is unknown, write **"Unknown — to confirm with data owner"**. Do not delete the
row. An explicit gap tells a stakeholder to ask; a missing row tells them nothing.

---

## Header block

| Field | Notes |
|---|---|
| Status | ✅ Verified / 🟡 Draft / ⚪ Stub |
| Dataset family | Human-readable name |
| Catalogue alias(es) | Exact string(s) used to load the data on the platform |
| Partitions | How many files, and the naming pattern |
| Format | CSV / Parquet / XLSX, plus delimiter |
| Last reviewed | Date + reviewer |

---

## §1 Content & Scope

Answers *"what is in it, for whom, and for when?"*

| Field | What to record |
|---|---|
| **Information type** | Clinical / lab / billing / administrative / registry / immunisation / demographic. A dataset may be more than one. |
| **Unit of observation** | One row per *what*: patient, encounter, diagnosis event, test result, dispensed item. This is the single most misread property of a dataset. |
| **Population represented** | Who is in it and — just as important — who is *not*. Whole-population registry, or only patients meeting some condition (e.g. insured patients, confirmed cases, admitted patients)? |
| **Period covered** | Earliest and latest record dates observed. |
| **Variable availability over time** | Fields that do not exist, or are largely empty, in earlier records because the collection tool did not exist yet. Record the approximate date each such field becomes usable. |
| **Variable list** | Every column, with a plain-language description. |

## §2 Provenance & Processing

Answers *"where did each value come from, and what happened to it on the way?"*

Every variable must be classified:

| Class | Meaning | Suitable for |
|---|---|---|
| **Raw** | As entered/measured at source; not transformed | Model training on source signal; audit; re-derivation |
| **Standardised** | Same information, mapped to a controlled vocabulary or normalised format | Cohort selection; cross-site comparison |
| **Derived** | Computed or *interpreted* — a human or algorithm made a judgement | Convenience analysis; **not** a substitute for the underlying signal |

Also record:

- **Collection mechanism** — how the value reaches the dataset (clinician entry at point of
  care, instrument feed, claims submission, statutory notification, batch extract).
- **Processing applied** — de-identification, pseudonymisation, standardisation mappings,
  de-duplication, truncation.
- **What is lost** — where a Derived or Standardised field replaces something richer, say so
  explicitly, and say whether the underlying raw value is available anywhere.

> This is the ECG case from the rationale. A field named `DIAGNOSIS` that holds a
> clinician's interpretation and a field holding the source waveform are not
> interchangeable, and a column list alone will not distinguish them. That is what this
> section exists to prevent.

## §3 Feasibility & Quality

Answers *"can I link it, and is it good enough to answer my question?"*

| Field | What to record |
|---|---|
| **Primary identifier** | Exact column name, type, and format (including leading zeros, casing, padding). |
| **Linkage keys** | Which other datasets this joins to, on which column, and at what granularity. |
| **Coding standards** | ICD-10 / SNOMED / local codes / free text. Note version and any within-dataset inconsistency. |
| **Known linkage pitfalls** | Everything that has actually bitten someone. See [linkage guide](03_linkage_guide.md). |
| **Scale** | Approximate rows, distinct patients, file size. |
| **Missingness** | Per-column, for the columns that matter. |
| **Known biases** | Coverage gaps, selection effects, systematic under-recording, changes in coding practice over time. |

Scale and missingness figures can be generated mechanically — see
[`tools/s3_data_catalog.py`](../tools/s3_data_catalog.py). Bias cannot, and needs the data
owner.

## §4 Ownership & Governance

Answers *"am I allowed to use this, and will approval arrive before my deadline?"*

| Field | What to record |
|---|---|
| **Data owner** | The agency or department accountable for the dataset. |
| **Steward / contact** | Who actually answers questions about it. |
| **Access restrictions** | Any restriction beyond baseline SingCLOUD access. |
| **Approval requirements** | Named approvals needed — ethics/IRB, data provider sign-off, additional DUA. |
| **Typical lead time** | Realistic elapsed time from request to access. Stakeholders plan against this number. |
| **Permitted use / conditions** | Publication restrictions, small-cell suppression thresholds, output review, retention limits. |

---

## Writing conventions

- **Exact strings, verbatim.** Column and alias names are copied exactly, including
  inconsistent casing and awkward suffixes. Tidying them up in the documentation is how
  someone's load call fails at 2am.
- **Distinguish observed from specified.** "Observed in the 2024-07 extract" and
  "per data dictionary" are different claims. Say which one you have.
- **No patient-level data.** Example values must be synthetic or already-public category
  labels, never real records.
- **No study findings.** This catalogue describes datasets, not results obtained from them.
