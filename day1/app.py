from flask import Flask, jsonify, request

# jsonify : 딕셔너리타입을 javascrip에서 사용하는 json이라는 저장형식으로 바꿔주는 모듈,
# requset : HTTP requset를 다눌수 있는 모듈

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]


@app.route('/')  # @ : 데코레이터 - () 안에 인자가 입력되었을때 아래 함수를 실행
def hello_flask():
    return "Hello World!"


# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})  # 리스트인 menus를 리턴하지 못하므로 menus라는 딕셔너리를 만들어 json으로 리턴


# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])  # methods=['GET'] 의 경우가 default 이므로 GET에서는 명시하지 않았음
def create_menu():  # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()  # {"name": ..., "price": ...}
    new_menu = {
        "id": menus[-1]['id'] + 1,                            # 추가되는 것을 반영
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)


# PUT /menus/<int:id> | 자료를 자원에서 수정한다.
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    update_data = request.get_json()

    for menu in menus:
        if menu["id"] == menu_id:
            menu["name"] = update_data["name"]
            menu["price"] = update_data["price"]
            return jsonify(menu)
    return jsonify({'error_msg': "해당 자료가 존재하지 않습니다."})


# DELETE /menu/<int:id> : 해당하는 id에 해당하는 데이터를 삭제합니다.
@app.route("/menus/<int:menu_id>", methods=['DELETE'])
def del_menu(menu_id):
    # del_data = request.get_json()

    for idx, menu in enumerate(menus):
        if menu["id"] == menu_id:
            return jsonify(menus.pop(idx))
    return jsonify({'error_msg': "해당 자료가 존재하지 않습니다."})


if __name__ == '__main__':  # __name__ <- app.py가 모듈로써가 아니라 직접적으로 실행될때 app.run()을 사용하라는 의미
    app.run()
