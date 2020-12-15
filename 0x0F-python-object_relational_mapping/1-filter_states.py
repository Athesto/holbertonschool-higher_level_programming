#!/usr/bin/python3
"""task from holberton"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    credentials = {
        "host": "localhost",
        "port": 3306,
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3],
    }

    connection = MySQLdb.connect(**credentials)
    query = "SELECT * FROM states WHERE name like 'n%' ORDER BY id ASC;"

    with connection.cursor() as cursor:
        cursor.execute(query)
        array = cursor.fetchall()
        for data in array:
            print(data)

    connection.close()
