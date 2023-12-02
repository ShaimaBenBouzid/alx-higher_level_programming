#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -(lastdigit)
the string = "last digit of {} is {}".format(number, lastdigit)
if lastdigit > 5:
    print(f"{thestring} and is greater than 5")
