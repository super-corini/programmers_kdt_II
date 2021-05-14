from flask import Flask, jsonify, request


app = Flask(__name__)


weapons = []
idx = 1


@app.route('/')
def hello_flask():
    return "WEEK4 DAY5"


# github id return
@app.route('/whoami')
def get_user_id():
    return jsonify({'name': 'khakha93'})


# string return
@app.route('/echo')
def chk_string():
    txt = request.args.get('string', '')
    return jsonify({'value': txt})


# Read
@app.route('/weapons')
def get_menus():
    return jsonify({'weapons': weapons})


# Create
@app.route('/weapons', methods=['POST'])
def create_menu():
    global idx
    # 전달 받은 자료를 weapons 에 추가
    request_data = request.get_json()
    new_menu = {
        'id': idx,
        'name': request_data['name'],
        'stock ': request_data['stock']
    }
    idx += 1
    weapons.append(new_menu)
    return jsonify(new_menu)


# UPDATE, DELETE
@app.route('/weapons/<int:weapon_id>', methods=['PUT', 'DELETE'])
def update_menu(weapon_id):

    # 무기 변경
    if request.method == 'PUT':
        request_data = request.get_json()

        # 해당 무기 찾아서 바꾸기
        for weapon in weapons:
            if weapon['id'] == weapon_id:
                weapon['name'] = request_data['name']
                weapon['stock'] = request_data['stock']
                return jsonify(weapon)

    # 무기 삭제
    if request.method == 'DELETE':
        # 해당 무기 찾아서 바꾸기
        for i, weapon in enumerate(weapons):
            if weapon['id'] == weapon_id:
                return jsonify(weapons.pop(i))

    return jsonify({})


if __name__ == '__main__':
    app.run()