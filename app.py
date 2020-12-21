from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1,"name":"Espresso","price":3800},
    {"id":2,"name":"Americano","price":4100},
    {"id":3,"name":"CafeLatte","price":4600}
]

#GET /menus | 자료를 가져온다
@app.route('/menus') 
def get_menus():
    return jsonify({"menus":menus})

#POST /menus | 자료를 자원에 추가한다.
#과제 - ID야 움직여라 얍
next_id = len(menus) + 1
@app.route('/menus', methods=['POST'])
def create_menus(): #request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() #{"name":...,}
    global next_id
    new_menu = {
        "id" : next_id,
        "name" : request_data['name'],
        "price" : request_data['price'],
    } # PST에서 딸려오는 데이터들을 payload라고도 함.
    next_id += 1
    menus.append(new_menu)
    return jsonify(new_menu)

#과제 - 메뉴 관리 CRUD 구현하기
@app.route('/menus/<int:id>',methods=['PUT'])
def update_menus(id):
    request_data = request.get_json()
    for item in menus:
        if item['id'] == id:
            item['name'] = request_data['name']
            item['price'] = request_data['price']
            break
    else:
        return 'Data not exist'
    return jsonify(menus)

@app.route('/menus/<int:id>',methods=['DELETE'])
def delete_menus(id):
    request_data = request.get_json()
    for item in menus:
        if item['id'] == id:
            menus.remove(item)
            break
    else:
        return 'Data not exist'
    return jsonify(menus)

@app.route('/')
def hello_flask():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
