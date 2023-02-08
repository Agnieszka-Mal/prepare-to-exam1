from flask import Flask, request, render_template
from random import randint

rnd = randint(1, 10)

app = Flask(__name__)

@app.route('/guess', methods=['GET', 'POST'])
def guess_the_number():
    if request.method == 'POST':
        user_num = request.form['user_num']
        if int(user_num) > rnd:
            result = 'Too big!'
            return render_template('form4.html', msg=result)
        if int(user_num) < rnd:
            result = 'Too small!'
            return render_template('form5.html', msg=result)
        else:
            result = 'Zgadłeś!!!:)'
            return render_template('form4.html', msg=result)
    else:
        return render_template('form4.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)