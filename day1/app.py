from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americno", "price": 4100},
    {"id": 3, "name": "CaffeLatte", "price": 4600},
]


@app.route('/')
def hello_flask():
    return "Hello World!"


# Get/menus | 자료를 가지고 온다.
@app.route('/menus')  ## method = ['GET']은 생랴가능
def get_menus():
    return jsonify({"menus": menus})


# Post/menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():  # request가 JSON이라고 가
    # 전달받은 자룔를 menus 자원에 추가
    request_data = request.get_json()  # {"name" : ..., "price":....}
    num = len(menus)
    new_menu = {
        "id": num+1,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)


# Update/menus | id에 해당하는 데이터를 업데이트한다.
@app.route('/menus/<int:id>', methods=['PUT'])  # URL에 <>를 붙임으로서 이를 함수의 인자로 대입할 수 있습니다.
def put_menu(id):
    update_data = request.get_json()

    for i in menus:
        if i['id'] == id:
            i['name'] = update_data['name']
            i['price'] = update_data['price']

    return jsonify(menus)


# Delete/menus | id에 해당하는 데이터를 삭제한다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):

    for ind, i in enumerate(menus):
        if i['id'] == id:
            del menus[ind]
            return jsonify(i)



if __name__ == '__main__':
    app.run()
