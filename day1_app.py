from flask import Flask, jsonify, request

app  = Flask(__name__) # flask의 이 이름을 app으로 넣겠다.

menus = [
    {'id':1, "name":"Expresso","price":3800},
    {'id':2, "name":"Americano","price":4100},
    {'id':3, "name":"CafeLatte","price":4600}
]

@app.route('/') # @ : 데코레이터 -> 요 주소를 요청받았을때 아래 함수를 실행시켜라
def hello_flask():
    return "Hello World!"
    
#GET /menus | 자료를 가지고 온다.
@app.route('/menus') #methods = ['GET']은 생략가능 다른 애들은 써줘야함
def get_menus():
    return jsonify({"menus":menus})

#POST /menus | 자료를 자원에 추가한다.
@app.route('/menus',methods=['POST'])
def create_menu(): #request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # json -> dict
    new_menu = {
        'id':4,
        'name': request_data['name'],
        'price':request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)
  
#PUT /menus | 자료를 수정한다.
@app.route('/menus/<int:menu_id>',methods=['PUT'])
def update_menus(menu_id):
    request_data = request.get_json()
    for menu in menus:
        if menu['id']==menu_id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            return jsonify({"menus":menus})
    else:
        return 'Wrong ID'
 
#DELETE /menus | 자료를 삭제한다.
@app.route('/menus/<int:menu_id>',methods=['DELETE']) 
def delete_menu(menu_id):
    for i, menu in enumerate(menus):
        if menu['id']==menu_id:
            del menus[i]
            return jsonify({"menus":menus})
    else:
        return 'Wrong ID'
    
if __name__ == '__main__': #name 스페이스가 main일 경우 아래 app을 실행해라
    app.run()

