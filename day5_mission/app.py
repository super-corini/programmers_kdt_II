from flask import Flask, jsonify, request, json

app = Flask(__name__)

weapons = [
    {"id":1, "name":"Gun", "stock":20},
    {"id":2, "name":"Sword", "stock":45},
]

# Main
@app.route('/')
def root_page():
    return "Week4-Day5 (Mission 1. My New Assistant) Core Mission"

# READ(GET) /whoami | 깃헙 ID와 이름을 가지고 온다.
@app.route('/whoami', methods=['GET'])
def get_github_id():
    my_name = {
        "id": "junyup2\n",
        "name": "JunYupLee"
    }
    return jsonify(my_name)

# CREATE(GET) /echo |
@app.route('/echo', methods=['GET'])
def get_echo():
    echo = {
        "value": "string"
    }
    return jsonify(echo)

# READ(GET) /weapon | 자료를 가지고 온다.
@app.route('/weapon')
def get_weapons():
    return jsonify({"weapons" : weapons})

# CREATE(POST) /weapon | 자료를 자원에 추가한다.
@app.route('/weapon', methods=['POST'])
def create_weapon():
    request_data = request.get_json() # {"name" : ..., "stock": ...}
    new_weapon = {
        "id" : len(weapons) + 1,
        "name" : request_data['name'],
        "stock" : request_data['stock'],
    }
    weapons.append(new_weapon)
    return jsonify(new_weapon)

# UPDATE
@app.route('/weapon/<int:id>',methods=['PUT'])
def update_weapons(id):
    request_data = request.get_json()
    try:
        weapons[id-1]['name'] = request_data['name']
        weapons[id-1]['stock'] = request_data['stock']
        return jsonify({"weapons" : weapons})
    except Exception as e:
        return  f'해당 id가 존재하지 않습니다.: {e}'

# DELETE
@app.route('/weapon/<int:id>',methods=['DELETE'])
def delete_weapon(id):
    try:
        # id를 확인
        id_l = len(weapons)
        if id_l == id:
            del weapons[id-1]
        else:
            del weapons[id-1]
            for i in range(id_l-id):
                weapons[id+i-1]['id'] = id+i
        return jsonify({"weapons" : weapons})
    except Exception as e:
        return  f'해당 id가 존재하지 않습니다.: {e}'

if __name__ == '__main__':
    app.run()