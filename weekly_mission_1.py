from flask import Flask, jsonify, request

app = Flask(__name__)

weapons = [{"id": 1, "name": "Gun", "stock": 3}]


@app.route('/')
def hello_world():
    return 'Hello World!'


# 깃헙 아이디 반환
@app.route('/whoami', methods=['GET'])
def who_am_i():
    name = {'name': 'dhelee'}
    return name


# string 반환
@app.route('/echo', methods=['GET'])
def echo():
    value = {'value': request.args.get('string')}
    return value


# Create | 새로운 weapon 추가
@app.route('/weapons', methods=['POST'])
def create():
    request_data = request.get_json()
    new_weapon = {"id": len(weapons) + 1,
                  "name": request_data['name'],
                  "stock": request_data['stock']}
    weapons.append(new_weapon)
    return jsonify(new_weapon)


# Read | 현재 존재하는 weapon 확인
@app.route('/weapons')
def read():
    return jsonify({'weapons': weapons})


# Update | 현재 존재하는 weapon 중 특정 속성(이름, 수량)을 변경
@app.route('/weapons/<int:weapon_id>', methods=['PUT'])
def update(weapon_id):
    request_data = request.get_json()
    for w in weapons:
        if w['id'] == weapon_id:
            w['name'] = request_data['name']
            w['stock'] = request_data['stock']
    return jsonify({'weapons': weapons})


# Delete | 현재 존재하는 특정 weapon 삭제
@app.route('/weapons/<int:weapon_id>', methods=['DELETE'])
def delete(weapon_id):
    for i, m in enumerate(weapons):
        if m['id'] == weapon_id:
            del weapons[i]
            break
    return jsonify({'weapons': weapons})


if __name__ == '__main__':
    app.run()
