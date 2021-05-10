from flask import Flask, jsonify, request
import pymysql

# DB 연동하기
db = pymysql.connect(host="localhost", port=3306, user="root", password="Leedahye97!", db="menus")
curs = db.cursor(pymysql.cursors.DictCursor)

app = Flask(__name__)

# # 아래 데이터는 DB에 저장되어있다.
# menus = [{"id": 1, "name": "Espresso", "price": 3800},
#          {"id": 2, "name": "Americano", "price": 4100},
#          {"id": 3, "name": "CafeLatte", "price": 4600}
#          ]


@app.route('/')
def hello_world():
    return 'Hello World!'


# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    curs.execute('SELECT * FROM menu')
    return jsonify(curs.fetchall())


# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    sql = '''INSERT INTO menu (`name`, `price`)
        VALUES (%s, %s)'''
    curs.execute(sql, (request_data["name"], request_data["price"]))
    db.commit()
    curs.execute('SELECT * FROM menu')
    return jsonify(curs.fetchall())


# PUT | id에 해당하는 데이터를 갱신한다.
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    request_data = request.get_json()
    sql = '''UPDATE menu SET name=%s, price=%s
            WHERE id=%s'''
    curs.execute(sql, (request_data["name"], request_data["price"], menu_id))
    db.commit()
    curs.execute('SELECT * FROM menu')
    return jsonify(curs.fetchall())


# DELETE | id에 해당하는 데이터를 삭제한다.
@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    sql = '''DELETE FROM menu where id=%s'''
    curs.execute(sql, menu_id)
    db.commit()
    curs.execute('SELECT * FROM menu')
    return jsonify(curs.fetchall())


if __name__ == '__main__':
    app.run()
