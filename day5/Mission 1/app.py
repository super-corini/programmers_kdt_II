from flask import Flask, jsonify, request
from mysql_migration import *

app = Flask(__name__)

def as_dict(query_data):
    response = []
    for data in query_data:
        response.append({
            "name": data.name,
            "stock": data.stock
        })
    return response


# GET / whoami
@app.route('/whoami')
def get_id():
    return jsonify({"name": "ketkat001"})


# GET / echo?string="string"
@app.route('/echo')
def echo():
    query = request.args.get('string')
    return jsonify({'value': query})


@app.route('/weapon', methods=['GET', 'POST', 'PUT', 'DELETE'])
def weapon_api():
    request_data = request.get_json()
    if request.method == 'GET':
        result = as_dict(mysql_select_weapon())
        return jsonify({"weapons": result})
    
    elif request.method == 'POST':
        mysql_create_weapon(request_data['name'], request_data['stock'])
        return jsonify({"name": request_data['name'], "stock": request_data['stock']})
    
    elif request.method == 'PUT':
        name = request_data['name']
        mysql_update_weapon(name, request_data['modify_name'], request_data['stock'])
        return jsonify({"name": request_data['modify_name'], "stock": request_data['stock']})

    elif request.method == 'DELETE':
        name = request_data['name']
        mysql_delete_weapon(name)
        return jsonify({"name": request_data['name'], "stock": request_data['stock']})
        

if __name__ == '__main__':
    app.run()