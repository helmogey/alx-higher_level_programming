#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    out = ()
    for i in range(2 - len(tuple_a)):
        tuple_a += (0, )
    for i in range(2 - len(tuple_b)):
        tuple_b += (0, )
    for i in range(2):
        out += (tuple_a[i] + tuple_b[i], )
    return out
