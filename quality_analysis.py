from Bio import SeqIO
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
FASTQ_FILE = BASE_DIR / "data" / "sample_R1.fastq"
RESULTS_DIR = BASE_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)

# Read FASTQ file
records = list(SeqIO.parse(FASTQ_FILE, "fastq"))

print("=" * 50)
print("NGS QUALITY SCORE ANALYSIS")
print("=" * 50)

quality_data = []

for record in records:
    qualities = record.letter_annotations["phred_quality"]

    quality_data.append({
        "Read_ID": record.id,
        "Average_Quality": sum(qualities) / len(qualities),
        "Minimum_Quality": min(qualities),
        "Maximum_Quality": max(qualities)
    })

# Create DataFrame
df = pd.DataFrame(quality_data)

print(df)

# Save quality report
output_file = RESULTS_DIR / "quality_report.csv"
df.to_csv(output_file, index=False)

# Calculate overall average quality
overall_quality = df["Average_Quality"].mean()

print("\nOverall Average Quality:",
      round(overall_quality, 2))

print("\nQuality report saved to:")
print(output_file)

# Create graph
plt.figure(figsize=(8, 5))

plt.bar(df["Read_ID"], df["Average_Quality"])

plt.xlabel("Read ID")
plt.ylabel("Average Phred Quality")
plt.title("FASTQ Read Quality Analysis")

plt.tight_layout()

graph_file = RESULTS_DIR / "quality_score_plot.png"
plt.savefig(graph_file)

plt.show()

print("\nQuality graph saved to:")
print(graph_file)