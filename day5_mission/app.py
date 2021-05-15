from flask import Flask, jsonify, request, json

app = Flask(__name__)

weapons = []
weapon_cnt = 0
weapon_id = []

@app.route('/')
def root_page():
    return "mission week4"

@app.route('/whoami', methods=['GET'])
def get_github_id():
    my_name = {
        "id": "dohoonsong",
        "name": "DoHoonSong"
    }
    return jsonify(my_name)

@app.route('/echo', methods=['POST'])
def get_echo():
    # args_dict = request.args.to_dict()
    s = request.args["string"]
    echo = {
        "value": s
    }
    return jsonify(echo)

@app.route('/create', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    new_name = request_data['name']
    new_stock = int(request_data['stock'])
    new_weapon = {
        "id": len(weapon_id),
        "name": new_name,
        "stock": new_stock
    }
    weapon_id.append(len(weapon_id))
    weapons.append(new_weapon)
    return jsonify(new_weapon)

@app.route('/read', methods=['GET'])
def read_weapon():
    return jsonify({"weapons": weapons, "count": len(weapons)})

@app.route('/update/<id>', methods=['PUT'])
def update_weapon(id):
    request_data = request.get_json()
    update_id = int(id)
    new_name = request_data['name']
    new_stock = request_data['stock']
    new_weapon = {}
    for w in weapons:
        if w['id'] == update_id:
            if not new_name=='':
                w['name'] = new_name
            if not new_stock=='':
                w['stock'] = new_stock
            new_weapon = w
            break
    return jsonify(new_weapon)

@app.route('/delete/<id>', methods=['DELETE'])
def delete_weapon(id):
    r = False
    num = int(id)
    for w in weapons:
        if w['id'] == num:
            weapons.remove(w)
            r = True
            break
    return jsonify({"deleted": r, "weapons": weapons, "count": len(weapons)})

if __name__== '__main__':
    weapon_cnt = 0
    app.run()