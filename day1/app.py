"""
번호는 항상 1번부터 차례대로 되게 유지했습니다.
update는 그 다음 번호로 지정했고,
delete의 경우 pop을 사용했고, 번호도 등차수열이 되게끔 조절했습니다.
"""
from flask import Flask, jsonify, request
app = Flask(__name__)
menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "CafeLatte", "price": 4600},
]


# 기본 제목
@app.route('/')
def page_title():
    return "Coffee Menu"


# GET /menus | 자료를 가지고 온다.
@app.route('/menus')  # default: GET
def get_menus():
    return jsonify({"menus": menus})


# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():  # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()  # {"name":, ... , "price": ...}
    new_menu = {
        "id": len(menus)+1,
        "name": request_data['name'],
        "price": request_data['price'],
    }
    menus.append(new_menu)
    """자료형 확인용
    print('-------------------------------------')
    print(request.get_json())
    print(type(request.get_json()))

    print(request.get_data())

    print(type(jsonify(new_menu)))
    print('-------------------------------------')
    """
    return jsonify(new_menu)


# UPDATE /menus/<id> | 자료를 자원에 업데이트한다.
@app.route('/menus/<id_no>', methods=["PUT"])  # URL에 <>를 붙임으로서 이를 함수의 인자로 대입할 수 있습니다.
def my_view_func(id_no: str):
    request_data = request.get_json()
    menus[int(id_no)-1]['name'] = request_data['name']
    menus[int(id_no)-1]['name'] = request_data['name']
    update_menu = {
        "id": int(id_no),
        "name": request_data['name'],
        "price": request_data['price'],
    }
    return jsonify(update_menu)


# DELETE /menus/<id> | 자료를 자원에서 제거한다.(보너스 과제1 내용 포함)
@app.route('/menus/<id_no>', methods=["DELETE"])  # URL에 <>를 붙임으로서 이를 함수의 인자로 대입할 수 있습니다.
def my_view_func2(id_no: str):
    for i, menu in enumerate(menus):
        if menu["id"] == int(id_no):
            menus.pop(i)
            for j in range(i, len(menus)):
                menus[j]["id"] -= 1
            return "delete {}".format(id_no)
    return "Fail to delete"


if __name__ == "__main__":
    app.run()