# Dataset index

Master list of datasets **documented** in this catalogue. Sorted by information type.

> ⚠️ **This is 13 of roughly 80 dataset families on the platform.** The profiler summary
> reports **275 datasets**, spanning billing, cardiac registries, imaging and procedures —
> domains with no page here at all. See
> [**full_inventory.md**](full_inventory.md) for the complete scope before concluding that
> a dataset you need is unavailable.

**Status:** ✅ Verified (profiler-checked *and* owner-confirmed) · 🟡 Draft (analyst
knowledge, not owner-confirmed) · ⚪ Stub (known to exist, not documented)

---

## Clinical

| Dataset | Alias pattern | Unit of observation | Parts | ID family | Status |
|---|---|---|---|---|---|
| [SingCLOUD — Event Diagnosis](singcloud-event-diagnosis.md) | `Event_Diagnosis_P{1-8}` | Diagnosis within encounter | 8 (~5.1M rows in P1) | `PATIENT_ID_EXTN_X` | 🟡 |
| [SingCLOUD — Medication Items](singcloud-medications.md) | `SingCLOUD_medication_items{1-29}` | Dispensed medication | 29 | *unconfirmed* | 🟡 |

## Laboratory

| Dataset | Alias pattern | Unit of observation | Parts | ID family | Status |
|---|---|---|---|---|---|
| [SingCLOUD — Laboratory Items](singcloud-laboratory-items.md) | `VW_LABORATORY_ITEM_FIL_F_Export_{date}_P{1-22}` | Test result | 22 | `PATIENT_ID_EXTN_X` | 🟡 |
| [COVID-19 Serology Tests](serology-tests-covid.md) | `Serology_Tests_COVID` | Serology test | 1 | `uin` | 🟡 |

## Billing / claims

| Dataset | Alias pattern | Unit of observation | Parts | ID family | Status |
|---|---|---|---|---|---|
| [MediClaims — Diagnosis](mediclaims-diagnosis.md) | `mediclaims_diag_{2015-2023}` | Diagnosis event | 9 | `uin` | 🟡 |
| [MediClaims — Episodes](mediclaims-episodes.md) | `mediclaims_epi_{2017-2023}` | Inpatient episode | 7 | `uin` | 🟡 |
| [Casemix](casemix.md) | `casemix_data_{fy}` | Inpatient spell | per FY | *encrypted, unconfirmed* | ⚪ |

## Registry / surveillance

| Dataset | Alias pattern | Unit of observation | Parts | ID family | Status |
|---|---|---|---|---|---|
| [COVID-19 Confirmed Case Registry](covid-confirmed-case-registry.md) | `ConfirmedCaseHeadersForAgencies*` | Confirmed case | 7 | `uin` | 🟡 |
| [COVID-19 Reinfections](covid-reinfections.md) | `COVID Reinfections` | Reinfection event | 1 | `uin` | 🟡 |
| [Death Registry](death-registry.md) | `death_registry` | Death event | 1 | `uin` | 🟡 |
| [NIR — National Immunisation Registry](nir-immunisation.md) | `NIRListtruncated` | **Person** | 1 | `uin` | 🟡 |

## Administrative / facility

| Dataset | Alias pattern | Unit of observation | Parts | ID family | Status |
|---|---|---|---|---|---|
| [COVIDFACILLOS](covid-facility-los.md) | `COVIDFACILLOS` | Case episode | 1 | `uin` | 🟡 |
| [Facility Utilisation — Reinfections](covid-reinfection-facility-utilisation.md) | `FacilityUtilizationLOSSubsequentRI` | Reinfection episode | 1 | `uin` | 🟡 |

## Demographic

| Dataset | Alias pattern | Unit of observation | Parts | ID family | Status |
|---|---|---|---|---|---|
| [SingCLOUD — Demographics](singcloud-demographics.md) | `SingCLOUD_gender`, `SingCLOUD_DOB` | **Person** | 2 | *unconfirmed* | 🟡 |

---

## Coverage at a glance

| Dataset | 2012 | 2015 | 2017 | 2020 | 2023 | 2024 |
|---|---|---|---|---|---|---|
| Casemix | ▓ *(from FY2012/13; full range unknown)* | ? | ? | ? | ? | ? |
| MediClaims — Diagnosis | | ▓▓▓▓▓▓▓▓▓ 2015–2023 | | | ▓ | |
| MediClaims — Episodes | | | ▓▓▓▓▓▓▓ 2017–2023 | | ▓ | |
| COVID datasets | | | | ▓▓ 2020-01 onward | ▓ | ▓ to 2024-02 |
| SingCLOUD clinical views | ? | ? | ? | ? | ? | extract 2024-07 |

Cells marked `?` are undocumented, not empty. Establishing the true period covered for each
dataset is an open task — it is the single most commonly needed field for a suitability
decision and currently the least complete.

---

## Known gaps across the whole catalogue

These apply to nearly every page and are tracked here rather than repeated:

0. **Coverage: 13 families documented, ~80 present.** See
   [full_inventory.md](full_inventory.md). Undocumented domains include billing (the
   largest on the platform at ~441M rows), cardiac registries, cardiac imaging, procedures
   and the reference/lookup tables that define other datasets' coding standards.
1. **Ownership and governance is undocumented for every dataset.** No data owner, approval
   requirement or lead time is recorded anywhere. Stakeholders currently cannot make the
   governance decision from this catalogue. See
   [docs/02_access_and_governance.md](../docs/02_access_and_governance.md).
2. **Period covered is unconfirmed for most datasets.** Derivable empirically from the date
   columns; not yet done.
3. **Missingness and row counts are unprofiled** except where noted. Mechanically
   obtainable via [`tools/s3_data_catalog.py`](../tools/s3_data_catalog.py).
4. **The `uin` ↔ `PATIENT_ID_EXTN_X` crosswalk is unresolved.** This determines whether
   claims/registry data can be joined to SingCLOUD clinical data at all, and is the highest
   priority open question in the catalogue. See
   [docs/03_linkage_guide.md](../docs/03_linkage_guide.md).
5. **Column manifests are partial** for MediClaims diagnosis, medications, demographics,
   death registry and casemix — they record fields used in one analysis, not the full
   schema.
6. **Variable availability over time is undocumented** for all datasets except where
   structurally obvious (vaccination fields, dataset start years).
