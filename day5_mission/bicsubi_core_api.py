from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

@app.route('/')
def hello_flask():
    return "Hello World!"

@app.route('/whoami')
def show_githubid():
    return jsonify({"name": "spongebob03"})

@app.route('/echo')
def echo_string():
    string = request.args.get('string')
    return jsonify({"value": string})

@app.route('/weapon')
def read_weapon():
    weapons = []
    for weapon in Weapon.query.all():
        weapons.append({'weapon': weapon.name, 'stock': weapon.stock})
    return jsonify({"weapons": weapons})

@app.route('/weapon',methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    weapon = Weapon(name=request_data['name'], stock=request_data['stock'])
    db.session.add(weapon)
    db.session.commit()
    
    weapons = []
    for weapon in Weapon.query.all():
        weapons.append({'weapon': weapon.name, 'stock': weapon.stock})
    return jsonify({"weapons": weapons})

@app.route('/weapon/<string:name>', methods=['PUT'])
def update_weapon(name):
    request_data = request.get_json()
    weapon = Weapon.query.filter_by(name=name).first()
    weapon.name = request_data['name']
    weapon.stock = request_data['stock']
    db.session.commit()
    
    weapons = []
    for weapon in Weapon.query.all():
        weapons.append({'weapon': weapon.name, 'stock': weapon.stock})
    return jsonify({"weapons": weapons})

@app.route('/weapon/<string:name>', methods=['DELETE'])
def delete_weapon(name):
    weapon = Weapon.query.filter_by(name=name).first()
    db.session.delete(weapon)
    db.session.commit()
    
    weapons = []
    for weapon in Weapon.query.all():
        weapons.append({'weapon': weapon.name, 'stock': weapon.stock})
    return jsonify({"weapons": weapons})

if __name__ == '__main__':
    app.run(debug=True)