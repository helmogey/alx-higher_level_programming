#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0 # initialize result to 0
    for i in range(1, 3): # loop over the range from 1 to 3
        try:
            if i > a: # if i is greater than a
                raise Exception('Too far') # raise an exception with the message 'Too far'
            else:
                result += a ** b / i # add a to the power of b divided by i to the result
        except: # in case of an exception
            result += a + b # add a and b to the result
            break # break the loop
    return result # return the result
