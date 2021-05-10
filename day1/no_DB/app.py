from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]

@app.route('/')
def hello_flask():
    return "Hello World."

# GET
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST
@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = {
        "id" : menus[-1]['id'] + 1,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT
@app.route('/menus/<id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    for m in menus:
        if m["id"] == int(id):
            m['name'] = request_data['name']
            m['price'] = request_data['price']
            break
    return jsonify(m)

# DELETE
@app.route('/menus/<id>', methods=['DELETE'])
def delete_menu(id):
    for m in menus:
        if m["id"] == int(id):
            menus.remove(m)
            break
    return get_menus()

if __name__ == '__main__':
    app.run()

