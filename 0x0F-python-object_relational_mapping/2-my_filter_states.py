#!/usr/bin/python3
"""task from holberton"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    credentials = {
        "host": "localhost",
        "port": 3306,
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3]
    }

    con = MySQLdb.connect(**credentials)
    query = "SELECT * FROM states WHERE name = '{}'".format(argv[4])

    with con.cursor() as cur:
        cur.execute(query)
        results = cur.fetchall()

        for line in results:
            print(line)

    con.close()
