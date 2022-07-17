from flask import Flask, request, render_template, redirect

app = Flask(__name__)

form_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Srask</title>
</head>
<body>
<div>
        <form action="/movies" class="formularz" method="POST">
            <label>Wpisz N</label><br>
            <input name="title" type="text"/><br>
            <button type="submit" name="submit" value="n">Wyślij</button>
        </form>
    </div>
</body>
</html>'''

movies = {
    "favourite": ["A New Hope", "Empire Strikes Back", "Return of the Jedi",
                  "The Force Awakens", "Jaws", "Predator", "Mad Max",
                  "Back to the Future", "2001: A Space Odyssey", "Robocop",
                  "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                  "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

    "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
              "Alien Resurrection", "Twilight"]}

@app.route('/movies', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        return form_html
    else:
        # new_list = []
        title = request.form['title']
        # new_list.append(title)
        # for movie in new_list:
        #     if movie in movies["favourite"]:
        #         return "Movie in favourite"
        #     elif movie in movies["hated"]:
        #         return "hated"
        #     else:
        #         return "no such movie"
        if title in movies["favourite"]:
            return "Movie in favourite"
        elif title in movies["hated"]:
            return "hated"
        else:
            return "no such movie"


app.run(port=11000)