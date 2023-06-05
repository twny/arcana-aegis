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

find "$dir" -type f | awk -F. '/\./ {print $NF}' | tr '[:upper:]' '[:lower:]' | sort | uniq -c

exit 0
