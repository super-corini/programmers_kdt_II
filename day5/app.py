from flask import Flask, jsonify, request

app = Flask(__name__) #flask를 바탕으로한 객체를 생성 

weapons = [
    {"id" : 1 ,"name":"meow_punch", "stock":2}
]

whoami = {"name": "mioow"}


@app.route('/') #@ 파이썬 데코레이터
def hello_flask():
    return "bicsubi"

# GET /whoami | 자료를 가지고 온다.
@app.route('/whoami')
def get_gitName():
    return jsonify(whoami)

@app.route('/echo')
def echo():
    str = request.args.get('string')
    return jsonify({"value" : str})

@app.route('/weapons')
def get_weapon():
    return jsonify(weapons)

# POST (like... INSERT)/weapon | 자료를 자원에 추가한다.
@app.route('/weapons', methods=['POST'])
def crate_weapon(): # request가 JSON이라고 가정

    idx = len(weapons) + 1

    # 전달받은 자료를 weapon 자원에 추가
    request_data = request.get_json()

    new_weapon = {
        "id" : idx,
        "name" : request_data['name'],
        "stock" : request_data['stock'],
        }
    weapons.append(new_weapon)

    return jsonify(new_weapon)


# PUT(UPDATE) /weapons/id | 자료를 수정한다
@app.route('/weapons/<int:id>', methods=['PUT'])
def put_weapon(id):

    request_data = request.get_json()

    update_weapon = {
        'id' : id,
        'name' : request_data['name'],
        'stock' : request_data['stock']
    }

    for i, weapon in enumerate(weapons): # id는 idx보다 1높음
        if weapon['id'] == id:
            weapons[i] = update_weapon #전달받은 데이터를 가지고 업데이트

    return jsonify(update_weapon)

# DELETE /menus/id | 자료를 삭제한다
@app.route('/weapons/<int:id>', methods=['DELETE'])
def delete_menu(id):

    for i, weapon in enumerate(weapons):
        if weapon['id'] == id:
            del_weapon = weapons.pop(i)
            return jsonify(del_weapon)

if __name__ == '__main__': #app.py를 모듈이 아닌 직접적으로 실행될때
    app.run()