from flask import Flask, jsonify, request
# jsonify -> json 형태로 바꾸는 모듈
# request -> HTTP request를 다룰수 있는 모듈

app = Flask(__name__)  # 이 flask의 이름을 app의 변수에 넣어준다.

menus = [
    {'id':1, 'name':'Expresso', 'price':3800},
    {'id':2, 'name':'Americano', 'price':4100},
    {'id':3, 'name':'CafeLatte', 'price':4600}
]


# @ = 데코레이터
# 가로안에 있는 주소를 인자로 받았을 때
# 밑에 있는 함수를 실행하라는 뜻
@app.route('/')
def hello_flask():
    return 'Hello World!'


# GET /menus | 자료를 가지고 온다.
# method에 default는 GET이므로 생략가능
@app.route('/menus')
def get_menus():
    # List 타입은 json화 시킬수 없다.
    # 따라서 dict를 새로 만든다.
    return jsonify({'menus':menus})


# POST /menus | 자료를 자원에 추가한다.
# POST, PUT, DELETE 등 method인자로 넣겨줘야한다.
@app.route('/menus', methods=['POST'])
def create_menu():  # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()  # {'name' : ..., 'price':...}
    new_menu = {
        'id' : len(menus)+1,
        'name' : request_data['name'],
        'price' : request_data['price']
    }

    menus.append(new_menu)
    return jsonify(new_menu)


# PUT /menus/<int:id> | 자료를 자원에서 수정한다.
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()

    for menu in menus:
        if menu['id'] == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            return jsonify(menu)
    
    # exception 조건을 만들어주는 것이 좋다.
    return jsonify({'Error_msg' : '해당 자료가 존재하지 않습니다!'})


# DELETE /menus/<int:id> | 자료를 자원에서 삭제한다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for i, menu in enumerate(menus):
        if menu['id'] == id:
            return jsonify(menus.pop(i))
    
    # exception 조건을 만들어주는 것이 좋다.
    return jsonify({'Error_msg' : '해당 자료가 존재하지 않습니다!'})


# __name__ 가 __main__일 때 실행해라
# 즉, app.py 파일을 직접적으로 실행할 때 이 로직을 사용해라
if __name__ == '__main__':
    app.run()