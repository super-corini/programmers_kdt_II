from flask import Flask, jsonify, request

app = Flask(__name__)


menus = [
    {"id": 1, 'name':"Espresso", "price": 3800},
    {"id": 2, 'name':"Americano", "price": 4100},
    {"id": 3, 'name':"CafeLatte", "price": 4600},
]


@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})



# POST /menus
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달 받은 자료를 menus를 자원에 추가
    request_data = request.get_json() # request 요청된 데이터를 가져온다.
    new_menu = {
        "id": len(menus) + 1, # 보너스 과제 I: ID야 움직여라 얍!
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)


# PUT /menus
@app.route('/menus/<int:ID>', methods=['PUT'])
def update_menu(ID) -> object :
    request_data = request.get_json()
    idx = 0

    for i, menu in enumerate(menus):
        if menu['id'] == ID:
            idx = i
    menus[i]['name'] = request_data['name']
    menus[i]['price'] = request_data['price']
    return jsonify(menus)

# DELETE
@app.route('/menus/<int:ID>', methods=['DELETE'])
def del_menu(ID):
    idx = 0
    for i, menu in enumerate(menus):
        if menu['id'] == ID:
            idx = i
    return jsonify(menus.pop(idx))


if __name__ == '__main__':
    app.run()
