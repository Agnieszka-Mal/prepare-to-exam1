from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateTable

USER = "postgres"
HOST = "127.0.0.1"
PASSWORD = "coderslab"
DB = "exam2"

CREATE_TABLE_USER = " CREATE TABLE Users(" \
                    "id serial not null PRIMARY KEY," \
                    "name varchar(60)," \
                    "email varchar(60) UNIQUE," \
                    "password varchar(60));"

CREATE_TABLE_MESSAGES = "CREATE TABLE Messages(" \
                        "id serial not null PRIMARY KEY," \
                        "user_id int," \
                        "message text," \
                        "FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE);"

CREATE_TABLE_ITEMS = " CREATE TABLE Items(" \
                     "id serial not null PRIMARY KEY," \
                     "name varchar(40)," \
                     "description text," \
                     "price decimal(7,2));"

CREATE_TABLE_ORDERS = "CREATE TABLE Orders(" \
                      "id serial not null PRIMARY KEY," \
                      "description text);"

CREATE_TABLE_ITEMSORDERS = "CREATE TABLE ItemsOrders(" \
                           "id serial PRIMARY KEY," \
                           "item_id serial REFERENCES Items(id) ON DELETE CASCADE," \
                           "order_id serial REFERENCES Orders(id) ON DELETE CASCADE);"

try:
    cnx = connect(database=DB, user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_TABLE_MESSAGES)
        print("Table Items created")
    except DuplicateTable as e:
        print("Table Items exist", e)
    cnx.close()
    cursor.close()
except OperationalError as e:
    print("Connect error", e)