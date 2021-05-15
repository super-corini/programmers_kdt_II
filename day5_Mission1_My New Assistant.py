from flask import Flask, jsonify, request

app = Flask(__name__)

weapons = [
    
]

### 깃허브 아이디 반환
@app.route('/whoami')
def whoami():
    return jsonify({"name":"ohjongseo"})

# Query String
@app.route('/echo')
def echo_string():
    text = request.args.get('string')
    data = {
        "string" : text
    }
    return jsonify(data)

# Create Weapon
@app.route('/weapon', methods=['POST'])
def create_weapon(): 
    request_data = request.get_json()
    new_weapon = {
        "name" : request_data['name'],
        "stock" : request_data['stock']
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)

# Read Weapon
@app.route('/weapon')
def read_weapon():
    return jsonify({"weapon" :weapons})

# Update Weapon
@app.route('/weapon/<string:name>', methods=['PUT'])
def update_menu(name):
    request_data = request.get_json()
    weapon_count = len(weapons)
    for weapon in weapons:
        if weapon['name'] == name:
            weapon['stock'] = request_data['stock']
            break
        weapon_count -= 1
        if weapon_count == 0:
            '무기가 없습니다.'

    return jsonify({"menus" :weapons})


# DELETE Weapon
@app.route('/weapon/<string:name>', methods=['DELETE'])
def delete_menu(name):
    request_data = request.get_json()
    for weapon in weapons:
        if weapon['name'] == name:
            remove_data = weapon
            break
    weapons.remove(remove_data)
    return jsonify({"menus" :weapons})

if __name__ == '__main__':
    app.run()