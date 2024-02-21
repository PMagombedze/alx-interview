#!/usr/bin/python3


"""
log parsing
"""


import sys


def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None


def main():
    total_file_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip_address, status_code, file_size = parse_line(line)
            if ip_address is None:
                continue

            total_file_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            if i % 10 == 0:
                print(f"File size: {total_file_size}")
                for code in sorted(status_counts.keys()):
                    if status_counts[code] > 0:
                        print(f"{code}: {status_counts[code]}")
                print()

    except KeyboardInterrupt:
        print(f"File size: {total_file_size}")
        for code in sorted(status_counts.keys()):
            if status_counts[code] > 0:
                print(f"{code}: {status_counts[code]}")


if __name__ == "__main__":
    main()
