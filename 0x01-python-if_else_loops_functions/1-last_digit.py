#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lnumber = number % -10
else:
    lnumber = number % 10

s = ("Last digit of")

if lnumber > 5:
    print(" {} {} is {} and is greater than 5".format(s, number, lnumber))
elif lnumber == 0:
    print("{} {} is {} and is 0".format(s, number, lnumber))
else:
    print("{} {} is {} and is less than 6 and not\
 0".format(s, number, lnumber))
