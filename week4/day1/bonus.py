# 보너스 과제 1을 위한 코드
##
from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name": "Americano", "price": 4100},
    {"id":3, "name": "CafeLatte", "price": 4600},
]

@app.route('/')
# def hello_flask():
#     return "Hello World!"

def print_menus():
    return str(menus)

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /mesnus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menus(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가,
    request_data = request.get_json() # {"name" : ..., "price":...}
    new_menu = {
        "id" : menus[-1]['id'] + 1, # menus 마지막 자료의 id값에 1을 더한 값
        "name" : request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /mesnus | 자원을 업데이트 한다.
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menus(id): # request가 JSON이라고 가정
    # 수정할 menu를 search
    for i,m in enumerate(menus):
        if m['id'] == id:
            idx = i
            break

    request_data = request.get_json() # {"name" : ..., "price":...}
    menus[idx] = {
        "name" : request_data['name'],
        "price": request_data['price'],
    }
    return jsonify(menus[id-1])

# DELETE /mesnus | 자료를 자원에서 삭제한다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menus(id): # request가 JSON이라고 가정
    # 삭제할 menu를 search
    for i, m in enumerate(menus):
        if m['id'] == id:
            idx = i
            break

    deleted_menu = menus.pop(idx)
    return jsonify(deleted_menu)

if __name__ == '__main__':
    app.run()