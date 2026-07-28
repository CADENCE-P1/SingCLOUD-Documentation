# SingCLOUD — Demographics (Gender, Date of Birth)

| | |
|---|---|
| **Status** | 🟡 Draft |
| **Catalogue alias(es)** | `SingCLOUD_gender`, `SingCLOUD_DOB` |
| **Partitions** | 1 each |
| **Format** | CSV |
| **Last reviewed** | *from 2024 working notes; not owner-confirmed* |

---

## 1. Content & Scope

**Information type:** Demographic / master patient index

**Unit of observation:** One row per **patient**

**Population represented:** Patients in the national patient master index. Coverage relative
to other datasets in the catalogue is **not complete** — see §3.

**Period covered:** Not time-series data; represents current recorded values.

**Variable availability over time:** Not applicable.

### Variables

| Column | Description | Class | Notes |
|---|---|---|---|
| `PATIENT_ID` | Patient identifier | Raw | Confirm exact name and identifier family |
| `GENDER` / `SEX` | Recorded gender | Standardised | Column naming observed to vary between the two files |
| `DATE_OF_BIRTH` | Date of birth | Raw | |

---

## 2. Provenance & Processing

**Collection mechanism:** National patient master index — administrative registration
rather than clinical encounter.

**Processing applied:** Split into two separate files (gender, DOB) that must be joined.

**Raw vs interpreted:** These are recorded administrative values. Note that **age is not
supplied** — it is derived by the researcher from `DATE_OF_BIRTH` relative to an index date,
and different index-date choices give different ages for the same patient. Where age
appears in other datasets in this catalogue (e.g. the COVID registry's `age`), it is age at
*that* dataset's reference event and is not interchangeable with an age derived here.

---

## 3. Feasibility & Quality

**Primary identifier:** `PATIENT_ID` — confirm which identifier family

**Linkage keys:** Joins to other datasets sharing its identifier family. Two files
(`SingCLOUD_gender`, `SingCLOUD_DOB`) must first be joined to each other.

**Coding standards:** Gender values are category labels — enumerate them in your extract
rather than assuming a binary coding.

**Known linkage pitfalls:**
- Column naming differs between the gender and DOB files (`GENDER` vs `SEX` observed).
- **Linkage is not 100%.** Patients present in clinical or claims datasets may have no
  demographic record here. Any pipeline must handle missing demographics explicitly rather
  than dropping those patients silently — a silent inner join here removes patients from
  the study for a reason unrelated to the research question.

**Scale:** Not yet profiled.

**Missingness:** Not yet profiled. **Match rate against each other dataset is the figure
that actually matters here** and should be measured and recorded on this page.

**Known biases:**
- Incomplete linkage means demographic-adjusted analyses are performed on a subset, and
  that subset may not be random.

---

## 4. Ownership & Governance

| | |
|---|---|
| **Data owner** | Unknown — to confirm with data owner |
| **Steward / contact** | Unknown — to confirm with data owner |
| **Access restrictions** | Unknown — to confirm with data owner. Date of birth is a direct-identifier-adjacent field and may carry additional restrictions |
| **Approval requirements** | Unknown — to confirm with data owner |
| **Typical lead time** | Unknown — to confirm with data owner |
| **Permitted use / conditions** | Unknown — to confirm with data owner |

---

## 5. Notes for analysts

- Join gender and DOB before enriching a cohort.
- Use a left join from your cohort and report the match rate; do not use an inner join.
- Compute age relative to an explicitly stated index date.
