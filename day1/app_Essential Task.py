from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3800},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "Caffe Latte", "price": 4600},
]

@app.route("/")
def hello_flask():
    return "Hello, World!"


# GET /menus  |  자료를 가지고 온다.
@app.route("/menus")
def get_menus():
    return jsonify({"menus": menus})


# POST /menus  |  자료를 자원에 추가한다.
@app.route("/menus", methods=["POST"])
def create_menus():

    request_data = request.get_json()  # {"name": ..., "price": ...}

    new_menu = {
        "id" : 4
        "name": request_data["name"],
        "price": request_data["price"],
    }
    menus.append(new_menu)
    return jsonify(new_menu)

# PUT /menus/<int:id>
@app.route("/menus/<int:id>", methods=["PUT"])
def update_menus(id):
    request_data = request.get_json()

    for i in range(len(menus)):
        if menus[i]["id"] == id:
            menus[i]["name"] = request_data["name"]
            menus[i]["price"] = request_data["price"]

    return jsonify({"menus": menus})

# DELETE /menus/<int:id>
@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):

    del menus[id-1]
    return jsonify({"menus": menus})

if __name__ == "__main__":
    app.run()