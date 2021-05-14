from flask import json, request, Flask, jsonify

app = Flask(__name__)

github_id = 'LeeSeongYeob'
"""
weapon 의 값 : {str: name : int:stock}
"""
weapons = []


@app.route('/')
def init_page():
    return '초기 화면 입니다.!'


@app.route('/whoami')
def get_github():
    return jsonify({'name': github_id})


@app.route('/echo')
def echo_query():
    val = request.args.get('string')
    if val:
        return jsonify({'value': val})


"""
get_weapon():
현재 저장되어 있는 무기의 정보를 가져옴
return : weapons
"""


@app.route('/weapon', methods=['GET'])
def get_weapon():
    return jsonify({"weapons": weapons})


"""
put_weapon():
새로운 무기 정보를 입력받아 weapons list에 저장함
return : 새롭게 추가한 weapon 정보
"""


@app.route('/weapon', methods=['POST'])
def put_weapon():
    request_data = request.get_json()
    new_weapon = {
        'name': request_data['name'],
        'stock': request_data['stock']
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)


"""
update_weapon()
Update 하려는 무기의 이름을 입력받아 새로운 정보로 update 하는 함수
return : weapons
"""


@app.route('/weapon/<string:name>', methods=['PUT'])
def update_weapon(name):
    print(weapons)
    request_data = request.get_json()
    for weapon in weapons:
        print(weapon['name'])
        if weapon['name'] == name:
            weapon['name'] = request_data['name']
            weapon['stock'] = request_data['stock']
            break
    else:
        return 'Not Found weapon'
    return jsonify({'weapons': weapons})


"""
del_weapon()
Delete 하려는 무기의 이름을 입력받아 해당하는 data를 삭제
return : weapons
"""


@app.route('/weapon/<string:name>', methods=['DELETE'])
def del_weapon(name):
    for idx, weapon in enumerate(weapons):
        if weapon['name'] == name:
            weapons.pop(idx)
            break
    else:
        return 'Not Found weapon'
    return jsonify({'weapons': weapons})


if __name__ == '__main__':
    app.run(debug=True)
