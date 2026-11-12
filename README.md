# SWYNEX Final Bioinformatics Report

## Basic Sequence Analysis, Data Cleaning, Visualization and Interpretation of *Bacillus subtilis*

### Internship Task 4 – Final Bioinformatics Report

---

## 1. Research Question

**What are the basic sequence characteristics and nucleotide composition of the analyzed *Bacillus subtilis* genome sequence, and what can these characteristics reveal about its overall genomic composition?**

---

## 2. Introduction

Bioinformatics provides computational approaches for storing, processing, analyzing, and interpreting biological data. Genome sequences are commonly represented in FASTA format, which allows nucleotide sequences to be processed computationally and analyzed for characteristics such as sequence length, nucleotide composition, and GC content.

In this project, a *Bacillus subtilis* genome sequence was analyzed using Python-based bioinformatics tools. The workflow included sequence data processing, basic data cleaning, statistical analysis, nucleotide composition analysis, visualization, and scientific interpretation.

The purpose of this analysis was not to perform a complete genome annotation or functional analysis, but to demonstrate a basic and reproducible workflow for handling biological sequence data.

---

## 3. Dataset

The dataset consisted of a *Bacillus subtilis* genome sequence in FASTA format.

### Dataset Information

| Parameter | Value |
|---|---:|
| Organism | *Bacillus subtilis* |
| File format | FASTA |
| Number of sequences | 1 |
| Sequence length | 4,215,606 bp |
| Unknown bases (N) | 0 |

The FASTA sequence was processed using Python and Biopython.

---

## 4. Tools and Technologies

The analysis was performed using the following tools:

- **Python**
- **Biopython**
- **Matplotlib**
- **Visual Studio Code**
- **GitHub**

### Python Libraries

```python
from Bio import SeqIO
from collections import Counter
from statistics import mean, median
import matplotlib.pyplot as plt
```

---

## 5. Methods

### 5.1 FASTA Sequence Processing

The FASTA file was read using Biopython's `SeqIO` module.

The sequence was converted to uppercase and unnecessary whitespace was removed before further analysis.

### 5.2 Data Cleaning

Basic sequence-cleaning operations were performed to ensure consistent processing.

The cleaning workflow included:

1. Loading the FASTA sequence.
2. Converting nucleotide characters to uppercase.
3. Removing unnecessary spaces and newline characters.
4. Checking for unknown nucleotide bases represented by `N`.
5. Checking for duplicate sequences.

### 5.3 Basic Sequence Statistics

The following sequence-level statistics were calculated:

- Number of sequences
- Total sequence length
- Minimum sequence length
- Maximum sequence length
- Mean sequence length
- Median sequence length

Because the dataset contained one sequence, the minimum, maximum, mean, and median sequence lengths were identical.

### 5.4 Nucleotide Composition

The number of A, T, G, C, and N bases was calculated using Python's `Counter`.

GC and AT content were calculated using:

**GC content:**

\[
GC\% = \frac{G+C}{A+T+G+C} \times 100
\]

**AT content:**

\[
AT\% = \frac{A+T}{A+T+G+C} \times 100
\]

### 5.5 Data Visualization

Matplotlib was used to create two visualizations:

1. **Nucleotide Composition of *Bacillus subtilis***
2. **GC vs AT Content of *Bacillus subtilis***

These charts were used to make the nucleotide distribution easier to interpret.

---

# 6. Results

## 6.1 Basic Sequence Statistics

The analysis identified one sequence with a total length of **4,215,606 base pairs**.

| Statistic | Result |
|---|---:|
| Number of sequences | 1 |
| Total sequence length | 4,215,606 bp |
| Minimum sequence length | 4,215,606 bp |
| Maximum sequence length | 4,215,606 bp |
| Mean sequence length | 4,215,606 bp |
| Median sequence length | 4,215,606 bp |

Since only one sequence was analyzed, all sequence-length statistics have the same value.

---

## 6.2 Nucleotide Composition

The nucleotide counts obtained from the sequence were:

| Nucleotide | Count | Percentage |
|---|---:|---:|
| A | 1,188,073 | 28.18% |
| T | 1,193,137 | 28.30% |
| G | 915,112 | 21.71% |
| C | 919,284 | 21.81% |
| N | 0 | 0% |

The results show that A and T were more abundant than G and C.

---

## 6.3 GC and AT Content

The overall base composition was:

| Parameter | Result |
|---|---:|
| GC content | 43.51% |
| AT content | 56.49% |
| N content | 0% |

The GC and AT percentages together account for the complete analyzed sequence because no unknown `N` bases were detected.

---

# 7. Data Quality Assessment

Basic quality checks were performed on the sequence.

| Quality Check | Result |
|---|---:|
| Number of sequences | 1 |
| Unique sequences | 1 |
| Duplicate sequences | 0 |
| Unknown bases | 0 |

No duplicate sequence was detected, and no unknown nucleotide bases were present in the analyzed sequence.

The absence of `N` bases indicates that the analyzed FASTA sequence did not contain ambiguous nucleotide positions represented by `N`.

---

# 8. Visualization

Two charts were generated using Matplotlib.

## 8.1 Nucleotide Composition Chart

The nucleotide composition chart displays the number of A, T, G, and C bases present in the analyzed sequence.

