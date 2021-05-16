from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_flask():
    return "Hello World!"


@app.route('/whoami')
# GET /whoami
def get_whoami():
    return jsonify({"name": "devmei"})


@app.route('/echo')
# GET /echo
def echo():
    args = request.args.get('string')
    return jsonify({"value": args})


weapons = [
    {"name": "weapon01", "stock": 100},
    {"name": "weapon02", "stock": 500},
    {"name": "weapon03", "stock": 300},
]


@app.route('/weapon')
# GET /weapon
def get_weapon():
    return jsonify({"weapon": weapons})


@app.route('/weapon', methods=['POST'])
# POST /weapon
def create_weapon():
    request_data = request.get_json()  # {"name": ..., "stock": ...}
    new_weapon = {
        "name": request_data['name'],
        "stock": request_data['stock'],
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)


@app.route('/weapon/<string:name>', methods=['PUT'])
def update_weapon(name):
    idx = get_index(name)
    if idx != -1:
        request_data = request.get_json()
        weapons[idx].update(dict(request_data))
        return jsonify(weapons[idx])
    return jsonify({"weapon": weapons})


@app.route('/weapon/<string:name>', methods=['DELETE'])
def delete_weapon(name):
    idx = get_index(name)
    if idx != -1:
        del weapons[idx]
    return jsonify({"weapon": weapons})


def get_index(name):
    for i in range(len(weapons)):
        if name == weapons[i].get('name'):
            return i
    # 해당 index 값이 없을 때 예외처리 필요
    return -1


if __name__ == '__main__':
    app.run()
