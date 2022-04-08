#!/usr/bin/python3
"""
returns matching states, safe from injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to databse
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # create cursor to exec queries using SQL; match arg given
    cursor = db.cursor()
    cmd = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(cmd, (argv[4],))

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
