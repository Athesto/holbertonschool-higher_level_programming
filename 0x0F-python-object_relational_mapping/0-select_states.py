#!/usr/bin/python3
"""task from holberton"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    data = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3]
    }
    query = "SELECT * from states ORDER BY id ASC"

    db = MySQLdb.connect(
        user=data["user"],
        host=data["host"],
        port=data["port"],
        passwd=data["passwd"],
        db=data["db"],
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute(query)
    array = cur.fetchall()

    for data in array:
        print(data)
    cur.close()
    db.close()
