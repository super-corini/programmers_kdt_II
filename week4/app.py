from flask import Flask, jsonify, request
# jsonify: 딕셔너리 타입을 자바스크립트에서 사용되는 json 저장 방식으로 바꿔준다.  
# request: HTTP Request를 다룰 수 있는 모듈  

app = Flask(__name__)

menus = [
    {'id':1, 'name':'Espresso', 'price':3800},
    {'id':2, 'name':'Americano', 'price':4100},
    {'id':3, 'name':'CafeLatte', 'price':4600},
]

# @: 파이썬 데코레이터
@app.route('/') # 주소 '/'를 입력받았을 때 아래의 함수를 실행하라는 의미
def hello_flask():
    return 'Hello World!'

# GET /menus
@app.route('/menus')
def get_menus():
    return jsonify({'menus': menus})

# POST /menus
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # request에 클라이언트가 서버에 요청한 자료가 담김
    request_data = request.get_json() # {'name':..., 'price':...}
    new_menu = {
        'id':menus[-1]['id'] + 1,
        'name':request_data['name'],
        'price':request_data['price'],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# UPDATE /menus
@app.route('/menus/<int:id>', methods=['PUT'])
# URL에 <>를 붙여 이를 함수의 인자로 대입할 수 있다.  
def update_menu(id):
    request_data = request.get_json()
    put_menu = {
        'id':id,
        'name':request_data['name'],
        'price':request_data['price']
    }
    for i, x in enumerate(menus):
        if x['id'] == id:
            menus[i] = put_menu
    return jsonify(put_menu)

# DELETE /menus
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    for i in menus:
        if i['id'] == id:
            del_menu = i
            menus.remove(i)
    return jsonify(del_menu)
    

# __name__ 스페이스가 __main__인 경우, 즉 app.py 파일을 직접 실행한 경우
# app을 실행하라는 의미
if __name__ == '__main__':
    app.run()