from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

USER = "postgres"
HOST = "127.0.0.1"
PASSWORD = "coderslab"
DB = "exam2"

sql = "INSERT INTO items(name, description, price) VALUES (%s, %s, %s);"
values = ('dress', 'yellow', 179.14)

try:
    cnx = connect(database=DB, user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(sql, values)
        print("Added")
    except ValueError as e:
        print("Invalid data!", e)
    cnx.close()
    cursor.close()
except OperationalError as e:
    print("Connect error", e)