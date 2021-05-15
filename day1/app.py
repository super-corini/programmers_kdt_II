from flask import Flask, jsonify, request

app = Flask(__name__)   # 이름으로 생성한 Flask 객체 생성

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]

@app.route('/')     # '/'가 등장했을때, 아래의 함수를 실행해라
def hello_flask():
    return "Hello World"

# GET /menus | 자료를 가져온다
@app.route('/menus')       # GET은 methods 생략 가능
def get_menus():
    return jsonify({"menus":menus})     # 리스트는 json으로 만들 수 없다.

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():      # request가 json이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()   # {"id":... , "name":... , "price":...}
    new_menu = {
        "id": len(menus)+1,
        "name": request_data["name"],
        "price": request_data["price"]
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT
@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    request_data = request.get_json()
    for i in range(len(menus)):
        if id==menus[i]["id"]:
            menus[i]["name"] = request_data["name"]
            menus[i]["price"] = request_data["price"]
            break
    else:
        return "ID not Found"
    update_menu = {
        "id": id,
        "name": request_data["name"],
        "price": request_data["price"]
    }
    return jsonify(update_menu)

# DELETE
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    request_data = request.get_json()
    for i in range(len(menus)):
        if id==menus[i]["id"]:
            menus.pop(i)
            break
    else:
        return "ID not Found"
    return jsonify({"menus": menus})

if __name__ == '__main__':      # app.py를 직접 실행한 경우 (모듈로 실행되는게 아닌..)
    app.run()