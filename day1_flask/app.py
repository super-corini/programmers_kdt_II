from flask import Flask, jsonify, request
from models import db, Menu


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.app = app
db.create_all()


@app.route('/')
def hello_flask():
    return 'hello flask:)'


# GET
@app.route('/menus') 
def get_menus():
    return jsonify(Menu.get_menus())

    
# POST
@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    return jsonify(Menu.add_menu(request_data["name"], request_data["price"]))


# PUT
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    return jsonify(Menu.update_menu(id, request_data["name"], request_data["price"]))


# DELETE
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    return jsonify(Menu.delete_menu(id))


if __name__ == '__main__':
    app.run(debug=True)
