# Day 1 - Flask를 Flask 답게

실습에서는 `GET` 과 `POST` 를 이용해서 `/menu` 자원으로부터 데이터를 가지고오고, 자원에 데이터를 추가해보았습니다. 이는 자원에서 할 수 있는 4가지 logic인 CRUD(Create, Read, Update, Delete) 중 Create와 Read에 해당하는 부분입니다. 이를 바탕으로 다음 과제를 해결해봅시다.

## 필수 과제 : 메뉴 관리 CRUD 구현하기

- HTTP 메서드 `PUT` 를 이용해 Update, `DELETE` 를 이용해 Delete 기능을 구현해주세요.
- `PUT /menu/<int:id>` : 해당하는 id에 해당하는 데이터를 갱신합니다. (HTTPRequest으로 Body가 주어집니다.)
- `DELETE /menu/<int:id>` : 해당하는 id에 해당하는 데이터를 삭제합니다.
- `@app.route()` 의 인자로 들어가는 경로에는 다음과 같이 사용해줄 수도 있습니다.

```python
@app.route('/<name>') # URL에 <>를 붙임으로서 이를 함수의 인자로 대입할 수 있습니다.
def my_view_func(name):
    return name
```

### TIL

- `import jsonify`: python dictionary type을 json이라는 java script에서 사용하는 data 저장방식으로 바꿔주기 위해 사용하는 모듈입니다.

- `import request`: HTTP request를 다룰 수 있는 모듈입니다.

- `GET`: 자료를 가지고 올 때 사용합니다.

  - `@app.route('/menus')`
    - `menus`의 자원에 접근하고, `GET` 메소드(default값)를 사용할 때 라우팅합니다.

    - `def get_menus():` 자원(메뉴)을 얻어오는 함수입니다.
    - `jsonify({"menus": menus})`: Python의 List type은 jsonify를 이용하여 변환할 수 없기 때문에 list를 dictionary type에 담아서 jsonify 메소드로 json type으로 변환하여 반환합니다.

- `POST`: 자료를 자원에 추가할 때 사용합니다.

  - `@app.route('/menus', method=['POST'])`
    - `menus` 자원에 접근하고, `POST` 메소드를 사용할 때 라우팅합니다.
    - `def create_menu():` 자원(메뉴)을 추가하는 함수입니다.
    - `request_data = request.get_json()`  
    : `request`모듈을 사용하여 사용자가 입력한 정보를 `get_jason()` 함수로 parsing하여 dictionary type으로 변환하여 `request_data`에 담습니다.
      - 사용자가 입력한 정보는 JSON이라고 가정합니다.
      - {"name": ..., "price": ....}의 형태입니다.

- `PUT`: 자원을 수정할 때 사용합니다.

  - `@app.route('/menus/<int:id>', methods=['PUT'])`  
    -  `menus` 자원에 접근하고 `id`는 정수값을 전달합니다.
    - `PUST` 메소드를 사용할 때 라우팅합니다.

  - `def update_menu(id):` 자원(메뉴)을 수정하는 함수입니다.
    - 해당 id 값을 가진 `menu`의 `name`과 `price`를 수정합니다.
    - 받아온 데이터는 `POST`와 같이 JSON임을 가정합니다. (ex) {"name": ..., "price": ...}
    - 값을 수정하고 수정된 `menus`를 반환합니다.
    - 해당 id가 없다면 for-else문을 통해 에러 메시지 출력합니다.

- `DELETE`: 자원을 삭제할 때 사용합니다.

  - `@app.route('/menus/<int:id>', methods=['DELETE'])`  
    - `menus` 자원에 접근하고, 정수값 `id` 를 전달합니다.
    - `DELETE` 메소드를 사용할 때 라우팅합니다.

  - `def delete_menu(id):` 자원(메뉴)을 수정하는 함수입니다.
    - 해당 id 값을 찾아 해당 dictionary 삭제합니다.
    - 삭제하고, 삭제된 `menus`를 반환합니다.
    - 해당 id가 없다면 for-else문을 통해 에러메시지 출력합니다.

---

## 보너스 과제 I: ID야 움직여라 얍!

- 새로운 menu를 추가하는 `POST` 영역에서 id가 4로 고정되어있는 문제가 발생합니다.
- POST 요청이 들어올 때마다 id가 하나씩 증가하여 `menu` 리스트에 추가될 수 있도록 코드를 수정해주세요.
- 이 과제는 필수 과제 이후에 진행되어야 합니다.

### TIL

1. id를 증가시키기 위해서 `POST` 부분을 수정했습니다.
- 기존의 코드에서는 `new_menu`의 `id`를 상수로 넣어줬지만, 이번에는 `id`를 `len(menus)+1`을 넣어줍니다.
- 메뉴를 추가할 때는 무조건 가장 뒤에 메뉴가 추가되는 것으로 가정했습니다.

