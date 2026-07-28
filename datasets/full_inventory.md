# Full dataset inventory

> 🟡 **Draft, reconstructed from screenshots.** Built from
> [`profiler_report_full.txt`](../source_material/imported/profiler_report_full.txt), a
> two-pass OCR reconstruction of the profiler's condensed summary (rebuilt 2026-07-23).
> Figures are transcribed, not verified against the platform. Spot-checked against the
> source screenshots at five datasets with exact agreement, but residual OCR error in
> less common identifiers should be assumed.

---

## Scope

The profiler header reports **275 datasets**. The screenshots capture **205** of them —
the final image stops part-way through a heart-failure dataset, so roughly 50–70
datasets at the end of the report were never photographed. What was captured resolves
to **84 dataset families**, **741,999,934 rows** and about **218 GB**.

| | Documented in `datasets/` | Captured in the screenshots | Reported by the profiler |
|---|---|---|---|
| Dataset families | 13 | 84 | unknown (not all photographed) |
| Individual files | ~100 | 205 | 275 |

The gap between 13 and 84 is a scoping discovery, not a documentation backlog: entire
domains — billing, cardiac registries, imaging, procedures — have no page at all.

---

## Two findings worth acting on

**1. The platform holds ~849,308 patients.** Every `VW_PATIENT_*_D_Export` table —
gender, race, religion, language, nationality, residential status, occupation — reports
exactly **849,308** rows, with DOB at 849,164 and marital status at 849,012. One row per
patient per attribute makes that the size of the SingCLOUD patient master. It is the
denominator every dataset page's "population represented" field should be stated
against, and it currently appears on none of them.

**2. The ECG example from the rationale is real and specific.** The rationale argues a
researcher building an AI model needs raw data rather than an interpreted diagnosis.
This platform contains exactly that pair:

| Dataset | Rows | What it holds |
|---|---:|---|
| `VW_CIIMS_ECHO_MEASUREMENTS_D_Export` | 11,520,086 | Quantitative echo **measurements** |
| `VW_CIIMS_ECHO_FINDINGS_D_Export` | 1,130,597 | Echo **findings** — interpretation |

The ten-to-one ratio is the compression of interpretation: many measurements collapse
into one reported finding. A model trained on findings learns to predict cardiologists;
a model trained on measurements learns to predict hearts. Which is which is exactly what
the standard's §2 exists to record, and these two should be the first pages written
after the governance gap is closed.

---

## Billing

*7 families · 80 files · 440,940,235 rows · 131.2 GB*

The largest domain on the platform by a wide margin, and entirely undocumented in `datasets/`. Outpatient, inpatient and medication billing.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_IP_BILLING_F_Export` | 32 | 168,843,719 | 53.9 GB | NonFreeText |
| `VW_OP_BILLING_F_Export` | 27 | 156,267,077 | 43.6 GB | NonFreeText |
| `VW_MED_BILLING_F_Export` | 17 | 93,302,155 | 26.7 GB | NonFreeText |
| `VW_IP_BILLING_F_Export:` | 1 | 6,887,095 | 2.2 GB | NonFreeText |
| `VW_IP_BILLING_F-_Export` | 1 | 6,254,562 | 2.0 GB | NonFreeText |
| `VW_OP_BILLING_F_Export:` | 1 | 4,855,493 | 1.3 GB | NonFreeText |
| `VW_LIP_BILLING_F_Export` | 1 | 4,530,134 | 1.4 GB | NonFreeText |

## Medications

*5 families · 32 files · 136,029,828 rows · 41.1 GB*

`VW_DISPENSED_MEDICATION_ITEM_F_Export` is the item-level detail; `VW_DISPENSED_MEDICATION_F_Export` the order level; `VW_DRUG_D_Export` the drug reference table. The existing [medications page](singcloud-medications.md) documents 29 parts under a different alias and needs reconciling against these.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_DISPENSED_MEDICATION_ITEM_F_Export` | 26 | 114,996,944 | 36.3 GB | FreeText |
| `VW_DISPENSED_MEDICATION_F_Export` | 3 | 13,288,910 | 2.7 GB | FreeText |
| `VW_DISPENSED_MEDICATION_CROSS_MAPS_MV2_D_Export` | 1 | 4,219,826 | 1.2 GB | NonFreeText |
| `VW_DISPENSED_MEDICATION_ITEM_F_Export:` | 1 | 3,124,838 | 980 MB | FreeText |
| `VW_DRUG_D_Export` | 1 | 399,310 | 51 MB | NonFreeText |

