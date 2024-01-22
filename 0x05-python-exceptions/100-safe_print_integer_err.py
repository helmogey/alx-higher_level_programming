#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        1 + value
        print(value)
        return True
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return False
