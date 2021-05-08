import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'cafe_menu.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbfile}'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Menu('{self.id}', '{self.name}', '{self.price}')"

'''
menu_list = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]
'''

@app.route('/menus', methods=['GET', 'POST'])
def menus():
    if request.method == 'GET':
        return jsonify({"menus":[{"id":m.id, "name":m.name, "price":m.price} for m in Menu.query.all()]})
    else:
        request_data = request.get_json()
        new_menu = Menu(name=request_data['name'], price=request_data['price'])
        db.session.add(new_menu)

        new_menu = Menu.query.filter_by(name=request_data['name']).first_or_404()
        return {"id":new_menu.id, "name":new_menu.name, "price":new_menu.price}

@app.route('/menu/<int:id>', methods=['PUT', 'DELETE'])
def edit_menu(id):
    edit_menu = Menu.query.filter_by(id=id).first_or_404()

    if request.method == 'PUT':
        request_data = request.get_json()
        if 'name' in request_data:
            edit_menu.name = request_data['name']
        if 'price' in request_data:
            edit_menu.price = request_data['price']
        return {"id":edit_menu.id, "name":edit_menu.name, "price":edit_menu.price}
    else:
        delete_menu = edit_menu.name
        db.session.delete(edit_menu)
        return f"Delete {delete_menu}."

if __name__ == '__main__':
    app.run()