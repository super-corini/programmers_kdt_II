from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
import pandas as pd

app = Flask(__name__)
app.config.from_pyfile('config.py')

database = create_engine(app.config['DB_URL'], encoding = 'utf-8')
app.database = database

#app.database.execute(text(
#    """INSERT INTO coffee VALUES(1, 'Espresso', 3000), (2, 'Americano', 4000), (3, 'CafeLatte', 5000)"""
#))

data_lsit = pd.read_sql("SELECT * FROM coffee", con = app.database)
menus = data_lsit.to_dict('records')

@app.route('/')
def hello_flask():
    return "Hello World! " + __name__


# GET /menus | 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    data_lsit = pd.read_sql("SELECT * FROM coffee", con = app.database)
    menus = data_lsit.to_dict('records')
    return jsonify({"menus": menus})


# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus  자원에 추가
    request_data = request.get_json() # {"name": ..., "Price": ...}
    id = len(menus) + 1
    name = request_data['name']
    price = int(request_data['price'])
    new_menu = {
        "id": id,
        "name": name,
        "price": price,
    }
    sql = """INSERT INTO coffee VALUES(id = {}, name = '{}', price = {})""".format(len(menus) + 1, name, price)
    app.database.execute(sql)
    menus.append(new_menu)
    return jsonify(new_menu)


@app.route('/menu/<id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    name = request_data['name']
    price = int(request_data['price'])
    update_menu = {
        "id": id,
        "name": name,
        "price": price,
    }
    menus[int(id)] = update_menu
    sql = """UPDATE coffee SET name = '{}', price = {} WHERE id = {}""".format(name, price, int(id))
    app.database.execute(sql)
    return "Success"


@app.route('/menu/<id>', methods=['DELETE'])
def delete_menu(id):
    menus.remove(menus[int(id)])
    sql = "DELETE FROM coffee WHERE id = '{}'".format(int(id))
    app.database.execute(sql)
    return 'Success'


if __name__ == '__main__':
    app.run()
