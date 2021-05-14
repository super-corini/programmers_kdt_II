from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {'id': 1, 'name': 'Espresso', 'price': 3000},
    {'id': 2, 'name': 'Americano', 'price': 4100},
    {'id': 3, 'name': 'CafeLatte', 'price': 4600},
]

# 이 주소를 요청받았을 때, 밑에 있는 함수를 실행시켜라


@app.route('/')
def hello_flask():
    return 'Hello World!'

# GET /menus | 자료를 가지고 온다.


@app.route('/menus')
def get_menus():
    # 리스트값은 Json화 할 수 없음
    return jsonify({'menus': menus})


# POST /menus | 자료를 자원에 추가한다.
# method의 기본값은 GET 으로 설정
@app.route('/menus', methods=['POST'])
def create_menu():  # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    nxt_id = len(menus)
    request_data = request.get_json()   # Json 파싱 후, dict 형태가 됨
    new_menu = {
        'id': nxt_id+1,
        'name': request_data['name'],
        'price': request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)


@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    print(request_data)
    for menu in menus:
        if menu['id'] == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            break
    else:
        return "Not Found ID"
    return jsonify({'menus': menus})


@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for idx, menu in enumerate(menus):
        if menu['id'] == id:
            menus.pop(idx)
            break
    else:
        return "Not Found ID"
    return jsonify({'menus': menus})


    # CLI 환경에서 직접 호출 되었을 경우
if __name__ == '__main__':
    app.run(debug=True)
