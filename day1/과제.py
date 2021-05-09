from flask import Flask, jsonify, request


app = Flask(__name__)

menu = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]


# main
@app.route('/')
def homepage():
    return "Week 4 / Day 1 과제인 Flask CRUD 구현입니다."


# READ
@app.route('/menu')
def get_menu():
    return jsonify({'menu': menu})


# CREATE
@app.route('/menu', methods=['POST'])
def post_menu():
    global menu
    request_json = request.get_json()
    new_menu = {
        'id': len(menu)+1,
        'name': request_json['name'],
        'price': request_json['price'],
    }
    menu.append(new_menu)
    return jsonify({'menu': menu})

    

# UPDATE
@app.route('/menu/<int:id>', methods=['PUT'])
def put_menu(id):
    request_json = request.get_json()
    try:
        menu[id-1]['name'] = request_json['name']
        menu[id-1]['price'] = request_json['price']
        return jsonify({'menu': menu})


    except Exception as e:
        return f'에러발생!: {e}'


# DELETE
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    try:
        del menu[id-1]
        return jsonify({'menu': menu})
    
    except Exception as e:
        return f'에러발생!: {e}'


if __name__ == '__main__':
    app.run()