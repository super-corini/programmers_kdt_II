from flask import Flask, jsonify, request

app = Flask(__name__) #flask를 바탕으로한 객체를 생성 

menus = [
    {"id" : 1, "name":"Espresso", "price":3000},
    {"id" : 2, "name":"Americano", "price":4100},
    {"id" : 3, "name":"CafeLatte", "price":4600},
]

@app.route('/') #@ 파이썬 데코레이터
def hello_flask():
    return "Hello World!"

# POST (like... INSERT)/menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def crate_menu(): # request가 JSON이라고 가정

    idx = len(menus) + 1

    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()

    new_menu = {
        "id" : idx,
        "name" : request_data['name'],
        "price" : request_data['price'],
        }
    menus.append(new_menu)

    return jsonify(new_menu)

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})

# PUT(UPDATE) /menus/id | 자료를 수정한다
@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):

    request_data = request.get_json()

    update_menu = {
        'id':id,
        'name':request_data['name'],
        'price':request_data['price']
    }

    for i, menu in enumerate(menus): # id는 idx보다 1높음
        if menu['id'] == id:
            menus[i] = update_menu #전달받은 데이터를 가지고 업데이트

    return jsonify(update_menu)

# DELETE /menus/id | 자료를 삭제한다
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):

    for i, menu in enumerate(menus):
        if menu['id'] == id:
            del_menu = menus.pop(i)
            return jsonify(del_menu)
        #삭제 이후 다음 메뉴들의 id를 1씩 줄이는 방법은?

if __name__ == '__main__': #app.py를 모듈이 아닌 직접적으로 실행될때
    app.run()