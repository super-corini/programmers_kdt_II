from flask import Flask, jsonify, request
# jsonify는 딕셔너리 타입을 json타입으로 변환하는 것
# request는 HTTP request를 다룰 수 있는 모듈

app = Flask(__name__)

menus = [
    {"id" : 1, "name" : "Espresso", "price" : 3800},
    {"id" : 2, "name" : "Americano", "price" : 4100},
    {"id" : 3, "name" : "CafeLatte", "price" : 4600}
]

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name" : ..., "price" : ...}

    ########## 보너스 과제 1 : ID야 움직여랴 얍! ##########

    new_menu = {
        "id" : len(menus)+1,
        "name" : request_data['name'],
        "price" : request_data['price']
    }

    ########## 보너스 과제 1 완료 ##########

    menus.append(new_menu)
    return jsonify(new_menu)

######### 필수 과제 메뉴 관리 CRUD 구현하기##########

# PUT /menus/id 해당하는 id에 해당하는 데이터를 갱신한다.
@app.route('/menus/<id>', methods=['PUT'])
def update_data(id):
    request_data=request.get_json()
    request_data["id"]=id
    for i in range(len(menus)):
        if menus[i]["id"]==int(id):
            menus[i]=request_data
    return jsonify({"menus" : menus})

# DELETE /menus/id 해당하는 id에 해당하는 데이터를 삭제한다.
@app.route('/menus/<id>', methods=['DELETE'])
def delete_data(id):
    print(id)
    for i in range(len(menus)):
        if menus[i]["id"]==int(id):
            menus.pop(i)
    return jsonify({"menus" : menus})
    
########## 필수 과제 완료 ##########

if __name__ == '__main__':
    app.run()