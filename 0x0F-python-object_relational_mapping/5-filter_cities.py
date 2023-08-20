#!/usr/bin/python3
"""script that lists all cities of a given state"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = mydb.cursor()
    query = ("SELECT cities.id, cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC")
    cur.execute(query, (sys.argv[4],))
    res = cur.fetchall()
    if res is not None:
        print(", ".join([row[1] for row in res]))
