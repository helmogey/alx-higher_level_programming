#!/usr/bin/python3
def max_integer(my_list=[]):
    mx = 0
    if len(my_list) > 0:
        for lst in my_list:
            if lst > mx:
                mx = lst
        return mx
    else:
        return None