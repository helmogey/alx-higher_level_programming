#!/usr/bin/python3
def search_replace(my_list, search, replace):
    out = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            out.append(replace)
        else:
            out.append(my_list[i])
    return out
