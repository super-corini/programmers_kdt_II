import os
from models import db
from flask import Flask, jsonify, request

# jsonify : 파이썬의 딕셔너리 타입(menus)을 json이라는 데이터 저장 방식으로 바꿔줌
# request : HTTP request를 다룰 수 있는 모듈

app = Flask(__name__)
# Flask를 바탕으로 한 객체 생성. 인자로 __name__전달. Flask에 이름을 앱으로 넣어준다는 의미

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]
next_id = len(menus)+1

# 홈 디렉토리
@app.route('/')
def hello_flask():
    return "Hello World!"


# GET /menus    | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})


# menus는 리스트. json 변환이 안되기 때문에, menus를 value로 하는 새로운 딕셔너리 생성

# POST /menus   | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menus():
    global next_id
    # request가 JSON이라고 가정
    request_data = request.get_json()  # {"id": ..., "name": ..., "price": ...},
    # request는 자동적으로 클라이언트가 서버에 POST로 요쳥할 때 담긴 자료가 있음
    # 이를 get_jason()으로 파싱해서 딕셔너리 형태로 담음
    new_menu = {
        "id": next_id,
        "name": request_data['name'],
        "price": request_data['price'],
    }
    # 전달받은 자료를 menus 자원에 추가
    menus.append(new_menu)
    next_id += 1
    return jsonify(new_menu)


# PUT /menus   | 해당 자료를 수정한다.
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menus(id):
    update_data = request.get_json()
    try:
        menus[id - 1]["name"] = update_data["name"]
        menus[id - 1]["price"] = update_data['price']
        return jsonify(menus[id - 1])
    except Exception as e:
        print(e)
        return jsonify({'error': "해당 자료가 존재하지 않습니다."})


# DELETE /menus   | 해당 자료를 삭제한다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menus(id):
    try:
        del menus[id - 1]
        return jsonify(menus)
    except Exception as e:
        print(e)
        return jsonify({'error': "해당 자료가 존재하지 않습니다."})


if __name__ == "__main__":
    app.run(debug=True)
