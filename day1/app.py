from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from model import Menu

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    menus = Menu.query.all()
    menu_list = []
    for menu in menus:
        menu_list.append(dict(
            id=menu.id,
            name=menu.name,
            price=menu.price,
        ))
    return jsonify({"menus":menu_list})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    #  전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    new_menu = Menu(name=request_data['name'], price=request_data['price'])
    db.session.add(new_menu)
    db.session.commit()
    return "Success"

# PUT
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    menu = Menu.query.filter_by(id=id).first()
    if menu:
        menu.id = id
        menu.name = request_data['name']
        menu.price = request_data['price']
        db.session.commit()
    else:
        return "Fail"
    return "Success"

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    menu = menu = Menu.query.filter_by(id=id).first()
    if menu:
        db.session.delete(menu)
        db.session.commit()
    else:
        return "Fail"
    return "Success"

if __name__ == '__main__':
    app.run()