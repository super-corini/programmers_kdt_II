from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Espresso", "price":4100},
    {"id":3, "name":"Espresso", "price":4600},
]

@app.route('/')
def hello_flask():
    return "Hello World!"


# GET /menus
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus 
@app.route('/menus', methods=['POST'])
def create_menus():
    request_data = request.get_json()
    new_menu = {
        "id" : 4,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# POST /menus/id
@app.route('/menus/<id>', methods=['PUT'])
def update_menus(id):
    request_data = request.get_json()
    for i in range(len(menus)):
        if menus[i]['id'] == int(id):
            menus[i]['name'] = request_data['name']
            menus[i]['price'] = request_data['price']
            break

    return jsonify(menus[i])

# Delete /menus/id
@app.route('/menus/<id>', methods=['DELETE'])
def delete_menus(id):
    for i in range(len(menus)):
        if menus[i]['id'] == int(id):
            deleted_menu = menus[i]
            del menus[i]
            break

    return jsonify(deleted_menu)


if __name__ == '__main__':
    app.run()