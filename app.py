from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name": "Espresso", "price": 3800},
    {"id":2, "name": "Americano", "price": 4100},
    {"id":3, "name": "CafeLatte", "price": 4600},
]


@app.route('/') # home 디렉토리
def gello_flask():
    return "Hello World"

# GET/menus : 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    # return값을 꼭 json와 해야
    return jsonify({"menus":menus})


# POST/menus: 자료를 자원에 추가한다
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    #전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name" : ... , "price" : ...}
    new_menu = {
        "id": 4,
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    for menu in menus:
        if menu.get("id", -1) == id:
            menu["name"] = request_data["name"]
            menu["price"] = request_data["price"]
    return jsonify({"menus": menus})

# DELETE
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    request_data = request.get_json()
    for i in range(len(menus)):
        if menus[i].get("id", -1) == id:
            menus.pop(i)
            break
    return jsonify({"menus": menus})



if __name__ == '__main__':
    app.run()


