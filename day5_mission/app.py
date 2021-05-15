from flask import Flask, jsonify, request

app  = Flask(__name__) 

user_name = {'name':'cyssu73'}

weapons = [
    {"name":"자료구조","stock":1},
    {"name":"선형대수","stock":2},
    {"name":"numpy", "stock":3}
]

@app.route('/whoami')
def my_name():
    return jsonify(user_name)

@app.route('/echo')
def echo():
    string = request.args.get('string')
    echo_value = {'value':string}
    return jsonify(echo_value)

@app.route('/weapon') 
def read_weapon():
    return jsonify({"weapons":weapons})

@app.route('/weapon',methods=['POST'])
def create_weapon():
    request_data = request.get_json() 
    new_weapon = {
        'name': request_data['name'],
        'stock':request_data['stock']
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)

@app.route('/weapon',methods=['PUT'])
def update_weapons():
    name = request.args.get('name')
    request_data = request.get_json()
    for weapon in weapons:
        print(weapon['name'],name)
        if weapon['name']==name:
            weapon['name'] = request_data['name']
            weapon['stock'] = request_data['stock']
            return jsonify({"weapons":weapons})
    else:
        return 'Wrong Name'

@app.route('/weapon',methods=['DELETE']) 
def delete_weapon():
    name = request.args.get('name')
    for i, weapon in enumerate(weapons):
        if weapon['name']==name:
            del weapons[i]
            return jsonify({"weapons":weapons})
    else:
        return 'Wrong Name'

    
if __name__ == '__main__': 
    app.run()

