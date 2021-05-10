from flask import Flask, jsonify, request

# Flask app의 이름
app = Flask(__name__)

menus = [
    {"id": 1, "name": "Esspresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4200},
    {"id": 3, "name": "CafeLatte", "price": 4600}
]

# 주소 '/'(root) 를 만나면 아래의 함수를 실행
@app.route('/')
def hello_falsk():
    return "Hello World!!!!!!"

# GET
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})

# POST
@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    new_menu = {
        "id": 4,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)


# 처음 실행한(main) 함수의 경우 현재 app을 실행하라는 의미
if __name__ == '__main__':
    app.run(debug=True)
