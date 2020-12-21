from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3000},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

id_cnt = 3

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
    global id_cnt
    # 전달받은 자료를 menus 자원에 추가 
    request_data = request.get_json() #{"name":..., "price"...}
    id_cnt += 1
    new_menu = {
        "id": id_cnt,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /menu/<int:id> | 자료 갱신
@app.route('/menu/<id>', methods=["PUT"]) # method default가 get이다. 
def put_menu(id):
    id = int(id)
    request_data = request.get_json() #{"name":..., "price"...}
    for menu in menus:
        if menu['id'] == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            break
    else: print("id {0} is not in menus".format(str(id))) 

    return jsonify({"menus" : menus})

# DELETE /menu/<int:id> | 자료 삭제
@app.route('/menu/<id>', methods=["DELETE"]) # method default가 get이다. 
def delete_menu(id):
    global id_cnt
    id = int(id)
    for i, menu in enumerate(menus):
        if menu['id'] == id:
            del menus[i]
            break
    else: print("id {0} is not in menus".format(str(id))) 
         
    return jsonify({"menus" : menus})

if __name__ == '__main__':
    app.run()