# -*- coding: utf-8 -*-

import os
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Weapon

# 현재있는 파일의 디렉토리 절대경로
basedir = os.path.abspath(os.path.dirname(__file__))
# basdir 경로안에 DB파일 만들기
dbfile  = os.path.join(basedir, 'db.sqlite')

app = Flask(__name__)

# SQLAlchemy 설정
# 내가 사용 할 DB URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
# 비지니스 로직이 끝날때 Commit 실행(DB반영)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 수정사항에 대한 TRACK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
# app.config['SECRET_KEY'] = 

# DB 설정
db = SQLAlchemy()
db.init_app(app)
db.app = app
db.create_all()

# End of Constructing App and Database
# ===========================================================================

@app.route('/')
def hello_flask() :
    return "Hello World"

@app.route('/whoami')
def get_github_id() : #{
    return json.dumps({'name':'yuseon27'})
#}

@app.route('/echo')
def echo() : #{
    value = request.args.get('string')
    return json.dumps({'string':value})
#}

# ===========================================================================

def search_weapon_by_name(name) :
    return Weapon.query.filter_by(name=name).first()

def show_weapons() : #{
    weapons = []
    queries = Weapon.query
    for q in queries :
        weapons.append({'name':q.name, 'stock':q.stock})

    return weapons
#}

## Read
@app.route('/weapons')
@app.route('/weapons/read')
def read(): #{
    return jsonify({"wapons":show_weapons()})
#}

## Create
@app.route('/weapons/create', methods=["POST"])
def create_menu() : #{
    request_data = request.get_json()

    if 'name' in request_data and 'stock' in request_data : #{
        if search_weapon_by_name(requeste_data['name']) == None : #{
            new_weapon = Weapon(requeste_data['name'], requeste_data['stock'])
            db.session.add(new_weapon)
            db.session.commit()
        #}
        else : print(f'weapon name={name} already exists in Weapon Table')
    #}
    else : print('name or stock are not given in the request')

    return jsonify({"wapons":show_weapons()})
#}

## Update : 해당하는 name의 stock update
@app.route('/weapons/update/<str:name>', methods=["PUT"])
def update_menu(name) : #{
    request_data = request.get_json()

    if search_weapon_by_name(requeste_data['name']) != None :
        if 'stock' in request_data :
            db.session.query(Weapon).filter(Weapon.name==requeste_data['name']).update({'stock':request_data['stock']})
            db.session.commit()
        else : print('stock is not given in the request')
    else : print(f'weapon name={name} does not exist in Weapon Table')

    return jsonify({"wapons":show_weapons()})
#}

## DELETE : 해당하는 name에 해당하는 데이터를 삭제
@app.route('/weapons/delete/<str:name>', methods=["DELETE"])
def delete_menu(name) : #{

    if search_weapon_by_name(requeste_data['name']) != None :
        db.session.query(Weapon).filter(Weapon.name == name).delete()
        db.session.commit() 
    else : print(f'weapon name={name} does not exist in Weapon Table')

    return jsonify({"weapons":show_weapon()})
#}


# ===========================================================================
if __name__ == "__main__" :
    app.run()