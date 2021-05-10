from flask import Flask, jsonify, request

app = Flask(__name__)
app.id_count = 3

menus = [
    {'id':1, 'name':'Espresso', 'price':3800},
    {'id':2, 'name':'Americano', 'price':4100},
    {'id':3, 'name':'CafeLatte', 'price':4600},

]

@app.route('/')
def hello_flask():
    return 'Hello World!'

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    menus.sort(key=lambda x:x['id'])
    return jsonify({'menus' : menus})

# POST /menus | 자료를 자원에 추가한다
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    app.id_count += 1
    request_data = request.get_json() # {'name': ..., 'price' : ...}
    new_menu = {
        'id' : app.id_count,
        'name' : request_data['name'],
        'price' : request_data['price']
    }
    menus.append(new_menu)
    menus.sort(key=lambda x:x['id'])

    return jsonify(new_menu)

# PUT /menu/<int:id> | Update
@app.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json() # {'name' : ..., 'price' : ...}
    update_menu = {
        'id' : id,
        'name' : request_data['name'],
        'price' : request_data['price']
    }
    del menus[id-1]
    menus.insert(id-1, update_menu)
    return jsonify(update_menu)


# DELETE /menus | Delete
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    del menus[id-1]
    return jsonify(menus)

if __name__ == '__main__':
    app.run()