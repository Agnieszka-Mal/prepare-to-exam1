from flask import Flask, request, render_template

movies = {
    "favourite": ["A New Hope", "Empire Strikes Back", "Return of the Jedi",
                  "The Force Awakens", "Jaws", "Predator", "Mad Max",
                  "Back to the Future", "2001: A Space Odyssey", "Robocop",
                  "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                  "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

    "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
              "Alien Resurrection", "Twilight"]
}

app = Flask(__name__)

@app.route('/movies', methods=['GET', 'POST'])
def my_movies():
    if request.method == 'POST':
        user_title = request.form['user_title']
        if user_title in movies['favourite']:
            result = "favourite!"
            return render_template('form1.html', msg=result)
        elif user_title in movies['hated']:
            result = 'hated'
            return render_template('form1.html', msg=result)
        else:
            result = 'no such movie!'
            return render_template('form1.html', msg=result)
    else:
        return render_template('form1.html')


if __name__ == "__main__":
    app.run(debug=True)

