from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {'id': 0    , "name":"Espresso"     , "price":3800},
    {'id': 1    , "name":"Americano"    , "price":4100},
    {'id': 2    , "name":"CafeLatte"    , "price":4600},
]
menu_id = [
    0, 1, 2
]

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus
@app.route('/menu')
def get_menus():
    return jsonify({"menus": menus})

# POST /menus
# 보너스 과제 1 적용
@app.route('/menu', methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus 자원에 추가.
    # 전달받은 데이터는 json이라 가정
    request_data = request.get_json()
    new_menu = {
        # 새로운 id는 menu_id를 기반으로 개수를 카운트
        # 삭제할 때에도 id는 그대로 유지한다. (그 뒤 번호를 유지해야하므로)
        "id": len(menu_id),
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    menu_id.append(new_menu['id'])
    return jsonify(new_menu)

#입력받은 id에 대한 메뉴의 정보를 수정한다.
@app.route('/menu/<id>', methods=['PUT'])
def edit_menu(id):
    request_data = request.get_json()
    new_name = request_data['name']
    new_price = request_data['price']
    edit_id = int(id)
    for m in menus:
        if m['id'] == edit_id:
            if not new_name == '':
                m['name'] = new_name
            if not new_price == '':
                m['price'] = int(new_price)
            new_menu = m
            break

    return jsonify(new_menu)

#입력받은 id에 대한 메뉴의 정보를 삭제한다.
@app.route('/menu/<id>', methods=['DELETE'])
def delete_menu(id):
    delete_id = int(id)
    deleted = False
    for m in menus:
        if m['id'] == delete_id:
            menus.remove(m)
            deleted = True
            break
    menu = {
        "deleted": deleted,
        "deleted_id": delete_id,
        "count": len(menus)
    }
    return jsonify(menu)

if __name__== '__main__':
    app.run()
"""
# HTTP URI
URI : 대상을 식별


# HTTP Method
Method: 일종의 함수 같은 느낌.
몇가지 요청 방법에 따라 CRUD를 진행
"""