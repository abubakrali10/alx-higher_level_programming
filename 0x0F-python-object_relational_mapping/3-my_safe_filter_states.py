#!/usr/bin/python3
"""script filters states that is safe from MySQL injections"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = mydb.cursor()
    query = ("SELECT * FROM states" +
             "WHERE states.name LIKE BINARY %s ORDER BY states.id")
    arg = sys.argv[4]
    cur.execute(query, (arg + '%',))
    res = cur.fetchall()
    for state in res:
        print(state)
