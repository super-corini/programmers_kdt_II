from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" :menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가 
    request_data = request.get_json() # {"name":..., "price":...}
    new_menu = {
        "id" : 4,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /menus
@app.route('/menus/<int:idx>', methods=['PUT'])
def update_menu(idx):
    request_data = request.get_json()
    for menu in menus:
        if menu['id'] == idx:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
    return jsonify({"menus" :menus})

# DELETE /menus
@app.route('/menus/<int:idx>', methods=['DELETE'])
def delete_menu(idx):
    request_data = request.get_json()
    for menu in menus:
        if menu['id'] == idx:
            remove_data = menu
            break
    menus.remove(remove_data)
    return jsonify({"menus" :menus})

if __name__ == '__main__':
    app.run()
