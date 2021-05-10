from flask import Flask, jsonify, request, Response
import pymysql
# from flask.wrappers import Request, Response
# from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config.from_object("config.Config")
db = pymysql.connect(
    host = app.config["DB_HOST"],
    port = 3306,
    user = app.config["DB_USERNAME"],
    passwd = app.config["DB_PASSWORD"],
    db = app.config["DB_NAME"]
)
# table
# +-------+-------------+------+-----+---------+----------------+
# | Field | Type        | Null | Key | Default | Extra          |
# +-------+-------------+------+-----+---------+----------------+
# | id    | int         | NO   | PRI | NULL    | auto_increment |
# | name  | varchar(20) | YES  |     | NULL    |                |
# | price | int         | YES  |     | NULL    |                |
# +-------+-------------+------+-----+---------+----------------+

@app.route("/")
def hello_flask():
    return "Hello app_db World!"


# GET /menus | 자료를 가지고 온다
@app.route("/menu", methods=["GET"])
def get_menus():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM menu_info;"
    try:
        cursor.execute(sql)
        select_all = cursor.fetchall()
    except Exception as e:
        return e, 500
    return jsonify(select_all)

# # POST /menus | 자료를 자원에 추가한다.
@app.route("/menu", methods=["POST"])
def create_menus(): # request가 JSON이라고 가정
    #전달받은 json을 db table에 mapping 해야함
    request_data = request.get_json() # {"name": ..., "price": ...}
    dict_cursor = db.cursor(pymysql.cursors.DictCursor)
    insert_name, insert_price = request_data["name"], int(request_data["price"])
    sql = f'INSERT menu_info (name, price) values ("{insert_name}", {insert_price});'
    try:
        dict_cursor.execute(sql)
        result = dict_cursor.fetchone()
        db.commit()
    except Exception as e:
        print(e)
        return "실패", 500
    return "성공", {"name": insert_name, "price": insert_price}


@app.route("/menu/<int:id>", methods=["PUT"])
def update_menu(id):
    request_data = request.get_json()
    insert_name, insert_price = request_data["name"], int(request_data["price"])
    sql = f'UPDATE menu_info set name="{insert_name}", price={insert_price} where id = {id};'
    dict_cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        dict_cursor.execute(sql)
        result = dict_cursor.fetchone()
        db.commit()
    except Exception as e:
        return e, 500
    return "성공", {"name": insert_name, "price": insert_price}

@app.route("/menu/<int:id>", methods=["DELETE"])
def delete_menu(id):
    sql = f'DELETE FROM menu_info WHERE id = {id}'
    dict_cursor = db.cursor(pymysql.cursors.DictCursor)
    try:
        result = dict_cursor.execute(sql)
        db.commit()
    except Exception as e:
        return e, 500
    return jsonify(result)
    
if __name__ == '__main__':
    app.run()