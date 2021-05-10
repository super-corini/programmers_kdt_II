from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='flask', charset='utf8')

curs = db.cursor()

@app.route('/')
def hello_flask():
    return 'Hello World!'

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    sql =   '''
            SELECT * FROM coffee;
            '''        
    curs.execute(sql)
    return jsonify(curs.fetchall())

# POST /menus | 자료를 자원에 추가한다
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {'name': ..., 'price' : ...}
    sql =   '''
            INSERT INTO `coffee`(`name`, `price`)
            VALUES  (%s, %s)
            '''
    curs.execute(sql, (request_data['name'], request_data['price']))
    db.commit()
    return jsonify(curs.fetchall())

# PUT /menu/<int:id> | Update
@app.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json() # {'name' : ..., 'price' : ...}
    sql =   '''
            UPDATE `coffee` SET name = %s, price = %s
            WHERE id = %s
            '''
    curs.execute(sql, (request_data['name'], request_data['price'], id))
    db.commit()
    return jsonify(curs.fetchall())

# DELETE /menus | Delete
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    sql = '''
            DELETE FROM `coffee` where id = %s
            '''
    curs.execute(sql, id)
    return jsonify(curs.fetchall())

if __name__ == '__main__':
    app.run(debug=True)