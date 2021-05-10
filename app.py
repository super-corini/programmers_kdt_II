from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import pandas as pd


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///menus.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)


class Menus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)


def get_all():
    """
    Menus에 있는 모든 데이터를 가져오는 함수
    Input -> None
    Output -> list(dict)
    """
    queryset = Menus.query
    df = pd.read_sql(queryset.statement, queryset.session.bind)
    menus = df.to_json(orient="records")
    return json.loads(menus)


@app.route("/")
def hello_flask():
    return "Hello, World!"


# GET /menus  |  자료를 가지고 온다.
@app.route("/menus")
def get_menus():
    return jsonify(get_all())


# POST /menus  |  자료를 자원에 추가한다.
@app.route("/menus", methods=["POST"])
def create_menu():
    request_data = request.get_json()  # {"name": ..., "price": ...}

    new_menu = Menus(name=request_data["name"], price=request_data["price"])
    db.session.add(new_menu)
    db.session.commit()

    return jsonify(get_all())


# PUT /menus/<int:id>
@app.route("/menus/<int:id>", methods=["PUT"])
def update_menu(id):
    request_data = request.get_json()

    menu = Menus.query.get(id)
    if not menu:
        return "해당 id값이 메뉴에 없습니다.", 404

    menu.name = request_data["name"]
    menu.price = request_data["price"]

    db.session.commit()

    return jsonify(get_all())


# DELETE /menus/<int:id>
@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    menu = Menus.query.get(id)
    if not menu:
        return "해당 id값이 메뉴에 없습니다.", 404

    db.session.delete(menu)
    db.session.commit()

    return jsonify(get_all())


if __name__ == "__main__":
    app.run()
