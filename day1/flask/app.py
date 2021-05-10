from flask import Flask, jsonify, request
import os
from db import db
app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(base_dir, 'db.sqlite')


menus = [
    {"id":1, "name":"Espresso", "price":3000},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]


@app.route('/')
def hello_flask():
    return "Hello World!"


@app.route('/menu')
def get_menus():
    return jsonify({"menus":menus})


@app.route('/menu', methods=['POST'])
def create_menu():
    request_data = request.get_json() 
    new_menu={
        "id":menus[-1]['id']+1 if menus else 1,
        "name":request_data['name'],
        "price":request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json() 

    for i in range(len(menus)):
        if menus[i]['id']==id:
            menus[i]['name']=request_data['name']
            menus[i]['price']=request_data['price']
            return jsonify(menus[i])
    return 'Error No ID'

@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    request_data = request.get_json() 
    for i in range(len(menus)):
        if menus[i]['id']==id:
            return menus.pop(i)
    return 'Error No ID'
            
if __name__=='__main__':
    app.run()