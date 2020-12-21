from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

menus = {
    1: {'name':"Espresso", 'price':3000},
    2: {'name':"Americano", 'price':3900},
    3: {'name':"CaffeLatte", 'price':4300},
}

def idx_generator():
    i = 4
    while True:
        yield i
        i += 1
idx = idx_generator()

@app.route('/')
def hello_flask():
    return "Day1 Assignment"

# GET /menus
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})

# POST /menus
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라 가정
    request_data = request.get_json() # {"name:..., "price":....}
    p = next(idx)
    menus[p] = {'name' : request_data['name'], 'price' : request_data['price']}

    return jsonify(menus[p])

# PUT /menu/<int:id>
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    try:
        menus[id] = {'name' : request_data['name'], 'price' : request_data['price']}
    except:
        return "No data Come in"

    return jsonify(menus[id])

# DELETE /menu/<int:id>
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    try:
        del menus[id]
        return jsonify({"menus": menus})
    except:
        return "fail"


if __name__ == '__main__':
    app.run()