
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

