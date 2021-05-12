from flask import Flask #F 대문자는 class객체
from flask import jsonify, request, render_template, redirect 
from flask_sqlalchemy import SQLAlchemy # ORM - SQLAlchemy db 패키지 연동

app = Flask(__name__)  # __name__ flask 이름 넣기

############
app.config['SECRET_KEY'] = 'week4day1bonus2@kim'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menus.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # SQLAlchemy의 이벤트를 처리하는 옵션 
############

db = SQLAlchemy(app)

class Menus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer,nullable=False)  

    def __init__(self,name,price):
        # self.id = id    primary_key(기본키) 자동으로 증가한다. Auto-incrementing
        self.name = name
        self.price = price

# menus = [
#     {"id":1,"name" : "Espresso", "price": 3800},
#     {"id":2,"name" : "Americano", "price": 4100},
#     {"id":3,"name" : "CafeLatte", "price": 4600}
# ]

@app.route('/')  # '@' 파이썬 데코레이터 -> '/' root 주소가 요청 받았을때 밑에있는 함수 실행
def hello_flask():
    # db 초기화 작업
    db.session.query(Menus).delete()
    db.session.add(Menus(name = 'Espresso',price = 3800))
    db.session.add(Menus('Americano',4100))
    db.session.add(Menus('CafeLatte',4600))
    db.session.commit()
    db.session.commit()   

    return "Hello Stranger!"

# GET /menus  | GET -> 자료를 가지고 온다.
@app.route('/menus') # methods=['GET'] 이 기본 메소드 생략가능
def get_menus():
    #return jsonify({"menus" : menus})
    m = Menus.query.all()
    return render_template('index.html', menus=m) # html로 표시
    
# POST /menus | POST -> 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST']) # methods에 2개 이상의 메소드 추가 가능
def create_menu():  #request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()  # {"name" : ... , "price": ...}
    # request를 쓰면 알아서 client의 요청이 담긴다. 

    # new_menu = {
    #     "id" : len(menus)+1,  # POST 될 때, id 증가
    #     "name" : request_data['name'],
    #     "price" : request_data['price']
    # }
    new_menu = Menus(request_data['name'],request_data['price'])

    #menus.append(new_menu)
    db.session.add(new_menu)
    db.session.commit()

    return redirect("/menus")

# PUT /menus/<int:id> | PUT -> 자료를 자원에 갱신(업데이트) 한다.
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    # 전달받은 자료를 menus 자원에 갱신
    request_data = request.get_json()  # {"name" : ... , "price": ...}
    # request를 쓰면 알아서 client의 요청이 담긴다. 
    
    # update_menu = {
    #     "id" : id,
    #     "name" : request_data['name'],
    #     "price" : request_data['price']
    # }

    # for menu in menus :
    #     if menu['id'] == id :
    #         menu['name'] = request_data['name']
    #         menu['price'] = request_data['price']
    #         break
    # else:
    #     return "NOT FOUND ID"

    try:
        update_menu = Menus.query.filter_by(id=id).first()
        update_menu.name = request_data['name']
        update_menu.price = request_data['price']
        db.session.commit()

        return redirect("/menus")
    
    except:
        return "NOT FOUND ID"



# DELETE /menus/<int:id> | DELETE -> 자료를 자원에 삭제한다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    # 전달받은 id를 menus 자원에서 삭제
    # for i, menu in enumerate(menus):
    #     if menu['id'] == id:
    #         menus.pop(i)
    #         break
    # else:
    #     return "NOT FOUND ID"

    try:
        select_menu = Menus.query.filter_by(id=id).first()
        db.session.delete(select_menu)
        db.session.commit()

        return redirect("/menus")

    except:
        return "NOT FOUND ID"


if __name__ == '__main__':   #  app.py를 내가 직접적으로 실행할 때 해당 로직 사용
    db.create_all() # db 생성
    app.run(debug=True) # debug=True 하면 서버 껏다켯다 필요없이 세이브하면 새로 됨