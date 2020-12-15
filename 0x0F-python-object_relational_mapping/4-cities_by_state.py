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
    query = "SELECT cities.id, cities.name, states.name\
    FROM cities\
    LEFT JOIN states\
    ON cities.state_id = states.id"

    con = MySQLdb.connect(**credentials)
    with con.cursor() as cur:
        cur.execute(query)
        results = cur.fetchall()
        for line in results:
            print(line)

    con.close()
