from flask import Flask, jsonify, request
from models import db, Menu
import os

app = Flask(__name__)

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'menus.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
db.create_all()

@app.route('/')
def show_main():
    return 'Hello World!'

@app.route('/menu/init', methods=['PUT', 'DELETE'])
def init_menus():
    if os.path.isfile(dbfile):
        os.remove(dbfile)
    db.init_app(app)
    db.app = app
    db.create_all()
    init_menus = [
        {'id': 1, 'name': 'Espresso', 'price': 3800},
        {'id': 2, 'name': 'Americano', 'price': 4100},
        {'id': 3, 'name': 'CafeLatte', 'price': 4600},
    ]
    for init_menu in init_menus:
        db.session.add(Menu(id=init_menu['id'], name=init_menu['name'], price=init_menu['price']))
        db.session.commit()
    return get_menus()

# GET /menu
@app.route('/menu')
def get_menus():
    return jsonify([menu.serialize for menu in Menu.query.all()])

# POST /menu
@app.route('/menu', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = Menu(name=request_data['name'], price=request_data['price'])
    db.session.add(new_menu)
    db.session.commit()
    return get_menus()

# PUT /menu/<int:id>
@app.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id: int):
    find_menu = Menu.query.filter_by(id=id).first()
    request_data = request.get_json()
    for key, value in request_data.items():
        setattr(find_menu, key, value)
    db.session.commit()
    return get_menus()

# DELETE /menu/<int:id>
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id: int):
    find_menu = Menu.query.filter_by(id=id).first()
    db.session.delete(find_menu)
    db.session.commit()
    return get_menus()

if __name__ == '__main__':
    app.run()