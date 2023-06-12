import os
import argparse
from collections import defaultdict


def count_file_extensions(directory):
    extension_counts = defaultdict(int)
    total_files = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            extension = extension.lower()
            if extension:
                extension_counts[extension[1:]] += 1  # [1:] to remove leading '.'
            else:
                extension_counts["No extension"] += 1
            total_files += 1

    return extension_counts, total_files


def write_counts_to_file(counts, total_files, file_path):
    with open(file_path, "w") as f:
        f.write(f"Total files: {total_files}\n")
        for ext, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
            f.write(f"{ext}: {count}\n")


def main():
    parser = argparse.ArgumentParser(description="Count file extensions in a directory.")
    parser.add_argument("-i", "--input", required=True, help="Input directory to scan.")
    parser.add_argument("-o", "--output", required=True, help="Output file to write results to.")
    args = parser.parse_args()

    counts, total_files = count_file_extensions(args.input)
    write_counts_to_file(counts, total_files, args.output)


if __name__ == "__main__":
    main()
