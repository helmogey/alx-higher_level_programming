#!/usr/bin/python3
def magic_calculation(a, b):
    """
    This function calculates a^i / b for i in range(1, 3).

    Args:
        a: A positive integer.
        b: A positive integer.

    Returns:
        The sum of a^i / b for i in range(1, 3).
    """
    result = 0
    try:
        for i in range(1, 3):
            if i > a:
                raise Exception('Too far')
            result += a ** i / b
    except Exception as e:
        print(e)
    result += b + a
    return result
