from flask import Flask, jsonify, request


app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

# Home directory
@app.route('/')
def hello_flask():
    return "Hello World!"

# Get /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# Post /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name" : ..., "price" : ...}
    new_menu = {
        "id" : menus[-1]['id'] + 1,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# Put /menus | 해당 id에 해당하는 데이터를 갱신한다.
@app.route('/menus', methods=['PUT'])
def put_menu():
    request_data = request.get_json() # {"id" : ..., "name" : ..., "price" : ...}
    new_menu = {
        "id" : request_data['id'],
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    for idx, item in enumerate(menus):
        if item['id'] == request_data['id']:
            menus[idx]['name'] = request_data['name']
            menus[idx]['price'] = request_data['price']
            return jsonify(menus)
    menus.append(new_menu)
    return jsonify(new_menu)

# Delete /menus | 해당 id에 해당하는 데이터를 삭제한다.
@app.route('/menus', methods=['DELETE'])
def delete_menu():
    request_data = request.get_json() # {"id" : ...}
    delete_menu = {
        "id" : request_data['id'],
    }
    is_delete = False
    for i in range(len(menus)):
        if menus[i]['id'] == delete_menu['id']:
            menus.pop(i)
            is_delete = True
            break
    return jsonify(delete_menu) if is_delete else jsonify({'menus' : menus})


if __name__ == '__main__':
    app.run()