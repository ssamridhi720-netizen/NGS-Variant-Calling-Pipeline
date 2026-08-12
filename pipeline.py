from pathlib import Path
import subprocess
import sys

# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = BASE_DIR / "scripts"

print("=" * 60)
print("      NGS VARIANT CALLING PIPELINE")
print("=" * 60)

# Pipeline steps
steps = [
    ("FASTQ Analysis", "fastq_analysis.py"),
    ("Quality Analysis", "quality_analysis.py"),
    ("Adapter Trimming", "trimming.py"),
    ("Reference Alignment", "alignment.py"),
    ("Variant Calling", "variant_calling.py"),
    ("Variant Filtering", "variant_filtering.py"),
    ("Variant Annotation", "variant_annotation.py"),
    ("Final Report Generation", "final_report.py")
]

# Run each step
for step_number, (step_name, script_name) in enumerate(steps, start=1):

    print("\n" + "=" * 60)
    print(f"STEP {step_number}: {step_name}")
    print("=" * 60)

    script_path = SCRIPTS_DIR / script_name

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=True
        )

        print(f"\n✓ {step_name} completed successfully!")

    except subprocess.CalledProcessError:
        print(f"\n✗ ERROR: {step_name} failed.")
        print("Pipeline stopped.")
        sys.exit(1)

print("\n" + "=" * 60)
print("      PIPELINE COMPLETED SUCCESSFULLY!")
print("=" * 60)

print("\nFinal results are available in:")
print(BASE_DIR / "results")