#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host='localhost', user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = mydb.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities INNER JOIN states "
             "ON cities.state_id = states.id ORDER BY cities.id")
    cur.execute(query)
    res = cur.fetchall()
    for state in res:
        print(state)
