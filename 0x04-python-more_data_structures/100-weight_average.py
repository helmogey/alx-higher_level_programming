#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        a = sum([tup[0] * tup[1] for tup in my_list])
        b = sum([tup[1] for tup in my_list])
        return a/b
    else:
        return 0
