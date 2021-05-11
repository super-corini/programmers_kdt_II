'''
Mandatory : CRUD 만들기
Bonus 1 : id 번호 변경하여 추가하기
Bonus 2 : 데이터베이스 연동하기
'''

import os

from flask import Flask, json, jsonify, request, redirect, url_for, abort
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

    #new_menu = {'id':len(menus)+1, 'name':request_data['name'], 'price':request_data['price']}
    # Bonus 1 : menus의 아이템 개수를 체크하여 +1 한 것을 id번호로 부여

    new_item = Item(request_data['name'], request_data['price'])
    
    db.session.add(new_item)
    db.session.commit()

    return jsonify(new_item.to_json())

# Mandatory
# PUT /menus -> Update
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id) :
    request_data = request.get_json()

    try :
        update_item = search_by_id(id)
        update_item.name = request_data['name']
        update_item.price = request_data['price']
        
    except MissingIdException :
        abort(400)

    db.session.commit()
    return jsonify(update_item.to_json())

# Mandatory
#DELETE /menus -> Delete
@app.route('/menus/<int:id>', methods=['DELETE'])
def del_menu(id) :
    try :
        del_item = search_by_id(id)
        db.session.delete(del_item)
    except MissingIdException :
        abort(400)

    db.session.commit()
    return get_menus()

@app.errorhandler(400)
def bad_request(error) :
    return '400 Bad Request'

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

    