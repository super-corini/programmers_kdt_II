from flask import Flask, jsonify, request

app = Flask(__name__)

weapon = [{'name':'목검', 'stock':1}]

@app.route('/')
def hello_flask():
    return "hello bronze-man"

@app.route('/whoami')
def whoami():
    return jsonify({'name':"xcellentbird"})

@app.route('/echo/<string:s>')
def get_string(s):
    return jsonify({"value":s})

@app.route('/weapon', methods=['POST'])
def create_weapon():
    new_stuff = request.get_json()
    for i in range(len(weapon)):
        if weapon[i]['name'] == new_stuff['name']:
            weapon[i]['stock'] += 1
            break
    else:
        weapon.append({'name':new_stuff['name'], 'stock':1})
    return jsonify({'weapon':weapon})

@app.route('/weapon')
def read_weapon():
    return jsonify({'weapon':weapon})

@app.route('/weapon/<int:index>', methods=['PUT'])
def update_weapon(index):
    if index >= len(weapon):
        return 'No weapon ' + str(index)

    new_data = request.get_json()

    weapon[index]['name'] = new_data['name']
    weapon[index]['stock'] = new_data['stock']
    return jsonify({'weapon':weapon})

@app.route('/weapon', methods=['DELETE'])
def delete_weapon():
    del_order = request.get_json()
    for i in range(len(weapon)):
        if weapon[i]['name'] == del_order['name']:
            return jsonify(weapon.pop(i))
    return 'No weapon ' + del_order['name']

if __name__=='__main__':
    app.run()