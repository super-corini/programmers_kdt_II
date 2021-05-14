import os

from flask import Flask, jsonify, abort, request
from models import *

app = Flask(__name__)

# WhoAmI
@app.route('/whoami')
def who_am_i() :
    return jsonify({'name' : 'nsms556'})

# echo String
@app.route('/echo')
def echo() :
    request_param = request.args.to_dict()

    return jsonify({'value' : request_param['string']})

# Read All Weapons
@app.route('/weapons')
def get_all_weapons() :
    weapons = []

    for weapon in query_all() :
        weapons.append({'id':weapon._id, 'name':weapon.name, 'stock':weapon.stock})

    return jsonify({'weapons' : weapons})

# Read One Weapon
@app.route('/weapons/<int:_id>')
def get_one_weapon(_id) :
    try :
        weapon = search_by_id(_id)
    except MissingIdException :
        abort(400)

    return jsonify(weapon.to_dict())

# Create Weapon
@app.route('/weapons', methods=['POST'])
def create_weapon() :
    request_data = request.get_json()

    new_weapon = Weapon(request_data['name'], request_data['stock'])

    db.session.add(new_weapon)
    db.session.commit()

    return jsonify(new_weapon.to_dict())

# Update Weapon
@app.route('/weapons/<int:_id>', methods=['PUT'])
def ud_weapon(_id) :
    request_data = request.get_json()

    try :
        update_weapon = search_by_id(_id)
        update_weapon.name = request_data['name']
        update_weapon.stock = request_data['stock']

    except MissingIdException :
        abort(400)

    return jsonify(update_weapon.to_dict())

# Delete Weapon
@app.route('/weapons/<int:_id>', methods=['DELETE'])
def delete_weapon(_id) :
    try :
        del_weapon = search_by_id(_id)
        db.session.delete(del_weapon)
    except MissingIdException :
        abort(400)

    db.session.commit()
    return get_all_weapons()

@app.errorhandler(400)
def bad_request(error) :
    return '400 Bad Request'

base_dir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(base_dir, 'weapons.sqlite')

app.config['SECREY_KEY'] = 'ProgrammersDevCourse'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__' :
    app.run()