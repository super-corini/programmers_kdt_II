from flask import Flask, jsonify, request

app = Flask(__name__)

weapons = list()

# GET /whoami | github id를 반환.
@app.route('/whoami')
def get_gitid():
    return jsonify({"name" : "rabbit1996"})

# GET /echo?string="string" | "string"을 반환.
@app.route('/echo')
def echo():
    args = request.args.get('string')
    return jsonify({"value" : args})

# POST /weapons | 자료를 자원에 추가한다.
@app.route('/weapons', methods=['POST'])
def create_weapons(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가,
    request_data = request.get_json() # {"name" : ..., "stock":...}

    # id값 결정
    id = 1 if len(weapons) < 1 else (weapons[-1]['id'] + 1)

    new_weapon = {
        "id" : id,
        "name" : request_data["name"],
        "stock": request_data["stock"],
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)

# GET /weapons | 모든 자료를 가지고 온다.
@app.route('/weapons')
def get_weapons():
    return jsonify({"weapons" : weapons})

# GET /weapons | 특정 index의 자료를 가지고 온다.
@app.route('/weapons/<int:id>')
def get_weapons_id(id):
    # 읽을 weapon을 research
    for i,w in enumerate(weapons):
        if w['id'] == id:
            idx = i
            break

    return jsonify(weapons[idx])

# PUT /weapons | 자원을 업데이트 한다.
@app.route('/weapons/<int:id>', methods=['PUT'])
def update_weapons(id): # request가 JSON이라고 가정
    # 수정할 weapons를 search
    for i,w in enumerate(weapons):
        if w['id'] == id:
            idx = i
            break

    request_data = request.get_json() # {"name" : ..., "stock":...}
    weapons[idx] = {
        "id" : weapons[idx]['id'],
        "name" : request_data['name'],
        "stock": request_data['stock'],
    }
    return jsonify(weapons[idx])

# DELETE /weapons | 특정 자료를 자원에서 삭제한다.
@app.route('/weapons/<int:id>', methods=['DELETE'])
def delete_weapons(id): # request가 JSON이라고 가정
    # 삭제할 weapons를 search
    for i, w in enumerate(weapons):
        if w['id'] == id:
            idx = i
            break

    deleted_weapons = weapons.pop(idx)
    return jsonify(deleted_weapons)

if __name__ == '__main__':
    app.run()