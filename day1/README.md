# Day 1 - Flask를 Flask 답게

실습에서는 `GET` 과 `POST` 를 이용해서 `/menu` 자원으로부터 데이터를 가지고오고, 자원에 데이터를 추가해보았습니다. 이는 자원에서 할 수 있는 4가지 logic인 CRUD(Create, Read, Update, Delete) 중 Create와 Read에 해당하는 부분입니다. 이를 바탕으로 다음 과제를 해결해봅시다.

### 필수 과제 : 메뉴 관리 CRUD 구현하기

- HTTP 메서드 `PUT` 를 이용해 Update, `DELETE` 를 이용해 Delete 기능을 구현해주세요.
- `PUT /menu/<int:id>` : 해당하는 id에 해당하는 데이터를 갱신합니다. (HTTPRequest으로 Body가 주어집니다.)
- `DELETE /menu/<int:id>` : 해당하는 id에 해당하는 데이터를 삭제합니다.
- `@app.route()` 의 인자로 들어가는 경로에는 다음과 같이 사용해줄 수도 있습니다.

```python
@app.route('/<name>') # URL에 <>를 붙임으로서 이를 함수의 인자로 대입할 수 있습니다.
def my_view_func(name):
    return name
```
#### TIL

- `import jsonify`: python dictionary type을 json이라는 java script에서 사용하는 data 저장방식으로 바꿔주기 위해 사용하는 모듈

- `import request`: HTTP request를 다룰 수 있는 모듈


- `GET`: 자료를 가지고 올 때 사용

  - `@app.route('/menus')`
    - `menus`의 자원에 접근하고, `GET` 메소드(default값)를 사용할 때 라우팅

    - `def get_menus():` 자원(메뉴)을 얻어오는 함수
    - `jsonify({"menus": menus})`: Python의 List type은 jsonify를 이용하여 변환할 수 없기 때문에 list를 dictionary type에 담아서 jsonify 메소드로 json type으로 변환하여 반환

- `POST`: 자료를 자원에 추가할 때 사용

  - `@app.route('/menus', method=['POST'])`
    - `menus` 자원에 접근하고, `POST` 메소드를 사용할 때 라우팅
    - `def create_menu():` 자원(메뉴)을 추가하는 함수
    - `request_data = request.get_json()`  
    : `request`모듈을 사용하여 사용자가 입력한 정보를 `get_jason()` 함수로 parsing하여 dictionary type으로 변환하여 `request_data`에 담는다.
      - 사용자가 입력한 정보는 JSON이라고 가정
      - {"name": ..., "price": ....}의 형태

### 보너스 과제 I: ID야 움직여라 얍!

- 새로운 menu를 추가하는 `POST` 영역에서 id가 4로 고정되어있는 문제가 발생합니다.
- POST 요청이 들어올 때마다 id가 하나씩 증가하여 `menu` 리스트에 추가될 수 있도록 코드를 수정해주세요.
- 이 과제는 필수 과제 이후에 진행되어야 합니다.

### 보너스 과제 II : 데이터베이스 연동하기

- 수업에서 다룬 API는 서버를 재시작하면 모든 정보가 리셋되는 치명적인 문제가 있었습니다. 이를 해결하기 위해 데이터만을 저장하는 **데이터베이스**를 도입하여 Flask과 연동할 필요가 생겼습니다.
- SQL과 ORM 중 하나를 선택하여 데이터베이스와 Flask app을 연동해봅시다. (즉, 자원에 CRUD가 발생하면 이 정보가 데이터베이스에 저장되어야합니다.)
- 이 과제는 필수 과제, 보너스 과제 I 이후에 진행되어야 합니다.