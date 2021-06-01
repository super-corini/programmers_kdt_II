from flask import Flask, jsonify, request

app = Flask(__name__)


menus = [
    {"id":1, "name":'Espresso', "price":3800},
    {"id":2, "name":'Americano', "price":4100},
    {"id":3, "name":'CafeLatte', "price":4600}
]


ids = len(menus)

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})



# POST /menus | 자료를 자원에 추가한다
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    global ids
    ids = len(menus) + 1
    request_data = request.get_json() # {"name":..., "prine":... }
    new_menu = {
        "id": ids,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)


# PUT /menus/<int:id> | 자료를 갱신한다.
@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    request_data = request.get_json()
    update_menu = {
        "id":id,
        "name": request_data['name'],
        "price": request_data['price']
    }

    del menus[id-1]
    menus.insert(id-1, update_menu)
    return jsonify(update_menu)



# DELETE /menus<int:id> | 해당 id의 데이터를 삭제한다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def del_menu(id):
    request_data = request.get_json()
    delete_menu = {
        "id" : id,
    }
    del menus[id-1]
    ids -= 1
    return jsonify(delete_menu)

if __name__ == '__main__':
    app.run()
