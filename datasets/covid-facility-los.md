# COVIDFACILLOS — COVID-19 Facility Utilisation and Severity

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `COVIDFACILLOS` |
| **Partitions** | 1 |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Administrative / facility management, with clinical severity markers

**Unit of observation:** One row per **COVID case episode**. A patient with multiple
admissions may appear more than once — this is not a patient-level file.

**Population represented:** COVID-19 cases managed through the facility management system.

**Period covered:** 2020-01-22 to 2024-02-28 *(observed)*

**Variable availability over time:** The vaccination columns cannot be populated before
vaccines were available (2021 onward), and `VaccinationFourthDoseDate` later still. Early
2020 records will have these systematically empty — **absent, not missing at random.** This
is the clearest example in the catalogue of the "earlier records may not contain certain
variables" problem.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `uin` | Patient identifier | Raw | |
| `Casenumber` | Case number | Raw | |
| `notificationdate` | Notification date | Raw | Format `%d%b%Y`, e.g. `15Mar2021` |
| `CaseClass` | Case classification | Standardised | |
| `age`, `gender`, `race` | Demographics | Standardised | Note: **no `cat_` prefix here**, unlike the reinfection dataset |
| `passtype`, `flattype` | Pass type, housing type | Standardised | Again unprefixed |
| `Exposuretype` | Exposure category | Derived | An epidemiological assessment |
| `LOS` | Length of stay | Derived | |
| `DaysInICU` | Days in ICU | Derived | |
| `Deceased` | Death indicator | Standardised | |
| `O2StartDate`, `O2EndDate` | Oxygen therapy period | Raw | |
| `EarliestEDVisit`, `EDVisits` | Emergency department contact | Raw / Derived | |
| `CPlus`, `AGPlus` | Case flags | Derived | Meaning undocumented — **confirm with data owner** |
| `HistoricalStatus`, `Status` | Case status | Standardised | |
| `vacc_date1`–`vacc_date5` | Vaccination dates, doses 1–5 | Raw | Wide format; **5 doses only** |
| `vaccbrand1`–`vaccbrand5` | Vaccine brands, doses 1–5 | Standardised | |
| `VaccinationFourthDoseDate` | Fourth dose date | Raw | Redundant with `vacc_date4`; consistency not verified |

**Approximate rows:** ~2,349,112 *(observed)*

---

## 2. Provenance & Processing

**Collection mechanism:** COVID-19 facility management system — operational records of
where cases were managed and for how long.

**Processing applied:** Dates use the non-ISO format `%d%b%Y` (`15Mar2021`), which will
misparse under default settings. Vaccination data is denormalised into wide dose columns.

**Raw vs interpreted:**
- `LOS` and `DaysInICU` are **derived durations**. The counting convention (inclusive of
  admission day? transfers between facilities?) is undocumented — confirm with the data
  owner before using them as clinical severity measures.
- `Exposuretype` is an epidemiological classification made during contact tracing, not an
  observed fact.
- **There is no severity variable in this dataset.** Severity categories (mild / moderate /
  severe / critical) must be constructed by the researcher from `LOS`, `DaysInICU`,
  oxygen dates and `Deceased`, and the construction rule is a study design decision that
  materially affects results. Two studies using "severity" from this dataset are not
  necessarily measuring the same thing.
- `CPlus` and `AGPlus` are undocumented flags. Do not use them without confirming meaning.

---

## 3. Feasibility & Quality

**Primary identifier:** `uin`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [COVID case registry](covid-confirmed-case-registry.md) | `uin` | Episode → case | Same identifier family |
| [NIR immunisation](nir-immunisation.md) | `uin` | Episode → person | NIR is the more complete vaccination source |
| [COVID reinfections](covid-reinfections.md) | `uin` | Episode → reinfection | Note the `cat_` prefix difference in demographic columns |

**Coding standards:** Category labels; not clinically coded.

**Known linkage pitfalls:**
- **Multiple rows per patient.** Reduce to patient level with an explicit rule before
  merging, or the merge will multiply the cohort.
- Demographic columns are **unprefixed** here (`gender`, `race`) but **prefixed** in the
  reinfection dataset (`cat_gender`, `cat_race`). Code that assumes one convention fails
  silently against the other.
- The `%d%b%Y` date format must be given explicitly to the parser.

**Scale:** ~2,349,112 rows *(observed)*

**Missingness:** Not yet profiled. Vaccination columns will show high missingness that is
structural (pre-vaccine period) rather than a data quality defect — profile by year to
separate the two.

**Known biases:**
- Facility-managed cases only. Cases managed at home or not requiring facility care are
  under-represented, and the threshold for facility management **changed substantially over
  the pandemic**. Severity distributions are therefore not comparable across time periods
  without accounting for this.

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

- Parse dates with `format='%d%b%Y'`.
- Prefer [NIR](nir-immunisation.md) for vaccination (6 doses, whole-resident coverage); use
  this dataset's vaccination columns as a fallback only.
- Define and document your severity construction rule explicitly.
