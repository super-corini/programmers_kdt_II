from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]

@app.route('/') # 홈 dir에 접근하는 주소
def hello_flask():
    return "hello world"

# Get /menus | 자료를 가지고 온다.
# app.route(*, methods=['GET']) : 기본적으로 route의 methods는 GET으로 설정되어 있다.
@app.route('/menus') # menus 자료에 접근
def get_menus():
    #jsonify는 dict형태만 입력받을 수 있다.
    return jsonify({"menus":menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()

    new_id = len(menus)+1
    for check, id in enumerate(sorted(map(lambda x: x['id'], menus)), start=1):
        if check != id:
            new_id = check
            break

    new_menu = {
        "id": new_id,
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    for m in menus:
        if m['id'] == id:
            m['name'] = request_data['name']
            m['price'] = request_data['price']
            break
    else:
        return "No id" + str(id)
    return jsonify(request_data)

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for i, m in enumerate(menus):
        if m['id'] == id:
            return jsonify(menus.pop(i))
    return "No id" + str(id)

if __name__=='__main__':
    app.run()