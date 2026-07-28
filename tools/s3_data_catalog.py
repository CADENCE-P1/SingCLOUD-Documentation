#!/usr/bin/env python3
"""
S3 CSV Data Catalog Generator
=============================
Walks the CSV datasets under:
    s3://$SINGCLOUD_BUCKET/common-data/SingCLoud/FreeText_FTA/
    s3://$SINGCLOUD_BUCKET/common-data/SingCLoud/NonFreeText_Files/

The bucket is read from the SINGCLOUD_BUCKET environment variable so that no
environment-specific infrastructure identifier is committed to this repository:

    export SINGCLOUD_BUCKET=<bucket-name>
    python3 s3_data_catalog.py

For every CSV it records:
  - file size, number of rows, number of columns, column names
  - per-column missingness and overall dataset missingness
  - for non-numeric, non-ID-like columns: top 20 values with counts
    (ID-like = most values contain more than 7 digits, e.g. NRIC/UIN/claim numbers)
  - for date-like columns: min/max date range
  - for numeric columns: min / max / mean

Outputs (in ./data_catalog_output/):
  - data_catalog_report.txt   one continuous human-readable report (appended live)
  - data_catalog_summary.txt  condensed report: size, rows, columns + missingness only
                              (rebuilt from the CSVs after every dataset, so it is
                              always complete even across resumes)
  - dataset_summary.csv       one row per dataset
  - column_summary.csv        one row per column per dataset
  - checkpoint.json           progress tracker enabling resume

Resume behaviour: the checkpoint marks each file "in_progress" before reading it
and "completed" only after its report section is written. If the script hangs or
is killed, rerunning it skips completed files and re-attempts the last one.

Requirements: python3, pandas, boto3 (both standard on SageMaker/Workspaces AWS images).
Usage:  python3 s3_data_catalog.py
"""

import csv
import io
import json
import os
import re
import sys
import time
import traceback
from collections import Counter
from datetime import datetime

import boto3
import pandas as pd

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
BUCKET = os.environ.get("SINGCLOUD_BUCKET")
if not BUCKET:
    sys.exit(
        "SINGCLOUD_BUCKET is not set.\n"
        "The bucket name is deliberately not hard-coded in this repository.\n"
        "Set it from your platform configuration before running:\n"
        "    export SINGCLOUD_BUCKET=<bucket-name>"
    )
# Scanned recursively — every .csv at any depth below these prefixes is included.
# Override from the command line, e.g.:
#   python3 s3_data_catalog.py common-data/SingCLoud/FreeText_FTA/ common-data/SingCLoud/NonFreeText_Files/
# (full s3://bucket/... URIs are also accepted)
PREFIXES = [
    "common-data/SingCLoud/",
]

OUTPUT_DIR = "data_catalog_output"
REPORT_PATH = os.path.join(OUTPUT_DIR, "data_catalog_report.txt")
SUMMARY_REPORT_PATH = os.path.join(OUTPUT_DIR, "data_catalog_summary.txt")
DATASET_CSV_PATH = os.path.join(OUTPUT_DIR, "dataset_summary.csv")
COLUMN_CSV_PATH = os.path.join(OUTPUT_DIR, "column_summary.csv")
CHECKPOINT_PATH = os.path.join(OUTPUT_DIR, "checkpoint.json")

CHUNKSIZE = 100_000          # rows per chunk when streaming the CSV
SAMPLE_SIZE = 2_000          # non-null values sampled per column for type detection
TOP_N = 20                   # top values to report for categorical columns
MAX_TRACKED_UNIQUES = 200_000  # stop tracking value counts beyond this cardinality
ID_DIGIT_THRESHOLD = 7       # "ID-like" if most values contain > 7 digits
ID_LIKE_FRACTION = 0.5       # fraction of sampled values that must be ID-like
NUMERIC_FRACTION = 0.95      # fraction of sample that must parse as numeric
DATE_FRACTION = 0.80         # fraction of sample that must parse as a date

