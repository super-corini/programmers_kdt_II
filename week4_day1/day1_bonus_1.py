from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [{"id": 1, "name": "Espresso", "price": 3800},
         {"id": 2, "name": "Americano", "price": 4100},
         {"id": 3, "name": "CafeLatte", "price": 4600}
         ]


@app.route('/')
def hello_world():
    return 'Hello World!'


# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})


# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 json이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name" : ..., "price" : ...}
    # id가 하나씩 증가하여 menu 리스트에 추가될 수 있도록 수정
    new_id = len(menus) + 1
    new_menu = {
        "id": new_id,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)


# PUT | id에 해당하는 데이터를 갱신한다.
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    request_data = request.get_json() # {"name" : ..., "price" : ...}
    for m in menus:
        if m["id"] == menu_id:
            m["name"] = request_data['name']
            m["price"] = request_data['price']
    return jsonify({"menus": menus})


# DELETE | id에 해당하는 데이터를 삭제한다.
@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    for i, m in enumerate(menus):
        if m["id"] == menu_id:
            del menus[i]
            break
    return jsonify({"menus": menus})


if __name__ == '__main__':
    app.run()
