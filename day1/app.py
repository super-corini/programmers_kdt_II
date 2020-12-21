from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow # db model을 JSON형식으로 표현하기 위한 라이브러리

app = Flask(__name__)

app.config['SECRET_KEY'] = 'programmers_kdt_II'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menus.sqlite3'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(100))

    def __init__(self, name, price):
        self.name = name
        self.price = price

class MenuSchema(ma.Schema):
    class Meta:
        fields = ("id","name","price")
        model = Menu

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)


@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료 가져오기
@app.route('/menus') # method의 default는 get이다. 
def get_menus():
    menu = Menu.query.all()
    return jsonify(menus_schema.dump(menu))

# POST /menus | 자료 추가하기
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라 가정
    request_data = request.get_json() #{"name":..., "price"...}
    # menu 스키마에 맞춰서 json으로 받아온 데이터 매핑하기 
    new_menu = Menu(
        request_data['name'], 
        request_data['price']
    )
    db.session.add(new_menu)
    db.session.commit()
    return jsonify(menu_schema.dump(new_menu))

# PUT /menu/<int:id> | 자료 갱신
@app.route('/menu/<id>', methods=["PUT"]) 
def put_menu(id):
    menu = Menu.query.get_or_404(id)
    if 'name' in request.json:
        menu.name = request.json['name']
    if 'price' in request.json:
        menu.price = request.json['price']
    db.session.commit()    
    return jsonify(menu_schema.dump(menu))

# DELETE /menu/<int:id> | 자료 삭제
@app.route('/menu/<id>', methods=["DELETE"])  
def delete_menu(id):
    menu = Menu.query.get_or_404(id)
    db.session.delete(menu)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)