DATE_NAME_HINTS = re.compile(r"(date|_dt$|^dt_|dob|admission|discharge|visit|death)", re.I)

DATASET_CSV_FIELDS = [
    "s3_key", "status", "file_size_mb", "n_rows", "n_cols",
    "overall_missing_pct", "columns", "error", "profiled_at",
]
COLUMN_CSV_FIELDS = [
    "s3_key", "column", "inferred_type", "n_missing", "missing_pct",
    "n_unique_tracked", "top_values", "date_min", "date_max",
    "num_min", "num_max", "num_mean",
]

# ----------------------------------------------------------------------------
# Checkpoint helpers
# ----------------------------------------------------------------------------

def load_checkpoint():
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH) as f:
            return json.load(f)
    return {"files": {}}


def save_checkpoint(cp):
    tmp = CHECKPOINT_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(cp, f, indent=2)
    os.replace(tmp, CHECKPOINT_PATH)


# ----------------------------------------------------------------------------
# S3 listing
# ----------------------------------------------------------------------------

def list_csv_files(s3, prefixes):
    """Return [(key, size_bytes), ...] for every .csv under the prefixes."""
    files = []
    skipped = Counter()
    paginator = s3.get_paginator("list_objects_v2")
    for prefix in prefixes:
        n_before = len(files)
        for page in paginator.paginate(Bucket=BUCKET, Prefix=prefix):
            for obj in page.get("Contents", []):
                key = obj["Key"]
                if key.lower().endswith(".csv"):
                    files.append((key, obj["Size"]))
                elif not key.endswith("/"):
                    ext = os.path.splitext(key)[1].lower() or "(no extension)"
                    skipped[ext] += 1
        print(f"  {prefix}: {len(files) - n_before} CSV files")
    if skipped:
        print("  Skipped non-CSV objects by extension: "
              + ", ".join(f"{ext} x{n}" for ext, n in skipped.most_common()))
    files.sort()
    return files


def diagnose_empty_listing(s3, prefixes):
    """Nothing matched — show what actually exists so the prefixes can be fixed."""
    for prefix in prefixes:
        print(f"\nDIAGNOSTIC: contents under s3://{BUCKET}/{prefix}")
        resp = s3.list_objects_v2(Bucket=BUCKET, Prefix=prefix, Delimiter="/", MaxKeys=100)
        subdirs = [p["Prefix"] for p in resp.get("CommonPrefixes", [])]
        objects = [o["Key"] for o in resp.get("Contents", [])]
        if subdirs:
            print("  Subfolders:")
            for d in subdirs:
                print(f"    {d}")
        if objects:
            print("  Objects (first 100 at this level):")
            for k in objects:
                print(f"    {k}")
        if not subdirs and not objects:
            # Prefix itself matches nothing — walk up to the parent to show siblings
            parent = prefix.rstrip("/")
            parent = parent[: parent.rfind("/") + 1] if "/" in parent else ""
            print(f"  Nothing found at this prefix. Contents of parent "
                  f"s3://{BUCKET}/{parent} :")
            presp = s3.list_objects_v2(Bucket=BUCKET, Prefix=parent, Delimiter="/", MaxKeys=100)
            for p in presp.get("CommonPrefixes", []):
                print(f"    {p['Prefix']}")
            for o in presp.get("Contents", []):
                print(f"    {o['Key']}")
    print("\nRe-run with the correct prefix(es), e.g.:")
    print(f"  python3 {os.path.basename(sys.argv[0])} common-data/SingCLoud/FreeText_FTA/")


# ----------------------------------------------------------------------------
# Type-detection heuristics (run on a sample of non-null values)
# ----------------------------------------------------------------------------

def looks_numeric(sample):
    if len(sample) == 0:
        return False
    converted = pd.to_numeric(sample, errors="coerce")
    return converted.notna().mean() >= NUMERIC_FRACTION


