# Mission1_core (Flask 이용)
# bicsubi_core_20210514
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Weapons(db.Model):
    name = db.Column(db.String(60), primary_key = True)
    stock = db.Column(db.Integer, nullable = False)

# 첫 시작에 db 생성을 위해 반드시 필요
db.create_all()

# Home Directory
@app.route('/')
def hello_bicsubi():
    return "I'm not a Sirii, I'm just bicsubi. This is Mission 1."

# Get | whoami
@app.route('/whoami')
def who_am_i():
    return jsonify({'name': 'SeongwonTak' })

# Get | whoami
@app.route('/echo')
def return_string():
    string = request.args.get('string')
    return jsonify({"string":string})

# Get | 자료를 가지고 옴 (READ)
@app.route('/weapons')
def get_weapons():
    return jsonify([
       {'name':weapon.name,
        'stock':weapon.stock
        } for weapon in Weapons.query.all()])

# POST | 자원 추가 (CREATE)
@app.route('/weapons', methods=['POST'])
def post_weapons(): # request가 JSON이라고 가정한다.
    try:
        request_data = request.get_json()
        new_weapon = Weapons(name=request_data['name'],
                        stock=request_data['stock'])

        if new_weapon.stock <= 0 or type(new_weapon.stock) is not int:
            return 'Error Code 02 : Stock value must be positive integer'
        else:
            db.session.add(new_weapon)
            db.session.commit()

        return jsonify([
            {'name': weapon.name,
         '  stock': weapon.stock
            } for weapon in Weapons.query.all()])
    except exc.IntegrityError :
        return 'Error Code 01 : duplicated name exists in Weapons'


@app.route('/weapons/<string:name>', methods=['PUT'])
def put_weapons(name):
    try:
        alter_weapon = Weapons.query.get_or_404(name)
        update_data = request.get_json()

        alter_weapon.name = update_data['name']
        alter_weapon.stock = update_data['stock']

        if alter_weapon.stock <= 0 or type(alter_weapon.stock) is not int:
            return 'Error Code 02 : Stock value must be positive integer'
        else:
            db.session.commit()

        return jsonify([
            {'name': alter_weapon.name,
            'stock': alter_weapon.stock
            }])
    except exc.IntegrityError :
        return 'Error Code 01 : duplicated name exists in Weapons'

@app.route('/weapons/<string:name>', methods=['DELETE'])
def delete_weapons(name):
    del_weapon = Weapons.query.get_or_404(name)
    db.session.delete(del_weapon)
    db.session.commit()

    return jsonify([
        {'name': weapon.name,
         'stock': weapon.stock
         } for weapon in Weapons.query.all()])


if __name__ == '__main__':
    app.run()
