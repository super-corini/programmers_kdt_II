from flask import Flask, jsonify, request, json

app = Flask(__name__)

weapons = []
weapons_cnt = 0


@app.route('/')
def root_page():
    return "Hello"

@app.route('/whoami')
def get_github_id():
    names = {
        "id": "yn-e-si",
        "name": "Jinyong Lee"
    }
    return jsonify(names)

@app.route('/echo')
def echo_string():
    string = request.args.get('string')
    return jsonify({"value": string})

@app.route('/weapon', methods=['POST'])
def create_weapon():
    request_data = request.get_json()

    new_weapon = {
        
        "name": request_data['name'],
        "stock": request_data['stock']
    }
    
    weapons.append(new_weapon)
    return jsonify(new_weapon)

@app.route('/weapon')
def read_weapon():
    return jsonify({"weapons": weapons})

@app.route('/weapon/<str:name>', methods=['PUT'])
def update_weapon(name):
    request_data = request.get_json()

    for weapon in weapons:
        if weapon['name'] == name:
            weapon['name'] = request_data['name']
            weapon['stock'] = request_data['stock']
    return jsonify({"weapons": weapons})
 

@app.route('/weapon/<str:name>', methods=['DELETE'])
def delete_weapon(name):
        
    weapons.sort(key = lambda x:x['name'])    
    idx_value, cnt = 0, 0
    
    for idx, weapon in enumerate(weapons):
        if weapon['name'] == name and cnt ==0: 
           idx_value = idx
           cnt += 1
        elif weapon['name'] == name: 
            cnt += 1
    
    for _ in range(cnt):
        del weapons[idx_value]
        
    return jsonify({"weapons": weapons})


if __name__== '__main__':
    weapon_cnt = 0
    app.run()