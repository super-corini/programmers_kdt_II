from flask import Flask, json, jsonify, request

app = Flask(__name__)

menus = [
    {'id':1, 'name':'Latte', 'price':3900},
    {'id':2, 'name':'Americano', 'price':2500},
    {'id':3, 'name':'Espresso', 'price':2500},
]

@app.route('/')
def hello_flask() :
    return 'Hello Flask!'

# GET /menus -> Read
@app.route('/menus')
def get_menus() :
    return jsonify({'menus':menus})

# POST /menus -> Create
@app.route('/menus', methods=['POST'])
def create_menu() :
    request_data = request.get_json()

    new_menu = {'id':len(menus)+1, 'name':request_data['name'], 'price':request_data['price']}

    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /menus -> Update
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id) :
    request_data = request.get_json()

    update_item = menus[id - 1]
    update_item['name'] = request_data['name']
    update_item['price'] = request_data['price']

    return jsonify(update_item)

#DELETE /menus -> Delete
@app.route('/menus/<int:id>', methods=['DELETE'])
def del_menu(id) :
    del(menus[id - 1])

    return jsonify({'menus':menus})

if __name__ == '__main__' :
    app.run()

    