from Bio import SeqIO
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

FASTQ_FILE = BASE_DIR / "results" / "trimmed_sample_R1.fastq"
REFERENCE_FILE = BASE_DIR / "data" / "reference.fasta"
RESULTS_DIR = BASE_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)

# Read reference genome
reference_record = SeqIO.read(REFERENCE_FILE, "fasta")
reference = str(reference_record.seq)

print("=" * 50)
print("VARIANT CALLING")
print("=" * 50)

variants = []

for record in SeqIO.parse(FASTQ_FILE, "fastq"):

    read = str(record.seq)

    # Find read position in reference
    start_position = reference.find(read)

    if start_position == -1:
        continue

    # Compare read with reference
    for i, base in enumerate(read):

        reference_position = start_position + i
        reference_base = reference[reference_position]

        if base != reference_base:

            variants.append({
                "Read_ID": record.id,
                "Position": reference_position + 1,
                "Reference": reference_base,
                "Alternate": base,
                "Variant_Type": "SNP"
            })

# Create DataFrame
if variants:

    variant_df = pd.DataFrame(variants)

else:

    variant_df = pd.DataFrame(
        columns=[
            "Read_ID",
            "Position",
            "Reference",
            "Alternate",
            "Variant_Type"
        ]
    )

# Save variants
output_file = RESULTS_DIR / "variants.csv"

variant_df.to_csv(output_file, index=False)

print(f"Variants Detected : {len(variant_df)}")

print("\nVariant calling completed successfully!")

print("Result saved to:")
print(output_file)