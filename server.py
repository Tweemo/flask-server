'''
Flask Server
'''

from flask import Flask, request
from flask_cors import CORS
import psycopg2
from dotenv import dotenv_values

app = Flask(__name__)
CORS(app)
config = dotenv_values(".env")
SQL_URI = config["POSTGRESQL_URI"]

connection = psycopg2.connect(SQL_URI)
try:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
        'CREATE TABLE pantry (food TEXT, brand TEXT, quantity TEXT, expiry TEXT, date_added TEXT)'
                )
except psycopg2.errors.DuplicateTable:
    pass

@app.route("/api", methods=["GET", "POST"])
def add_food():
    '''Returns a list of pantry items'''
    if request.method == "POST":
        food = request.json['Food']
        brand = request.json['Brand']
        quantity = request.json['Quantity']
        expiry = request.json['Expiry']
        date_added = request.json['Date_Added']
        with connection:
            with connection.cursor() as cursor1:
                cursor1.execute(
                    'INSERT INTO pantry VALUES (%s, %s, %s, %s, %s)',
                    (food, brand, quantity, expiry, date_added)
                    )
                connection.commit()
    return 'Item Added'

@app.route("/pantry")
def show_pantry():
    '''Returns a list of pantry items'''
    with connection:
        with connection.cursor() as cursor2:
            cursor2.execute('SELECT * FROM pantry;')
            pantry = cursor2.fetchall()
            full_pantry = []
            for item in pantry:
                single_item = {
                    "food": item[0],
                    "brand": item[1],
                    "quantity": item[2],
                    "expiry": item[3],
                    "date_added": item[4],
                }
                full_pantry.append(single_item)
    return {
        "pantry": full_pantry
    }

if __name__ == '__main__':
    app.run(debug=True)
