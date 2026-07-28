# Source material

Raw inputs the dataset pages are built from. **Nothing here is documentation** — it is
evidence and working notes. Anything genuinely useful should be promoted into a
`datasets/*.md` page and cited from here.

---

## `screenshots/`

Screenshots of dataset summaries taken from the platform, used to supplement and verify the
written documentation.

**Before committing a screenshot:**

- ✅ Schema views, column lists, `df.info()` / `df.describe()` output, aggregate counts,
  category value counts
- ❌ **Any visible patient-level record.** A screenshot of `df.head()` shows real rows.
  Crop or redact them.
- ❌ Any real identifier, even partially visible
- ❌ Visible bucket paths, ARNs, credentials or environment URLs in window chrome
- ❌ Small cell counts that could identify an individual

A pushed screenshot cannot be un-pushed — git history keeps it even after deletion. Check
before committing, not after.

**Naming:** `<dataset-alias>__<what-it-shows>.png`, e.g.
`Event_Diagnosis_P1__columns.png`. Predictable names let dataset pages link directly to the
evidence for a claim.

### `mass_columns_screenshots/` — present on disk, deliberately untracked

28 full-page screenshots (~159 MB) of the condensed profiler summary covering **275
datasets**. Kept in `.gitignore` for two reasons:

1. **`section_01.png` shows the S3 bucket name** in the report header — the one identifier
   deliberately kept out of the rest of this repo.
2. **They are screenshots of a text file.** 159 MB of PNG that nobody can grep, holding
   content that is a few hundred KB as text.

Rather than commit them, their contents were **OCR-transcribed into
[`imported/profiler_summary_ocr.txt`](imported/profiler_summary_ocr.txt)** (1.2 MB,
searchable, bucket name redacted), and the scope was summarised in
[`datasets/full_inventory.md`](../datasets/full_inventory.md).

The images remain on disk for reference and can be re-read at any time.

> **The transcription is not a substitute for the source file.** OCR misreads characters,
> and none of the digits are independently verified. Retrieving the real
> `data_catalog_summary.txt` from the platform remains the recommended next step — it would
> upgrade the inventory from "transcribed" to "verified" and close the "Not yet profiled"
> gaps across every dataset page at once.

## `imported/`

Working documentation carried over from an analysis project that used SingCLOUD. See the
[provenance note in the README](../README.md#provenance-of-the-current-content).

These are **analyst working notes, not verified documentation.** They were written to get
one study done, not to describe the platform, and they carry that study's assumptions. They
are kept for traceability: when a `datasets/*.md` page makes a claim, these files are where
it came from.

Study-specific content — cohort definitions, sample sizes, statistical results, clinical
code lists specific to that study's research question — was **removed** during import.
Only dataset-descriptive material was retained.

| File | Origin | What it gives you |
|---|---|---|
| `data_context_extract.md` | Analysis project data context, dataset sections only | Dataset inventory with observed row counts, date ranges, key columns |
| `hf_diagnosis_data_context.md` | Analysis project catalogue notes | The most complete column manifests available — lab items, event diagnosis, mediclaims episodes |
| `catalogue_config_snapshot.md` | Analysis pipeline configuration | Exact alias strings as used against the platform |
| `profiler_summary_ocr.txt` | OCR of the 28 profiler screenshots | Row counts, column names, types and missingness for 218 datasets. Machine-transcribed — read its header before quoting any figure |
