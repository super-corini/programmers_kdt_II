from flask import Flask,jsonify, request
import pymysql

''' local 환 경 용 세 팅 
db = pymysql.connect(host="localhost", user="root", passwd="*****", db="flask_test", charset="utf8")
cur = db.cursor()
app = Flask(__name__)
sql = "SELECT * from menus"
cur.execute(sql)
data_list = cur.fetchall()
'''

@app.route('/')
def hello_flask():
    return "Bonus_2 과제 구현을 위한 Homepage"

# Get /menus / 자료를 가져온다.
@app.route('/menus')
def get_menus():
    cur = db.cursor()
    sql = "SELECT * from menus"
    cur.execute(sql)
    data_list = cur.fetchall()
    return jsonify({"menus":data_list})

# Post
@app.route('/menus', methods = ['POST'])
def create_menu():
    global data_list
    cur = db.cursor()
    #전달받은 자료를 메뉴에 추가
    request_data = request.get_json()
    sql_post ="INSERT INTO menus (id, name, price) VALUES (%s, %s, %s);"
    cur.execute(sql_post,(len(data_list)+1,request_data['name'],request_data['price']))
    cur.execute("SELECT * from menus")
    data_list=cur.fetchall()
    db.commit()
    return jsonify({"menus":data_list})


@app.route('/menus/<int:id>', methods = ['PUT'])
def update_id(id):
    global data_list
    cur = db.cursor()
    request_data = request.get_json()
    name,price = request_data['name'],request_data['price']
    sql_update = 'UPDATE menus SET name = %s, price = %s WHERE id = %s;'
    cur.execute(sql_update,(name,price,id))
    cur.execute("SELECT * from menus")
    db.commit()
    data_list = cur.fetchall()
    return jsonify({"menus":data_list})

# DELETE
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    global data_list
    cur = db.cursor()
    sql_delete = 'DELETE From menus WHERE id = %s'
    cur.execute(sql_delete,id)
    cur.execute("SELECT * from menus")
    data_list = cur.fetchall()
    db.commit()
    return jsonify({'menu': data_list})

if __name__ == '__main__':
    app.run()
