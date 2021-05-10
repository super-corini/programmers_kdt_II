from flask import Flask, jsonify, request


app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Amerciano", "price": 4100},
    {"id": 3, "name": "Caffe Latte", "price": 4600},
]

next_id = len(menus) + 1


@app.route("/")
def hello_flask():
    return "Hello, World!"


# GET /menus  |  자료를 가지고 온다.
@app.route("/menus")
def get_menus():
    return jsonify({"menus": menus})


# POST /menus  |  자료를 자원에 추가한다.
@app.route("/menus", methods=["POST"])
def create_menu():
    global next_id
    # 전달받은 자료를 menus 자원에 추가
    # request에는 클라이언트가 서버에 요청할 때 담기는 자료가 담겨있다.
    # 전달되는 자료는 json형태라고 가정
    request_data = request.get_json()  # {"name": ..., "price": ...}

    new_menu = {
        "id": next_id,
        "name": request_data["name"],
        "price": request_data["price"],
    }
    next_id += 1
    menus.append(new_menu)
    return jsonify(new_menu)


# PUT /menus/<int:id>
@app.route("/menus/<int:id>", methods=["PUT"])
def update_menu(id):
    request_data = request.get_json()

    for menu in menus:
        if menu["id"] == id:
            menu["name"] = request_data["name"]
            menu["price"] = request_data["price"]

            return jsonify({"menus": menus})

    return "id not found", 400


# DELETE /menus/<int:id>
@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    for i, menu in enumerate(menus):
        if menu["id"] == id:
            del menus[i]

            return jsonify({"menus": menus})

    return "id not found", 400


if __name__ == "__main__":
    app.run()
