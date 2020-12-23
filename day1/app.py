from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "pricc":4100},
    {"id":3, "name":"cafeLatte", "price":4600},
]

idx = [3]   # id를 저장하고 있는 리스트, post를 통해 메뉴가 추가될 때마다 +1을 해준다. 
            # 리스트로 저장하는 이유는 함수 내부에서 사용하기 위해서이다. (menus처럼) 

@app.route('/')
def hello_flask():
    return "Hello World"

# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})
    
# Post /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():   # request가 JSON이라고 가정
    # 전달 받은 자료를 menus 자원에 추가
    request_data = request.get_json()    # {"name": ..., "price": ...}
    idx[0] += 1
    new_menu = {
        "id" : idx[0],
        "name" : request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify({"menus": menus})

# PUT /munus/<int:id> | 해당하는 id에 해당하는 데이터를 갱신
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):    # request가 json으로 전달된다.
    # 해당하는 id의 해당하는 데이터 갱신
    request_data = request.get_json()
    update_menu = {
        "id" : id,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus[id - 1] = update_menu
    return jsonify({"munes": menus})

# DELETE /menu/<int:id> | 해당하는 id에 해당하는 데이터를 삭제
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):    
    #해당하는 id의 해당하는 데이터 삭제
    menus.pop(id-1)
    return jsonify({"menus": menus})

if __name__ == '__main__':
    app.run()