import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
db = SQLAlchemy(app)




class Menus(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Integer)

#홈 디렉토리
@app.route('/')
def home():
    return "Welcome to Starbucks Menu"

#GET
@app.route('/menus')
def get_menus():
    menus = []
    for m in Menus.query.all():
        menu = {}
        menu['id'] = m.id
        menu['name'] = m.name
        menu['price'] = m.price
        menus.append(menu)
    return jsonify({"menus": menus})

#POST
@app.route('/menus', methods=['Post'])
def create_menus():
    req = request.get_json()
    menu = Menus(name=req['name'], price=req['price'])
    db.session.add(menu)
    db.session.commit()
    return get_menus()

#PUT
@app.route('/menus/<int:id>', methods=['PUT'] )
def update_menus(id):
    req = request.get_json()
    Menus.query.filter_by(id=id).update(dict(name=req['name'],price=req['price']))
    db.session.commit()
    return get_menus()

# DELETE /menus   | 해당 자료를 삭제한다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menus(id):
    Menus.query.filter_by(id=id).delete()
    db.session.commit()
    return get_menus()
