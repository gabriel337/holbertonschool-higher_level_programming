#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]
    state_search = argv[4]

    connect = MySQLdb.connect(host="localhost", port=3306, user=user,
                              passwd=password,
                              db=database)

    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM states WHERE BINARY name='{}'
                    ORDER BY id""".format(state_search))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connect.close()