## Laboratory

*3 families · 14 files · 64,328,647 rows · 18.6 GB*

`VW_LABORATORY_F_Export` is substantially larger than the `VW_LABORATORY_ITEM_FIL_F_Export` family the [laboratory page](singcloud-laboratory-items.md) documents. Establishing the relationship between them is an open task.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_LABORATORY_F_Export` | 11 | 49,620,429 | 15.1 GB | FreeText |
| `VW_LABORATORY_ITEM_FIL_F_Export` | 2 | 14,392,594 | 3.4 GB | FreeText |
| `VW_LABORATORY_DIM_F_Export` | 1 | 315,624 | 35 MB | NonFreeText |

## Diagnosis & encounters

*5 families · 10 files · 37,287,655 rows · 8.3 GB*

`VW_EVENT_DIAGNOSIS_F_Export` is documented on the [event diagnosis page](singcloud-event-diagnosis.md). The `_CODE_D_` and `_TYPE_D_` tables alongside it are its reference vocabularies.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_EVENT_DIAGNOSIS_F_Export` | 6 | 32,000,357 | 7.8 GB | FreeText |
| `VW_DIAGNOSIS_CODE_D_Export` | 1 | 5,286,383 | 529 MB | NonFreeText |
| `VW_SINGCLOUD_DIAGNOSIS_CODE_D_Export` | 1 | 859 | 0 MB | NonFreeText |
| `VW_DIAGNOSIS_TYPE_D_Export` | 1 | 47 | 0 MB | NonFreeText |
| `VW_DIAGNOSIS_STATUS_D_Export` | 1 | 9 | 0 MB | NonFreeText |

## Procedures & operations

*9 families · 11 files · 21,440,907 rows · 8.2 GB*

Procedure and operation records plus surgical registry links. No page exists for any of these.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_MOH_OB_PROCEDURE_F_Export` | 2 | 7,398,828 | 2.7 GB | NonFreeText |
| `VW_MOH_OB_OPERATION_F_Export` | 2 | 6,745,298 | 2.5 GB | NonFreeText |
| `VW_MOH_OB_PROCEDURE_F_Export:` | 1 | 3,325,012 | 1.2 GB | NonFreeText |
| `VW_MOH_OB_WO_SHI_F_Export` | 1 | 2,654,121 | 1.5 GB | NonFreeText |
| `VW_MOH_OB_OPERATION_F_Export:` | 1 | 706,032 | 126 MB | NonFreeText |
| `VW_NUHCS_PROC_D_Export` | 1 | 408,586 | 76 MB | NonFreeText |
| `VW_SCDB_SURGERY_DIM_F_Export` | 1 | 189,067 | 55 MB | NonFreeText |
| `VW_SCDB_SURGERY_F_Export` | 1 | 8,026 | 10 MB | FreeText |
| `VW_SCDB_SURGERY_BEFORE_F_Export` | 1 | 5,937 | 10 MB | NonFreeText |

## Cardiac registries (SCDB)

*15 families · 16 files · 2,763,975 rows · 1.2 GB*

A cardiac registry family (ICD, pacemakers, EPS, surgery, intervention, heart failure), each with a paired `_DIM_` dimension table. Small in rows, high in clinical depth — several carry 90+ columns.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_SCDB_INTERVENTION_DIM_F_Export` | 1 | 1,634,566 | 555 MB | FreeText |
| `VW_SCDB_HF_DIM_F_Export` | 1 | 655,784 | 152 MB | NonFreeText |
| `VW_SCDB_INTERVENTION_F_Export` | 1 | 107,689 | 60 MB | FreeText |
| `VW_SCDB_HF_F_Export` | 2 | 97,258 | 98 MB | FreeText/NonFreeText |
| `VW_SCDB_INTERVENTION_BEFORE_T2_F_Export` | 1 | 62,348 | 211 MB | NonFreeText |
| `VW_SCDB_INTERVENTION_BEFORE_T1_F_Export` | 1 | 62,342 | 84 MB | FreeText |
| `VW_SCDB_EPS_DIM_F_Export` | 1 | 51,379 | 24 MB | NonFreeText |
| `VW_SCDB_PPM_DIM_F_Export` | 1 | 35,994 | 18 MB | FreeText |
| `VW_SCDB_ICD_DIM_F_Export` | 1 | 24,450 | 13 MB | NonFreeText |
| `VW_SCDB_ZLMAUDITEPS_DIM_F_Export` | 1 | 10,810 | 3 MB | NonFreeText |
| `VW_SCDB_PPM_F_Export` | 1 | 6,434 | 4 MB | FreeText |
| `VW_SCDB_EPS_F_Export` | 1 | 6,220 | 4 MB | NonFreeText |
| `VW_SCDB_ICD_F_Export` | 1 | 4,043 | 3 MB | FreeText |
| `VW_SCDB_ZLMAUDITEPS_F_Export` | 1 | 2,942 | 1 MB | NonFreeText |
| `VW_SCDB_ZLMAUDITICD_F_Export` | 1 | 1,716 | 1 MB | NonFreeText |

