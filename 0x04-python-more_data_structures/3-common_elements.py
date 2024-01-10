#!/usr/bin/python3
def common_elements(set_1, set_2):
    out = []
    if set_1 and set_2:
        for lst in set_1:
            if lst in set_2:
                out.append(lst)
        return out
