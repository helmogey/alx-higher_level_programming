#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        1 + value
        print(value)
        return True
    except Exception as e:
        print(e)
        return False
