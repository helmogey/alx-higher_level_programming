#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if int(str(number)[-1]) > 5:
    print("Last digit of " + str(number) + " is " + str(number)[-1] + " and is greater than 5")
if int(str(number)[-1]) == 0:
    print("Last digit of " + str(number) + " is " + str(number)[-1] + " and is 0")
if int(str(number)[-1]) < 6:
    print("Last digit of " + str(number) + " is " + str(number)[-1] + " and is less than 6 and not 0")
    