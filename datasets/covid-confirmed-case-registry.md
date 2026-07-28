# COVID-19 Confirmed Case Registry

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `ConfirmedCaseHeadersForAgenciesCNo0to100000`, `…100000to200000`, `…200000to300000`, `…300000to400000`, `…400000to500000`, `ConfirmedCaseHeadersForAgencies1Dec2022`, `ConfirmedCaseHeadersForAgencies1Jan2023` |
| **Partitions** | 7 — five chunked by case-number range, plus two date-specific files |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Statutory disease registry

**Unit of observation:** One row per **confirmed COVID-19 case**

**Population represented:** All confirmed COVID-19 cases in Singapore — **citizens,
permanent residents and non-residents**. Broader than the resident population, which makes
it unsuitable as a denominator without filtering.

**Period covered:** Pandemic period; derive exact bounds from `notificationdate`.

**Variable availability over time:** Unknown — to confirm with data owner. Registry
variables commonly change mid-pandemic as reporting requirements evolve; the two
date-specific files (`1Dec2022`, `1Jan2023`) alongside the range-chunked files suggest the
extract structure itself changed over time, which is worth understanding before assuming a
uniform schema.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `uin` | Patient identifier | Raw | Column names are lowercased on load in some pipelines |
| `notificationdate` | Date of case notification | Raw | Notification date, **not** symptom onset or test date |
| `age` | Age | Derived | Age at notification |
| `gender` / `cat_gender` | Gender | Standardised | Naming varies between files |
| `cat_passtype` | Pass / residency type | Standardised | Values include `SINGAPORE CITIZEN`, `PERMANENT RESIDENT`; others denote work and dependant passes |

> The manifest above covers the columns used in practice. A full manifest should be
> generated with the profiler.

---

## 2. Provenance & Processing

**Collection mechanism:** Statutory notification of confirmed cases.

**Processing applied:** Split into seven files — five by case-number range and two by date.
The `cat_` prefix on some demographic columns indicates a categorised/standardised
derivation, and the prefix is applied inconsistently across the files in this family and
across related COVID datasets.

**Raw vs interpreted:**
- `notificationdate` is an **administrative** date — when the case entered the reporting
  system. It is a proxy for infection date, and the gap between infection and notification
  varied substantially over the pandemic with testing policy. Any study using it as an
  exposure date should acknowledge this rather than treat it as an infection date.
- `age` is a derived value at notification, not a birth date.

---

## 3. Feasibility & Quality

**Primary identifier:** `uin`

**Linkage keys:**

| Links to | On | Granularity | Notes |
|---|---|---|---|
| [MediClaims](mediclaims-diagnosis.md) | `uin` | Case → event | Same identifier family |
| [COVIDFACILLOS](covid-facility-los.md) | `uin` | Case → episode | |
| [NIR immunisation](nir-immunisation.md) | `uin` | Case → person | |
| [Serology](serology-tests-covid.md) | `uin` | Case → test | |
| SingCLOUD clinical views | — | — | **Different identifier family**; crosswalk not confirmed |

**Coding standards:** Category labels for pass type and gender; not clinically coded.

**Known linkage pitfalls:**
- **Column casing varies** between the seven files. Normalise on load.
- A patient may appear across chunk boundaries if they have more than one case record;
  de-duplicate across all seven files, not within each.
- Residency filtering uses `cat_passtype` here, but `resident_type` in
  [MediClaims episodes](mediclaims-episodes.md), with different value strings. The two
  filters are not equivalent and will not select identical populations.

**Scale:** Approximately 500,000 case-number range across the five chunked files, plus the
two date-specific files. Not yet profiled precisely.

**Missingness:** Not yet profiled.

**Known biases:**
- **Confirmed cases only.** Undetected and untested infections are absent, and detection
  rates varied enormously with testing policy across the pandemic. Comparisons across time
  periods are comparing different ascertainment regimes as much as different infection
  rates.
- Includes non-residents; using this as a resident-population numerator without filtering
  overstates counts.

---

## 4. Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner |
| **Approval requirements** | Unknown — to confirm with data owner. Notifiable-disease registry data may carry conditions beyond baseline access |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |

---

## 5. Notes for analysts

- Load all seven files and concatenate before de-duplicating.
- Lowercase column names on load to absorb casing differences.
- Enumerate `cat_passtype` values before filtering.
