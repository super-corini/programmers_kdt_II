from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600}
]
@app.route('/')
def hello_flask():
    return "Hello World!"

@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})


@app.route('/menus', methods = ['POST']) 
def create_menus():

    request_data = request.get_json() 
    # idx 를  list 의 길이 + 1 로 계산
    idx = len(menus) + 1
    new_menu = {
        "id": idx
        "name": request_data['name'],
        "price": request_data['price']
    }
    
    menus.append(new_menu)
    return jsonify(new_menu)

@app.route('/menus/<int:id>', methods = ['PUT'])
def update_menus(id):
    request_data = request.get_json()
    # menus list 에 대해 for loop 을 돌면서
    # id 가 같을 경우 update 를 진행합니다.
    for menu in menus:
        if menu['id'] == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
    return jsonify({"menus":menus})

@app.route('/menus/<int:id>', methods = ['DELETE'])
def delete_menus(id):
    # delete 연산을 보다 쉽게 하기 위해 id 값을 기준으로 정렬시켜줍니다.
    menus.sort(key = lambda x:x['id'])

    # 같은 id 값을 가지는 데이터가 여럿일 경우를 대비하여 
    # delete 가 처음 시작되는 id 의 index 값과, 중복된 데이터의 개수를 count 해주는 변수를 선언합니다.
    idx_value, cnt = 0, 0
    
    for idx, menu in enumerate(menus):
        if menu['id'] == id and cnt ==0: # 처음 delete 가 되는 id 의 index 를 저장 후 count +1
           idx_value = idx
           cnt += 1
        elif menu['id'] == id: # 중복되는 id 의 개수 count
            cnt += 1
    
    # count 의 수 만큼 반복하여 해당 idx 를 del 시켜줍니다.
    # 이 때, 처음 정렬을 시켜줬기에 idx_value 의 값은 변함없이 같은 값 만을 가지게 됩니다.
    for _ in range(cnt):
        del menus[idx_value]
    return jsonify({"menus": menus})

if __name__ == '__main__':
    app.run()