#!/usr/bin/python3

"""
Takes in URL, sends request and displays value of the var
"""

import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
