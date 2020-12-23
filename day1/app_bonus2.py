from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.create_all()


'''
from app import db
db.create_all()
터미널에서 실행
'''

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    price = db.Column(db.Integer, nullable=False)


@app.route("/")
def hello_flask():
    return "Hello, World"

@app.route("/menus")
def get_menus():
    menus = Menu.query.all()
    datas = []
    for menu in menus:
        data = {"id": menu.id, "name": menu.name, "price": menu.price}
        datas.append(data)
    return jsonify({"menus": datas})

@app.route("/menus", methods=["POST"])
def post_menu():
    request_data = request.get_json()
    new_menu = Menu(name=request_data['name'], price=request_data['price'])
    db.session.add(new_menu)
    db.session.commit()
    return jsonify({'id' : new_menu.id, 'name' : new_menu.name, 'price' : new_menu.price})


@app.route("/menus/<int:id>", methods=["PUT"])
def put_menu(id):
    length = Menu.query.count()
    if id > length:
        return "index error"

    request_data = request.get_json()
    change_menu = Menu.query.filter_by(id = id).first()
    # change_menu = Menu.query.get(id) #id가 primary_key이기 때문에 get으로 가능
    change_menu.name = request_data['name']
    change_menu.price = request_data['price']
    db.session.commit()
    return jsonify({'id' : change_menu.id, 'name' : change_menu.name, 'price' : change_menu.price})


@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    length = Menu.query.count()
    if id > length:
        return "index error"

    delete_menu = Menu.query.get(id)
    db.session.delete(delete_menu)

    for i in range(id+1, length+1):
        index_change = Menu.query.get(i)
        index_change.id  = index_change.id -1

    db.session.commit()
    return jsonify({'id' : delete_menu.id, 'name' : delete_menu.name, 'price' : delete_menu.price})

if __name__ == "__main__":
    app.run()