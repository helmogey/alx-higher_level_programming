#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    out = []
    for lst in my_list:
        if lst % 2 == 0:
            out.append(True)
        else:
            out.append(False)
    return out
