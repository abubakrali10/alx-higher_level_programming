#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    res = cur.fetchall()
    for state in res:
        print(state)
