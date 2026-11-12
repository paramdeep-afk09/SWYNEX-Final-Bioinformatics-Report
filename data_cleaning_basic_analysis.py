from Bio import SeqIO
from collections import Counter
from statistics import mean, median

# FASTA file
file = "bacillus_subtilis.fasta"

# Read FASTA
records = list(SeqIO.parse(file, "fasta"))

print("=" * 50)
print("BACILLUS SUBTILIS - DATA CLEANING & BASIC ANALYSIS")
print("=" * 50)

# -----------------------------
# Data Cleaning
# -----------------------------

sequences = []

for record in records:
    sequence = str(record.seq).upper()
    sequence = sequence.replace(" ", "").replace("\n", "")
    sequences.append(sequence)

print("\nData cleaning completed.")

# -----------------------------
# Basic Statistics
# -----------------------------

lengths = [len(seq) for seq in sequences]

print("\n--- BASIC STATISTICS ---")

print("Number of sequences:", len(sequences))
print("Total sequence length:", sum(lengths), "bp")
print("Minimum sequence length:", min(lengths), "bp")
print("Maximum sequence length:", max(lengths), "bp")
print("Mean sequence length:", round(mean(lengths), 2), "bp")
print("Median sequence length:", round(median(lengths), 2), "bp")

# -----------------------------
# Base Composition
# -----------------------------

all_sequence = "".join(sequences)
base_count = Counter(all_sequence)

A = base_count["A"]
T = base_count["T"]
G = base_count["G"]
C = base_count["C"]
N = base_count["N"]

total_bases = len(all_sequence)

GC_content = ((G + C) / total_bases) * 100
AT_content = ((A + T) / total_bases) * 100
N_content = (N / total_bases) * 100

print("\n--- BASE COMPOSITION ---")

print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)
print("N:", N)

print("\nGC content:", round(GC_content, 2), "%")
print("AT content:", round(AT_content, 2), "%")
print("N content:", round(N_content, 4), "%")

# -----------------------------
# Data Quality
# -----------------------------

unique_sequences = set(sequences)
duplicate_sequences = len(sequences) - len(unique_sequences)

print("\n--- DATA QUALITY ---")

print("Unique sequences:", len(unique_sequences))
print("Duplicate sequences:", duplicate_sequences)

print("\nAnalysis completed successfully.")