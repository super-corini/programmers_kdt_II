# -*- coding: utf-8 -*-

import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Menu

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

def search_menu_by_id(id) : #{
    return Menu.query.filter_by(id=id).first()
#}

def get_max_id() : #{
    return db.session.query(db.func.max(Menu.id)).scalar()
#}

def show_menu() : #{
    menus = []
    queries = Menu.query
    for q in queries :
        menus.append({'id':q.id, 'name':q.name, 'price':q.price})

    return menus
#}


@app.route('/')
def hello_flask() :
    return "Welcome! This is Coffee Shop :)"       


@app.route('/menus')
def get_menus(): #{
    return jsonify({"menus":show_menu()})
#}

## POST / menus : 자료를 자원에 추가한다.
@app.route('/menus', methods=["POST"])  ## methods를 list 형태로 저장 -> 여러가지 method에 대해 처리 가능
def create_menu() : #{
    request_data = request.get_json()  # {"name" : ..., "price" : ...}

    if 'id' in request_data : #{     ## request에 id가 있는 경우
        if search_menu_by_id(request_data['id']) == None : id = request_data["id"]
        else :                       ## 테이블에 이미 id가 있는 경우 maximun value + 1로 재할당
            id = get_max_id()+1   
            print(f'id={request_data["id"]} already exists in Menu Table -> {id}')
    #}
    else :                           ## request에 id가 없는 경우 maximun value + 1로 할당
        id = get_max_id()+1    

    new_menu = Menu(id,
                    request_data["name"],
                    request_data["price"],
                   )
    db.session.add(new_menu)
    db.session.commit()

    return jsonify({'id':new_menu.id, 'name':new_menu.name, 'price':new_menu.price})
#}

## PUT : 해당하는 id에 해당하는 데이터를 갱신
@app.route('/menu/<int:id>', methods=["PUT"])
def update_menu(id) : #{
    request_data = request.get_json()

    menu = search_menu_by_id(id)
    if search_menu_by_id(id) != None :
        db.session.query(Menu).filter(Menu.id==id).update({'name':request_data['name'], 'price':request_data['price']})
        db.session.commit()
    else : print(f'id={id} does not exist in Menu Table')

    return jsonify({"menus":show_menu()})
#}

## DELETE : 해당하는 id에 해당하는 데이터를 삭제
@app.route('/menu/<int:id>', methods=["DELETE"])
def delete_menu(id) : #{
    menu = search_menu_by_id(id)

    if menu != None :
        db.session.query(Menu).filter(Menu.id==menu.id).delete()
    else : print(f'id={id} does not exist in Menu Table')
    db.session.commit() 

    return jsonify({"menus":show_menu()})
#}

if __name__ == "__main__" :
    app.run()