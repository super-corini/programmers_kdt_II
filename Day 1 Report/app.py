########## 보너스 과제 2 ##########
from flask import Flask, jsonify, request
#import os
#from flask_sqlalchemy import SQLAlchemy
from model import db
from model import Menu
from model import app

@app.route('/')
def hello_flask():
    return "Hello World!"

@app.route('/menus')
def get_menus():
    menus = Menu.query.all()
    m_list = []
    for menu in menus:
        m_list.append({"id":menu.id, "name":menu.name,"price":menu.price})

    return jsonify({"menu" : m_list})


@app.route('/menus', methods=['POST'])
def create_menu(): 
    request_data = request.get_json()
    menus = Menu.query.all()
    new_menu = Menu(id = len(menus)+1, name = request_data['name'],price = request_data['price'])
    db.session.add(new_menu)
    db.session.commit()
    return {"id":len(menus)+1, "name":request_data['name'], "price":request_data['price']}

@app.route('/menus/<id>', methods=['PUT'])
def update_data(id):
    request_data=request.get_json()
    menu = db.session.query(Menu).filter(Menu.id==int(id)).first()
    menu.name = request_data['name']
    menu.price = request_data['price']
    db.session.commit()
    return get_menus()

@app.route('/menus/<id>', methods=['DELETE'])
def delete_data(id):
    menu = db.session.query(Menu).filter(Menu.id==int(id)).first()
    db.session.delete(menu)
    db.session.commit()
    return get_menus()

if __name__ == '__main__':
    app.run()
########### 보너스 과제 2 완료 ###########