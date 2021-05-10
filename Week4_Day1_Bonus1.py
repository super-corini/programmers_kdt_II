from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

# Main
@app.route('/')
def home_flask():
    return "Week4 Day1 - 보너스 과제 1 : ID야 움직여라 얍!"

# READ(GET) /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# CREATE(POST) /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # id 번호 바꿈
    request_data = request.get_json() # {"name" : ..., "price": ...}
    new_menu = {
        "id" : len(menus) + 1, # 번호 확인 
        # 생각해볼 점 - del한 경우 번호가 빠지게 되면 len으로 계산하면
        # 빠지는 번호에 대한 대처가 안됨
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# UPDATE
@app.route('/menus/<int:id>',methods=['PUT'])
def update_menus(id):
    request_data = request.get_json()
    try:
        menus[id-1]['name'] = request_data['name']
        menus[id-1]['price'] = request_data['price']
        return jsonify({"menus" : menus})
    except Exception as e:
        return  f'해당 id가 존재하지 않습니다.: {e}'

# DELETE
@app.route('/menus/<int:id>',methods=['DELETE'])
def delete_menu(id):
    try:
        # id를 확인
        id_l = len(menus)
        if id_l == id:
            del menus[id-1]
        else:
            del menus[id-1]
            # 메뉴가 삭제되고 뒷번호를 당겨서 비는 번호가 없게 함
            for i in range(id_l-id):
                menus[id+i-1]['id'] = id+i
        return jsonify({"menus" : menus})
    except Exception as e:
        return  f'해당 id가 존재하지 않습니다.: {e}'

if __name__ == '__main__':
    app.run()