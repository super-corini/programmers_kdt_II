from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4000},
    {"id":3, "name":"CafeLatte", "price":4500}
]
next_id = len(menus) + 1


# Home Directory
@app.route('/')
def hello_flask():
    return "Hello Flask! Ah! Hard!"

# Get /menus | 자료를 가지고 옴 (READ)
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | 자원 추가 (CREATE)
@app.route('/menus', methods=['POST'])
def post_menu(): # request가 JSON이라고 가정한다.
    # 전달받은 자료를 menus 자원에 추가함
    global next_id
    request_data = request.get_json()
    new_menu = {
        "id": next_id,
        "name": request_data['name'],
        'price': request_data['price']
    }
    next_id += 1
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    update_data = request.get_json()
    for menu in menus:
        if menu['id'] == id:
            menu['name'] = update_data['name']
            menu['price'] = update_data['price']
            return jsonify(menu)
    return jsonify("Failure! Index Error!")

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for i, menu in enumerate(menus):
        if menu['id'] == id:
            menus.pop(i)
            return jsonify(menus)
    return jsonify("Failure! Index Error!")

if __name__ == '__main__':
    app.run()