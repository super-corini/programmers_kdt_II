# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# menus
menus = [
    {"id":1,
    "name":"Espresso",
    "price":3000},
    {"id":2,
    "name":"Americano",
    "price":5100},
    {"id":3,
    "name":"CafeLatte",
    "price":4500}
]

@app.route('/')
def hello_flask():
    return "Hello World!"

# /menu
# GET
@app.route('/menu', methods=['GET'])
def get_menus():
    return jsonify({"menus": menus})
# POST
@app.route('/menu', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = {
        "id": 4,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

if __name__ == '__main__':
    app.run()
