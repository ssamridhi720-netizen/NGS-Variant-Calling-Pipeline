from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"

OUTPUT_FILE = RESULTS_DIR / "NGS_Variant_Analysis_Report.xlsx"

print("=" * 60)
print("GENERATING FINAL NGS ANALYSIS REPORT")
print("=" * 60)

# Create Excel writer
with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:

    # 1. FASTQ Summary
    file = RESULTS_DIR / "fastq_summary.csv"

    if file.exists():
        df = pd.read_csv(file)
        df.to_excel(writer, sheet_name="QC Summary", index=False)

    # 2. Quality Report
    file = RESULTS_DIR / "quality_report.csv"

    if file.exists():
        df = pd.read_csv(file)
        df.to_excel(writer, sheet_name="Quality Scores", index=False)

    # 3. Alignment
    file = RESULTS_DIR / "alignment_results.csv"

    if file.exists():
        df = pd.read_csv(file)
        df.to_excel(writer, sheet_name="Alignment", index=False)

    # 4. Variants
    file = RESULTS_DIR / "variants.csv"

    if file.exists():
        df = pd.read_csv(file)
        df.to_excel(writer, sheet_name="Variants", index=False)

    # 5. Filtered Variants
    file = RESULTS_DIR / "filtered_variants.csv"

    if file.exists():
        df = pd.read_csv(file)
        df.to_excel(
            writer,
            sheet_name="Filtered Variants",
            index=False
        )

    # 6. Annotation
    file = RESULTS_DIR / "annotated_variants.csv"

    if file.exists():
        df = pd.read_csv(file)
        df.to_excel(
            writer,
            sheet_name="Annotation",
            index=False
        )

print("\nFinal report generated successfully!")
print(f"Excel Report: {OUTPUT_FILE}")