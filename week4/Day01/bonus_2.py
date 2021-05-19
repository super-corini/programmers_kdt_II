from flask import Flask, jsonify, request
import pymysql

# DB 연동하기
# 스키마 이름 : kdt, 테이블 이름 : menus
db = pymysql.connect(host="localhost", port=3306, user="root", password="1q2w3e", db="kdt")
# DictCursor가 아닌 일반 Cursor를 사용하면 결과가 튜플 형태로 리턴된다.
cursor = db.cursor(pymysql.cursors.DictCursor)


app = Flask(__name__)


@app.route("/")
def check():
    return "Using DataBase"


# GET /menus | 자료를 가지고 온다.
@app.route("/menus")
def get_menus():
    # sql 실행
    cursor.execute("SELECT * FROM menus")
    # 해당 조회 데이터를 다 호출해 가져온다.
    return jsonify(cursor.fetchall())


# POST /menus | 자료를 자원에 추가한다.
@app.route("/menus", methods=["POST"])
def create_menu():
    request_data = request.get_json()

    sql = """
        INSERT INTO menus 
                    (`id`, `name`, `price`)
                VALUES 
                    ((SELECT IFNULL(MAX(id) + 1, 1) from menus m), %s, %s)
        """
    cursor.execute(sql, (request_data['name'], request_data['price']))
    db.commit()
    cursor.execute("SELECT * FROM menus")
    return jsonify(cursor.fetchall())
    

# PUT /menus/<int:id> | 자료를 자원에서 수정한다.
@app.route("/menus/<int:id>", methods=["PUT"])
def update_menu(id):
    request_data = request.get_json()

    sql = """
        UPDATE menus SET name=%s, price=%s
        WHERE id=%s
        """
    cursor.execute(sql, (request_data['name'], request_data['price'], id))
    db.commit()
    cursor.execute("SELECT * FROM menus")
    return jsonify(cursor.fetchall())


# DELETE /menus/<int:id> | 자료를 자원에서 삭제한다.
@app.route("/menus/<int:id>", methods=["DELETE"])
def delete_menu(id):
    sql = """
        DELETE FROM menus WHERE id=%s
        """
    cursor.execute(sql, (id))
    db.commit()
    cursor.execute("SELECT * FROM menus")
    return jsonify(cursor.fetchall())


if __name__ == "__main__":
    app.run()