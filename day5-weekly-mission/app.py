from flask import Flask, jsonify, request


app = Flask(__name__)


weapon = [
    {"name" : "test weapon", "stock" : 1}
]


@app.route('/')
def hello_flask():
    return "Hello World"


@app.route('/whoami', methods=['GET'])
def whoami():
    return jsonify({"name" : "DongIk-Jang"})


@app.route('/echo')
def echo():
    echo_string = request.args.get('string', '')
    return jsonify({"value" : echo_string})


@app.route('/weapons/create', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    new_weapon = {
        "name" : request_data['name'],
        "stock" : request_data['stock']
    }
    for i in range(len(weapon)):
        if weapon[i]['name'] == request_data['name']:
            weapon[i]['stock'] += request_data['stock']
            return jsonify(new_weapon)
    else:
        weapon.append(new_weapon)
        return jsonify(new_weapon)


@app.route('/weapons/read')
def read_weapon():
    return jsonify(weapon)


@app.route('/weapons/update', methods=['PUT'])
def update_weapon():
    request_data = request.get_json()
    update_weapon = {
        "name" : request_data['name'],
        "stock" : request_data['stock']
    }
    for i in range(len(weapon)):
        if weapon[i]['name'] == request_data['name']:
            weapon[i] = update_weapon
    return jsonify(update_weapon)


@app.route('/weapons/delete', methods=['DELETE'])
def delete_weapon():
    request_data = request.get_json()
    for i in range(len(weapon)):
        if weapon[i]['name'] == request_data['name']:
            if weapon[i]['stock'] >= request_data['stock']:
                weapon[i]['stock'] -= request_data['stock']
                #deleted_weapon = weapon.pop(i)
                return jsonify({"weapons": weapon})
            if weapon[i]['stock'] < request_data['stock']:
                deleted_weapon = weapon.pop(i)
                return jsonify({"deleted weapon" : deleted_weapon})
            else:
                return "this weapon is out of stock"


if __name__ == '__main__':
    app.run()

