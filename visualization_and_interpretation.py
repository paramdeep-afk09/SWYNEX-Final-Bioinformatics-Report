from Bio import SeqIO
from collections import Counter
import matplotlib.pyplot as plt

# Load FASTA file
file = "bacillus_subtilis.fasta"

records = list(SeqIO.parse(file, "fasta"))

# Clean sequence
sequence = str(records[0].seq).upper()
sequence = sequence.replace(" ", "").replace("\n", "")

# Count bases
base_count = Counter(sequence)

A = base_count["A"]
T = base_count["T"]
G = base_count["G"]
C = base_count["C"]

total = A + T + G + C

# Calculate percentages
A_percent = (A / total) * 100
T_percent = (T / total) * 100
G_percent = (G / total) * 100
C_percent = (C / total) * 100

GC_content = G_percent + C_percent
AT_content = A_percent + T_percent

print("=" * 55)
print("BACILLUS SUBTILIS - VISUALIZATION & INTERPRETATION")
print("=" * 55)

print("\nNucleotide Counts")
print("-----------------")
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)

print("\nNucleotide Percentages")
print("----------------------")
print("A:", round(A_percent, 2), "%")
print("T:", round(T_percent, 2), "%")
print("G:", round(G_percent, 2), "%")
print("C:", round(C_percent, 2), "%")

print("\nGC Content:", round(GC_content, 2), "%")
print("AT Content:", round(AT_content, 2), "%")


# --------------------------------
# Chart 1: Nucleotide Composition
# --------------------------------

bases = ["A", "T", "G", "C"]
counts = [A, T, G, C]

plt.figure(figsize=(8, 5))

plt.bar(bases, counts)

plt.title("Nucleotide Composition of Bacillus subtilis")
plt.xlabel("Nucleotide")
plt.ylabel("Number of Bases")

plt.tight_layout()
plt.savefig("nucleotide_composition.png", dpi=300)
plt.show()


# --------------------------------
# Chart 2: GC vs AT Content
# --------------------------------

contents = ["GC", "AT"]
percentages = [GC_content, AT_content]

plt.figure(figsize=(7, 5))

plt.bar(contents, percentages)

plt.title("GC vs AT Content of Bacillus subtilis")
plt.xlabel("Base Composition")
plt.ylabel("Percentage (%)")

plt.ylim(0, 100)

plt.tight_layout()
plt.savefig("GC_AT_content.png", dpi=300)
plt.show()


print("\nCharts generated successfully.")
print("Saved as:")
print("- nucleotide_composition.png")
print("- GC_AT_content.png")