#!/usr/bin/python3
def safe_print_integer(value):
    while value != str(value):
        try:
            print("{}".format(value))
            return True
        except ValueError:
            return False
