#TODO add to DB with FLASK


from flask import Flask, request, render_template
from psycopg2 import connect, OperationalError

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

def execute_sql(sql_code, db):
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST, database=db)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_code)
        cursor.close()
        cnx.close()
    except Exception as ex:
        print("There is error in execute_sql")
        print(ex)

app = Flask(__name__)


@app.route("/add_product", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        execute_sql(
            "INSERT INTO items(name, description, price) VALUES ('{}','{}','{}')".format(request.form['name'],
                                                                                             request.form['desc'],
                                                                                             request.form['price']),
            "exam2")
        return 'Product added'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
