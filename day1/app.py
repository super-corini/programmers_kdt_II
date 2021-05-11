import os
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db = SQLAlchemy(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)

    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id,
           'name': self.name,
           'price': self.price
       }

db.init_app(app)
db.app = app
db.create_all()

@app.route('/')
def hello_code():
    return "Hello World!"

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    menus = Menu.query.all()
    return jsonify([i.serialize() for i in menus])

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name": ..., "price": ...}
    menu = Menu(name=request_data['name'], price=request_data['price'])
    db.session.add(menu)
    db.session.commit()
    return menu.serialize()

@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    request_data = request.get_json()

    target_menu = Menu.query.get(id)
    target_menu.name = request_data['name']
    target_menu.price = request_data['price']

    db.session.commit()

    return "update complete"


@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    target_menu = Menu.query.get(id)
    db.session.delete(target_menu)
    db.session.commit()
    return f"del id:{id}"

    
    

# app 파일을 직접적으로 실행할경우 실행되는 코드
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, FLASK_ENV="development")