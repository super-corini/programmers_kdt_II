from flask import Flask, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

# jsonify : 딕셔너리타입을 javascrip에서 사용하는 json이라는 저장형식으로 바꿔주는 모듈,
# requset : HTTP requset를 다눌수 있는 모듈

app = Flask(__name__)

## db info setting
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/flask-proj"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 추가적 메모리가 필요한 기능이므로 꺼둠

## db set
db = SQLAlchemy(app)
db.init_app(app)


class Menu(db.Model):
    __tablename__ = 'menus'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        # return jsonify("{'id': %d, 'name': '%s', 'price': %d}" % (self.id, self.name, self.price))
        return "{'id': %d, 'name': '%s', 'price': %d}" % (self.id, self.name, self.price)


# menus = [
#     {"id": 1, "name": "Espresso", "price": 3800},
#     {"id": 2, "name": "Americano", "price": 4100},
#     {"id": 3, "name": "CafeLatte", "price": 4600},
# ]

@app.route('/')  # @ : 데코레이터 - () 안에 인자가 입력되었을때 아래 함수를 실행
def hello_flask():
    return "Hello World!"


# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    def get():
        lst = db.session.query(Menu).all()
        dict_lst = [{'id': val.id, 'name': val.name, 'price': val.price} for val in lst]
        return dict_lst

    menus = get()

    return jsonify({"menus": menus})  # 리스트인 menus를 리턴하지 못하므로 menus라는 딕셔너리를 만들어 json으로 리턴


# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])  # methods=['GET'] 의 경우가 default 이므로 GET에서는 명시하지 않았음
def create_menu():  # request가 JSON이라고 가정
    def create(new):
        db.session.add(new)

    # 전달받은 자료를 menus 자원에 추가, request에 Client가 Server로 부터 POST 요청할 때 담겨진 자료를 parsing
    request_data = request.get_json()  # {"name": ..., "price": ...}

    ## work with session
    # 입력받은 내용으로 Menu 인스턴스 생성
    menu = Menu(name=request_data['name'], price=request_data['price'])

    try:
        create(menu)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    finally:
        db.session.close()

    return get_menus()

    # new_menu = {
    #     "id": menus[-1]['id'] + 1,  # 추가되는 것을 반영
    #     "name": request_data['name'],
    #     "price": request_data['price'],
    # }
    # menus.append(new_menu)
    # return jsonify(new_menu)


# PUT /menus/<int:id> | 자료를 자원에서 수정한다.
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):

    find_menu = db.session.query(Menu).filter_by(menu_id=menu_id).first() # 결과가 없을 시 None 반환

    if find_menu is None:
        return jsonify({'error_msg': "해당 자료가 존재하지 않습니다."})

    update_data = request.get_json()
    find_menu.name = update_data['name']
    find_menu.price = update_data['price']

    return get_menus()

    # for menu in menus:
    #     if menu["id"] == menu_id:
    #         menu["name"] = update_data["name"]
    #         menu["price"] = update_data["price"]
    #         return jsonify(menu)
    # return jsonify({'error_msg': "해당 자료가 존재하지 않습니다."})


# DELETE /menu/<int:id> : 해당하는 id에 해당하는 데이터를 삭제합니다.
@app.route("/menus/<int:menu_id>", methods=['DELETE'])
def del_menu(menu_id):
    # del_data = request.get_json()
    def delete(del_menu):
        db.session.delete(del_menu)

    find_menu = db.session.query(Menu).filter_by(menu_id=menu_id).first()
    if find_menu is None:
        return jsonify({"error_msg": "해당 자료가 존재하지 않습니다."})

    try:
        delete(find_menu)
        db.session.commit()

    except:
        db.session.rollback()
        raise

    finally:
        db.session.close()

    return get_menus()

    # for idx, menu in enumerate(menus):
    #     if menu["id"] == menu_id:
    #         return jsonify(menus.pop(idx))
    # return jsonify({'error_msg': "해당 자료가 존재하지 않습니다."})


if __name__ == '__main__':  # __name__ <- app.py가 모듈로써가 아니라 직접적으로 실행될때 app.run()을 사용하라는 의미
    app.run()
