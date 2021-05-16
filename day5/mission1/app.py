from flask import Flask, jsonify, request
import db_module

app = Flask(__name__)

@app.route('/whoami')
def i_am():
    return jsonify({"name" : 'gebinabi'})

@app.route('/echo')
def echoString():
    string = request.args.get('string', '')
    return jsonify({"value" : string})

# CREATE
@app.route('/weapons', methods=['POST'])
def create_weapon():
    db = db_module.Database()
    request_data = request.get_json()
    return jsonify({"weapons" : db.create_weapon(request_data)})

# READ
@app.route('/weapons')
def get_weapons():
    db = db_module.Database()
    return jsonify({"weapons" : db.get_weapons()})

# UPDATE
@app.route('/weapons', methods=['PUT'])
def update_weapon():
    db = db_module.Database()
    request_data = request.get_json()
    return ({"weapons" : db.update_weapon(request_data)})

# DELETE
@app.route('/weapons/<name>', methods=['DELETE'])
def delete_weapon(name):
    db = db_module.Database()
    return jsonify({"weapons" : db.delete_weapon(name)})

if __name__ == '__main__':
    app.run()

