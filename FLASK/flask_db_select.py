from flask import Flask, request, render_template
from psycopg2 import connect, OperationalError


app = Flask(__name__)

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
DB = "exam2"



def select_from_db(cursor, items_id):
    sql = "SELECT * FROM items WHERE id=%s"
    values = items_id
    cursor.execute(sql, values)



@app.route("/product", methods=['GET', 'POST'])
def app_run():
    if request.method == 'GET':
        return render_template('form5.html')
    if request.method == 'POST':
        items_id = request.form['items_id']
        try:
            cnx = connect(user=USER, password=PASSWORD, host=HOST, database=DB)
            cnx.autocommit = True
            cursor = cnx.cursor()
            select_from_db(cursor, items_id)
            output = "<table>"
            for res in cursor:
                output += "<tr><td>{}</td></tr>".format(res)
            output += "</table>"
            cnx.close()
            return output
        except OperationalError as ex:
            print("There is error in execute_sql")
            print(ex)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)