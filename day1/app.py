from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {'id': 1, 'name': 'Espresso', 'price': 3800},
    {'id': 2, 'name': 'Americano', 'price': 4100},
    {'id': 3, 'name': 'CafeLatte', 'price': 4600},
]


@app.route('/')
def hello_flask():
    return 'Hello World'


# GET /menus  | 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    return jsonify({'menus': menus})


# POST /menus  | 자료를 자원에 추가한다
@app.route('/menus', methods=['POST'])
def create_menu():  # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()  # {'name': ..., 'price': ...}
    new_menu = {
        'id': 4,
        'name': request_data['name'],
        'price': request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)


@app.route('/menus/<id>', methods=['PUT'])
def update_menu(id):
    # 전달받은 자료를 dict로 변경
    request_data = request.get_json()  # {'name': ..., 'price': ...}
    id = int(id)

    # id 확인
    idx = -1
    for n, i in enumerate(menus):
        if i['id'] == id:
            idx = n

    # 데이터 변경
    if idx != -1:
        update_menu = {
            'id': id,
            'name': request_data['name'],
            'price': request_data['price'],
        }
        menus[idx] = update_menu
    else:
        return 'Can not find id: {}'.format(id)

    return jsonify(menus[idx])


@app.route('/menus/<id>', methods=['DELETE'])
def delete_menu(id):
    # int로 변경
    id = int(id)

    # id 확인
    idx = -1
    for n, i in enumerate(menus):
        if i['id'] == id:
            idx = n

    # 데이터 삭제
    if idx != -1:
        menus.pop(idx)
    else:
        return 'Can not find id: {}'.format(id)

    return jsonify({'menus': menus})


if __name__ == '__main__':
    app.run()
