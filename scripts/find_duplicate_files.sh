#!/bin/zsh

dir=$1

if [[ -z "$dir" ]]; then
    echo "Please provide a directory."
    exit 1
fi

if [[ ! -d "$dir" ]]; then
    echo "The provided path is not a directory."
    exit 1
fi

echo "Calculating hashes..."

# Create a temporary file to store the hashes
temp_file=$(mktemp)
echo "Temporary file: $temp_file"

find "$dir" -type f -exec sh -c 'echo "$(shasum -a 256 "{}" | cut -f1 -d" ") {}"' \; > "$temp_file"

echo "Identifying duplicates..."

# Sort the file and identify duplicates
duplicates=$(sort "$temp_file" | uniq -d)

# Count the number of duplicate hashes (i.e., the number of groups of duplicate files)
num_duplicates=$(echo "$duplicates" | cut -f1 -d" " | uniq | wc -l)

echo "Number of duplicate files: $num_duplicates"

echo "Listing duplicate files:"

# Print the file names of the duplicates
echo "$duplicates" | cut -f2- -d" "

# Remove the temporary file
rm "$temp_file"

exit 0
