from flask import Flask #F 대문자는 class객체
from flask import jsonify, request  

app = Flask(__name__)  # __name__ flask 이름 넣기

menus = [
    {"id":1,"name" : "Espresso", "price": 3800},
    {"id":2,"name" : "Americano", "price": 4100},
    {"id":3,"name" : "CafeLatte", "price": 4600}
]


@app.route('/')  # '@' 파이썬 데코레이터 -> '/' root 주소가 요청 받았을때 밑에있는 함수 실행
def hello_flask():
    return "Hello World!"

# GET /menus  | GET -> 자료를 가지고 온다.
@app.route('/menus') # methods=['GET'] 이 기본 메소드 생략가능
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | POST -> 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST']) # methods에 2개 이상의 메소드 추가 가능
def create_menu():  #request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()  # {"name" : ... , "price": ...}
    # request를 쓰면 알아서 client의 요청이 담긴다. 
    new_menu = {
        "id" : 4,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /menus/<int:id> | PUT -> 자료를 자원에 갱신(업데이트) 한다.
@app.route('/menus/<id_num>', methods=['PUT'])
def update_menu(id_num):
    # 전달받은 자료를 menus 자원에 갱신
    request_data = request.get_json()  # {"name" : ... , "price": ...}
    # request를 쓰면 알아서 client의 요청이 담긴다. 
    update_menu = {
        "id" : id_num,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    return jsonify(update_menu)

# DELETE /menus/<int:id> | DELETE -> 자료를 자원에 삭제한다.
@app.route('/menus/<id_num>', methods=['DELETE'])
def delete_menu(id_num):
    # 전달받은 id를 menus 자원에서 삭제
    # 전달받은 자료를 menus 자원에 갱신

    # id가 같은 값을 찾아서 삭제한다.
    return jsonify(id_num)




if __name__ == '__main__':   #  app.py를 내가 직접적으로 실행할 때 해당 로직 사용
    app.run()