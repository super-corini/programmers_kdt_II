from flask import Flask, jsonify, request

import os
from models import db

app = Flask(__name__)

# 현재있는 파일의 디렉토리 절대경로
basdir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB파일 만들기
dbfile = os.path.join(basdir, 'db.sqlite')

# SQLAlchemy 설정

# 내가 사용 할 DB URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
# 비지니스 로직이 끝날때 Commit 실행(DB반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app
db.create_all()

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]

count = 1

# / : 루트의 자료를 접근하는 주소
@app.route('/')

def hello_flask():
    return "hello world!"

# 같은 엔드포인트에 대해 다른 동사를 씀.
# /menus : menus의 자료를 접근하는 주소
# GET /menus | 자료를 가지고 온다.
@app.route('/menus', methods = ['GET']) #methods = ['GET']은 default로 있음
def get_menus():
    # 이 함수를 실행했을 때 return 값이 https response에 해당하는 값이 만들어짐.
    # return menus / 리스트 타입은 jsonify가 불가능
    return jsonify({"menus" : menus}) #딕셔너리

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods = ['POST'])
def create_menu(): #request가 JSON이라고 가정
    #전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() #변환과정 반드시 거쳐야함.
    # {"name" : ..., "price" : ...}
    # menus의 길이 + 1을 통해 실시간 숫자 올리기 가능
    new_menu = {
        "id" : len(menus) + 1,
        "name" : request_data['name'],
        "price" : request_data['price']
    }

    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /menus | 자료를 수정한다.
# <int:id>!! 함수의 인자로 대입  
@app.route('/menus/<int:id>', methods = ['PUT'])
def update_menu(id):
    #전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()

    for menu in menus:
        if menu['id'] == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            break
    else:
        return "아이디 없습니다"
    return jsonify({"menus" : menus})
        
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for idx, menu in enumerate(menus):
        if menu['id'] == id:
            menus.pop(idx)
            break
    else:
        return "아이디 없습니다."
    return jsonify({"menus" : menus})

if __name__ == '__main__':
    app.run()