#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    lnumber = number % 10
    print("{}".format(lnumber), end='')
    return lnumber
