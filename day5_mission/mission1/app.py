import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app  = Flask(__name__)

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
db = SQLAlchemy(app)

user_name = {'name' : 'kim-jeonghyun'}

class Weapons(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    stock = db.Column(db.Integer)

# db 생성
db.create_all()

# home
@app.route('/')
def home():
    return "Welcome! I'm Bicsubi."

# 1. GET /whoami github id를 반환
@app.route('/whoami')
def whoami():
    return jsonify(user_name)

# 2. GET /echo?string="string" 입력된 string 반환
@app.route('/echo')
def echo():
    string = request.args.get('string')
    return jsonify({'value': string})

# 3. GET /weapons 현재 존재하는 weapon 을 확인
@app.route('/weapons')
def get_weapons():
    weapons = []
    for w in Weapons.query.all():
        weapon= {}
        weapon['name'] = w.name
        weapon['stock'] = w.stock
        weapons.append(weapon)
    return jsonify({'weapons': weapons})

# 4. POST /create_weapons 새로운 weapon 을 추가
@app.route('/create_weapons', methods=['POST'])
def add_weapon():
    req = request.get_json()
    weapon = Weapons(name=req['name'], stock=req['stock'])
    db.session.add(weapon)
    db.session.commit()
    return "The addition has successfully completed."

# 5. PUT /update_weapons 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경
@app.route('/update_weapons', methods=['PUT'])
def update_weapon():
    req = request.get_json()
    Weapons.query.filter_by(name=req['name']).update(dict(stock=req['stock']))
    db.session.commit()
    return "The update has successfully completed."


# 6. DELETE / delete_weapons 현재 존재하는 특정 weapon 을 삭제
@app.route('/delete_weapons', methods=['DELETE'])
def delete_weapon():
    req = request.get_json()
    Weapons.query.filter_by(name=req['name']).delete()
    db.session.commit()

    return "The deletion has successfully completed."

if __name__ == '__main__':
    app.run()