## Cardiac imaging & diagnostics

*13 families · 15 files · 20,390,646 rows · 6.1 GB*

Echo, nuclear, radiology and catheterisation data across several institutions (CIIMS, NUHCS, CGH, SKH, CVIS). **Where the raw-versus-interpreted distinction bites hardest** — see the note above.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_CIIMS_ECHO_MEASUREMENTS_D_Export` | 1 | 11,520,086 | 1.5 GB | NonFreeText |
| `VW_RADIOLOGY_F_Export` | 1 | 6,569,893 | 2.6 GB | FreeText |
| `VW_CIIMS_ECHO_FINDINGS_D_Export` | 1 | 1,130,597 | 209 MB | NonFreeText |
| `VW_NUHCS_ECHO_D_Export` | 1 | 270,906 | 542 MB | FreeText |
| `VW_CIIMS_WALLMOTION_D_Export` | 1 | 259,487 | 53 MB | NonFreeText |
| `VW_NUHCS_PCI_D_Export` | 1 | 230,968 | 823 MB | FreeText |
| `VW_CIIMS_RHYTHM_D_Export` | 1 | 148,278 | 22 MB | NonFreeText |
| `VW_NUHS_HFSI_F_Export` | 3 | 128,086 | 250 MB | FreeText/NonFreeText |
| `VW_NUHCS_NUC_D_Export` | 1 | 63,656 | 161 MB | FreeText |
| `VW_CVIS_NUCLEAR_D_Export` | 1 | 54,449 | 34 MB | FreeText |
| `VW_NUH_CABG_09_21_D_Export` | 1 | 5,007 | 8 MB | FreeText |
| `VW_SKH_CVIS_MIBI_D_Export` | 1 | 4,846 | 5 MB | NonFreeText |
| `VW_CGH_NUCLEAR_F_Export` | 1 | 4,387 | 6 MB | FreeText |

## Patient master / demographics

*11 families · 11 files · 8,693,653 rows · 1.6 GB*

One table per demographic attribute rather than one wide table — gender, race, religion, language, nationality, DOB, marital status, occupation, residential status, death indicator.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_PATIENT_DEATH_IND_D_Export` | 1 | 1,050,317 | 217 MB | NonFreeText |
| `VW_PATIENT_OCCUPATION_D_Export:` | 1 | 849,308 | 134 MB | FreeText |
| `VW_PATIENT_GENDER_D_Export` | 1 | 849,308 | 154 MB | NonFreeText |
| `VW_PATIENT_LANGUAGE_D_Export` | 1 | 849,308 | 154 MB | NonFreeText |
| `VW_PATIENT_NATIONALITY_D_Export` | 1 | 849,308 | 161 MB | NonFreeText |
| `VW_PATIENT_RACE_D_Export` | 1 | 849,308 | 154 MB | NonFreeText |
| `VW_PATIENT_RELIGION_D_Export` | 1 | 849,308 | 152 MB | NonFreeText |
| `VW_PATIENT_RESIDENTIAL_STATUS_D_Export` | 1 | 849,308 | 154 MB | NonFreeText |
| `VW_PATIENT_DOB_D_Export` | 1 | 849,164 | 164 MB | NonFreeText |
| `VW_PATIENT_MARITAL_STATUS_D_Export` | 1 | 849,012 | 153 MB | NonFreeText |
| `VW_PATIENT_TYPE_D_Export` | 1 | 4 | 0 MB | NonFreeText |

