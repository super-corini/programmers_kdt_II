from flask import Flask, jsonify, request
"""
jsonify : dictionary를 json(javascript에서 사용하는 데이터 형식) 형식으로 변환
request : HTTP Request를 다룰 수 있는 모듈
"""

app = Flask(__name__)

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]

@app.route('/')  ## '/' 이 주소를 요청받았을 때 아래 함수를 실행해라 '/' 는 root!
def hello_flask() :
    return "Hello World"       

## 같은 end point인 menus에 대해서 각각 다른 처리(동사)를 이용해 상황에 맞는 로직을 구현할 수 있음
## GET /menus : 자료를 가지고 온다
@app.route('/menus')    ## 인자로 methods가 있는데, default 값이 GET임!
def get_menus(): #{
    return jsonify({"menus":menus})  ## List 타입은 json형식으로 변형 X -> list를 새로운 dictionary로 만들기 -> json형으로 변환
#}

## POST / menus : 자료를 자원에 추가한다.
@app.route('/menus', methods=["POST"])  ## methods를 list 형태로 저장 -> 여러가지 method에 대해 처리 가능
def create_menu() : #{
    # 전달받은 자료를 menus 자원에 추가
    # request가 JSON이라고 가정
    ## 자동적으로 client가 서버로부터 POST를 이용해서 요청할 때 준 자료가 자동적으로 담겨있음 -> json을 dict형으로 파싱
    request_data = request.get_json()  # {"name" : ..., "price" : ...}
    new_menu = {
        "id"    : request_data["id"] if "id" in request_data else menus[-1]['id']+1,  ## 보너스 과제 1
        "name"  : request_data["name"],
        "price" : request_data["price"],
    }
    menus.append(new_menu)
    return jsonify(new_menu)
#}

## PUT : 해당하는 id에 해당하는 데이터를 갱신
@app.route('/menu/<int:id>', methods=["PUT"])
def update_menu(id) : #{
    request_data = request.get_json()
    for m in menus : #{
        if m['id'] == id : #{
            m['name']  = request_data['name']
            m['price'] = request_data['price']
            break
        #}
    #}
    return jsonify({"menus":menus})
#}

## DELETE : 해당하는 id에 해당하는 데이터를 삭제
@app.route('/menu/<int:id>', methods=["DELETE"])
def delete_menu(id) : #{
    for m in menus : #{
        if m['id'] == id : 
            menus.remove(m)
            break
    #}    
    return jsonify({"menus":menus})
#}

@app.route('/<name>')
def my_view_func(name) : #{
    return name
#}


if __name__ == "__main__" :
    app.run()