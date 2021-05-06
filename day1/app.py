from flask import Flask, jsonify, request


app = Flask(__name__)


menus = [
    {"id":1, "name":"Espresso","price":3800},
    {"id":2, "name":"Americano","price":4100},
    {"id":3, "name":"CafeLatte","price":4600}
]

i = 4

@app.route('/')
def hello_flask():
    return "Hello World!"

# Get /menus
@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})

# POST /menus
@app.route('/menus', methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus 자원에 추가
    global i
    request_data = request.get_json()
    new_menu = {
        "id" : i,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    i += 1
    menus.append(new_menu)
    return jsonify(new_menu)

#PUT /menus
@app.route('/menus/<_id>', methods=['PUT'])
def change_menu(_id):
    request_data = request.get_json()
    for i in range(len(menus)):
        if menus[i]['id'] == int(_id):
            menus[i]['name'] = request_data['name']
            menus[i]['price'] = request_data['price']
            break
    return jsonify({"menus":menus})

#DEL /menus
@app.route('/menus/<_id>', methods=['DELETE'])
def del_menu(_id):
    for i in range(len(menus)):
        if menus[i]["id"] == int(_id):
            a = menus[i]
            del menus[i]
            return a

if __name__ == "__main__":
    app.run()