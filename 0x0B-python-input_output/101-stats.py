#!/usr/bin/python3
""" reads stdin line by line and computes metrics"""
import sys


total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_statistics():
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

try:
    for line in sys.stdin:
        try:
            ip, _, _, status_code, file_size = line.split(" ", 4)  # Split into fields
            status_code = int(status_code)
            file_size = int(file_size)

            total_file_size += file_size
            status_code_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:  # Print stats every 10 lines
                print_statistics()
        except ValueError:
            pass  # Ignore invalid lines

except KeyboardInterrupt:
    print_statistics()  # Print stats on CTRL+C


