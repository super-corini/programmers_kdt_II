from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://week4:Bj6LF]C+mVYn4KL@localhost:3306/AI_COURSE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(45))
    price = db.Column(db.VARCHAR(45))


# init db
db.create_all()


class MenuClass:
    def __init__(self):
        pass

    def get_menu_by_id(self, menu_id):
        return db.session.query(Menu).filter(Menu.id == int(menu_id))

    def add_menu(self, info):
        new_menu = Menu(name=info['name'], price=info['price'])
        db.session.add(new_menu)

        db.session.commit()

        return new_menu.id

    def update_menu(self, menu_id, info):
        self.get_menu_by_id(menu_id).update(info)
        db.session.commit()
        return True

    def remove_menu(self, menu_id):
        self.get_menu_by_id(menu_id).delete()
        db.session.commit()
        return True


menu = MenuClass()
db.session.execute('''TRUNCATE TABLE menu''')
db.session.commit()
for m in [{"name": "Espresso", "price": "3800"},
          {"name": "Americano", "price": "4100"},
          {"name": "CafeLatte", "price": "4600"}]:
    menu.add_menu({"name": m["name"], "price": m["price"]})


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/menus')
def get_menus_route():
    return jsonify({"menus": [{"id": m.id, "name": m.name, "price": m.price} for m in Menu.query.all()]})


@app.route('/menus', methods=['POST'])
def create_menu_route():
    if menu.add_menu(request.get_json()):
        return '', 204
    return '', 500


@app.route('/menus/<menu_id>', methods=['PUT'])
def update_menu_route(menu_id):
    updated_menu = menu.update_menu(menu_id, request.get_json())
    if updated_menu:
        return '', 204
    return '', 500


@app.route('/menus/<menu_id>', methods=['DELETE'])
def remove_menu_route(menu_id):
    if menu.remove_menu(menu_id):
        return '', 204
    return '', 500


if __name__ == '__main__':
    app.run()
