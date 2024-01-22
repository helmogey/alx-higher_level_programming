#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    out = {}
    for key in a_dictionary:
        out[key] = a_dictionary[key] * 2
    return out
