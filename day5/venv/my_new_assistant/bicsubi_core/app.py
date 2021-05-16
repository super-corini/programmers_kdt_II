from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)
app.config.from_object('config.Config')
# app.config.from_object(config.Config())
# con = sqlalchemy.create_engine('sqlite:///bicsubi_core.db')
db = SQLAlchemy()
class Weapon(db.Model):
    __tablename__ = 'bicsubi_core'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    stock = db.Column(db.Integer)

db.init_app(app)
db.app = app
db.create_all()

session = db.session

@app.route('/whoami')
def my_github_id():
    return {
        "name": "ohtjqkd"
    }

@app.route('/echo', methods=['GET'])
def echo_string():
    params = request.args.to_dict()
    return {
        "value": params.get('string', 'None')
    }

@app.route('/weapon', methods=['GET'])
def get_weapon():
    ret = session.query(Weapon).all()
    return jsonify([{"name": w.name, "stock": w.stock} for w in ret])

@app.route('/weapon', methods=['POST'])
def insert_weapon():
    req_data = request.get_json()
    name, stock = req_data['name'], req_data['stock']
    new_weapon = Weapon()
    new_weapon.name = name
    new_weapon.stock = stock
    session.add(new_weapon)
    session.commit()
    return {
        "name": name,
        "stock": stock
    }

@app.route('/weapon', methods=['PUT'])
def update_weapon():
    req_data = request.get_json()   
    name, stock = req_data['name'], req_data['stock']
    session.query(Weapon).filter(Weapon.name == name).update({Weapon.name: name, Weapon.stock: stock}, synchronize_session=False)
    session.commit()
    return {
        "name": name,
        "stock": stock
    }

@app.route('/weapon', methods=['DELETE'])
def delete_weapon():
    req_data = request.get_json()
    target_name = req_data['name']
    try:
        session.query(Weapon).filter(Weapon.name == target_name).delete(synchronize_session=False)
        session.commit()
        return '1'
    except:
        return '-1'


if __name__ == "__main__":
    app.run()