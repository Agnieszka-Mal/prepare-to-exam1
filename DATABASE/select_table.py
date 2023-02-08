from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

USER = "postgres"
HOST = "127.0.0.1"
PASSWORD = "coderslab"

SQL_1 = "SELECT * FROM Users;"

try:
    cnx = connect(database="exam2", user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    cursor.execute(SQL_1)
    for row in cursor:
        print(row)
    cnx.close()
    cursor.close()
except OperationalError as e:
    print("Connect error", e)