from flask import Flask, jsonify, request
from models import Weapon, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./weapon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.app = app
db.create_all()

@app.route('/')
def hello_flask():
    return 'hello flask:) \n my name is MinHyeok Lee! \n I will stand tall!'


# GET | gihub ID
@app.route('/whoami') 
def get_githubID():
    return jsonify({"name": "illstandtall"})

# GET | echo
@app.route('/echo') 
def echo():
    return jsonify({"value": request.args.get('string')})


# GET | Read
@app.route('/weapon') 
def get_weapon():
    return jsonify(Weapon.get_weapon())

    
# POST | Create
@app.route('/weapon', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    return jsonify(Weapon.add_weapon(request_data["name"], request_data["stock"]))


# PUT | Update
@app.route('/weapon', methods=['PUT'])
def update_weapon():
    request_data = request.get_json()
    return jsonify(Weapon.update_weapon(request_data["name"], request_data["stock"]))


# DELETE | Delete
@app.route('/weapon', methods=['DELETE'])
def delete_weapon():
    return jsonify(Weapon.delete_weapon(request.get_json("name")))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
