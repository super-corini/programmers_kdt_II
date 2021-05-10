# from flask import Flask, jsonify, request, Response
# import pymysql
# # from flask.wrappers import Request, Response
# # from werkzeug.exceptions import HTTPException

# app = Flask(__name__)
# app.config.from_object("config.Config")
# db = pymysql.connect(
#     host = app.config["DB_HOST"],
#     port = 3306,
#     user = app.config["DB_USERNAME"],
#     passwd = app.config["DB_PASSWORD"],
#     db = app.config["DB_NAME"]
# )
# menus = [
#     {
#         "id": 1,
#         "name": "Espresso",
#         "price": 3800
#     },
#     {
#         "id": 2,
#         "name": "Americano",
#         "price": 4100
#     },
#     {
#         "id": 3,
#         "name": "CafeLatte",
#         "price": 4600
#     }
# ]

# next_post_id = max([menu["id"] for menu in menus]) + 1

# @app.route("/")
# def hello_flask():
#     return "Hello World!"


# # GET /menus | 자료를 가지고 온다
# @app.route("/menu", methods=["GET"])
# def get_menus():
#     return jsonify({"menus": menus})

# # POST /menus | 자료를 자원에 추가한다.
# @app.route("/menu", methods=["POST"])
# def create_menus(): # request가 JSON이라고 가정
#     # 전달받은 자료를 menus 자원에 추가
#     request_data = request.get_json() # {"name": ..., "price": ...}

#     # 되긴하는데 짜친다...
#     global next_post_id
#     new_menu = {
#         "id": next_post_id,
#         "name": request_data['name'],
#         "price": request_data['price']
#     }

#     menus.append(new_menu)
#     next_post_id += 1

#     return jsonify(new_menu)

# @app.route("/menu/<int:id>", methods=["PUT"])
# def update_menu(id):
#     request_data = request.get_json()
#     for menu in menus:
#         if menu.get("id") == id:
#             menu["name"], menu["price"] = request_data["name"], request_data["price"]
#             return jsonify(menu)
#     return "Can't update", 404

# @app.route("/menu/<int:id>", methods=["DELETE"])
# def delete_menu(id):
#     for menu in menus:
#         if menu.get("id") == id:
#             menus.remove(menu)
#             return "success to delete"
#     return "Can't delete", 404
    
# if __name__ == '__main__':
#     app.run()