2.  인덱스 조정을 하다보니까 `DELETE`의 부분에서도 수정이 필요했습니다.
- 지울 `id`를 가진 메뉴를을 삭제할 때 뒤의 메뉴를 순차적으로 돌며 모두 id 조정을 해줍니다.

---

## 보너스 과제 II : 데이터베이스 연동하기

- 수업에서 다룬 API는 서버를 재시작하면 모든 정보가 리셋되는 치명적인 문제가 있었습니다. 이를 해결하기 위해 데이터만을 저장하는 **데이터베이스**를 도입하여 Flask과 연동할 필요가 생겼습니다.
- SQL과 ORM 중 하나를 선택하여 데이터베이스와 Flask app을 연동해봅시다. (즉, 자원에 CRUD가 발생하면 이 정보가 데이터베이스에 저장되어야합니다.)
- 이 과제는 필수 과제, 보너스 과제 I 이후에 진행되어야 합니다.

### TIL
#### ORM(Object Relational Mapping, 객체-관계 매핑)
- 객체와 관계형 데이터베이스의 데이터를 자동으로 매핑해주는 것을 의미합니다.
  - 객체지향 프로그래밍(OOP: Object Oriented Programming)은 클래스(Class)를 사용하고, 관계형 데이터베이스는 테이블(Table)을 사용합니다.
  - Persistant API라고도 합니다.
  - DB의 schema를 그대로 Class로 맵핑하고 SQL문을 사용하지 않고 schema를 디자인 할 수 있습니다.
- 장점
  - 객체지향적인 코드를 통해 더 직관적이게 이해할 수 있습니다.
  - SQL Query가 아닌 메소드로 데이터를 조작할 수 있습니다.
  - 재사용 및 유지보수에 용이합니다.
- 단점
  - 자동으로 생성되는 query를 사용하기 때문에 섬세한 조작이 어렵습니다.
  - 개발하는 시스템이 복잡해질 수록 코드가 점점 복잡해질 수 있습니다.
  - 속도가 느릴 수 있습니다.

#### Flask-SQLAlchemy 설치
```
pip install flask-sqlalchemy
```

#### app.py 수정
```py
from flask import Flask, jsonify, request
from models import db, Menu


app = Flask(__name__)

# db는 sqlite를 사용, 현재 폴더에 menu.db파일 작성
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./menu.db'
# 추가적인 메모리쓰지 않기, False로 하지 않으면 Warning 메시지 발생
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 앱 구동
db.init_app(app)
db.app = app
# db 생성, db가 이미 있다면 아무것도 하지 않음
db.create_all()


@app.route('/')
def hello_flask():
    return 'hello flask:)'


# GET | models.py의 Menu Class의 get_menus() method 사용
@app.route('/menus') 
def get_menus():
    return jsonify(Menu.get_menus())

    
# POST | models.py의 Menu Class의 add_menu() method 사용
@app.route('/menus', methods=['POST'])
def create_menu():
    request_data = request.get_json()
    return jsonify(Menu.add_menu(request_data["name"], request_data["price"]))

    
# PUT | models.py의 Menu Class의 update_menu() method 사용
@app.route('/menus/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    return jsonify(Menu.update_menu(id, request_data["name"], request_data["price"]))

    
# DELETE | models.py의 Menu Class의 delete_menu() method 사용
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    return jsonify(Menu.delete_menu(id))


if __name__ == '__main__':
    app.run(debug=True)
```
- `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./menu.db'`  
  - db는 sqlite를 사용하고, 현재 폴더에 menu.db파일 작성합니다.

- `app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False`
  - 추가적인 메모리쓰지 않고, False로 하지 않으면 Warning 메시지 발생합니다.

- `db.init_app(app)`, `db.app = app`: 앱을 시작합니다.

- `db.create_all()`: db 생성, db가 이미 있다면 아무것도 하지 않습니다.

- `GET`:  `models.py`의 `Menu` Class의 `get_menus()` method 사용합니다.
    
- `POST`: `models.py`의 `Menu` Class의 `add_menu()` method 사용합니다.
- `PUT`: `models.py`의 `Menu` Class의 `update_menu()` method 사용합니다.
- `DELETE`: `models.py`의 `Menu` Class의 `delete_menu()` method 사용합니다.



