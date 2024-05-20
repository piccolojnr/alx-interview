#!/usr/bin/python3
"""
Reads from stdin and computes metrics
"""
import sys
import signal
import re

total_size = 0
line_count = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

log_pattern = re.compile(
    r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)


def print_stats():
    """
    Print the accumulated file size and status code count
    """
    global total_size, status_code_count
    print(f"File size: {total_size}")
    for code in sorted(status_code_count):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def signal_handler(sig, frame):
    """
    Handle the SIGINT signal
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            ip, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    print(f"Error: {e}")

finally:
    print_stats()
