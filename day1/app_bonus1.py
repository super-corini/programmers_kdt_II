from flask import Flask, jsonify, request
app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800}, 
    {"id":2, "name":"Americano", "price":4100}, 
    {"id":3, "name":"CafeLatte", "price":4600}
]

@app.route('/')
def hello_code():
    return 'Hello World!'

# GET /menu
@app.route('/menu') 
def get_menus(): 
    return jsonify({"menus":menus})
    

# POST /menu
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


# PUT /menu/<int:id>
@app.route('/menu/<int:menu_id>', methods=['PUT']) 
def update_menu(menu_id):
    request_data = request.get_json()
    modified_menu = {
        "id": menu_id,
        "name": request_data['name'],
        "price": request_data['price']
    }
    for i in range(len(menus)):
        if menus[i]['id'] == menu_id:
            menus[i] = modified_menu
            break    
        
    return jsonify(modified_menu)


# DELETE /menu/<int:id>
@app.route('/menu/<int:menu_id>', methods=['DELETE']) 
def delete_menu(menu_id):
    deleted_menu = {}
    for i in range(len(menus)):
        if menus[i]['id'] == menu_id:
            deleted_menu = menus[i]
            del menus[i]
            break
        
    return jsonify(deleted_menu)
    
    
if __name__ == '__main__':
    app.run()