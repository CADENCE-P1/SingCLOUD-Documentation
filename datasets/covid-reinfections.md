# COVID-19 Reinfections

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `COVID Reinfections` *(note the space in the alias)* |
| **Partitions** | 1 |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Disease surveillance

**Unit of observation:** One row per **reinfection event**

**Population represented:** Individuals recorded as having a COVID-19 reinfection. By
definition a subset of the confirmed case population.

**Period covered:** Derive from `notificationdate`. Reinfections only become meaningful
after a first wave has passed, so early-pandemic coverage is structurally absent.

**Variable availability over time:** Vaccination columns are structurally empty before
vaccine rollout.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `uin` | Patient identifier | Raw | |
| `Casenumber` | Case number | Raw | |
| `notificationdate` | Notification date | Raw | |
| `CaseClass` | Case classification | Standardised | |
| `reinfection_type` | Type of reinfection | Derived | A surveillance classification |
| `HistoricalStatus` | Historical case status | Standardised | |
| `age` | Age | Derived | |
| `cat_gender`, `cat_race`, `cat_passtype`, `cat_flattype` | Demographics | Standardised | **`cat_` prefixed here** — unlike COVIDFACILLOS |
| `DaysAtPHI`, `DaysAtCTF`, `DaysAtCIF`, `DaysAtCIFM`, `DaysAtDRF`, `DaysAtHRP` | Days at each facility type | Derived | Facility-type acronyms **undocumented — confirm with data owner** |
| `DaysO2` | Days on oxygen | Derived | |
| `DaysInICU` | Days in ICU | Derived | |
| `Deceased` | Death indicator | Standardised | |
| `vacc_date1`–`vacc_date5` | Vaccination dates | Raw | 5 doses |
| `vaccbrand1`–`vaccbrand5` | Vaccine brands | Standardised | |

**Approximate rows:** ~128,101 *(observed)*

---

## 2. Provenance & Processing

**Collection mechanism:** COVID-19 reinfection surveillance.

**Processing applied:** Demographic fields carry a `cat_` prefix indicating a categorisation
step, matching the confirmed case registry convention but **not** COVIDFACILLOS.

**Raw vs interpreted:**
- `reinfection_type` is a surveillance classification. The rule that distinguishes a
  reinfection from prolonged shedding or a persistent positive is a case definition, and it
  is not documented here — confirm with the data owner, because it directly determines who
  is in this dataset.
- The `DaysAt*` fields are derived durations across six facility types whose acronyms are
  undocumented. Do not aggregate them into a total without confirming what each represents.

---

## 3. Feasibility & Quality

**Primary identifier:** `uin`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [COVID case registry](covid-confirmed-case-registry.md) | `uin` | Reinfection → case | |
| [COVIDFACILLOS](covid-facility-los.md) | `uin` | Reinfection → episode | Watch the `cat_` prefix mismatch |
| [Facility utilisation (reinfections)](covid-reinfection-facility-utilisation.md) | `uin` | Overlapping scope | The two datasets differ by ~two orders of magnitude in size — establish what each actually covers before combining |

**Coding standards:** Category labels.

**Known linkage pitfalls:**
- **`cat_` prefix inconsistency** with COVIDFACILLOS is the standard cause of an all-null
  merged demographic column here.
- The alias contains a **space** (`COVID Reinfections`), which breaks naive path handling.
- Multiple reinfection events per patient are possible — reduce before patient-level merge.

**Scale:** ~128,101 rows *(observed)*

**Missingness:** Not yet profiled.

**Known biases:**
- A reinfection is only recorded if both infections were detected. Given how much testing
  intensity varied over the pandemic, reinfection ascertainment is strongly
  period-dependent, and reinfection rates over time reflect testing policy at least as much
  as they reflect epidemiology.

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

- Normalise the `cat_` prefix when combining demographic columns across COVID datasets.
- Establish the relationship between this dataset and the reinfection facility-utilisation
  file before treating either as complete.
