from flask import Flask,jsonify,request   #Flask라는 클래슬를 flask에서부터 가져옴
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)    #Flask 클래스의 instance가 만들어짐
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)


# class Menus(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100),nullable=False)
#     price = db.Column(db.Integer, nullable=False)

# db.create_all()

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"Cafe Latte", "price":4500}
]

@app.route('/')          #해당 "/"주소인 경우 아래 함수 실행시킴: hello world 출력.
def hello_flask():
    return 'Hello World'

# GET /menus | 자료를 가지고 옴
@app.route('/menus')
def get_menus():
    return jsonify({"menus":menus})   #list은 json으로 변환불가, dictionary 형태로 만들어줘야함


# POST /menus  | 자료를 자원에 추가함
@app.route('/menus',methods=["POST"])
# 전달받은 자료를 menus 자원에 추가
def create_menus():
    request_data = request.get_json()    #client가 요청한 자료가 request에 자동적으로 담김 -> json으로 parsing
    new_menu = {"id":(menus[-1]["id"])+1, "name": request_data['name'], "price":request_data["price"]}
    menus.append(new_menu)

    return jsonify(new_menu)

@app.route('/menus/<int:menu_id>',methods=["PUT"])
def update_menu(menu_id):
    request_data = request.get_json()
    for menu in menus:
        if menu["id"] == menu_id:
            menu["name"] = request_data["name"]
            menu["price"] = request_data["price"]
            return jsonify(menu)
    
    else:
        return jsonify ({"error":"not a valid id"})


@app.route('/menus/<int:menu_id>',methods=["DELETE"])
def del_menu(menu_id):
    for idx, menu in enumerate(menus):
        if menu["id"] == menu_id:
            return jsonify(menus.pop(idx))
    else:
        return jsonify ({"error":"not a valid id"})

if __name__ == '__main__':  #이름이 메인인 경우: 앱실행
    app.run()