def looks_id_like(sample):
    """True if most values contain more than ID_DIGIT_THRESHOLD digits."""
    if len(sample) == 0:
        return False
    digit_heavy = sample.astype(str).str.count(r"\d") > ID_DIGIT_THRESHOLD
    return digit_heavy.mean() >= ID_LIKE_FRACTION


def looks_date(colname, sample):
    if len(sample) == 0:
        return False
    name_hint = bool(DATE_NAME_HINTS.search(colname))
    # Don't try to date-parse plain numbers unless the name says it's a date
    if looks_numeric(sample) and not name_hint:
        return False
    with pd.option_context("mode.chained_assignment", None):
        parsed = pd.to_datetime(sample.astype(str), errors="coerce", format="mixed", dayfirst=True)
    frac = parsed.notna().mean()
    return frac >= DATE_FRACTION or (name_hint and frac >= 0.5)


# ----------------------------------------------------------------------------
# Per-column streaming accumulator
# ----------------------------------------------------------------------------

class ColumnStats:
    def __init__(self, name):
        self.name = name
        self.n_total = 0
        self.n_missing = 0
        self.sample = None            # pd.Series of non-null sample values
        self.inferred_type = None     # numeric | date | id_like | categorical
        self.counter = Counter()
        self.counter_overflow = False
        self.date_min = None
        self.date_max = None
        self.num_min = None
        self.num_max = None
        self.num_sum = 0.0
        self.num_count = 0

    def infer_type(self):
        s = self.sample if self.sample is not None else pd.Series([], dtype=object)
        if looks_date(self.name, s):
            self.inferred_type = "date"
        elif looks_numeric(s):
            self.inferred_type = "numeric"
        elif looks_id_like(s):
            self.inferred_type = "id_like"
        else:
            self.inferred_type = "categorical"

    def update(self, series):
        self.n_total += len(series)
        nonnull = series.dropna()
        self.n_missing += len(series) - len(nonnull)

        if self.sample is None:
            self.sample = nonnull.head(SAMPLE_SIZE)
            self.infer_type()

        if len(nonnull) == 0:
            return

        if self.inferred_type == "date":
            parsed = pd.to_datetime(nonnull.astype(str), errors="coerce",
                                    format="mixed", dayfirst=True).dropna()
            if len(parsed):
                lo, hi = parsed.min(), parsed.max()
                self.date_min = lo if self.date_min is None else min(self.date_min, lo)
                self.date_max = hi if self.date_max is None else max(self.date_max, hi)
        elif self.inferred_type == "numeric":
            nums = pd.to_numeric(nonnull, errors="coerce").dropna()
            if len(nums):
                lo, hi = nums.min(), nums.max()
                self.num_min = lo if self.num_min is None else min(self.num_min, lo)
                self.num_max = hi if self.num_max is None else max(self.num_max, hi)
                self.num_sum += float(nums.sum())
                self.num_count += int(len(nums))
        elif self.inferred_type == "categorical":
            if not self.counter_overflow:
                vc = nonnull.astype(str).str.strip().value_counts()
                self.counter.update(vc.to_dict())
                if len(self.counter) > MAX_TRACKED_UNIQUES:
                    self.counter_overflow = True

    # ------------------------------------------------------------------
    def missing_pct(self):
        return 100.0 * self.n_missing / self.n_total if self.n_total else 0.0

    def top_values(self, n=TOP_N):
        return self.counter.most_common(n)

    def num_mean(self):
        return self.num_sum / self.num_count if self.num_count else None


# ----------------------------------------------------------------------------
# CSV streaming from S3 (with encoding fallback)
# ----------------------------------------------------------------------------

