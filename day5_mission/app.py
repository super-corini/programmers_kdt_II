import os
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db = SQLAlchemy(app)

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    stock = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'stock': self.stock
        }

db.init_app(app)
db.app = app
db.create_all()

@app.route('/whoami')
def whoami():
    return jsonify({"name": "Han-D-Peter"})

@app.route('/echo')
def echo_parameter():
    param = request.args.to_dict()['string']
    param = str(param)
    return jsonify({"value": param})

@app.route('/weapon')
def all_weapon():
    weapons = Weapon.query.all()
    return jsonify([i.serialize() for i in weapons])
    
@app.route('/weapon', methods=["POST"])
def create_weapon():
    request_data = request.get_json()
    print(request_data)
    weapon = Weapon(name=request_data['name'], stock=request_data['stock'])
    db.session.add(weapon)
    db.session.commit()
    return weapon.serialize()


@app.route('/weapon', methods=['PUT'])
def modify_weapon():
    request_data = request.get_json()
    param = request.args.to_dict()['name']
    param = str(param)
    target_weapon = Weapon.query.filter_by(name=param).first()
    
    target_weapon.name = request_data['name']
    target_weapon.stock = request_data['stock']

    db.session.commit()

    return f"{param} has been modified"

@app.route('/weapon', methods=["DELETE"])
def delete_weapon():
    param = request.args.to_dict()['name']
    param = str(param)

    target_weapon = Weapon.query.get(name=param)

    db.session.delete(target_weapon)
    db.session.commit()
    
    return f"{param} has been deleted"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)