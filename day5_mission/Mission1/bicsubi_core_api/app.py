from flask import Flask, jsonify, request
from sqlalchemy.util.langhelpers import NoneType
from model import db
from model import Weapon
from model import app

@app.route('/whoami')
def whoami():
    return jsonify({"name" : "Gangneng"})

@app.route('/echo')
def return_string():
    string = request.args.get('string')
    return jsonify({"string":string})

@app.route('/weapon')
def get_weapon_menu():
    weapon_menu = Weapon.query.all()
    w_list = []
    for weapon in weapon_menu:
        w_list.append({"id" : weapon.id, "name":weapon.name, "stock":weapon.stock})

    return jsonify({"weapons":w_list})

@app.route('/weapon', methods=['POST'])
def create_weapon(): 
    weapon_menu = Weapon.query.all()

    request_data = request.get_json()
    
    if request.args.get('name'):
        name_ = request.args.get('name')
        stock_ = request.args.get('stock')
        new_weapon = Weapon(id = len(weapon_menu)+1, name = name_,stock = stock_)
    
    else:
        name_ = request_data['name']
        stock_ = request_data['stock']
        new_weapon = Weapon(id = len(weapon_menu)+1, name = name_,stock = stock_)
    
    weapon = db.session.query(Weapon).filter(Weapon.name==name_).first()
    
    if weapon:
        return "Warning!!! Already exist weapon"
    
    else:
        db.session.add(new_weapon) 
        db.session.commit() 
        return get_weapon_menu()

@app.route('/weapon/<name>/<stock>', methods=['POST'])
def create_weapon_(name, stock):
    weapon_menu = Weapon.query.all()
    new_weapon = Weapon(id = len(weapon_menu)+1, name = name,stock = stock)
    weapon = db.session.query(Weapon).filter(Weapon.name==name).first()

    if weapon:
        return "Warning!!! Already exist weapon"

    else:
        db.session.add(new_weapon) 
        db.session.commit() 
        return get_weapon_menu()

@app.route('/weapon', methods=['PUT'])
def update_data():
    weapon = db.session.query(Weapon).filter(Weapon.name==request.args.get('name')).first()

    if weapon:
        request_data = request.get_json()
        try:
            update_weapon = db.session.query(Weapon).filter(Weapon.name==request_data['name']).first()
            if update_weapon:
                return "Warning!!! Already exist weapon"
            weapon.name = request_data['name']
        except:
            print("only stock")
        weapon.stock = request_data['stock']
        db.session.commit() 

        return get_weapon_menu()

    else:
        return "Warning!!! Not exist weapon"

@app.route('/weapon/<name>', methods=['PUT'])
def update_data_(name):
    weapon = db.session.query(Weapon).filter(Weapon.name==name).first()

    if weapon:
        request_data = request.get_json()
        try:
            update_weapon = db.session.query(Weapon).filter(Weapon.name==request_data['name']).first()
            if update_weapon:
                return "Warning!!! Already exist weapon"
            weapon.name = request_data['name']
        except:
            print("only stock")
        weapon.stock = request_data['stock']
        db.session.commit() 
        
        return get_weapon_menu()

    else:
        return "Warning!!! Not exist weapon"
      
@app.route('/weapon', methods=['DELETE'])
def delete_data():
    weapon = db.session.query(Weapon).filter(Weapon.name==request.args.get('name')).first()
    if weapon:
        db.session.delete(weapon)
        db.session.commit()
        return get_weapon_menu()
    else:
        return "Warning!!! Not exist weapon"


@app.route('/weapon/<name>', methods=['DELETE'])
def delete_data_(name):
    weapon = db.session.query(Weapon).filter(Weapon.name==name).first()
    if weapon:
        db.session.delete(weapon)
        db.session.commit()
        return get_weapon_menu()
    else:
        return "Warning!!! Not exist weapon"


if __name__ =="__main__":
    app.run()