## Reference & lookup tables

*15 families · 15 files · 2,267,699 rows · 0.3 GB*

Small controlled-vocabulary tables. **These answer "what coding standards does this dataset use?"** for much of the platform, and are cheap to read in full.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_SERVICE_CODE_D_Export` | 1 | 2,142,754 | 252 MB | NonFreeText |
| `VW_ITEM_D_Export` | 1 | 81,721 | 7 MB | NonFreeText |
| `VW_SERVICE_SPECIALITY_D_Export` | 1 | 25,088 | 2 MB | NonFreeText |
| `VW_INSTITUTION_D_Export` | 1 | 9,727 | 1 MB | NonFreeText |
| `VW_DRG_D_Export` | 1 | 4,137 | 0 MB | NonFreeText |
| `VW_REFERRAL_FACILITY_D_Export` | 1 | 2,683 | 0 MB | NonFreeText |
| `VW_DISCHARGE_DISPOSITION_D_Export` | 1 | 527 | 0 MB | NonFreeText |
| `VW_MOV_TYPE_D_Export` | 1 | 396 | 0 MB | NonFreeText |
| `VW_INV_TYPE_D_Export` | 1 | 177 | 0 MB | NonFreeText |
| `VW_INV_SUBTYPE_D_Export` | 1 | 160 | 0 MB | NonFreeText |
| `VW_ADMIT_TYPE_D_Export` | 1 | 132 | 0 MB | NonFreeText |
| `VW_ITEM_STATUS_D_Export` | 1 | 125 | 0 MB | NonFreeText |
| `VW_CASE_TYPE_D_Export` | 1 | 37 | 0 MB | NonFreeText |
| `VW_INV_RESULT_STATUS_D_Export` | 1 | 32 | 0 MB | NonFreeText |
| `VW_MOV_CAT_D_Export` | 1 | 3 | 0 MB | NonFreeText |

## Other

*1 families · 1 files · 7,856,689 rows · 1.7 GB*

Not yet classified.

| Family | Files | Rows | Size | Zone |
|---|---:|---:|---:|---|
| `VW_EVENT_DIAGNO515_F_Export` | 1 | 7,856,689 | 1.7 GB | FreeText |

---

## Notes on this table

**Zone** is the storage prefix: `FreeText` (`FreeText_FTA/`) or `NonFreeText`
(`NonFreeText_Files/`). The split separates datasets containing free-text clinical
fields from those that do not, which is likely governance-relevant and should be
confirmed with the data owner.

**Family names carry residual OCR noise.** Near-duplicate entries in the billing rows
(`VW_IP_BILLING_F_Export` alongside variants) are the same family read differently
across partitions, not distinct datasets. Row counts and file counts are unaffected;
only the grouping is.

## What to do with this

1. **Get the real `data_catalog_summary.txt`.** It would replace the reconstruction with
   verified figures and cover the ~70 datasets the screenshots never captured.
2. **Decide scope.** Documenting 84 families to the full standard is a programme.
   The reference tables are nearly free and disproportionately useful, since they define
   the coding standards other datasets depend on.
3. **Reconcile the aliases.** Existing pages use catalogue aliases (`Event_Diagnosis_P1`);
   this inventory uses object filenames (`VW_EVENT_DIAGNOSIS_F_Export_31-07-2024_P1.csv`).
   Same data, two naming systems, no mapping written down anywhere.
