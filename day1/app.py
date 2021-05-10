from flask import Flask, request, Response
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
db_path = "./day1.sqlite"


def connect_db(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(e)

    return conn


@app.route('/')
def hello_code():
    return "Hello World!"


@app.route('/menus')
def menu_show_all():
    ret = ''
    conn = connect_db(db_path)
    cursor = conn.cursor()
    for r in cursor.execute("SELECT * FROM menus ORDER BY id ASC;"):
        ret += r
    conn.close()
    return ret


@app.route('/menu', methods=["POST"])
def menu_insert():
    ret = ''
    if request.is_json:
        menu_data = request.get_json()
        conn = connect_db(db_path)
        if not conn:
            return Response(status=500)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO menus (name, price)"
                           " VALUES ('{name}', {price});".format(**menu_data))
            conn.commit()
        except Error as e:
            return Response(status=501)
        finally:
            conn.close()
    else:
        return Response(status=501)
    return ret


@app.route('/menu/<int:menu_id>', methods=["PUT"])
def menu_update(menu_id):
    ret = ''
    if request.is_json:
        menu_data = request.get_json()
        conn = connect_db(db_path)
        if not conn:
            return Response(status=500)
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id FROM menus WHERE id={id}".format(id=menu_id))
            if not cursor.fetchone():
                return Response(status=204)
        except Error as e:
            conn.close()
            return Response(status=501)
        try:
            cursor.execute("UPDATE menus SET name = '{name}',"
                           "                 price = {price}"
                           " WHERE id = {id};".format(**menu_data, id=menu_id))
            conn.commit()
        except Error as e:
            conn.close()
            return Response(status=501)
        conn.close()
    else:
        return Response(status=501)
    return ret


@app.route('/menu/<menu_id>', methods=["DELETE"])
def menu_delete(menu_id):
    conn = connect_db(db_path)
    if not conn:
        return Response(status=500)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id FROM menus WHERE id={id}".format(id=menu_id))
        if not cursor.fetchone():
            return Response(status=204)
    except Error as e:
        return Response(status=501)
    try:
        cursor.execute("DELETE FROM menus WHERE id={id}".format(id=menu_id))
        conn.commit()
    except Error as e:
        conn.close()
        return Response(status=501)
    conn.close()
    return Response(status=200)


if __name__ == "__main__":
    app.run()
