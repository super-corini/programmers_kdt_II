from flask import Flask, jsonify, request
#jsonify: dic을 json으로 바꿔줌
#request: http.request를 다룰 수 있는 모듈

app = Flask(__name__) #flask객체 생성

menus = [
    {"id" : 1, "name": "Espresso", "price":3800},
    {"id" : 2, "name": "Americano", "price":4100},
    {"id" : 3, "name": "CafeLatte", "price":4600}
]

@app.route('/') #주소를 요청받았을 때 밑에있는 함수를 실행하라(데코레이터)
def hello_flask():
    return 'hello world'

#GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})


#POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods = ['POST']) #default가 get
def create_menus(): #requestark JSON이라고 가정
    #전달받은 자료를 menus 자원에 추가
    newid = len(menus)-1
    request_data = request.get_json() #{"name: ...", ...}
    new_menu = {
        "id" : newid,
        "name" : request_data['name'],
        "price" : request_data['price']
    }
    menus.append(new_menu)
    return jsonify({"menus": menus})

@app.route('/menus/<int:id>', methods = ['PUT'])
def put_menu(id):
    request_data = request.get_json()
    if id > len(menus):
        return "index error"

    menus[id-1]['name'] = request_data['name']
    menus[id-1]['price'] = request_data['price']
    return jsonify({'menus': menus})

@app.route('/menus/<int:id>', methods = ['DELETE'])
def delete_menu(id):
    if id > len(menus):
        return "index error"

    menus.pop(id-1)
    for i in range(id-1, len(menus)):
        menus[i]['id'] -= 1
    return jsonify({'menus':menus})


if __name__ == '__main__': ##이 파일이 실행되면 실행하라는 뜻
    app.run()