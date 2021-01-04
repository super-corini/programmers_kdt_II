from flask import Flask, jsonify, request
# jsonify -> python dic 타입을 JSON으로 변환하기 위해
# requst -> http request를 다룰 수 있는 module

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3000},
    {"id": 2, "name": "Latte", "price": 4000},
    {"id": 3, "name": "Mocha", "price": 4500},
]

@app.route('/')
def hello_flask():
    return "Hello World!!"

# GET /menus -> 자료를 가져온다
@app.route("/menus") # methods param default -> "GET", 이 경우 GET이기 때문에 skip
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus -> 자료를 자원에 추가한다
@app.route("/menus", methods = ["POST"])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name" : ..., "price" : ...}
    post_num = len(menus) + 1
    for i, element in enumerate(menus):
        if i + 1 != element["id"]: # 만약 사이 빈 공간(id)가 보인다면 거길 채워주자
            post_num = i + 1
            break
    new_menu = {
        "id" : post_num,
        "name" : request_data["name"],
        "price" : request_data["price"]
    }
    menus.append(new_menu)
    menus.sort(key=lambda x: x["id"]) # 빈 공간을 뒤에다 append 했으니 순서가 엉켰을 수 있기 때문에 sort!
    return jsonify(menus)

# PUT /menus -> 자료를 바탕으로 자원을 갱신
@app.route("/menus/<int:id>", methods = ["PUT"])
def edit_menu(id): #request가 JSON이라고 가정
    # 전달받은 자료를 바탕으로 수정
    request_data = request.get_json() # {"name" : ..., "price" : ...}
    for i, element in enumerate(menus):
        if element["id"] == id:
            menus[i] = {
                "id": id,
                "name": request_data["name"],
                "price": request_data["price"]
            }
    return jsonify(menus)

# DELETE /menus -> 자료를 바탕으로 자원을 삭제
@app.route("/menus/<int:id>", methods = ["DELETE"])
def del_menu(id): #request가 JSON이라고 가정
    # 전달받은 자료를 바탕으로 삭제
    request_data = request.get_json() # {"name" : ..., "price" : ...}
    for i, element in enumerate(menus):
        if element["id"] == id:
            del menus[i]
    return jsonify(menus)

if __name__ == "__main__":
    app.run()