def open_csv_chunks(s3, key, encoding):
    body = s3.get_object(Bucket=BUCKET, Key=key)["Body"]
    text = io.TextIOWrapper(body, encoding=encoding, errors="strict" if encoding == "utf-8" else "replace")
    return pd.read_csv(
        text,
        chunksize=CHUNKSIZE,
        dtype=str,               # keep raw strings; typing is done by our heuristics
        keep_default_na=True,
        na_values=["", "NA", "N/A", "NULL", "null", "None", "NaN", "."],
        on_bad_lines="skip",
        low_memory=True,
    )


def profile_dataset(s3, key, size_bytes):
    """Stream one CSV and return (dataset_summary_dict, [ColumnStats,...])."""
    stats = {}
    col_order = []
    n_rows = 0

    for encoding in ("utf-8", "latin-1"):
        try:
            stats, col_order, n_rows = {}, [], 0
            for chunk in open_csv_chunks(s3, key, encoding):
                if not col_order:
                    col_order = list(chunk.columns)
                    stats = {c: ColumnStats(c) for c in col_order}
                n_rows += len(chunk)
                for c in col_order:
                    stats[c].update(chunk[c])
                print(f"    ... {n_rows:,} rows", end="\r", flush=True)
            break
        except UnicodeDecodeError:
            print(f"    utf-8 decode failed, retrying with latin-1 ...")
            continue

    print()
    total_cells = n_rows * len(col_order) if col_order else 0
    total_missing = sum(s.n_missing for s in stats.values())
    summary = {
        "s3_key": key,
        "status": "completed",
        "file_size_mb": round(size_bytes / 1024**2, 2),
        "n_rows": n_rows,
        "n_cols": len(col_order),
        "overall_missing_pct": round(100.0 * total_missing / total_cells, 2) if total_cells else 0.0,
        "columns": "; ".join(col_order),
        "error": "",
        "profiled_at": datetime.now().isoformat(timespec="seconds"),
    }
    return summary, [stats[c] for c in col_order]


# ----------------------------------------------------------------------------
# Report writing
# ----------------------------------------------------------------------------

def write_report_section(fh, summary, col_stats):
    key = summary["s3_key"]
    fh.write("\n" + "=" * 100 + "\n")
    fh.write(f"DATASET: s3://{BUCKET}/{key}\n")
    fh.write("=" * 100 + "\n")
    fh.write(f"File size      : {summary['file_size_mb']:,} MB\n")
    fh.write(f"Rows           : {summary['n_rows']:,}\n")
    fh.write(f"Columns        : {summary['n_cols']}\n")
    fh.write(f"Overall missing: {summary['overall_missing_pct']:.2f}% of all cells\n")
    fh.write(f"Column names   : {summary['columns']}\n\n")

    fh.write(f"{'COLUMN':<40} {'TYPE':<12} {'MISSING':>10} {'MISSING %':>10}\n")
    fh.write("-" * 76 + "\n")
    for cs in col_stats:
        fh.write(f"{cs.name[:39]:<40} {cs.inferred_type or 'empty':<12} "
                 f"{cs.n_missing:>10,} {cs.missing_pct():>9.2f}%\n")
    fh.write("\n")

    for cs in col_stats:
        if cs.inferred_type == "date" and cs.date_min is not None:
            fh.write(f"  [DATE ] {cs.name}: {cs.date_min.date()}  ->  {cs.date_max.date()}\n")
        elif cs.inferred_type == "numeric" and cs.num_count:
            fh.write(f"  [NUM  ] {cs.name}: min={cs.num_min:g}  max={cs.num_max:g}  "
                     f"mean={cs.num_mean():g}\n")
        elif cs.inferred_type == "id_like":
            fh.write(f"  [ID   ] {cs.name}: ID-like (values mostly contain >"
                     f"{ID_DIGIT_THRESHOLD} digits) — top values suppressed\n")
        elif cs.inferred_type == "categorical":
            note = " (high cardinality, counts approximate)" if cs.counter_overflow else ""
            fh.write(f"  [CAT  ] {cs.name}: top {TOP_N} values{note}\n")
            for val, cnt in cs.top_values():
                display = (val[:80] + "...") if len(val) > 80 else val
                fh.write(f"           {cnt:>10,}  |  {display}\n")
    fh.write("\n")
    fh.flush()


