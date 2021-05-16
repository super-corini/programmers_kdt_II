from flask import Flask, jsonify, request
from mysql_mgr import *

app = Flask(__name__)

def to_dict(values):
    res = {
           "name": values.name,
           "stock" : values.stock
           }

    return res

# GET /whoami
@app.route('/whoami')
def get_name():
    return jsonify({"name": "dltnwls9623"})


# GET /echo?string="string"
@app.route('/echo') 
def echo():
    query_str = request.args.get('string')
    return jsonify({"value": query_str})


@app.route('/weapon', methods=['GET', 'POST', 'PUT', 'DELETE'])
def weapon_request():
    if request.method == 'POST':  # Create
        request_data = request.get_json()
        new_weapon = {
            "name": request_data['name'],
            "stock": request_data['stock']
        }

        mysql_insert(new_weapon['name'], new_weapon['stock'])
        return jsonify(new_weapon)

    elif request.method == 'GET':  # Read
        result = mysql_select_all()
        res_list = []

        for item in result:
            res_list.append(to_dict(item))

        return jsonify({"weapons": res_list})

    elif request.method == 'PUT':  # Update
        weapon_name = request.args.get('name')
        request_data = request.get_json()
        modified_weapon = {
            "name": request_data['name'],
            "stock": request_data['stock']
        }

        mysql_update(weapon_name, modified_weapon['name'], modified_weapon['stock'])

        return jsonify(modified_weapon)

    elif request.method == 'DELETE':  # Delete
        weapon_name = request.args.get('name')
        result = mysql_select(weapon_name)
        deleted_weapon = []
        for item in result:
            deleted_weapon.append(to_dict(item))

        mysql_delete(weapon_name)

        return jsonify({"deleted weapon": deleted_weapon})


if __name__ == '__main__':
    app.run()
