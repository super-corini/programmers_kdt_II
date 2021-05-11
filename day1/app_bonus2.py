from flask import Flask, jsonify, request
import pymysql

db = pymysql.connect(host="localhost", port=3307, user="root", password="1234", db="study")
curs = db.cursor(pymysql.cursors.DictCursor)

app = Flask(__name__)


"""
아래 데이터는 study 스키마 속 menus 테이블에 입력해 놓았습니다.
menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "Caffe Latte", "price": 4600},
]
"""
@app.route("/")
def hello_flask():
    return "Hello, World!"


# GET /menus  |  자료를 가지고 온다.
@app.route("/menus")
def get_menus():
    curs.execute('select * from menus')
    return jsonify(curs.fetchall())


# POST /menus  |  자료를 자원에 추가한다.
@app.route("/menus", methods=["POST"])
def create_menus():

    request_data = request.get_json()

    sql = '''insert into menus(name, price)
                 values(%s, %s)'''
    curs.execute(sql, (request_data["name"], request_data["price"]))
    db.commit()
    curs.execute('select * from menus')
    return jsonify(curs.fetchall())

# PUT /menus/<int:id>
@app.route("/menus/<int:id>", methods=["PUT"])
def update_menus(id):
    request_data = request.get_json()

    sql = ''' update menus set name = %s, price =%s
              where id = %s '''
    curs.execute(sql, (request_data["name"], request_data["price"], id))
    db.commit()
    curs.execute('select * from menus')
    return jsonify(curs.fetchall())

# DELETE /menus/<int:id>
@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    sql = ''' delete from menus where id = %s '''
    curs.execute(sql, id)
    db.commit()
    curs.execute('select * from menus')
    return jsonify(curs.fetchall())

if __name__ == "__main__":
    app.run()