#!/usr/bin/python3
def add_integer(a, b=98):
    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
