import os
from models import db
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

@app.route('/menus')
def get_menus():
    return jsonify(menus)

global count
count = 4

@app.route('/menus', methods=['POST'])
def create_menu():
    global count
    request_data = request.get_json()
    new_menu = {
        "id" : count,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    count += 1
    menus.append(new_menu)
    return jsonify(menus)

@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    update_data = request.get_json()
    for menu in menus:
        if menu['id'] == id:
            menu['name'] = update_data['name']
            menu['price'] = update_data['price']
            break
        if menu['id'] > id:
            break
    return jsonify(menu)

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):

    for menu in menus:
        if menu['id'] == id:
            menus.remove(menu)
            break
        if menu['id'] > id:
            break
    return jsonify(menu)

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run()