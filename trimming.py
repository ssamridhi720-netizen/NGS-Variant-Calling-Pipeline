from Bio import SeqIO
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "sample_R1.fastq"
OUTPUT_FILE = BASE_DIR / "results" / "trimmed_sample_R1.fastq"

# Example adapter sequence for demonstration
ADAPTER = "AGATCGGAAGAGC"

print("=" * 50)
print("NGS READ TRIMMING")
print("=" * 50)

trimmed_count = 0
total_count = 0

with open(OUTPUT_FILE, "w") as output_handle:

    for record in SeqIO.parse(INPUT_FILE, "fastq"):
        total_count += 1

        sequence = str(record.seq)

        # Remove adapter if present
        if ADAPTER in sequence:
            sequence = sequence.split(ADAPTER)[0]
            trimmed_count += 1

        # Skip reads that become too short
        if len(sequence) < 10:
            continue

        record.seq = record.seq[:len(sequence)]

        SeqIO.write(record, output_handle, "fastq")

print(f"Total Reads       : {total_count}")
print(f"Reads Trimmed     : {trimmed_count}")
print(f"Output File       : {OUTPUT_FILE}")

print("\nTrimming completed successfully!")