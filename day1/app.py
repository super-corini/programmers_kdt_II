from flask import Flask,jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price": 4800},
    {"id":2, "name":"Americano", "price": 4100},
    {"id":3, "name":"CafeLatte", "price": 4600},
]


@app.route('/')
def hello_flask():
    return "Hello World"

# Get /menus / 자료를 가져온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})

# Post
@app.route('/menus', methods = ['POST'])
def create_menu():
    #전달받은 자료를 메뉴에 추가
    request_data = request.get_json()
    new_menu = {
        "id": len(menus)+1,
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods = ['PUT'])
def update_id(id):
    request_data = request.get_json()
    menus[id-1]['name'] = request_data['name']
    menus[id-1]['price'] = request_data['price']
    return jsonify({"menus":menus})
# DELETE
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    del menus[id-1]
    return jsonify({'menu': menus})

if __name__ == '__main__':
    app.run()
