#!/usr/bin/python3
def no_c(my_string):
    name = "".join(a for a in my_string if a != 'c' if a != 'C')
    return name
