#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         state_search=argv[4])

    # create cursor to exec queries using SQL; match arg given
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE BINARY name='{}'
                    ORDER BY id""".format(state_search))
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
