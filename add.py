from flask import Flask, jsonify, request


app = Flask(__name__)

menus = [
    {'id': 1, 'name': 'Espresso', 'price': 3800},
    {'id': 2, 'name': 'Americano', 'price': 4100},
    {'id': 3, 'name': 'CafeLatte', 'price': 4600}
]

idx = len(menus)+1


@app.route('/')
def hello_flask():
    return "Hello World!"


# get. 자료를 가져옴
@app.route('/menus')
def get_menus():
    return jsonify({'menus': menus})


# post. 자료를 추가함
@app.route('/menus', methods=['POST'])
def create_menu():
    global idx
    # 전달 받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    new_menu = {
        'id': idx,
        'name': request_data['name'],
        'price': request_data['price']
    }
    idx += 1
    menus.append(new_menu)
    return jsonify(new_menu)


# put
@app.route('/menus/<int:menu_id>', methods=['PUT', 'DELETE'])
def update_menu(menu_id):

    # 메뉴 변경
    if request.method == 'PUT':
        request_data = request.get_json()

        # 해당 메뉴 찾아서 바꾸기
        for menu in menus:
            if menu['id'] == menu_id:
                menu['name'] = request_data['name']
                menu['price'] = request_data['price']
                return jsonify(menu)

    # 메뉴 삭제
    if request.method == 'DELETE':
        # 해당 메뉴 찾아서 바꾸기
        for i, menu in enumerate(menus):
            if menu['id'] == menu_id:
                return jsonify(menus.pop(i))

    return jsonify({})


if __name__ == '__main__':
    app.run()
