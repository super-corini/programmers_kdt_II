from flask import Flask, jsonify, request
# jsonify : 파이썬의 딕셔너리 타입(menus)을 json이라는 데이터 저장 방식으로 바꿔줌
# request : HTTP request를 다룰 수 있는 모듈
app = Flask(__name__) # Flask를 바탕으로 한 객체 생성. 인자로 __name__전달. Flask에 이름을 앱으로 넣어준다는 의미

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]


# 홈 디렉토리
@app.route('/') # 이 주소를 요청받았을때 밑에 있는 함수를 실행하라.
def hello_code():
    return 'Hello World!'


# GET /menus : 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})
# menus는 리스트로 json으로 변환할 수 없다. 
#따라서 menus를 value로 하는 새로운 딕셔너리를 만들어준다.

new_id = 4
# POST /menus : 자료를 자원에 추가한다.
# @app.route는 기본적으로 methods=['GET']라고 되어있다.
# 나머지 HTTP 동작들, POST 등은 직접 명시를 해야한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    global new_id
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name" : ..., "price": ...}
    # request는 자동적으로 클라이언트가 서버에 POST로 요청할때 담긴 자료가 있다.
    # 따라서 이를 get_json()으로 파싱해주면 딕셔너리 형태로 담기게 된다.
    new_menu = {
        "id" : new_id,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    new_id += 1
    menus.append(new_menu)
    return jsonify(new_menu)


# PUT /menu/<int:id> : 해당하는 id에 해당하는 데이터를 갱신합니다. (HTTPRequest의 Body에 갱신할 내용이 json으로 전달됩니다.)
@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    update_data = request.get_json()
    try:
        menus[id-1]['name'] = update_data['name']
        menus[id-1]['price'] = update_data['price']
        return jsonify(menus[id-1])
    except Exception as e:
        print(e)
        return 'There was a problem!'


# DELETE /menu/<int:id> : 해당하는 id에 해당하는 데이터를 삭제합니다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    try:
        del menus[id-1]
        return jsonify(menus)
    except Exception as e:
        print(e)
        return 'There was a problem!'


if __name__ == '__main__':
    app.run()