def rebuild_summary_report():
    """Regenerate the condensed report (size / rows / columns / missingness only)
    from the two summary CSVs. Rewritten in full after every dataset, so it is
    always complete and deduplicated regardless of resumes."""
    if not os.path.exists(DATASET_CSV_PATH):
        return

    def read_csv_dedup(path, keyfields):
        rows = {}
        if os.path.exists(path):
            with open(path, newline="") as f:
                for row in csv.DictReader(f):
                    rows[tuple(row[k] for k in keyfields)] = row  # last write wins
        return list(rows.values())

    datasets = read_csv_dedup(DATASET_CSV_PATH, ["s3_key"])
    columns = read_csv_dedup(COLUMN_CSV_PATH, ["s3_key", "column"])
    cols_by_key = {}
    for row in columns:
        cols_by_key.setdefault(row["s3_key"], []).append(row)

    tmp = SUMMARY_REPORT_PATH + ".tmp"
    with open(tmp, "w") as fh:
        fh.write(f"S3 DATA CATALOG — CONDENSED SUMMARY — s3://{BUCKET}/\n")
        fh.write(f"Rebuilt {datetime.now():%Y-%m-%d %H:%M:%S} — "
                 f"{len(datasets)} datasets\n")
        for d in sorted(datasets, key=lambda r: r["s3_key"]):
            fh.write("\n" + "-" * 100 + "\n")
            fh.write(f"{d['s3_key']}\n")
            if d["status"] != "completed":
                fh.write(f"  STATUS: {d['status']} — {d['error']}\n")
                continue
            fh.write(f"  Size: {d['file_size_mb']} MB | Rows: {d['n_rows']} | "
                     f"Cols: {d['n_cols']} | Overall missing: {d['overall_missing_pct']}%\n")
            fh.write(f"  {'COLUMN':<50} {'TYPE':<12} {'MISSING %':>10}\n")
            for c in cols_by_key.get(d["s3_key"], []):
                fh.write(f"  {c['column'][:49]:<50} {c['inferred_type']:<12} "
                         f"{c['missing_pct']:>10}\n")
    os.replace(tmp, SUMMARY_REPORT_PATH)


def append_csv_row(path, fieldnames, row):
    new_file = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if new_file:
            w.writeheader()
        w.writerow(row)


def column_csv_rows(key, col_stats):
    for cs in col_stats:
        top = "; ".join(f"{v} ({c})" for v, c in cs.top_values()) \
              if cs.inferred_type == "categorical" else ""
        yield {
            "s3_key": key,
            "column": cs.name,
            "inferred_type": cs.inferred_type,
            "n_missing": cs.n_missing,
            "missing_pct": round(cs.missing_pct(), 2),
            "n_unique_tracked": len(cs.counter) if cs.inferred_type == "categorical" else "",
            "top_values": top[:2000],
            "date_min": cs.date_min.date() if cs.date_min is not None else "",
            "date_max": cs.date_max.date() if cs.date_max is not None else "",
            "num_min": cs.num_min if cs.num_min is not None else "",
            "num_max": cs.num_max if cs.num_max is not None else "",
            "num_mean": round(cs.num_mean(), 4) if cs.num_count else "",
        }


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def normalise_prefix(p):
    """Accept 'common-data/X/', 's3://bucket/common-data/X' or '/common-data/X'."""
    p = p.strip()
    if p.startswith("s3://"):
        p = p[len("s3://"):]
        p = p.split("/", 1)[1] if "/" in p else ""
    p = p.lstrip("/")
    if p and not p.endswith("/"):
        p += "/"
    return p


