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

### `mass_columns_screenshots/` — the profiler summary, as photographed

28 full-page screenshots (~159 MB) of `data_catalog_summary.txt`, the condensed report
produced by [`tools/s3_data_catalog.py`](../tools/s3_data_catalog.py) and rebuilt
2026-07-23. These are the primary evidence for everything in
[`imported/profiler_report_full.txt`](imported/profiler_report_full.txt) and
[`datasets/full_inventory.md`](../datasets/full_inventory.md).

They are committed in full and at original resolution so any figure in the reconstruction
can be checked against the image it came from.

⚠️ **`section_01.png` shows the S3 bucket name** in the report header. It is redacted
everywhere else in this repo. The repo is private; if it is ever made public, crop that
header first.

**Two things to know about the screenshots themselves:**

1. **They do not cover the whole report.** The header states 275 datasets; the images
   capture 205 files, and `section_28.png` stops part-way through a heart-failure dataset's
   column list. Roughly 50–70 datasets at the end of the report were never photographed.
2. **They are images of text**, so nothing in them is searchable. That is what the
   reconstruction below is for.

Retrieving the real `data_catalog_summary.txt` from the platform remains the recommended
next step: it would replace transcription with verified figures and cover the datasets the
screenshots miss.

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
| `profiler_report_full.txt` | Reconstruction of the profiler summary from the screenshots | **The full report**: object path, size, rows, columns and overall missingness per dataset, then every column with its type and missing %. 205 datasets, 11,914 column rows |
| `dataset_summary.csv` | Same, machine-readable | One row per dataset |
| `column_summary.csv` | Same, machine-readable | One row per column per dataset |

### How the reconstruction was built, and how far to trust it

Each screenshot was OCR'd **twice** with macOS Vision under different tiling and scaling
settings, producing two independent readings. The readings were aligned per dataset and per
column — by sequence alignment, so a row dropped in one pass does not cascade — and merged
field by field, letting each pass correct the other. Digits flanked by letters
(`DIAGNOS1S`) and spaces inside identifiers (`ITEM DESCRIPTION`) were repaired, since these
are SQL column names and cannot contain either.

**The two passes agreed on 84.5% of column names outright**; the rest were resolved by
preferring the cleaner reading.

Every dataset block is marked with an integrity flag comparing recovered columns against
the count the report itself declares:

| Flag | Meaning | Count |
|---|---|---|
| `[OK]` | Exactly as many columns recovered as declared | 186 of 207 |
| `[SHORT n]` | `n` column rows lost to OCR | — |
| `[OVER n]` | `n` spurious rows — treat that block as indicative | — |

Verified by spot-check against the source screenshots at five datasets across two
independent regions (~45 field values): exact agreement on every path, size, row count,
column count, missingness figure, column name and type.

**What to still be careful about.** Row counts, sizes and percentages are long digit runs
and read reliably, but none are independently verified against the platform. Column names
are the least reliable field — expect residual errors in unusual identifiers. Confirm any
specific figure before relying on it.
