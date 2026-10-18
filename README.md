
# Sequence Handling: FASTA Analysis

## Overview
A Python project for analyzing DNA sequences stored in FASTA format.

## Features
- Parses multiple DNA sequences from a FASTA file.
- Calculates sequence length.
- Counts A, T, G, and C nucleotides.
- Calculates GC content as a percentage.
- Exports results to a CSV file.
- Accepts an input FASTA file through the command line.

## Requirements
- Python 3
- No external Python packages required.

## How to Run

Run the script from the repository's root directory:

```bash
python sequence_analysis.py data/sample.fasta
```

The script prints sequence statistics and creates
a file named `results.csv` in the current directory.

## GC Content Formula

GC content (%) = ((G + C) / sequence length) * 100

## Input
The example input is `data/sample.fasta`.

## Output
The CSV output includes:
- Sequence ID
- Sequence length
- A, T, G and C counts
- GC content percentage

## Limitations
This version accepts DNA sequences containing only
A, T, G and C. Ambiguous bases such as N are rejected.

## Author
Aditi Gupta



## Public Dataset: TP53 mRNA

- **Organism:** Homo sapiens
- **Gene:** TP53
- **NCBI accession:** AM076972.1
- **Record:** Partial mRNA, mutant form, from the L1236 Hodgkin lymphoma cell line
- **Input file:** `data/tp53.fasta`
- **Output file:** `tp53_results.csv`

### Analysis Results

| Metric | Value |
|---|---:|
| Sequence length | 1032 nucleotides |
| A count | 237 |
| T count | 211 |
| G count | 258 |
| C count | 326 |
| GC content | 56.59% |

### Data Source

https://www.ncbi.nlm.nih.gov/nuccore/AM076972.1

The sequence is a partial mRNA record, not the complete TP53 gene.


