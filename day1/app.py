from flask import Flask, jsonify, request

app=Flask(__name__)

menus=[
    {"id":1,"name":"Espresso","price":3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4500},

]
@app.route('/')
def hello_flask():
    return "Hello World"

#GET /menus | 자료 가져오기
@app.route('/menus')
def get_menu():
    return jsonify({"menus":menus})
#리스트타입일때 json으로 변환 x
#따라서 딕셔너리로 만들어준 후, json으로 변환

#POST /menus | 자료를 리소스에 추가
@app.route('/menus', methods=['POST'])
def create_menu(): #request가 json이라 가정
    # 전달받은 자료 menus에 추가
    request_data=request.get_json() #{"name":..., "price":...}
    #get_json으로 파싱해서 딕셔너리로 변환

    new_menu={
        "id": menus[-1]['id']+1,
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

#PUT
@app.route("/menus/<int:id>", methods=["PUT"])
def put_menu(id):
    request_data = request.get_json()

    for i in range(len(menus)):
        if menus[i]['id']==id:
            menus[i]['name']=request_data['name']
            menus[i]['price']=request_data['price']
            return jsonify(menus)
    return "not exist ID"

#DELETE
@app.route("/menus/<int:id>", methods=['DELETE'])
def delete_menu(id):
    for i in range(len(menus)):
        if menus[i]['id']==id:
            menus.pop(i)
            return jsonify(menus)
    else:
        return "not exist ID"

if __name__ == '__main__':
    app.run()