#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb as MC
import sys

if __name__ == "__main__":
    conn = MC.connect(port=3306, user=sys.argv[1],
                      password=sys.argv[2], db=sys.argv[3])
    with conn.cursor() as cursor:
        cursor.execute("select * from states order by states.id")
        my_list = cursor.fetchall()
        for x in my_list:
            if x[1][0] == "N":
                print(x)
    conn.close()