#### model.py 작성
```py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Menu class
class Menu(db.Model):
    # table name
    __tablename__ = 'menus'

    # 기본 속성들, id=기본 키
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    price = db.Column(db.Integer)


    # 전체 menu를 반환하는 함수 Menu.query.all()을 사용
    def get_menus():
        return [{"menu.id": menu.id, "menu.name": menu.name, "menu.price": menu.price} for menu in Menu.query.all()]


    # 전체 menu에 새로운 menu를 추가하는 함수 
    # app.py에서 Menu.add_menu()를 호출할 때 request.get_jason()을 이용하여 값을 넘겨줌 (n, p)
    def add_menu(n, p):
        i = db.session.query(db.func.count(Menu.id)).scalar() + 1
        menu = Menu(id=i, name=n, price=p)
        db.session.add(menu)
        db.session.commit()
        return {"id": i, "name": n, "price": p}


    # id에 해당하는 menu를 수정하는 함수
    # app.py에서 Menu.update_menu()를 호출할 때 request.get_jason()을 이용하여 값을 넘겨줌 (i, n, p)
    def update_menu(i, n, p):
        menu = db.session.query(Menu).filter(Menu.id == i).first()
        if menu is None:
            return "찾으시는 id의 메뉴가 없습니다."
        menu.name, menu.price = n, p
        db.session.commit()
        return {"id": i, "name": n, "price": p}


    # id에 해당하는 menu를 삭제하는 함수
    def delete_menu(i):
        menu = db.session.query(Menu).filter(Menu.id == i).first()
        if menu is None:
            return "찾으시는 id의 메뉴가 없습니다."
        del_menu = {"id": i, "name": menu.name, "price": menu.price}

        db.session.delete(menu)
        db.session.query(Menu).filter(Menu.id > i).update({'id': Menu.id - 1})
        db.session.commit()
        return {"삭제된 menu": del_menu}
```

- `def get_menus():` 
  - **전체 menu를 조회**하는 함수 `Menu.query.all()`을 사용합니다.

- `def add_menu(n, p):` 
  - 전체 menu에 **새로운 menu를 추가**하는 함수입니다.
  - `app.py`에서 `Menu.add_menu()`를 호출할 때 `request.get_jason()`을 이용하여 값`(n, p)`을 넘겨줍니다.

  - `i = db.session.query(db.func.count(Menu.id)).scalar() + 1`
    - `func.count()` 함수를 사용하여 테이블의 길이에 + 1의 값을 id로 합니다..
    - 메뉴를 추가할 때는 무조건 가장 뒤에 메뉴가 추가되는 것으로 가정했습니다.

- `def update_menu(i, n, p):` id에 해당하는 **menu를 수정**하는 함수
  - `app.py`에서 `Menu.update_menu()`를 호출할 때 `request.get_jason()`을 이용하여 값`(i, n, p)`을 넘겨줍니다.
  - `db.session.query(Menu).filter(Menu.id == i).first()`
    - 쿼리를 조회할 때 `filter()`로 `Menu.id`와 수정하려는 `i`가 같을 때를 찾습니다.
    - `if menu is None:`
      - 찾으려는 `id` 값이 없으므로 "찾으시는 id의 메뉴가 없습니다." 출력합니다.
    - 찾았으면 name과 price의 값을 수정하고 저장합니다.

- `def delete_menu(i):` id에 해당하는 **menu를 삭제**하는 함수입니다.
  - `id`를 찾는 logic은 update와 같습니다.
  - `.filter(Menu.id > i).update({'id': Menu.id - 1})`
    - 중간에서 삭제된 `id`의 인덱스를 조정하기 위해 `id`의 아래에 있는 row들의 id를 모두 조정합니다.

--- 

#### Database 연동에 참고한 사이트
- https://gmlwjd9405.github.io/2019/02/01/orm.html
- https://m.blog.naver.com/PostView.nhn?blogId=ljc8808&logNo=220461868128&proxyReferer=https:%2F%2Fwww.google.com%2F
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- https://docs.sqlalchemy.org/en/14/orm/tutorial.html
- https://docs.sqlalchemy.org/en/14/errors.html#error-gkpj
- https://velog.io/@poiuyy0420/%ED%8C%8C%EC%9D%B4%EC%8D%AC-Flask-DB-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0SQLAlchemy
- https://lowelllll.github.io/til/2019/04/19/TIL-flask-sqlalchemy-orm/
- https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-1/
- https://edykim.com/ko/post/getting-started-with-sqlalchemy-part-2/
- https://www.python2.net/questions-812654.htm
- https://ourcstory.tistory.com/230
- https://stackoverflow.com/questions/10822635/get-the-number-of-rows-in-table-using-sqlalchemy
- https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
- https://kibua20.tistory.com/69
- https://planbs.tistory.com/entry/query-%EA%B0%9D%EC%B2%B4%EA%B0%80-%EC%8B%A4%EC%A0%9C%EB%A1%9C-%EC%BF%BC%EB%A6%AC%EB%A5%BC-%EC%8B%A4%ED%96%89%ED%95%98%EB%8A%94-%EC%8B%9C%EA%B8%B0
- https://stackoverflow.com/questions/42059049/what-type-of-result-sqlalchemy-query-returns
- https://dgkim5360.tistory.com/entry/not-JSON-serializable-error-on-python-json