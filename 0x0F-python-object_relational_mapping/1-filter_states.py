#!/usr/bin/python3
"""lists all states with name starting with N from the db hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE states.name like BINARY 'N%' ORDER BY states.id")
    res = cur.fetchall()
    for state in res:
        print(state)
