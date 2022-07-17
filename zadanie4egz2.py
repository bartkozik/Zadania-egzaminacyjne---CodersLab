from flask import Flask, request, render_template, redirect
from psycopg2 import connect

app = Flask(__name__)

user = "postgres"
password = "coderslab"
host = "localhost"
db = "exam2"

def execute_sql(db, sql_code, params):
    """
    Run given sql code with psycopg2.

    :param str sql_code: sql code to run
    :param str db: name of db,

    :rtype: list
    :return: data from psycobg2 cursor as a list (can be None) if nothing to fetch.
    """
    # Place exercise 2 solution here.
    conn = connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        database=db
    )

    with conn.cursor() as x:
        x.execute(sql_code, params)
        conn.commit()
        try:
            res = x.fetchall()
        except:
            res = None
    return res

form = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Srask</title>
</head>
<body>
<div>
        <form action="/add_product" class="formularz" method="POST">
            <label>Uzupełnij Formularz</label><br>
            <input name="name" type="text" placeholder="nazwa produktu" /><br>
            <input name="description" type="text" placeholder="opis produktu"/><br>
            <input name="price" type="number" placeholder="cena produktu"/><br>
            <button type="submit" name="submit" value="n">Wyślij</button>
        </form>
    </div>
</body>
</html>"""

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'GET':
        return form
    else:
        name = request.form['name']
        desc = request.form['description']
        price = request.form['price']

        try:
            if name and desc and price:
                params = (name, desc, price)
                sql = "insert into Items(name,description, price) values(%s,%s,%s);"
                execute_sql(db, sql, params)
                return 'Product added!'
        except:
            return 'Invalid data!'

app.run(port=60000)