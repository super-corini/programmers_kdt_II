from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#db 모델 생성
class menu(db.Model):
    __table_name__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<menu %r>' % self.name

#최초 db 생성 이미 생성해서 안씀
db.create_all()

'''
# 이미 db에 들어가있습니다! 실행할때마다 들어가서 주석처리 중!
Espresso = menu(name = 'Espresso', price = 3800)
Americano = menu(name = 'Americano', price = 4100)
CafeLatte = menu(name = 'CafeLatte', price = 4600)
db.session.add(Espresso)
db.session.add(Americano)
db.session.add(CafeLatte)
db.session.commit()
'''

@app.route('/')
def hello_flask():
    return "Hello World!"

# Get /menus
@app.route('/menus')
def get_menus():
    queryset = menu.query
    df = pd.read_sql(queryset.statement, queryset.session.bind)
    return jsonify(json.loads(df.to_json(orient='records')))

# POST /menus
@app.route('/menus', methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    new_item = menu(name = request_data['name'], price = request_data['price'])
    db.session.add(new_item)
    db.session.commit()
    obj = menu.query.order_by(menu.id.desc()).first()
    new_menu = {
        "id" : obj.id,
        "name" : obj.name,
        "price" : obj.price
    }
    return jsonify({"menu" : new_menu})

#PUT /menus
@app.route('/menus/<_id>', methods=['PUT'])
def change_menu(_id):
    request_data = request.get_json()
    put_item = menu.query.filter_by(id = int(_id)).first()
    put_item.name = request_data["name"]
    put_item.price = request_data["price"]
    put_menu = {
        "id" : put_item.id,
        "name" : put_item.name,
        "price" : put_item.price
    }
    db.session.commit()
    return jsonify({"menu" : put_menu})

#DEL /menus
@app.route('/menus/<_id>', methods=['DELETE'])
def del_menu(_id):
    del_item = menu.query.filter_by(id = int(_id)).first()
    del_menu = {
        "id" : del_item.id,
        "name" : del_item.name,
        "price" : del_item.price
    }
    db.session.delete(del_item)
    db.session.commit()
    return jsonify({"menu" : del_menu})


if __name__ == "__main__":
    app.run()