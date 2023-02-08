from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

USER = "postgres"
HOST = "127.0.0.1"
PASSWORD = "coderslab"

SQL_1 = "INSERT INTO items(name, description, price) VALUES ('dres', 'cotton', 159.14);"

try:
    cnx = connect(database="exam2", user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(SQL_1)
        print("Added")
    except DuplicateDatabase as e:
        print("Is exist", e)
    cnx.close()
    cursor.close()
except OperationalError as e:
    print("Connect error", e)