The visualization shows that A and T occur at higher frequencies than G and C.

The counts were:

- A = 1,188,073
- T = 1,193,137
- G = 915,112
- C = 919,284

## 8.2 GC vs AT Content Chart

The second visualization compares the overall GC and AT composition.

The results show:

- **GC = 43.51%**
- **AT = 56.49%**

Therefore, the analyzed sequence contains a higher proportion of AT bases than GC bases.

---

# 9. Scientific Interpretation

The analysis demonstrates that the analyzed *Bacillus subtilis* sequence has a GC content of **43.51%** and an AT content of **56.49%**.

The nucleotide composition is not evenly distributed. A and T together account for a greater proportion of the sequence than G and C.

The relatively higher AT proportion is reflected directly in the GC-versus-AT visualization.

The nucleotide composition provides a basic description of the sequence and can be useful as an initial quality-control and exploratory step in genome analysis.

However, nucleotide composition alone cannot provide information about the function of individual genes or genomic regions. More advanced analyses would be necessary to investigate biological function, gene organization, regulatory regions, evolutionary relationships, or other genomic characteristics.

---

# 10. What the Analysis Shows and Does Not Prove

### The analysis shows:

- Overall genome sequence length
- Distribution of A, T, G, and C nucleotides
- Overall GC and AT content
- Presence or absence of `N` bases
- Basic sequence-level data quality
- Visual representation of nucleotide composition

### The analysis does not prove:

- Gene function
- Protein function
- Pathogenicity
- Virulence
- Evolutionary relationships
- Gene expression
- Antibiotic resistance
- Specific biological mechanisms

These conclusions would require additional analyses such as genome annotation, gene prediction, comparative genomics, phylogenetic analysis, transcriptomics, or functional analysis.

---

# 11. Limitations

Several limitations should be considered when interpreting the results.

### 11.1 Single Sequence

Only one FASTA sequence was analyzed. Therefore, the analysis does not provide a comparison between multiple *Bacillus subtilis* strains or other bacterial species.

### 11.2 Basic Sequence Analysis

The workflow focused on basic sequence statistics and nucleotide composition. It did not include gene prediction, genome annotation, protein analysis, or functional characterization.

### 11.3 Limited Biological Interpretation

GC and AT content describe nucleotide composition but cannot independently explain biological traits or functions.

### 11.4 Dataset Dependence

The calculated results describe the specific FASTA sequence analyzed. Different genome assemblies, strains, or datasets may produce different values.

### 11.5 No Comparative Analysis

No comparison was performed with other *Bacillus* species, strains, or reference genomes. Therefore, evolutionary or comparative conclusions cannot be drawn from this analysis alone.

---

# 12. Conclusion

This project demonstrated a basic bioinformatics workflow for analyzing a biological genome sequence using Python.

A *Bacillus subtilis* FASTA sequence of **4,215,606 bp** was processed and analyzed. Basic sequence statistics, nucleotide composition, GC content, AT content, and data-quality characteristics were calculated.

The analysis identified:

- **43.51% GC content**
- **56.49% AT content**
- **0% N content**
- **1 unique sequence**
- **0 duplicate sequences**

Two visualizations were generated to represent nucleotide composition and the GC-to-AT relationship.

Overall, the project provided practical experience in **FASTA sequence processing, data cleaning, statistical analysis, biological data visualization, and scientific interpretation using Python and Biopython**.

The workflow also demonstrates the importance of distinguishing between what sequence-level statistics can directly show and what would require more advanced bioinformatics analysis.

---

# 13. Reproducibility

The analysis can be reproduced using the provided Python scripts and FASTA dataset.

### Required packages

```bash
pip install biopython matplotlib
```

### Run the data-cleaning analysis

```bash
python data_cleaning_basic_analysis.py
```

### Run the visualization analysis

```bash
python visualization_and_interpretation.py
```

The visualization script generates:

```text
nucleotide_composition.png
GC_AT_content.png
```

---

# 14. References

1. National Center for Biotechnology Information (NCBI). **GenBank and NCBI Genome Resources.** National Library of Medicine, National Institutes of Health.

2. Cock, P. J. A., Antao, T., Chang, J. T., Chapman, B. A., Cox, C. J., Dalke, A., Friedberg, I., Hamelryck, T., Kauff, F., Wilbanks, E. G., & de Hoon, M. J. L. (2009). **Biopython: freely available Python tools for computational molecular biology and bioinformatics.** *Bioinformatics*, 25(11), 1422–1423. https://doi.org/10.1093/bioinformatics/btp163

3. Hunter, J. D. (2007). **Matplotlib: A 2D Graphics Environment.** *Computing in Science & Engineering*, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55

4. The Python Software Foundation. **Python Documentation.** Python Programming Language.

---

# 15. Project Structure

```text
SWYNEX-Final-Bioinformatics-Report/
│
├── Final_Bioinformatics_Report.md
├── bacillus_subtilis.fasta
├── data_cleaning_basic_analysis.py
├── visualization_and_interpretation.py
├── nucleotide_composition.png
└── GC_AT_content.png
```

---

## Internship Task

**SWYNEX Technologies – Task 4**  
**Final Bioinformatics Report**

**Focus:** Sequence Data Cleaning, Basic Analysis, Visualization and Scientific Interpretation
