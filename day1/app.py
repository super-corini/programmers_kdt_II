import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHKMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# db.init_app(app)
# db.app = app
# db.create_all()


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=32))
    price = db.Column(db.Integer)

# m = Menu(id=4, name='TEST', price=9999)
# db.session.add(m)
# db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/menus')
def read_menus():
    return jsonify([
        {'id': menu.id,
         'name': menu.name,
         'price': menu.price}
        for menu in Menu.query.all()])

@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = Menu(name=request_data['name'], price=request_data['price'])
    # new_menu = {
    #     "id": len(menus)+1,
    #     "name": request_data['name'],
    #     "price": request_data['price']
    # }
    # menus.append(new_menu)
    db.session.add(new_menu)
    db.session.commit()
    return jsonify({'name': request_data['name'], 'price': request_data['price']})

# @app.route('/menus<int:id>', methods=['PUT'])
# def update_menus(id: int):
#     request_data = request.get_json()
#     try:
#         menus[id - 1].update(dict(request_data))
#         return jsonify(menus[id - 1])
#     except Exception as e:
#         print(e)
#
# @app.route('/menus<int:id>', methods=['DELETE'])
# def delete_menus(id: int):
#     try:
#         for i in range(id, len(menus)):
#             menus[i]['id'] -= 1
#         del menus[id-1]
#         return jsonify(menus)
#     except Exception as e:
#         print(e)


if __name__ == '__main__':
    app.run(debug=True)