# Tools

## `s3_data_catalog.py`

Profiles every CSV under the SingCLOUD storage prefixes and produces the mechanical half of
this catalogue: row counts, column lists, missingness, date ranges and value distributions.

Most of the "Not yet profiled" gaps in `datasets/*.md` are closed by running this and
pasting the output in.

### What it records per file

- File size, row count, column count, column names
- Per-column missingness, and overall dataset missingness
- Top 20 values with counts for categorical columns — **skipping ID-like columns**, detected
  as columns where most values contain more than 7 digits (NRIC/UIN/claim numbers). This is
  what keeps identifier values out of the report.
- Min/max date range for date-like columns
- Min/max/mean for numeric columns

### Running it

The bucket name is **not** hard-coded — it is read from the environment so that no
infrastructure identifier is committed here. Run from inside the analysis environment,
where the IAM role grants read access:

```bash
export SINGCLOUD_BUCKET=<bucket-name>

# Default prefixes (common-data/SingCLoud/)
python3 s3_data_catalog.py

# Or target specific prefixes
python3 s3_data_catalog.py common-data/SingCLoud/FreeText_FTA/ \
                           common-data/SingCLoud/NonFreeText_Files/
```

Requires `pandas` and `boto3`, both standard on the platform images.

### Output

Written to `./data_catalog_output/`:

| File | Contents |
|---|---|
| `data_catalog_report.txt` | Full human-readable report, appended live |
| `data_catalog_summary.txt` | Condensed: size, rows, columns, missingness. Rebuilt after every dataset, so it stays complete across resumes |
| `dataset_summary.csv` | One row per dataset |
| `column_summary.csv` | One row per column per dataset |
| `checkpoint.json` | Progress tracker enabling resume |

It reads in 100k-row chunks and checkpoints per file, so a run interrupted partway through a
multi-hour scan resumes rather than restarting. A file is marked `in_progress` before being
read and `completed` only once its report section is written, so an interrupted file is
re-attempted rather than skipped.

### Before committing output

⚠️ **The ID-like heuristic is a safeguard, not a guarantee.** It suppresses value listings
for columns whose values look like identifiers, but a free-text column can contain anything
— a `DIAGNOSIS_NAME_TXT` or `serologylabinterpretationnote` value could include a name, an
identifier, or other patient detail typed into a clinical note.

**Read the report before committing any of it**, and paste only aggregate figures (row
counts, missingness percentages, column names) into the dataset pages. Do not commit the
raw report files wholesale — `data_catalog_output/` is gitignored for that reason.
