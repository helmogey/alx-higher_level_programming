#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return my_list[x - 1]
    except:
        print()
        return my_list[4]
