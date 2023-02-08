from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

USER = "postgres"
HOST = "127.0.0.1"
PASSWORD = "coderslab"

CREATE_DATABASE = "CREATE DATABASE exam2"

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DATABASE)
        print("Database exam2 created")
    except DuplicateDatabase as e:
        print("Database exist", e)
    cnx.close()
    cursor.close()
except OperationalError as e:
    print("Connection error!", e)



