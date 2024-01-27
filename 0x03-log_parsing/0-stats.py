#!/usr/bin/python3

"""
log parsing
"""


import sys
import signal
import re


count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

log_ = re.compile(r'(\S+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')


def print_stats():
    """printing stats"""
    global count, status_codes
    print(f"Total file size: {count}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def handle_sigint(sig, frame):
    """handler"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_sigint)

try:
    for line in sys.stdin:
        match = log_.match(line)
        if match:
            count += int(match.group(4))
            status_codes[int(match.group(3))] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    pass
