from flask import Flask, jsonify, request

app = Flask(__name__)

whoami = [
    {"name": "heejuhee(ujst02@gmail.com)"}
]


weapon = [
    {"name": "weaponA", "stock": 5},
    {"name": "weaponB", "stock": 4},
    {"name": "weaponC", "stock": 3},
]


@app.route('/') # home 디렉토리
def gello_flask():
    return "Day5 Mission"

# GET/whoami : 자료를 가지고 온다
@app.route('/whoami')
def get_whoami():
    # return값을 꼭 json으로 해야
    return jsonify({"name": whoami})

# GET /echo?string="string"
@app.route('/echo', methods = ['GET'])
def echo(): ##str????
    # print(str)
    # return값을 꼭 json으로 해야
    string = request.args.get("string")
    return jsonify({"string": string})




# Create(POST) : 새로운 weapon 을 추가
# /weapon/weapon_name
@app.route('/weapon/<string:name>', methods=['POST'])
def create_weapon(name): # request가 JSON이라고 가정
    request_data = request.get_json() # {"name" : ... , "price" : ...}
    new_weapon = {
        "name": request_data["name"],
        "price": request_data["stock"],
    }
    weapon.append(new_weapon)
    return jsonify(new_weapon)


# Read(GET) : 현재 존재하는 weapon 을 확인
# /weapon
@app.route('/weapon', methods=['GET'])
def read_weapon():
    return jsonify(weapon)

# Update(PUT) : 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경
# /weapon/weapon_name
@app.route('/weapon/<string:name>', methods=['PUT'])
def update_weapon(name):
    request_data = request.get_json()
    for w in weapon:
        if w.get("name", -1) == name:
            w["name"] = request_data["name"]
            w["stock"] = request_data["stock"]
    return jsonify({"weapon": weapon})

# Delete(DELETE) : 현재 존재하는 특정 weapon 을 삭제
# /weapon/weapon_name
@app.route('/weapon/<string:name>', methods=['DELETE'])
def delete_weapon(name):
    request_data = request.get_json()
    for i in range(len(weapon)):
        if weapon[i].get("name", -1) == name:
            weapon.pop(i)
            break
    return jsonify({"weapon": weapon})



if __name__ == '__main__':
    app.run()


