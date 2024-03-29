#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    total_res = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            total_res.append(res)
    return total_res
