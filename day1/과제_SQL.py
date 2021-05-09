from flask import Flask, jsonify, request
import sqlite3 as sql

app = Flask(__name__)

'''
DATABASE = sqlite3.connect('sqlite.db')
cur = DATABASE.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS menu(id INTEGER, name STRING, price INTEGER)")
cur.executemany(
    "INSERT INTO menu VALUES(?, ?, ?)",
    [
        (1, "Espresso", 3800),
        (2, "Americano", 4100),
        (3, "CafeLatte", 4600)
    ]
)
DATABASE.commit()
# DATABASE.close()
'''

# main
@app.route('/')
def homepage():
    return "Week 4 / Day 1 과제인 Flask CRUD + SQL 구현입니다."


# READ
@app.route('/menu')
def get_menu():
    con = sql.connect('sqlite.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM menu')
    rows = cur.fetchall()
    con.commit()
    con.close()
    return jsonify({'menu': rows})


# CREATE
@app.route('/menu', methods=['POST'])
def post_menu():
    con = sql.connect('sqlite.db')
    cur = con.cursor()
    cur.execute('SELECT COUNT(0) FROM menu')
    request_json = request.get_json()
    id, name, price = cur.fetchone()[0] + 1, request_json['name'], request_json['price']
    cur.execute('INSERT INTO menu (id, name, price) VALUES (?, ?, ?)', (id, name, price))
    cur.execute('SELECT * FROM menu')
    rows = cur.fetchall()
    con.commit()
    con.close()
    return jsonify({'menu': rows})


# UPDATE
@app.route('/menu/<int:id>', methods=['PUT'])
def put_menu(id):
    con = sql.connect('sqlite.db')
    cur = con.cursor()
    request_json = request.get_json()
    name, price = request_json['name'], request_json['price']
    cur.execute('UPDATE menu SET name = ?, price = ? WHERE id = ?', (name, price, id))
    cur.execute('SELECT * FROM menu')
    rows = cur.fetchall()
    con.commit()
    con.close()
    return jsonify({'menu': rows})


# DELETE
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    con = sql.connect('sqlite.db')
    cur = con.cursor()
    cur.execute(f'DELETE FROM menu WHERE id = {id}')
    cur.execute('SELECT * FROM menu')
    rows = cur.fetchall()
    con.commit()
    con.close()
    return jsonify({'menu': rows})


if __name__ == '__main__':
    app.run()
