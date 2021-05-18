from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]


@app.route('/')
def hello_falsk():
    return 'Hello World!'

# GET / menus | 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})


# Post / menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    next_id = menus[-1]['id']+1
    new_menu = {
        "id": next_id,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)

    return jsonify(new_menu)


# PUT / menus / <int:id> | 자료 수정
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    for menu in menus:
        if menu['id'] == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            break
    return jsonify({"menus": menus})


# DELETE / menus / <int:id> | 자료 삭제
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for menu in menus:
        if menu['id'] == id:
            menus.remove(menu)
            break
    return jsonify({'menus': menus})



if __name__ == '__main__':
    app.run()