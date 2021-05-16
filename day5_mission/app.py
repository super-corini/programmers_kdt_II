from flask import Flask, request, jsonify
from model import Weapons, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////.weapons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.app = app
db.create_all()

my_id = {'name': "developerchoi90"}


@app.route('/')
def home():
    return "I'm Bicsubi, What do yo want to do?"


# 1. GET/whoami github id를 반환
@app.route('/whoami')
def whoami():
    return jsonify(my_id)


# 2. GET/echo?string="string" 입력된 string 반환
@app.route('/echo')
def echo():
    string = request.args.get('string')
    return jsonify(string)


# 3. GET/weapons 현재 존재하는 weapons을 확인
@app.route('/weapons')
def get_weapons():
    return jsonify(Weapons.get_weapon())


# 4. POST/weapons 새로운 weapon을 추가
@app.route('/weapons', methods=['POST'])
def create_weapon():
    rq_weapon = request.get_json()
    return jsonify(Weapons.add_weapon(rq_weapon['name'], rq_weapon['stock']))


# 5. PUT/weapons update weapons
@app.route('/weapons', methods=['PUT'])
def update_weapon():
    rq_weapon = request.get_json()
    return jsonify(Weapons.update_weapon(rq_weapon['name'], rq_weapon['stock']))


# 6. DELETE/weapons delete weapon
@app.route('weapons', methods=['DELETE'])
def delete_weapon():
    rq_weapon = request.get_json()
    return jsonify(Weapons.delete_weapon(rq_weapon['name']))


if __name__ == '__main__':
    app.run()
