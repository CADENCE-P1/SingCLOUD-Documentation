# COVID-19 Serology Tests

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `Serology_Tests_COVID` |
| **Partitions** | 1 |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Laboratory test results (serology)

**Unit of observation:** One row per **serology test**

**Population represented:** Individuals who underwent COVID-19 serology testing. Testing was
programme-driven rather than universal — see biases.

**Period covered:** Derive from `serologyswabdate`.

**Variable availability over time:** Unknown — to confirm with data owner. Assay platforms
and reporting fields changed over the pandemic.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `uin` | Patient identifier | Raw | |
| `accesionno` | Accession number | Raw | Spelling as-is in source |
| `serologyswabdate` | Date of sample collection | Raw | Use this as the event date |
| `serologyresultdate` | Date result issued | Raw | Administrative, not clinical |
| `serologyswabstatus` | Swab status | Standardised | |
| `serologyresult` | Result | Standardised | Categorical |
| `serologyctvalue` | CT value | Raw | Cycle threshold — a **quantitative** measure |
| `serologyresultindicator` | Result indicator | Derived | An interpretation |
| `serologyvalue` | Serology value | Raw | Quantitative |
| `serologylab` | Performing laboratory | Raw | **Assay differs by lab** |
| `serologyswablocation` | Collection location | Raw | |
| `serologylabinterpretationnote` | Lab interpretation note | Derived (free text) | |
| `createdat`, `createdby`, `updatedat`, `updatedby` | Record metadata | Raw | Audit fields, not clinical |

**Approximate rows:** ~1,067,600 *(observed)*

---

## 2. Provenance & Processing

**Collection mechanism:** COVID-19 serology testing programme; results fed from laboratory
systems.

**Processing applied:** Audit metadata (`createdat`/`updatedat`) retained, which is unusual
and useful — it allows detection of retrospectively amended results.

**Raw vs interpreted:** This dataset carries the quantitative measurement and its
interpretation side by side:

- **Raw / quantitative:** `serologyctvalue`, `serologyvalue`
- **Interpreted:** `serologyresult`, `serologyresultindicator`,
  `serologylabinterpretationnote`

The interpreted fields apply lab-specific thresholds that are not documented here and that
differ across `serologylab` values. A study using `serologyresult` inherits those
undocumented thresholds; a study using `serologyvalue` with a stated threshold does not.
For quantitative or model-development work, use the numeric fields and stratify or adjust
by `serologylab`.

CT values in particular are **not comparable across assay platforms**. Pooling them across
labs without accounting for platform produces a variable that is not measuring one thing.

---

## 3. Feasibility & Quality

**Primary identifier:** `uin`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [COVID case registry](covid-confirmed-case-registry.md) | `uin` | Test → case | Same identifier family |
| [COVIDFACILLOS](covid-facility-los.md) | `uin` | Test → episode | |

**Coding standards:** Result categories are lab-reported labels; enumerate them in your
extract.

**Known linkage pitfalls:**
- **Multiple tests per patient.** A patient-level analysis needs an explicit selection rule
  (earliest test, test nearest an index date, peak value) — stated, not implicit.
- Two dates are present. `serologyswabdate` is the clinical event; `serologyresultdate` is
  administrative. Using the wrong one shifts timing by a variable lag.

**Scale:** ~1,067,600 rows *(observed)*

**Missingness:** Not yet profiled. `serologyctvalue` and `serologyvalue` are the priorities —
both may be sparse depending on assay type.

**Known biases:**
- **Testing was programme-driven.** Who was tested reflects surveillance policy and
  occupational or exposure category, not a random or clinically-indicated sample. Serology
  results are therefore not representative of the general population.
- Assay platforms varied across labs and over time.

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

- Use `serologyswabdate` for timing.
- Prefer `serologyvalue` / `serologyctvalue` over `serologyresult` where thresholds matter,
  and stratify by `serologylab`.
- Define and document your one-test-per-patient rule.
