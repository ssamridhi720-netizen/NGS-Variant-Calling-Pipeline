from Bio import SeqIO
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

FASTQ_FILE = BASE_DIR / "results" / "trimmed_sample_R1.fastq"
REFERENCE_FILE = BASE_DIR / "data" / "reference.fasta"
RESULTS_DIR = BASE_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)

# Read reference sequence
reference_record = SeqIO.read(REFERENCE_FILE, "fasta")
reference = str(reference_record.seq)

print("=" * 50)
print("REFERENCE GENOME ALIGNMENT")
print("=" * 50)

alignment_results = []

# Read trimmed FASTQ
for record in SeqIO.parse(FASTQ_FILE, "fastq"):

    read_sequence = str(record.seq)

    position = reference.find(read_sequence)

    if position != -1:
        alignment_status = "Aligned"
        reference_position = position + 1
    else:
        alignment_status = "Not Aligned"
        reference_position = None

    alignment_results.append({
        "Read_ID": record.id,
        "Read_Length": len(read_sequence),
        "Alignment_Status": alignment_status,
        "Reference_Position": reference_position
    })

# Create DataFrame
df = pd.DataFrame(alignment_results)

print(df)

# Save alignment report
output_file = RESULTS_DIR / "alignment_results.csv"

df.to_csv(output_file, index=False)

aligned_reads = (df["Alignment_Status"] == "Aligned").sum()

print("\nTotal Reads     :", len(df))
print("Aligned Reads   :", aligned_reads)

print("\nAlignment completed successfully!")

print("Result saved to:")
print(output_file)