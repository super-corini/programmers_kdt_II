# bonus 2
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("menu.db")

db = conn.cursor()
db.execute("CREATE TABLE if not exists menu (id integer, name text, price integer)")

conn.commit()
conn.close()


@app.route('/')
def hello_flask():
    return "Hello world!"


# GET /menu : 자료를 가지고 온다
@app.route('/menu')
def get_menu():
    menu = []
    conn = sqlite3.connect("menu.db")
    db = conn.cursor()
    for row in db.execute("SELECT * from menu"):
        dic = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
        }
        menu.append(dic)
    conn.close()
    return jsonify({"menu": menu})

# POST /menu : 자료를 자원에 추가한다.


@app.route("/menu", methods=["POST"])
def create_menu():
    conn = sqlite3.connect("menu.db")
    db = conn.cursor()
    # 전달받은 자료를 menu 자원에 추가
    request_data = request.get_json()
    sql_read = db.execute("SELECT id FROM menu ORDER BY id desc LIMIT 1")
    element = sql_read.fetchone()
    if element:
        id = element[0] + 1
    else:
        id = 1
    name = request_data["name"]
    price = request_data["price"]
    db.execute("INSERT INTO menu(id, name, price) VALUES (?, ?, ?)",
               (id, name, price,))
    conn.commit()
    conn.close()
    new_menu = {
        "id": id,
        "name": name,
        "price": price,
    }
    return jsonify(new_menu)

# PUT /menu/<id> : id에 해당하는 데이터를 갱신한다.


@app.route("/menu/<int:id>", methods=["PUT"])
def update_menu(id):
    request_data = request.get_json()
    conn = sqlite3.connect("menu.db")
    db = conn.cursor()
    db.execute("UPDATE menu set name = ?, price = ? where id = ?",
               (request_data["name"], request_data["price"], id, ))
    now_menu = {
        "id": id,
        "name": request_data["name"],
        "price": request_data["price"],
    }
    conn.commit()
    conn.close()
    return jsonify(now_menu)

# DELETE /menu/<id> : id에 해당하는 데이터를 삭제한다.


@app.route("/menu/<int:id>", methods=["DELETE"])
def delete_menu(id):
    conn = sqlite3.connect("menu.db")
    db = conn.cursor()
    sql_read = db.execute("SELECT * FROM menu WHERE id = ?", (id,))
    data = sql_read.fetchone()
    delete_menu = {
        "id": id,
        "name": data[1],
        "price": data[2],
    }
    db.execute("DELETE FROM menu WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return delete_menu


if __name__ == '__main__':
    app.run()


# day 1 + bonus 1
# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# menu = [
#     {"id": 1, "name": "Espresso", "price": 3800},
#     {"id": 2, "name": "Americano", "price": 4100},
#     {"id": 3, "name": "Latte", "price": 4600},
# ]

# @app.route('/')
# def hello_flask():
#     return "Hello world!"


# # GET /menu : 자료를 가지고 온다
# @app.route('/menu')
# def get_menu():
#     return jsonify({"menu": menu})

# # POST /menu : 자료를 자원에 추가한다.


# @app.route("/menu", methods=["POST"])
# def create_menu():
#     # 전달받은 자료를 menu 자원에 추가
#     request_data = request.get_json()
#     new_menu = {
#         "id": menu[-1]["id"] + 1,
#         "name": request_data["name"],
#         "price": request_data["price"]
#     }
#     menu.append(new_menu)
#     return jsonify(new_menu)

# # PUT /menu/<id> : id에 해당하는 데이터를 갱신한다.


# @app.route("/menu/<int:id>", methods=["PUT"])
# def update_menu(id):
#     request_data = request.get_json()
#     element = menu[id - 1]
#     element["name"] = request_data["name"]
#     element["price"] = request_data["price"]
#     return jsonify(element)

# # DELETE /menu/<id> : id에 해당하는 데이터를 삭제한다.


# @app.route("/menu/<int:id>", methods=["DELETE"])
# def delete_menu(id):
#     data = menu[id - 1]
#     del menu[id - 1]
#     return data


# if __name__ == '__main__':
#     app.run()
