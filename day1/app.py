from flask import Flask,jsonify,request


app=Flask(__name__)

menus=[
    {"id":1 , "name":"Espresso","price": 38000},
    {"id":2 , "name":"Americano","price": 38000},
    {"id":3 , "name":"Cafe Latte","price": 38000},
]

@app.route('/')
def hello_flask():
    return "Hello World"

@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})

@app.route('/menus', methods=['POST'])
def create_menus():
    request_data=request.get_json()
    new_menu={
        "id":4,
        "name":request_data['name'],
        "price":request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>',methods=['PUT'])
def update_menus(id):
    request_data=request.get_json()
    for menu in menus:
        if menu["id"] == id:
            menu["name"]=request_data["name"]
            menu["price"]=request_data["price"]
            return jsonify(menus)
    return menus

@app.route('/menus/<int:id>',methods=['DELETE'])
def delete_menus(id):

    for menu in menus:
        if menu["id"] == id:
            del menus[menus.index(menu)]
            return jsonify(menus)
    return menus


if __name__=='__main__':
    app.run()