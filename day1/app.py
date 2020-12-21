from flask import Flask, request, jsonify

app = Flask(__name__)

menus = [
    {"id": 1, "name": "espresso", "price": 2500},
    {"id": 2, "name": "americano", "price": 3000},
    {"id": 3, "name": "cafe latte", "price": 3500},
]


@app.route("/")
def hello_flask():
    return "Hello, World"


@app.route("/menus")
def get_menus():
    return jsonify({"menus": menus})


@app.route("/menus", methods=["POST"])
def post_menu():
    request_data = request.get_json()
    new_menu = {
        "id": menus[-1]["id"] + 1,
        "name": request_data["name"],
        "price": request_data["price"],
    }
    menus.append(new_menu)
    return jsonify(new_menu)


@app.route("/menus/<int:id>", methods=["PUT"])
def put_menu(id):
    request_data = request.get_json()
    updated_menu = {
        "id": id,
        "name": request_data["name"],
        "price": request_data["price"],
    }
    for i, menu in enumerate(menus):
        if menu["id"] == id:
            menus[i] = updated_menu
            return jsonify(updated_menu)
    return "Wrong ID"


@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    for i, menu in enumerate(menus):
        if menu["id"] == id:
            return menus.pop(i)
    return "Wrong ID"


if __name__ == "__main__":
    app.run()