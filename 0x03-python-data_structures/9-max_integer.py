#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        mx = 0
        for lst in my_list:
            if lst > mx:
                mx = lst
        return mx
