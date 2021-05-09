"""
보너스 02 과제 입니다.
"""

import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

print(app.config['SQLALCHEMY_DATABASE_URI'])

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=32))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f'<id:{self.id}, name:{self.name}, price:{self.price}>'

    @property
    def serialize(self):
        return {'id': self.id, 'name':self.name, 'price':self.price}

@app.route('/')
def hello_world():
    return 'TEST'

@app.route('/menus')
def read_menus():
    return jsonify([
        {'id': menu.id,
         'name': menu.name,
         'price': menu.price}
        for menu in Menu.query.all()])

@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = Menu(name=request_data['name'], price=request_data['price'])
    db.session.add(new_menu)
    db.session.commit()
    return jsonify({'name': request_data['name'], 'price': request_data['price']})

@app.route('/menus<int:id>', methods=['PUT'])
def update_menus(id: int):
    request_data = request.get_json()
    try:
        menu = Menu.query.filter(Menu.id==id).first()
        menu.name = request_data['name']
        menu.price = request_data['price']
        db.session.commit()
        return jsonify(menu.serialize)
    except Exception as e:
        print(e)
        raise e


@app.route('/menus<int:id>', methods=['DELETE'])
def delete_menus(id: int):
    try:
        menu = Menu.query.filter(Menu.id==id).first()
        db.session.delete(menu)
        id_affected = Menu.query.filter(Menu.id > id).all()
        for i in range(len(id_affected)):
            id_affected[i].id -= 1
        db.session.commit()
        return jsonify([i.serialize for i in Menu.query.all()])
    except Exception as e:
        print(e)
        raise e

if __name__ == '__main__':
    app.run(debug=True)