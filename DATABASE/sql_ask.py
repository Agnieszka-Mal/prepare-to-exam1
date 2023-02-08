sql_wyświetlenie = "SELECT * FROM Items WHERE price > 13;"

sql_dodanie = "INSERT INTO Orders(description) VALUES ('Przykładowy opis');"

sql_usunięcie ="DELETE FROM Users WHERE id=7;"

sql_4 = "SELECT Users.name AS user_name, Users.id AS user_id, Messages.message AS u_message FROM Users JOIN Messages on Users.id=Messages.user_id"
# Wybranie wszystkich użytkowników z tabeli Users, którzy mają przypisaną jakąś wiadomość w tabeli Messages:) kosmos:)

sql_5 = "ALTER TABLE Messages ADD data_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"

sql_zmiana_danych = "UPDATE Users SET name='Aga' WHERE id=2;"

sql_usuwanie = "DELETE FROM table_name WHERE same_column=some_values"

sql_dodawanie_nowej_kolumny = "ALTER TABLE table_name ADD column_name datatype"

sql_ususwanie_kolumny = "ALTER TABLE table_name DROP COLUMN column_name"

sql_usuwanie_tabeli_bazy = DROP TABLE / DATABASE

sgl_join_1_do_wielu = "SELECT * FROM Users JOIN Messages ON users.id = messages.user_id;"

sql_join_wiele do wielu = "SELECT * FROM orders JOIN ItemsOrders ON orders.id=ItemsOrders.order_id JOIN Items ON Items.id=ItemsOrders.item_id;"










