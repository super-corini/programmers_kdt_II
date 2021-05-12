from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3000},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다.

@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menus():
    # 전달받은 자료를 menus 자원에 추가.
    request_data = request.get_json()
    new_menu = {
        "id" : menus[-1]['id'] + 1,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /munus/menu_id | 자료를 수정한다.
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    request_data = request.get_json()
    for menu in menus:
        if menu['id'] == menu_id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            break

    return jsonify({"menus" : menus})

# DELETE /menus/menu_id | 자료를 삭제한다.
@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    deleted_menu = {}
    for menu in menus:
        if menu['id'] == menu_id:
            deleted_menu = menu
            menus.remove(menu)
            break
    
    return jsonify(deleted_menu)

if __name__ == '__main__':
    app.run()