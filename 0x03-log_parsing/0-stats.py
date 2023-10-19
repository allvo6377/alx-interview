#!/usr/bin/python3
import sys

def compute_metrics():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    for i, line in enumerate(sys.stdin):
        if i % 10 == 0 and i != 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] != 0:
                    print(f"{code}: {status_codes[code]}")
            print()

        try:
            _, _, _, status_code, file_size = line.split()
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print(f"{code}: {status_codes[code]}")

