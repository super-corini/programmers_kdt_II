from flask import Flask, jsonify, request

app = Flask(__name__)


my_name = [
    {
        "name" : "rsh1994"
    }
]


@app.route('/')
def week4_day5():
    return "week4_day5 mission"

# GET /whoami | github id를 반환
@app.route('/whoami')
def get_who():
    return jsonify(my_name)


# GET /echo?string="string"
@app.route('/echo')
def get_string():
    order = request.args.get('string')
    if order:
        return jsonify({"value":order})
    return jsonify({"no no"})

weapon_list = []
weapon_name = []

# GET / | 무기 리스트를 조회한다.
@app.route('/weapon')
def get_weapon():
    return jsonify({"weapon" : weapon_list})

# POST | 새로운 무기를 추가한다. 무기가 이미 있으면 오류가 뜬다.
@app.route('/weapon/', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    if request_data['name'] not in weapon_name:
        new_weapon = {
            "name": request_data['name'],
            "stock": request_data['stock']
        }
        weapon_list.append(new_weapon)
        weapon_name.append(request_data['name'])
    return jsonify(new_weapon)


# GET /weapon/<string:name> | 무기를 조회한다.
@app.route('/weapon/<string:name>', methods=['GET'])
def read_weapon(name):
    for idx, w in enumerate(weapon_list):
        if w['name'] == name:
            return jsonify(w)
    return jsonify("X")
# POST /waepon/<string:name> | 무기를 조회한다.
@app.route('/weapon/<string:name>', methods=['POST'])
def modify_weapon(name):
    request_data = request.get_json()
    for idx, w in enumerate(weapon_list):
        if w['name'] ==name:
            w['name'] = request_data['name']
            w['stock'] = request_data['stock']
            return jsonify(w['name'])
    return jsonify("X")

# DELETE /menus<int:name> | 해당 name의 데이터를 삭제한다.
@app.route('/weapon/<string:name>', methods=['DELETE'])
def delete_weapon(name):
    for idx, w in enumerate(weapon_list):
        if w['name'] == name:
            del weapon_list[idx]
            return jsonify(w)
    return jsonify("X")



if __name__ == '__main__':
    app.run()
