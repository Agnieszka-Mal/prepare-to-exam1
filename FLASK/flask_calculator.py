from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/calculator', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        operation = request.form['operation']
        first_num = int(request.form['first_num'])
        second_num = int(request.form['second_num'])
        if operation == '+':
            result = f"{first_num} + {second_num} = {first_num + second_num}"
            return render_template('form3.html', msg=result)
        elif operation == '-':
            result = f"{first_num} - {second_num} = {first_num - second_num}"
            return render_template('form3.html', msg=result)
        elif operation == '*':
            result = f"{first_num} * {second_num} = {first_num * second_num}"
            return render_template('form3.html', msg=result)
        elif operation == ':':
            try:
                result = f"{first_num} : {second_num} = {first_num / second_num}"
                return render_template('form3.html', msg=result)
            except ZeroDivisionError:
                return "Nie dzielimy przez 0!"
    else:
        return render_template('form3.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)