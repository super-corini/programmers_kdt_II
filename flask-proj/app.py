from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from queue import PriorityQueue

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tkdals96@localhost:3306/server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(20))
    price = db.Column(db.VARCHAR(10))

    def __repr__(self):
        return f"id : {self.id}\nname : {self.name}\nprice : {self.price}"

db.create_all()

class MenuFunc():
    def init(self):
        pass

    def get_menus(self):
        return db.session.query(Menu).all()

    def add_menu(self, menu):
        new_menu = Menu(name=menu['name'], price=menu['price'])
        db.session.add(new_menu)
        db.session.commit()
        return new_menu

    def update_menu(self, id, menu):
        saved_menu = self.get_menu_byid(id)
        saved_menu.update(menu)
        db.session.commit()
        return saved_menu

    def delete_menu(self, id):
        rid_menu = self.get_menu_byid(id)
        rid_menu.delete()
        db.session.commit()
        return rid_menu

    def get_menu_byid(self, id):
        return db.session.query(Menu).filter(Menu.id == int(id))


menus = [
    {"name":"Espresso", "price":3800},
    {"name":"Americano", "price":4100},
    {"name":"CafeLatte", "price":4600},
]

menu = MenuFunc()
# db.session.execute('''TRUNCATE TABLE menu''')
# db.session.commit()
for m in menus:
    menu.add_menu({"name": m['name'], 'price': m["price"]})

# @ = python decorator
# => 다음 주소를 입력받았을 때 아래 함수를 실행하라는 뜻
@app.route('/')
def hello_flask():
    return "Hello World!@!@!"

# GET /menus | 자료를 가지고 온다.
@app.route('/menus') # GET은 methods 생략 가능
def get_menus():
    return jsonify(menu.get_menus())


# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu():
    ret = menu.add_menu(request.get_json())
    return ret if ret else '', 500

@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    ret = menu.update_menu(id, request.get_json())
    return ret if ret else '', 500

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    ret = menu.delete_menu(id)
    return ret if ret else '', 500

if __name__ == '__main__':
    app.run(debug=True)
