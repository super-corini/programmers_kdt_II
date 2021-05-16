from flask import Flask, jsonify, request

app = Flask(__name__)

weapons = []

@app.route('/')
def init():
    return "hi!"

# GET /whoami
@app.route('/whoami')
def whoami():
    return jsonify({"name":"Namkwangwoon"})

# GET /echo?string="string"
@app.route('/echo')
def echo():
    value = request.args.get("string")
    return jsonify({"value":value})

# GET /weapons
@app.route('/weapons')
def get_weapons():
    return jsonify({"weapons":weapons})

# POST /weapons
@app.route('/weapons', methods=['POST'])
def post_weapons():
    request_data = request.get_json()
    new_weapon = {
        "id": len(weapons)+1,
        "name": request_data["name"],
        "stock": request_data["stock"]
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)

# PUT /weapons/echo?name="name"
@app.route('/weapons/<string:name>', methods=["PUT"])
def change_weapon(name):
    request_data = request.get_json()
    for i in range(len(weapons)):
        if name==weapons[i]["name"]:
            weapons[i]["name"] = request_data["name"]
            weapons[i]["stock"] = request_data["stock"]
            break
    else:
        return "weapon name not found"
    return jsonify({"weapons":weapons})

# DELETE /weapons/echo?name="name"
@app.route('/weapons/<string:name>', methods=["DELETE"])
def delete_weapon(name):
    request_data = request.get_json()
    for i in range(len(weapons)):
        if name==weapons[i]["name"]:
            weapons.pop(i)
            break
    else:
        return "weapon name not found"
    return jsonify({"weapons":weapons})

if __name__ == '__main__':
    app.run()