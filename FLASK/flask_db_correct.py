#TODO add to DB with FLASK


from flask import Flask, request, render_template
from psycopg2 import connect, OperationalError


app = Flask(__name__)

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
DB = "exam2"



def save_to_db(cursor, name, description, price):
    sql = "INSERT INTO items(name, description, price) VALUES (%s, %s, %s)"
    values = (name, description, price)
    cursor.execute(sql, values)



@app.route("/add_product", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['desc']
        price = request.form['price']

        try:
            cnx = connect(user=USER, password=PASSWORD, host=HOST, database=DB)
            cnx.autocommit = True
            cursor = cnx.cursor()
            save_to_db(cursor, name, description, price)
            cnx.close()
            return "Product added!"
        except OperationalError as ex:
            print("There is error in execute_sql")
            print(ex)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)