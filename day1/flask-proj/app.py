from flask import Flask, jsonify, request
# jsonify는 파이썬의 딕셔너리 타입을 json 형식으로 바꿔줌
# 왜 cmd 통해서 가상환경에 모듈을 설치했는데 에디터 통해서 프로젝트를 열면 package가 없다고 할까?

app = Flask(__name__)

menus = [
    {"id":1, "name":"Expresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"Cafe Mocha", "price":4600},
]

id_index = 4

@app.route('/')
def hello_flask():
    return "Hello World!"

# GET / menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    global id_index

    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # request에 Client가 Server로 부터 POST 요청할 때 담겨진 자료를 parsing
    # {"name": ... , "price" : ...}
    new_menu = {
        "id" : id_index,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    id_index += 1
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<id>', methods=['PUT'])
def modify_menu(id):
    id = int(id)
    idx = binary_search(id)
    if idx == -1:
        return jsonify({"message" : "해당 id가 존재하지 않습니다."})
    request_data = request.get_json()
    menus[idx]['name'] = request_data['name']
    menus[idx]['price'] = request_data['price']

    return jsonify(menus)


@app.route('/menus/<id>', methods=['DELETE'])
def delete_menu(id):
    id = int(id)
    idx = binary_search(id)
    if idx == -1:
        return jsonify({"message" : "해당 id가 존재하지 않습니다."})

    menus.pop(idx)

    return jsonify(menus)

# 이진 탐색 - id에 해당하는 menus의 index 탐색
def binary_search(id):
    start = 0
    end = len(menus)-1

    while True:
        mid = (start + end) // 2
        idx = menus[mid]['id']
        if id == idx:
            return mid
        elif id < idx:
            end = mid - 1
        else:
            start = mid + 1

        if start > end:
            return -1


if __name__ == '__main__': # app.py에서 직접적인 실행파일로 사용될 때 실행하라는 로직
    app.run()


