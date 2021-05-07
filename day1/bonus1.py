from flask import Flask, jsonify, request

app = Flask(__name__)


menus = [
    {"id":1,
    "name":"Espresso",
    "price": 3800},
    {"id":2,
    "name":"Americano",
    "price": 4100},
    {"id":3,
    "name":"CaffeLatte",
    "price": 4800},
]


@app.route('/') # 해당 주소 입력시 아래 함수 실행(HOME에 접근)
def hello_flask():
    return "Hello World!"

# GET /menus : 자료 가지고옴
@app.route('/menus') # menus에 접근
def get_menus():
    return jsonify({"menus":menus})


###########################################################
### Mandatory Task: Implementing PUT & DELETE function
# PUT /menus/<int:id>: 'update' data by identified by 'id'
@app.route('/menus/<int:id>', methods=["PUT"])
def update_menus(id):
    request_data = request.get_json()
    for menu in menus:
        if menu['id'] == id:
            menu['name'] = request_data['name']
            menu['price'] = request_data['price']
            break
    else:
        return "Not Found"
    return jsonify(menus)

# DELETE /menus/<int:id>: 'delete' data by identified by 'id'
@app.route('/menus/<int:id>', methods=["DELETE"])
def delete_menus(id):
    request_data = request.get_json()
    menus = [m for m in menus if m['id'] != id] # O(n)
    return jsonify(menus)

def delete_menus_v2(id):
    request_data = request.get_json()
    id_sets = set([x['id'] for x in menus]) # get set of ids
    id_sets = list(id_sets.difference([id])) # make list of diff between id_sets and 'id'
    menus = [m for m in menus if m['id'] in id_sets] # O(n)
    return jsonify(menus)

#########################################################
### BONUS TASK 
# POST /menus : 자료 추가
# Increment ID
@app.route('/menus', methods=["POST"]) # POST 메서드 실행
def create_menu():
    # 전달받은 자료를 menus에 추가
    request_data = request.get_json() #get_json으로 파싱해 와서 dict타입으로 받는다.
    # {"name":...,...}
    new_id = menus[-1]['id']+1
    new_menu = {
        "id":new_id,
        "name":request_data['name'],
        "price":request_data['price']
        
    }
    menus.append(new_menu)
    return jsonify(new_menu)


if __name__ == "__main__":
    app.run()

