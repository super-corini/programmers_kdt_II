from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3000},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET /menus | 자료 가져오기
@app.route('/menus') # method default가 get이다. 
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | 자료 추가하기
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라 가정
    # 전달받은 자료를 menus 자원에 추가 
    request_data = request.get_json() #{"name":..., "price"...}
    new_menu = {
        "id": len(menus) + 1,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

if __name__ == '__main__':
    app.run()