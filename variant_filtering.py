from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "results" / "variants.csv"
OUTPUT_FILE = BASE_DIR / "results" / "filtered_variants.csv"

print("=" * 50)
print("VARIANT FILTERING")
print("=" * 50)

# Read variant results
df = pd.read_csv(INPUT_FILE)

print(f"Total Variants Before Filtering: {len(df)}")

# For this educational pipeline,
# keep valid SNP records with complete information.
if not df.empty:

    filtered_df = df[
        (df["Variant_Type"] == "SNP") &
        (df["Reference"].notna()) &
        (df["Alternate"].notna())
    ].copy()

else:
    filtered_df = df.copy()

# Save filtered variants
filtered_df.to_csv(OUTPUT_FILE, index=False)

print(f"High-Confidence Variants       : {len(filtered_df)}")

print("\nVariant filtering completed successfully!")

print("Filtered result saved to:")
print(OUTPUT_FILE)