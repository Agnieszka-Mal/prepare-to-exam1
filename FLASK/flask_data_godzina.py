from flask import Flask

app = Flask(__name__)

@app.route("/czas")
def time():
    import datetime
    time = datetime.datetime.now()
    time_2 = time.strftime("%H:%M:%S")
    return f"{time_2}"

@app.route("/czas2")
def date_akt():
    import datetime
    time = datetime.datetime.now()
    time_2 = time.strftime('%d %B %Y')
    return f"{time_2}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)