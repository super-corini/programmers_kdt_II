'''
Bonus 2. 데이터베이스 연동하기
'''

import os

from flask import Flask, json, jsonify, request, Response
from models import *

app = Flask(__name__)

@app.route('/')
def hello_flask() :
    return 'Hello Flask!'

# GET /menus -> Read
@app.route('/menus')
def get_menus() :
    menu = []
    for item in Item.query.all() :
        menu.append({'id':item.id, 'name':item.name, 'price':item.price})

    return jsonify({'menus':menu})

# POST /menus -> Create
@app.route('/menus', methods=['POST'])
def create_menu() :
    request_data = request.get_json()

    new_item = Item(request_data['name'], request_data['price'])
    
    db.session.add(new_item)
    db.session.commit()

    return jsonify(new_item.to_json())

# PUT /menus -> Update
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id) :
    request_data = request.get_json()

    update_item = search_by_id(id)
    update_item.name = request_data['name']
    update_item.price = request_data['price']

    db.session.commit()
    return jsonify(update_item.to_json())

#DELETE /menus -> Delete
@app.route('/menus/<int:id>', methods=['DELETE'])
def del_menu(id) :
    del_item = search_by_id(id)

    db.session.delete(del_item)
    db.session.commit()

    return get_menus()

@app.errorhandler(400)
def handle_400(e) :
    raise Exception('Bad Request')

base_dir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(base_dir, 'db.sqlite')

app.config['SECREY_KEY'] = 'ProgrammersDevCourse'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__' :
    app.run()

    