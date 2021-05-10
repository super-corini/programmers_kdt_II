from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

# Main
@app.route('/')
def home_flask():
    return "Week4 Day1 - 필수과제 : 메뉴관리 Flask CRUD 구현"

# READ(GET) /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# CREATE(POST) /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name" : ..., "price": ...}
    new_menu = {
        "id" : 4,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# UPDATE
@app.route('/menus/<int:id>',methods=['PUT'])
def update_menus(id):
    request_data = request.get_json()
    menus[id-1]['name'] = request_data['name']
    menus[id-1]['price'] = request_data['price']
    return jsonify({"menus" : menus})

# DELETE
@app.route('/menus/<int:id>',methods=['DELETE'])
def delete_menu(id):
    del menus[id-1]
    return jsonify({"menus" : menus})

if __name__ == '__main__':
    app.run()