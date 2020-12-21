from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "unclassified"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Menu %r>" % self.name


"""
menus = [
    {"id": 1, "name": "espresso", "price": 2500},
    {"id": 2, "name": "americano", "price": 3000},
    {"id": 3, "name": "cafe latte", "price": 3500},
]
"""


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
    new_menu = Menu(name=request_data["name"], price=request_data["price"])
    db.session.add(new_menu)
    db.session.commit()
    return "Posted well!"


@app.route("/menus/<int:id>", methods=["PUT"])
def put_menu(id):
    try:
        request_data = request.get_json()
        selected = Menu.query.get(id)
        selected.name = request_data["name"]
        selected.price = request_data["price"]
        db.session.commit()
        return "Updated well!"
    except:
        return "Something wrong. (maybe ID)"


@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    try:
        selected = Menu.query.get(id)
        db.session.delete(selected)
        db.session.commit()
        return "Deleted well!"
    except:
        return "Something wrong. (maybe ID)"


if __name__ == "__main__":
    app.run()