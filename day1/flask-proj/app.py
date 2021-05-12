from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id" : 1, "name" : "Espresso", "price" : 3800},
    {"id" : 2, "name" : "Americano", "price" : 4100},
    {"id" : 3, "name" : "CafeLatte", "price" : 4600}
]

@app.route('/')
def hello_flask():
    return "Hello World"

# GET /menus : 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})

# 전역변수 id_count 생성
id_count = 4

# POST /menus : 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus자원에 추가
    request_data = request.get_json()
    # 메뉴를 추가할 때마다 id 증가시키기 위해 전역변수 id_count 사용
    global id_count
    new_menu = {
        "id" : id_count,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    id_count += 1
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data2 = request.get_json()
    update_menu = {
        "id" : id,
        "name" : request_data2['name'],
        "price" : request_data2['price']
    }
    for i in range(len(menus)):
        if menus[i]['id'] == id:
            menus[i] = update_menu
    return jsonify(update_menu)

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for i in range(len(menus)):
        if menus[i]['id'] == id:
            menus.pop(i)
    return jsonify({"menus":menus})


if __name__ == '__main__':
    app.run()