def main():
    prefixes = [normalise_prefix(a) for a in sys.argv[1:]] or PREFIXES

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    s3 = boto3.client("s3")
    cp = load_checkpoint()

    print(f"Listing CSV files under s3://{BUCKET}/ ...")
    for p in prefixes:
        print(f"  prefix: {p}")
    files = list_csv_files(s3, prefixes)
    print(f"Found {len(files)} CSV files.\n")

    if not files:
        diagnose_empty_listing(s3, prefixes)
        sys.exit(1)

    done = {k for k, v in cp["files"].items() if v.get("status") == "completed"}
    pending = [(k, sz) for k, sz in files if k not in done]
    if done:
        print(f"Resuming: {len(done)} already completed, {len(pending)} remaining.\n")

    report = open(REPORT_PATH, "a")
    if report.tell() == 0:
        report.write(f"S3 DATA CATALOG REPORT — s3://{BUCKET}/common-data/\n")
        report.write(f"Generated starting {datetime.now():%Y-%m-%d %H:%M:%S}\n")
    else:
        report.write(f"\n\n### RESUMED {datetime.now():%Y-%m-%d %H:%M:%S} ###\n")
    report.flush()

    for i, (key, size_bytes) in enumerate(pending, 1):
        print(f"[{i}/{len(pending)}] {key}  ({size_bytes/1024**2:.1f} MB)")

        # Mark as in-progress BEFORE reading so a hang/kill resumes here
        cp["files"][key] = {"status": "in_progress",
                            "attempted_at": datetime.now().isoformat(timespec="seconds")}
        save_checkpoint(cp)

        t0 = time.time()
        try:
            summary, col_stats = profile_dataset(s3, key, size_bytes)
            write_report_section(report, summary, col_stats)
            append_csv_row(DATASET_CSV_PATH, DATASET_CSV_FIELDS, summary)
            for row in column_csv_rows(key, col_stats):
                append_csv_row(COLUMN_CSV_PATH, COLUMN_CSV_FIELDS, row)
            rebuild_summary_report()
            cp["files"][key] = {"status": "completed",
                                "seconds": round(time.time() - t0, 1),
                                "n_rows": summary["n_rows"]}
            print(f"    done in {time.time()-t0:.1f}s — "
                  f"{summary['n_rows']:,} rows x {summary['n_cols']} cols, "
                  f"{summary['overall_missing_pct']:.1f}% missing overall")
        except KeyboardInterrupt:
            print("\nInterrupted — progress saved; rerun to resume from this file.")
            save_checkpoint(cp)
            sys.exit(1)
        except Exception as e:
            err = f"{type(e).__name__}: {e}"
            print(f"    FAILED: {err}")
            traceback.print_exc(limit=3)
            report.write("\n" + "=" * 100 + "\n")
            report.write(f"DATASET: s3://{BUCKET}/{key}\nERROR  : {err}\n")
            report.flush()
            append_csv_row(DATASET_CSV_PATH, DATASET_CSV_FIELDS, {
                "s3_key": key, "status": "error",
                "file_size_mb": round(size_bytes / 1024**2, 2),
                "n_rows": "", "n_cols": "", "overall_missing_pct": "",
                "columns": "", "error": err,
                "profiled_at": datetime.now().isoformat(timespec="seconds"),
            })
            cp["files"][key] = {"status": "error", "error": err}
            rebuild_summary_report()
        save_checkpoint(cp)

    report.write(f"\n\n### FINISHED {datetime.now():%Y-%m-%d %H:%M:%S} ###\n")
    report.close()
    n_err = sum(1 for v in cp["files"].values() if v.get("status") == "error")
    print(f"\nAll done. {len(cp['files'])} files processed ({n_err} errors).")
    rebuild_summary_report()
    print(f"Report  : {REPORT_PATH}")
    print(f"Summary : {SUMMARY_REPORT_PATH}")
    print(f"CSVs    : {DATASET_CSV_PATH}, {COLUMN_CSV_PATH}")


if __name__ == "__main__":
    main()
