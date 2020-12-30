
from flask import Flask, jsonify, request
from queue import PriorityQueue

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

id_list = PriorityQueue()
for available_id in range(4, 10000): id_list.put(available_id)

# @ = python decorator
# => 다음 주소를 입력받았을 때 아래 함수를 실행하라는 뜻
@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다.
@app.route('/menus') # GET은 methods 생략 가능
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    # 전달 받은 자료를 menus 자원에 추가
    # request가 JSON이라고 가정
    request_data = request.get_json() # {"name" : ..., "price" : ...}
    using_id = id_list.get()
    new_menu = {
        "id" : using_id,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    for idx, menu in enumerate(menus):
        if id in menu.values():
            request_data = request.get_json()
            menus[id-1]["name"] = request_data['name']
            menus[id-1]["price"] = request_data['price']
        return jsonify(menus[id-1])
    return "not existed id"

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for idx, menu in enumerate(menus):
        if id in menu.values():
            id_list.put(menus[idx]["id"])
            menus.pop(idx)
            return "delete successfully"
    return "not existed id"

if __name__ == '__main__':
    app.run()

