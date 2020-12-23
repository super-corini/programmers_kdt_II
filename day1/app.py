from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]
next_id = len(menus) + 1


@app.route('/')
def hello_flask():
    return "Hello World!"


# GET /menus    | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})


# POST /menus   | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menus():  # request가 JSON이라고 가정
    global next_id                                          # 수정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()  # {"id": ..., "name": ..., "price": ...},
    new_menu = {
        "id": next_id,                                      # 수정
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    next_id += 1                                            # 수정
    return jsonify(new_menu)


# PUT /menus/<int:id>   | 자료를 자원에서 수정한다.
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menus(menu_id):
    request_data = request.get_json()

    for menu in menus:
        if menu['id'] == menu_id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            return jsonify(menu)
    return jsonify({'error_msg': "해당 자료가 존재하지 않습니다!"})


# DELETE /menus/<int:id>   | 자료를 자원에서 삭제한다.
@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menus(menu_id):
    request_data = request.get_json()

    for i, menu in enumerate(menus):
        if menu['id'] == menu_id:
            return jsonify(menus.pop(i))
    return jsonify({'error_msg': "해당 자료가 존재하지 않습니다!"})


if __name__ == "__main__":
    app.run()
