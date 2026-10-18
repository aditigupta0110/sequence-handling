
import csv
import sys
from pathlib import Path


def analyze_fasta(file_path):
    results = []
    header = None
    sequence_parts = []

    def save_record():
        if header is None:
            return

        sequence = "".join(sequence_parts).upper()
        sequence = "".join(sequence.split())

        invalid = set(sequence) - set("ATGC")
        if invalid:
            raise ValueError(
                f"Invalid DNA symbols in {header}: {sorted(invalid)}"
            )

        counts = {base: sequence.count(base) for base in "ATGC"}
        length = len(sequence)
        gc = (
            (counts["G"] + counts["C"]) / length * 100
            if length else 0.0
        )

        results.append({
            "sequence_id": header,
            "length": length,
            "A": counts["A"],
            "T": counts["T"],
            "G": counts["G"],
            "C": counts["C"],
            "GC_content_percent": round(gc, 2),
        })

    with open(file_path, encoding="utf-8") as fasta:
        for line in fasta:
            line = line.strip()

            if not line or line.startswith(";"):
                continue

            if line.startswith(">"):
                save_record()
                header = line[1:].strip()
                sequence_parts = []

                if not header:
                    raise ValueError("Empty FASTA header")
            else:
                if header is None:
                    raise ValueError(
                        "Sequence found before FASTA header"
                    )
                sequence_parts.append(line)

    save_record()

    if not results:
        raise ValueError("No FASTA sequences found")

    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: python sequence_analysis.py input.fasta")
        sys.exit(1)

    input_file = Path(sys.argv[1])

    try:
        results = analyze_fasta(input_file)

        with open("results.csv", "w", newline="",
                  encoding="utf-8") as output:
            writer = csv.DictWriter(
                output, fieldnames=results[0].keys()
            )
            writer.writeheader()
            writer.writerows(results)

        for result in results:
            print(result)

        print("\nResults saved to results.csv")

    except (OSError, UnicodeError, ValueError) as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
