from flask import Flask, jsonify, request
import dataset, json
import pandas as pd


app = Flask(__name__)

db = dataset.connect("sqlite:///menus.db")
Menus = db.create_table("menus")


def get_all():
    """
    Menus에 있는 모든 데이터를 가져오는 함수
    Input -> None
    Output -> list(dict)
    """
    df = pd.DataFrame(Menus.all())
    menus = df.to_json(orient="records")
    return json.loads(menus)


@app.route("/")
def hello_flask():
    return "Hello, World!"


# GET /menus  |  자료를 가지고 온다.
@app.route("/menus")
def get_menus():
    return jsonify(get_all())


# POST /menus  |  자료를 자원에 추가한다.
@app.route("/menus", methods=["POST"])
def create_menu():
    request_data = request.get_json()

    new_menu = dict(name=request_data["name"], price=request_data["price"])
    Menus.insert(new_menu)

    return jsonify(get_all())


# PUT /menus/<int:id>
@app.route("/menus/<int:id>", methods=["PUT"])
def update_menu(id):
    request_data = request.get_json()

    menu = list(Menus.find(id=id))
    if not menu:
        return "해당 id값이 메뉴에 없습니다.", 400

    request_data["id"] = id
    Menus.update(request_data, ["id"])

    return jsonify(get_all())


# DELETE /menus/<int:id>
@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    menu = list(Menus.find(id=id))
    if not menu:
        return "해당 id값이 메뉴에 없습니다.", 400

    Menus.delete(id=id)
    return jsonify(get_all())


if __name__ == "__main__":
    app.run()
