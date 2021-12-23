#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1 '''turns negative number to positive'''
    lnumber = number % 10 '''get last number'''
    print("{}".format(lnumber), end='')
    return lnumber
