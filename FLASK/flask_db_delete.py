#TODO delete db whit FLASK
from flask import Flask, request, render_template
from psycopg2 import connect

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

def execute_sql(sql_code, db):
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST, database=db)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute(sql_code)
        results = None
        if cursor.rowcount > 0:
            results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return results
    except:
        print("There is error in execute_sql")


app = Flask(__name__)


@app.route("/product/<int:product_id>")
def run_app(product_id):
    execute_sql(f"DELETE FROM items WHERE id={product_id}", 'exam2')
    return 'Deleted!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)