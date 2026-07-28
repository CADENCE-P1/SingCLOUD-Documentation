# SingCLOUD — Laboratory Items

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `VW_LABORATORY_ITEM_FIL_F_Export_{date}_P{n}` |
| **Partitions** | 22 (`P1`–`P22`). Partition dates observed in the 2024 extract: `P1–P4` = 28-07-2024, `P5–P13` = 29-07-2024, `P14–P22` = 30-07-2024 |
| **Format** | CSV, delimiter `,` |
| **Last reviewed** | *from the 2024-07 extract; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Laboratory test results

**Unit of observation:** One row per **individual test result** (one analyte, one
measurement)

**Population represented:** Patients with laboratory tests performed at participating
institutions. Coverage: unknown — to confirm with data owner.

**Period covered:** Unknown — to confirm. Derive empirically from `DISPLAY_DATE_Z`.

**Variable availability over time:** Unknown — to confirm with data owner.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `DATA_SOURCE` | Source system of the record | Raw | |
| `BATTERY_ID_ROOT` | Root identifier for the lab battery | Raw | Groups results ordered together |
| `BATTERY_ID_EXTN` | External battery identifier | Raw | |
| `FACILITY_EXTN` | External facility identifier | Raw | **Reference ranges and assay methods differ by lab — this column matters** |
| **`PATIENT_ID_EXTN_X`** | **Primary patient ID** | Raw | SingCLOUD identifier family |
| `DISPLAY_DATE_X` | Lab display date (format X) | Raw | |
| **`DISPLAY_DATE_Z`** | **Lab display date, standardised** | Standardised | Prefer this |
| `ITEM_SEQ_NO` | Sequence number of the item within the battery | Raw | |
| `ITEM_NAME_ETS_ID` | Standardised ETS identifier for the item name | Standardised | |
| **`ITEM_NAME_ORI_TXT`** | **Original test name** | Raw (free text) | Requires keyword matching — see below |
| **`ITEM_NUMERIC_VALUE`** | **Numeric result** | Raw | |
| `ITEM_NUMERIC_VALUE_UOM` | Unit of measure | Raw | **Must be checked — units are not guaranteed consistent across labs** |
| `ITEM_REFERENCE_RANGE` | Reference range for the test | Raw | Lab- and assay-specific |
| `ITEM_ABNORMAL_FLAG_ETS_ID` | Standardised abnormal-result flag | Derived | An interpretation, not a measurement |
| `ITEM_ABNORMAL_FLAG_ORI_TXT` | Original abnormal-result flag text | Derived | As above |
| `ITEM_STATUS_ETS_ID` | Item status | Standardised | Preliminary vs final results — check before analysis |

---

## 2. Provenance & Processing

**Collection mechanism:** Laboratory information systems at participating institutions,
extracted into a common view.

**Processing applied:** Partitioned into 22 files across three export dates. Standardised
`_ETS_ID` identifiers are provided alongside original text for test name and abnormal flag.

**Raw vs interpreted:** This dataset contains a clean example of the raw-vs-interpreted
distinction, and it is easy to get wrong:

- `ITEM_NUMERIC_VALUE` is the **measurement**.
- `ITEM_ABNORMAL_FLAG_*` is an **interpretation** of that measurement against a reference
  range that varies by laboratory, assay and sometimes patient demographics.

Filtering on the abnormal flag inherits every reference range decision made by every
contributing lab, and those decisions are neither uniform nor documented here. For anything
where the threshold matters — and especially for model development — work from
`ITEM_NUMERIC_VALUE` with your own explicitly stated threshold, and treat the flag as
metadata rather than as a result.

Note also that `ITEM_REFERENCE_RANGE` is free text, so it is not directly machine-comparable
across labs without parsing.

---

## 3. Feasibility & Quality

**Primary identifier:** `PATIENT_ID_EXTN_X`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [Event diagnosis](singcloud-event-diagnosis.md) | `PATIENT_ID_EXTN_X` | Result → diagnosis | Same identifier family; join on date proximity, not exact match |
| MediClaims / COVID datasets | — | — | **Different identifier family**; crosswalk not confirmed |

**Coding standards:** **None applied to test names.** `ITEM_NAME_ORI_TXT` is operator-entered
free text with no LOINC or equivalent standard vocabulary. Extracting a given analyte
requires a curated keyword list.

Illustrative keyword sets used in practice — offered as a starting point, not a validated
standard:

| Analyte | Keywords observed to be needed |
|---|---|
| C-reactive protein | `c-reactive`, `crp`, `hs-crp` |
| Erythrocyte sedimentation rate | `erythrocyte sedimentation`, `esr` |
| Creatinine | `creatinine`, `creat` |
| Albumin | `albumin` |

Note that `hs-crp` (high-sensitivity) and standard CRP are **different assays with different
ranges**; whether to pool them is a study design decision, not a data cleaning one.

**Known linkage pitfalls:**
- 22 partitions, no guarantee of patient locality — patient-level work must scan all of
  them.
- Multiple results per patient per analyte: a single-value-per-patient analysis needs an
  explicit selection rule (first, last, nearest to index date, peak).
- Unit inconsistency across labs will produce results that are numerically valid and
  clinically nonsense if pooled without checking `ITEM_NUMERIC_VALUE_UOM`.

**Scale:** 22 partitions; row counts not yet profiled. This is among the largest datasets in
the catalogue.

**Missingness:** Not yet profiled. Priority: `ITEM_NUMERIC_VALUE` (non-numeric and
qualitative results), `ITEM_NUMERIC_VALUE_UOM`, `ITEM_REFERENCE_RANGE`.

**Known biases:**
- **Testing is not random.** Patients with lab results are patients someone decided to test.
  Any analysis of lab values is conditioned on that decision, which correlates with severity
  — a selection effect that biases naive comparisons and must be addressed in design.
- Institutional coverage is partial.
- Assay methods change over time; a level measured in 2015 may not be comparable to the
  same level in 2023.

---

## 4. Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |

---

## 5. Notes for analysts

- Filter to the analytes you need *while streaming* each partition; do not load whole files.
- `ITEM_NUMERIC_VALUE` will not always parse as a number — qualitative results and
  censored values (`<0.5`, `>200`) appear in numeric-looking fields. Handle them explicitly
  rather than coercing to NaN.
- Check `ITEM_NUMERIC_VALUE_UOM` distributions per analyte before pooling.
