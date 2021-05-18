from flask import Flask, jsonify, request

app = Flask(__name__)

weapons = [
    {'name': 'default', 'stock': 1},
]


@app.route('/')
def hello_flask():
    return 'Hello weapon'


# GET /weapon?name=str  | 현재 존재하는 weapon 을 확인
@app.route('/weapon')
def get_weapon():
    name = request.args.get('name')

    # 파라미터가 있으면 해당요소만 출력, 없으면 전체출력
    if name:
        # name 확인
        idx = -1
        for n, i in enumerate(weapons):
            if i['name'] == name:
                idx = n

        if idx != -1:
            return weapons[idx]
        else:
            return 'Can not find name: {}'.format(name)
    else:
        return jsonify({'weapons': weapons})


# POST /weapon  | 새로운 weapon을 추가
@app.route('/weapon', methods=['POST'])
def create_weapon():  # request가 JSON이라고 가정
    request_data = request.get_json()  # {'name': ..., 'stock': ...}
    new_weapon = {
        'name': request_data['name'],
        'price': int(request_data['stock']),
    }
    weapons.append(new_weapon)
    return new_weapon


# PUT /weapon?name=str&stock=int&new_name=str | 현재 존재하는 weapon의 속성(이름, 수량) 변경
@app.route('/weapon', methods=['PUT'])
def update_weapon():
    name = request.args.get('name')
    stock = request.args.get('stock')
    new_name = request.args.get('new_name')

    if not new_name:
        new_name = name

    # name 확인
    idx = -1
    for n, i in enumerate(weapons):
        if i['name'] == name:
            idx = n

    if idx != -1:
        # 데이터 변경
        update_weapon = {
            'name': new_name,
            'stock': int(stock),
        }
        weapons[idx] = update_weapon
    else:
        return 'Can not find name or stock: {} or {}'.format(name, stock)

    return weapons[idx]


# DELETE /weapon?name=str | 현재 존재하는 특정 weapon 을 삭제
@app.route('/weapon', methods=['DELETE'])
def delete_weapon():
    name = request.args.get('name')

    # name 확인
    idx = -1
    for n, i in enumerate(weapons):
        if i['name'] == name:
            idx = n

    if idx != -1:
        # 데이터 삭제
        weapons.pop(idx)
    else:
        return 'Can not find name: {}'.format(name)

    return jsonify({'weapons': weapons})


if __name__ == '__main__':
    app.run()
