#!/usr/bin/python3
"""
    task 0 connect, and query with MySQLdb
    1) import libraries
    2) dictonary with credentials and query
    3) connect to database using credentials
    4) create a cursor https://www.python.org/dev/peps/pep-0249/#id7
        A cursor is like a pointer to a database
        A cursor is an iterator
            https://en.wikipedia.org/wiki/Cursor_(databases)
        4.1) send query through the pointer
        4.2) fetch all the results and save it
        4.3) print result saved
    5) close connection to database
"""

if __name__ == "__main__":
    # 1)
    import MySQLdb                  # connection mysql
    import sys                      # argv

    # 2)
    credentials = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "passwd": sys.argv[2],
        "db": sys.argv[3]
    }
    query = "SELECT * from states ORDER BY id ASC"

    # 3)
    db = MySQLdb.connect(**credentials)

    # 4)
    with db.cursor() as cur:            # create pointer to database
        cur.execute(query)              # pointer excecute query
        array = cur.fetchall()          # get answer in an array
        for data in array:
            print(data)

    # 5)
    db.close()                          # delete conection to db
