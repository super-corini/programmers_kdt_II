from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price":3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]

@app.route('/')
def hello_flask():
    return "Hello World!"

# Get /menus
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus
@app.route('/menus', methods=['POST'])
def create_menus():
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name : ..., "price" : ...}

    id = len(menus) + 1

    new_menu = {
        "id" : id,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# DELETE /menus/id
@app.route('/menus/<int:id>', methods=['DELETE'])
def del_menu(id):
    del menus[id - 1]

    return jsonify({"menus" : menus})

# PUT /menus/id
@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    request_data = request.get_json()  # {"name : ..., "price" : ...}

    menus[id-1] = {
        "id": id,
        "name": request_data['name'],
        "price": request_data['price']
    }

    return jsonify({"menus" : menus})

if __name__ == '__main__':
    app.run()
