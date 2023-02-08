from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_surname = request.form['user_surname']
        result = f"Hello {user_name} {user_surname}!!!:)"
        return render_template('form2.html', msg=result)
    else:
        return render_template('form2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)