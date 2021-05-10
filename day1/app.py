from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)


class Menus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)


@app.route('/')
def hello_flask():
    return "Hello World!"


@app.route('/menus')
# GET /menus   |  자료를 가지고 온다.
def get_menus():
    return jsonify([
        {"id": menu.id, "name": menu.name, "price": menu.price}
        for menu in Menus.query.all()
    ])


@app.route('/menus', methods=['POST'])
# POST /menus  |  자료를 자원에 추가한다.
def create_menus():
    # 전달받은 자료를 menus 자원에 추가
    # request가 JSON이라고 가정
    request_data = request.get_json()  # {"name": ..., "price": ...}
    item = Menus(name=request_data['name'], price=request_data['price'])
    db.session.add(item)
    db.session.commit()
    return jsonify([
        {"id": menu.id, "name": menu.name, "price": menu.price}
        for menu in Menus.query.all()
    ])


@app.route('/menus/<int:id>', methods=['PUT'])
def update_menus(id):
    item = Menus.query.get_or_404(id)
    request_data = request.get_json()
    if is_json_key(request_data, 'name'):
        item.name = request_data['name']
    if is_json_key(request_data, 'price'):
        item.price = request_data['price']
    db.session.commit()
    return jsonify([
        {"id": item.id, "name": item.name, "price": item.price}
    ])


@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menus(id):
    item = Menus.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify([
        {"id": menu.id, "name": menu.name, "price": menu.price}
        for menu in Menus.query.all()
    ])


def is_json_key(json, key):
    try:
        temp = json[key]
    except KeyError:
        return False
    return True


if __name__ == '__main__':
    app.run()
