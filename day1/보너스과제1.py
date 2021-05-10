from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Latte", "price":4100},
    {"id":3, "name":"Americano", "price":2000},
]

@app.route('/')
def hello_flask():
    return "Hello World!"

@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json() # {"name":..., "price":...}
    new_menu = {
        "id" : menus[-1]['id'] + 1, 
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu) 
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    for i in range(len(menus)):
        if menus[i]['id'] == id:
            menus[i]['name'] = request_data['name']
            menus[i]['price'] = request_data['price']
    
    return jsonify({"menus": menus})

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    index_del = []
    for i in range(len(menus)):
        if menus[i]['id'] == id:
            index_del.append(i)
    
    d = 0
    for idx in index_del:
        menus.pop(idx - d)
        d += 1
    return jsonify({"menus": menus})

if __name__ == '__main__':
    app.run(debug=True)