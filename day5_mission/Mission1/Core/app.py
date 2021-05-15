from flask import Flask, jsonify, request
import database
import models
import urllib


app = Flask(__name__)
db_session = database.db_session
database.init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def hello_flask():
    return 'Hello World'

# return Github username
@app.route('/whoami', methods=['GET'])
def return_github_id():
    return {"name": "JJ-HH"}

# echo Query Strings
@app.route('/echo', methods=['GET'])
def echo_query():
    params = request.query_string.decode().split('&')
    params_dict = {name: value for name, value in map(lambda x: x.split('='), params)}
    return jsonify(params_dict)

# /Weapons CRUD
@app.route('/weapons', methods=['POST'])
def weapon_C():
    request_data = request.get_json()
    if not request_data["name"] or not request_data["stock"]:
        return ("Due to lack of Information, can not add weapon")
    weapon = models.Weapon(request_data["name"], request_data["stock"])
    db_session.add(weapon)
    db_session.commit()
    
    newly_added_weapon = models.Weapon.query.filter_by(name=request_data["name"]).first()
    return jsonify(newly_added_weapon)

@app.route('/weapons', methods=['GET'])
def weapon_R():
    weapons = models.Weapon.query.all()
    return jsonify({"Weapons": weapons})


@app.route('/weapons/<int:id>', methods=['PUT'])
def weapon_U(id):
    request_data = request.get_json()
    if not (weapon_of_choice := models.Weapon.query.get(id)):
        return ("No such weapon in stock")
    if not request_data["name"] or not request_data["stock"]:
        return ("Bad Request")

    weapon_of_choice.name = request_data["name"]
    weapon_of_choice.stock = request_data["stock"]
    db_session.commit()
    return jsonify(weapon_of_choice)

@app.route('/weapons/<int:id>', methods=['DELETE'])
def weapon_D(id):
    if not (weapon_of_choice := models.Weapon.query.get(id)):
        return ("No such weapon in stock")
    db_session.delete(weapon_of_choice)
    db_session.commit()
    weapons = models.Weapon.query.all()
    return jsonify({"Weapons": weapons})


if __name__ == "__main__":
    app.run()
