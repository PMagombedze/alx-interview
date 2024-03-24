#!/usr/bin/python3


"""
log parsing
"""


import sys

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        count = status_counts[status_code]
        print(f"{status_code}: {count}")

def process_logs():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) != 7 or parts[2] != 'GET' or not parts[3].startswith('/projects/260'):
                continue

            try:
                file_size = int(parts[6])
                status_code = int(parts[5])
            except ValueError:
                continue

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

process_logs()
