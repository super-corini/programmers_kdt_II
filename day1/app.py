from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price": 3800},
    {"id":2, "name":"Americano", "price": 4100},
    {"id":3, "name":"CafeLatte", "price": 4600},
]

cnt = len(menus)
print(cnt, 'cnt')


@app.route('/')
def hello_flask():
    return "Hello World!!"

# GET/menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():    
    return jsonify({"menus" : menus})

# POST /menus | 자료를 자원에 추가한다

@app.route('/menus', methods=['POST'])
def create_menus(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    global cnt
    request_data = request.get_json() # {"name" : ...., "price" : ... }
    new_menu = {
        "id" : cnt,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    cnt += 1
    return jsonify(new_menu)

# PUT /menu/<int:id> : 해당하는 id에 해당하는 데이터를 갱신합니다. (HTTPRequest의 Body에 갱신할 내용이 json으로 전달됩니다.)
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menus(menu_id):
    request_data = request.get_json()

    for menu in menus:
        if menu['id'] == menu_id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            return jsonify(menu)
    
    return jsonify({'error_msg': "해당 자료가 존재하지 않습니다!"})

# DELETE /menu/<int:id> : 해당하는 id에 해당하는 데이터를 삭제합니다.

@app.route('/menus/<int:menu_id>', methods=['DELETE'])

def delete_menus(menu_id):
    request_data = request.get_json()

    for i, menu in enumerate(menus):
        if menu['id'] == menu_id:
            return jsonify(menus.pop(i))
    return jsonify({'error_msg': "해당 자료가 존재하지 않습니다!"})


if __name__ == '__main':
    app.run()

