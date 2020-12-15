#!/usr/bin/python3
"""task from holberton"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    credentials = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3]
    }
    word = sys.argv[4]

    if word.isalpha():
        query = "select * from states where binary name = '{}'".format(word)
        con = MySQLdb.connect(**credentials)
        with con.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            for line in results:
                print(line)
        con.close()
