from flask import Flask, jsonify, request, current_app
from sqlalchemy import create_engine, text
import mysql.connector


app = Flask(__name__)

# database 설정파일

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]


@app.route('/') #@ : decorator, '/'주소를 요청받았을때 밑의 함수를 실행
def hello_flask():
    return "Hello"


@app.route('/DBmenus',methods=['GET'])
def get_DBmenus():
    conn = mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='menu',auth_plugin='mysql_native_password')
    cursor = conn.cursor()

    Query = ("SELECT * FROM menus")
    cursor.execute(Query)
    DB_menus = []

    for (id, name, price) in cursor:
        print("{},{},{}".format(id,name,price))
        DB_menus.append({'id' : id,
                        'name' : name,
                        'price' : price})

    cursor.close() 
    conn.close( )
    
    
    return jsonify(DB_menus)

#GET /menus : 자료를 가지고 온다.
@app.route('/menus', methods=['GET']) #method는 GET이 default
def get_menus():


    return jsonify({"menus" : menus})



#POST /menus : 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST']) 
def create_menu(): # request가 JSON이라고 가정
    #전달받은 자료를 menus 자원에 추가
    #request는 클라이언트가 서버로 요청할때 담기는 자료가 자동으로 담겨짐$
    request_data = request.get_json() #{"name":..., "price":...}
    
    #보너스 과제(idx 자동으로 수정)
    idx = 1
    if menus:
        idx = menus[-1]['id'] + 1
    
    new_menu = {
        "id" : idx,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

#필수 과제
@app.route('/menu', methods=['PUT'])
def update_menu():
    request_data = request.get_json()
    new_menu = {
        "id" : request_data['id'],
        "name" : "0",
        "price" : 0
    }

    for menu in menus:
        if menu['id'] == request_data['id']:
            new_menu['name'] = menu['name']
            new_menu['price'] = menu['price']

    return jsonify(new_menu)

#필수 과제
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    new_menu = {
        "id" : id,
        "name" : "0",
        "price" : 0
    }

    for menu in menus:
        if menu['id'] == id:
            new_menu['name'] = menu['name']
            new_menu['price'] = menu['price']
    
    menus.remove(new_menu)
    return jsonify(new_menu)



#space가 메인인 경우, 즉 app.py를 직접 실행한 경우
if __name__ == '__main__':
    app.run()
