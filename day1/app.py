from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "cafe_menu.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



class Menu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer, nullable = False)



@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료를 가져온다
@app.route('/menus')
def get_menus():
    menus = Menu.query.all()
    # List 는 json으로 만들 수 없으므로, 딕셔너리의 형태로 넣어줘야함
    return jsonify({"menus" : [{"id" : new_menu.id, "name" : new_menu.name , "price" : new_menu.price} for new_menu in menus]})


# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods = ['POST']) # methods의 default값은 'GET'
def create_menu(): # request가 JSON이라고 가정
    request_data = request.get_json()
    # 전달받은 자료를 menus 자원에 추가
    new_menu = Menu(name = request_data["name"], price = request_data["price"])
    db.session.add(new_menu)
    db.session.commit()
    return jsonify({"id" : new_menu.id, "name" : new_menu.name , "price" : new_menu.price})

@app.route('/menu/<int:id_>', methods = ['PUT', 'DELETE'])
def modify_menu(id_):
    menu = Menu.query.filter_by(id = id_).first()
    # method를 같은 route에서 여러 개 받을 수 있게 처리하는 방법.
    if request.method == 'PUT':
        request_data = request.get_json()
        menu.name = request_data["name"]
        menu.price = request_data["price"]
        db.session.commit()

        return jsonify({"id" : menu.id, "name" : menu.name , "price" : menu.price})

    else:
        db.session.delete(menu)
        db.session.commit()
        menus = Menu.query.all()
        return jsonify({"menus" : [{"id" : new_menu.id, "name" : new_menu.name , "price" : new_menu.price} for new_menu in menus]})


if __name__ == '__main__':
    db.create_all()
    app.run()