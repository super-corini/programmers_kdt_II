from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3500},
    {"id": 2, "name": "Americano", "price": 4000},
    {"id": 3, "name": "Cafe Latte", "price": 4500},
]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/menus')
def read_menus():
    return jsonify({"menus": menus})

@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = {
        "id": len(menus)+1,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus<int:id>', methods=['PUT'])
def update_menus(id: int):
    request_data = request.get_json()
    try:
        menus[id - 1].update(dict(request_data))
        return jsonify(menus[id - 1])
    except Exception as e:
        print(e)

@app.route('/menus<int:id>', methods=['DELETE'])
def delete_menus(id: int):
    try:
        # menus[id - 1].clear()
        # menus[id - 1]['id'] = id
        for i in range(id, len(menus)):
            menus[i]['id'] -= 1
        del menus[id-1]
        return jsonify(menus)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=False)