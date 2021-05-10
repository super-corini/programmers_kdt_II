from flask import Flask, jsonify, request
import db_module

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "Hello World."

# GET
@app.route('/menus')
def get_menus():
    db = db_module.Database()
    return jsonify({"menus" : db.get_menus()})

# POST
@app.route('/menus', methods=['POST'])
def create_menu():
    db = db_module.Database()
    request_data = request.get_json()
    return jsonify(db.create_menu(request_data))

# PUT
@app.route('/menus/<id>', methods=['PUT'])
def update_menu(id):
    db = db_module.Database()
    request_data = request.get_json()
    request_data['id'] = id
    db.update_menu(request_data)
    return jsonify(request_data)

# DELETE
@app.route('/menus/<id>', methods=['DELETE'])
def delete_menu(id):
    db = db_module.Database()
    return jsonify({"menus" : db.delete_menu(id)})

if __name__ == '__main__':
    app.run()

