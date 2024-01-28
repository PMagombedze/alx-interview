#!/usr/bin/python3


import signal
import sys
import re
from collections import defaultdict


total_size = 0
status_codes = defaultdict(int)


def print_stats(signal, frame):
    """Print statistics when receiving a SIGINT (CTRL+C)"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")
    sys.exit(0)


signal.signal(signal.SIGINT, print_stats)

try:
    for i, line in enumerate(sys.stdin, start=1):
        match = re.search(r'(\d{3}) (\d+)$', line)
        if match:
            status_code, file_size = match.groups()
            total_size += int(file_size)
            status_codes[status_code] += 1

        if i % 10 == 0:
            print_stats(None, None)

except KeyboardInterrupt:
    print_stats(None, None)
