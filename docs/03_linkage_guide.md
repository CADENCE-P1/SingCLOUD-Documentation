# Linkage guide: identifiers, coding standards and known pitfalls

Most SingCLOUD studies require joining more than one dataset. This page collects the
cross-dataset facts that determine whether that is easy, hard, or impossible — and the
failure modes that have actually occurred in practice.

> 🟡 **Draft.** Content below is drawn from analyst experience on extracts received in
> 2024. It should be confirmed against current platform behaviour before being relied on
> for feasibility decisions.

---

## 1. There are two identifier families, and they are not the same column

This is the first thing to check on any new study design.

| Family | Column name | Appears in |
|---|---|---|
| **`uin`** | `uin` (lowercase in most extracts) | MediClaims (diagnosis and episode), COVID confirmed case registry, COVIDFACILLOS, NIR immunisation list, COVID reinfections, facility utilisation, serology |
| **`PATIENT_ID_EXTN_X`** | `PATIENT_ID_EXTN_X` | SingCLOUD Event Diagnosis, SingCLOUD Laboratory Items, and other `VW_*` SingCLOUD clinical views |

Datasets within a family join directly. Joining *across* families requires a crosswalk.

**Whether a crosswalk exists, and who provides it, is unresolved and must be confirmed with
the data owner before any study depending on it is scoped.** A study design that assumes
MediClaims billing records can be joined to SingCLOUD lab results at patient level is
making an assumption that has not been verified here.

## 2. Identifier format pitfalls

Even within an identifier family, a join can silently return zero rows. Observed causes:

- **Casing** — `uin` vs `UIN` across extracts. Normalise column names on load.
- **Type** — the same identifier read as `int64` in one file and `object` (string) in
  another. A string/int join matches nothing and raises no error.
- **Leading zeros** — lost when an identifier column is inferred as numeric. Force
  `dtype=str` on identifier columns at read time.
- **Whitespace and padding** — trailing spaces from fixed-width source systems.

**Recommended check before designing around any linkage.** A join that "runs fine" and
produces an all-null merged column is the standard failure mode, and it looks like a data
gap rather than a bug:

```python
a = set(df_left[key_l].astype(str).str.strip())
b = set(df_right[key_r].astype(str).str.strip())
print(f"left {len(a):,} | right {len(b):,} | overlap {len(a & b):,}")
```

If the overlap is zero or implausibly small, the problem is the key format, not the data.

## 3. Coding standards differ across datasets

| Dataset family | Diagnosis coding | Implication |
|---|---|---|
| MediClaims diagnosis | ICD-10 in `diagcode`, free-text in `diagdesc` | Codeable, but see the dot problem below |
| MediClaims episodes | ICD-10 in `finaldiagcode`, free-text in `finaldiagdesc` | One final diagnosis per episode, not a full problem list |
| SingCLOUD Event Diagnosis | Free-text `DIAGNOSIS_NAME_TXT`, standardised text `DIAGNOSIS_NAME_TXT_STD`, plus `DIAGNOSIS_NAME_ETS_ID`. ICD codes appear only in `ICD_CODE_PMH_STD` / `ICD_CODE_OUTCOME_STD` | **Not primarily ICD-coded.** Case-finding here means text matching against a curated description list, not a code lookup |
| Laboratory items | Free-text test names in `ITEM_NAME_ORI_TXT` | No standard test vocabulary; requires a keyword-matching dictionary per analyte |

The consequence is that "find all patients with condition X" is a *different operation* in
each dataset, and the three approaches will not return identical patient sets. Any study
ascertaining a condition from more than one source needs an explicit rule for combining
them (union, intersection, or source-priority) and should report the overlap.

### The ICD-10 dot problem

In MediClaims, ICD-10 codes appear **both with and without the decimal point** — `I21.0`
and `I210` both occur. Any regex, prefix match or code lookup must accept both forms, or it
will silently drop a subset of true cases. This is not a rare edge case; both forms are
common.

### Free-text test and diagnosis names

`ITEM_NAME_ORI_TXT` and `DIAGNOSIS_NAME_TXT` are operator-entered free text, so the same
concept appears under many spellings and abbreviations. Extracting an analyte or a
diagnosis requires a curated keyword list, and the list is a research artefact in its own
right — it should be versioned and published alongside any study using it, because
different keyword lists give different cohorts.

## 4. Granularity mismatches

Joining datasets with different units of observation multiplies rows. Before any merge,
establish what one row means on each side:

| Dataset | One row = |
|---|---|
| MediClaims diagnosis | One diagnosis event |
| MediClaims episodes | One inpatient episode |
| COVID confirmed case registry | One confirmed case |
| COVIDFACILLOS | One case episode (a patient may appear more than once) |
| NIR immunisation list | One person (doses are wide columns, not rows) |
| Serology | One test |
| Laboratory items | One test result |
| Event diagnosis | One diagnosis within an encounter |

A patient-level analysis must reduce each source to one row per patient *before* merging,
with an explicit and documented rule (earliest event, latest event, any-occurrence flag).

## 5. Wide-format vaccination data

Immunisation data is stored **wide**, not long: `vacc_date1`…`vacc_date6` and
`vaccbrand1`…`vaccbrand6`. Two consequences:

- The number of dose columns differs between sources (NIR carries up to 6; COVIDFACILLOS
  and the reinfection extracts carry up to 5). Code written against one will silently
  truncate the other.
- "Doses before date D" is a derived quantity requiring a row-wise scan across dose
  columns. It is not a column in any source dataset.

## 6. Residency and population filters are not in one place

Restricting a cohort to Singapore residents is done differently depending on the source:

- **MediClaims episodes** — `resident_type`, with values including
  `SINGAPORE PINK NRIC` and `SINGAPORE BLUE NRIC`.
- **COVID confirmed case registry** — `cat_passtype`, with values including
  `SINGAPORE CITIZEN` and `PERMANENT RESIDENT`; other values denote work passes,
  dependant passes and similar.

The exact value strings have been observed to vary between extracts (for example
`SINGAPORE PINK IC` vs `SINGAPORE PINK NRIC`). **Enumerate the distinct values in your own
extract before filtering** rather than hard-coding a list from documentation, including
this page.

## 7. Coverage differs by dataset, and that is a selection effect

The datasets do not cover the same population:

- **MediClaims** covers claims-generating care. It is not a whole-population record;
  patients whose care generated no claim will be absent.
- **The COVID case registry** covers confirmed cases across residents and non-residents.
- **NIR** covers all residents, not only those with a COVID episode — making it the
  broader vaccination source.
- **SingCLOUD clinical views** cover the participating institutions' encounters.

Requiring a patient to appear in two of these to be included in a cohort is a real and
often unintended selection criterion. It should be a stated design decision with a
documented effect on cohort size, not a side effect of an inner join.
