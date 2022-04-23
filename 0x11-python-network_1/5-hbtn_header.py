#!/usr/bin/python3
"""
given URL as parameter, fetch URL and display value from reponse header
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
