# Bonus 2. Flask와 DB 연동시키기(ORM 버전)
# 참고 : https://betterprogramming.pub/building-restful-apis-with-flask-and-sqlalchemy-part-1-b192c5846ddd
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app start 필요 없음
db = SQLAlchemy(app)


class Menus(db.Model):
    id = db.Column(db.Integer, primary_key = True, index = True)
    name = db.Column(db.String(120), nullable = False)
    price = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<menu %r>' % self.id

# 첫 시작에 db 생성을 위해 반드시 필요
db.create_all()

# Home Directory
@app.route('/')
def hello_flask():
    return "Hello Flask! Ah! Very Hard! with DB"

# Get /menus | 자료를 가지고 옴 (READ)
@app.route('/menus')
def get_menus():
    return jsonify([
        {'id':menu.id,
         'name':menu.name,
         'price':menu.price
        } for menu in Menus.query.all()])

# POST /menus | 자원 추가 (CREATE)
@app.route('/menus', methods=['POST'])
def post_menu(): # request가 JSON이라고 가정한다.
    # 전달받은 자료를 menus 자원에 추가함
    request_data = request.get_json()
    new_menu = Menus(name=request_data['name'],
                     price=request_data['price'])

    db.session.add(new_menu)
    db.session.commit()

    return jsonify([
        {'id': menu.id,
         'name': menu.name,
         'price': menu.price
         } for menu in Menus.query.all()])

@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    alter_menu = Menus.query.get_or_404(id)
    update_data = request.get_json()

    alter_menu.name = update_data['name']
    alter_menu.price = update_data['price']

    db.session.commit()

    return jsonify([
        {'id': alter_menu.id,
         'name': alter_menu.name,
         'price': alter_menu.price
         }])

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    del_menu = Menus.query.get_or_404(id)
    db.session.delete(del_menu)
    db.session.commit()

    return jsonify([
        {'id': menu.id,
         'name': menu.name,
         'price': menu.price
         } for menu in Menus.query.all()])

if __name__ == '__main__':
    app.run()