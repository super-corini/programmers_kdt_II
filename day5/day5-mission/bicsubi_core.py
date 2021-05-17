import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'weapon.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.create_all()


class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=32))
    stock = db.Column(db.Integer)

    def __repr__(self):
        return str(self.serialize)

    @property
    def serialize(self):
        return {'id': self.id, 'name': self.name, 'stock': self.stock}

    @staticmethod
    def modeling(name, stock):
        return Weapon(name, stock)


@app.route('/')
def hello_world():
    return 'bicsubi_core'


@app.route('/whoami')
def whoami():
    return jsonify({'name': 'bluesunb'})


@app.route('/echo')
def query_string():
    string = request.args.get('string')
    if string is None:
        raise ValueError('value:string is not exist')
    return jsonify({'value': string})


@app.route('/weapon', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    new_weapon = Weapon(name=request_data['name'], stock=request_data.get('stock', 0))
    db.session.add(new_weapon)
    db.session.commit()
    return new_weapon.serialize


@app.route('/weapon')
def read_weapon():
    return jsonify([weapon.serialize for weapon in Weapon.query.all()])


@app.route('/weapon<int:id>', methods=['PUT'])
def update_weapon(id: int):
    request_data = request.get_json()
    try:
        weapon = Weapon.query.filter(Weapon.id == id).first()
        weapon.name, weapon.stock = tuple(request_data.values())
        db.session.commit()
        return jsonify(weapon.serialize)
    except Exception as e:
        print(e)
        raise e


@app.route('/weapon<int:id>', methods=['DELETE'])
def delete_weapon(id: int):
    try:
        weapon = Weapon.query.filter(Weapon.id == id).first()
        db.session.delete(weapon)
        for w in Weapon.query.filter(Weapon.id > id):
            w.id -= 1
        db.session.commit()
        return read_weapon()
    except Exception as e:
        print(e)
        raise e

if __name__ == '__main__':
    app.run(debug=True)

