#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
