from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [{'id':1, "name":"Espresso", "price":3000},
         {'id':2, "name":"Americano", "price":3900},
         {'id':3, "name":"CaffeLatte", "price":4300},
         ]
current_id = 3


@app.route('/')
def hello_flask():
    return "Hello World"

# GET /menus | 자료를 가져온다
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})

# POST /menus | 자료를 자원에 추가한다
# POST 요청이 들어올 때마다 id가 하나씩 증가하여 menu 리스트에 추가될 수 있도록 코드를 수정해주세요.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라 가정
    global current_id
    current_id += 1
    # 전달받은 자료를 menus자원에 추가
    request_data = request.get_json() # {"name:..., "price":....}
    new_menu = {
        "id" : current_id,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /menu/<int:id> : 해당하는 id에 해당하는 데이터를 갱신합니다. (HTTPRequest으로 Body가 주어집니다.)
@app.route('/menus/<int:id>', methods=['PUT'])
def modify_menu(id): #
    modify_data = request.get_json()
    for dic in menus:
        if dic['id'] == id:
            dic['name'] = modify_data['name']
            dic['price'] = modify_data['price']
            return dic

    return "ID does not exist!"

# DELETE /menu/<int:id> : 해당하는 id에 해당하는 데이터를 삭제합니다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for idx, dic in enumerate(menus):
        if dic['id'] == id:
            del menus[idx]
            return dic
    return "ID does not exist!"


if __name__ == '__main__':
    app.run()
