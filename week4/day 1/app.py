#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]
curr_id = len(menus)

@app.route('/')
def hello_flask():
    return "Hello World"

@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

@app.route('/menus', methods = ['POST'])
def create_menu():
    global curr_id
    curr_id += 1
    request_data = request.get_json()
    new_menu = {
        "id" : curr_id,
        "name" : request_data['name'],
        "price" : request_data['price'],
     }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods=['PUT'])
def update_menus(id):
    update_data = request.get_json()
    menus[id - 1]["name"] = update_data["name"]
    menus[id - 1]["price"] = update_data['price']
    return jsonify(menus[id - 1])

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menus(id):
    for menu in menus:
        if menu['id'] == id:
            del menus[menus.index(menu)]
            break
    else:
        return "there in no menu"
    return jsonify(menus)

    
    
if __name__ == "__main__":
    app.run()