import os
from flask import Flask, jsonify, request
from models import db, Menu 

app = Flask(__name__)

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app
db.create_all()

menus = [
    {"id": 1,"name": "Espresso", "price":3800},
    {"id": 2,"name": "Amerocano", "price":4100},
    {"id": 3,"name": "CafeLatte", "price":4600}
]

@app.route('/')
def hello_code():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name": ..., "price": ...}
    new_id = menus[-1]["id"] + 1
    new_menu = {
        "id" : new_id,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    request_data = request.get_json()
    
    for menu in menus:
        if menu['id'] == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            return menu
    else:
        return "no menu"


@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for menu in menus:
        if menu['id'] == id:
           menus.remove(menu)
           print(menus)
           return f"delete {id}'s data"       
    else:
        return "no menu"

    
    

# app 파일을 직접적으로 실행할경우 실행되는 코드
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)