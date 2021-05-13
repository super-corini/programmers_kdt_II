from flask import Flask, jsonify, request
from models import db, Weapon
import os

app = Flask(__name__)

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'weapon.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
db.create_all()

# GET /whoami
@app.route('/whoami')
def whoami():
    return jsonify({'name': 'YummyCocopalm'})

# GET /echo?string='string'
@app.route('/echo')
def echo_str():
    request_str = request.args.get('string', type=str)
    return jsonify({'string': request_str})

# POST /weapon
@app.route('/weapon', methods=['POST'])
def create_weapon():
    request_weapon = request.get_json()
    request_name = request_weapon['name']
    new_weapon = Weapon(name=request_name,
                        stock=request_weapon['stock'])
    if Weapon.query.filter_by(name=request_name).first():
        return f'Weapon name {request_name} exists in db.', 400    
    db.session.add(new_weapon)
    db.session.commit()
    return jsonify(new_weapon.serialize)

# GET /weapon
@app.route('/weapon')
def get_weapon():
    return jsonify({'weapons': [w.serialize for w in Weapon.query.all()]})

# PUT /weapon?name="string"
@app.route('/weapon', methods=['PUT'])
def update_weapon():
    request_name = request.args.get('name', type=str)
    request_data = request.get_json()
    weapon = Weapon.query.filter_by(name=request_name).first_or_404(description=f'There is no data with {request_name}')
    for key, value in request_data.items():
        setattr(weapon, key, value)
        db.session.commit()
    return jsonify(weapon.serialize)
# DELETE /weapon?name="string"
@app.route('/weapon', methods=['DELETE'])
def delete_weapon():
    request_name = request.args.get('name', type=str)
    weapon = Weapon.query.filter_by(name=request_name).first_or_404(description=f'There is no data with {request_name}')
    db.session.delete(weapon)
    db.session.commit()
    return jsonify(weapon.serialize)

# DELETE /weapon/init
@app.route('/weapon/init', methods=['DELETE'])
def delete_db():
    if os.path.isfile(dbfile):
        os.remove(dbfile)
    db.init_app(app)
    db.app = app
    db.create_all()
    return get_weapon()

if __name__ == '__main__':
    app.run()