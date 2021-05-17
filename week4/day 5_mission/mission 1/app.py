#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify, request

app = Flask(__name__)

weapon = [
    {"id":1, "name":"Rifle", "stock":3},
    {"id":2, "name":"Pistol", "stock":4},
    {"id":3, "name":"Bazooka", "stock":2},
]
curr_id = len(weapon)

@app.route('/')
def hello_flask():
    return "Hello World"

@app.route('/whoami')
def get_myname():
    return jsonify({"name" : "lltera" })

@app.route('/echo')
def query_string():
    return jsonify({'value' : request.args.get('string')})


@app.route('/weapon')
def read_weapon():
    return jsonify({"weapon" : weapon})

@app.route('/weapon', methods = ['POST'])
def create_weapon():
    global curr_id
    request_data = request.get_json()
    
    for i in range(curr_id):
        if request_data['name'] == weapon[i]['name']:
            return jsonify('This weapon is already existed')
            break
    else:
        curr_id += 1
        new_weapon = {
            "id" : curr_id,
            "name" : request_data['name'],
            "stock" : request_data['stock'],
         }
        weapon.append(new_weapon)
        return jsonify(new_weapon)

@app.route('/weapon/<int:id>', methods=['PUT'])
def update_weapon(id):
    update_data = request.get_json()
    weapon[id - 1]["name"] = update_data["name"]
    weapon[id - 1]["stock"] = update_data["stock"]
    return jsonify(weapon[id - 1])

@app.route('/weapon/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    for w in weapon:
        if w['id'] == id:
            del weapon[weapon.index(w)]
            break
    else:
        return "there in no weapon"
    return jsonify(weapon)

    
if __name__ == "__main__":
    app.run()
