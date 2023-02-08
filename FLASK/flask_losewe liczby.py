import random

from flask import Flask
from random import shuffle

app = Flask(__name__)

#@app.route("/lotek")
#def lotek():
    #list_num = [i for i in range(1, 50)]
    #shuffle(list_num)
    #x = list_num[:6]
    #result = ", ".join([str(r) for r in x])
    #return f"Wylosowane liczby to {result}"

@app.route("/losuj")
def drawing_num():
    num_list = []
    for i in range(3):
        x = random.randint(1, 100)
        num_list.append(x)
    result = ", ".join([str(r) for r in num_list])
    return f"Wylosowane liczby to {result}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)