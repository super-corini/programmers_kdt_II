# Week4 Day5 _Mission 1. My New Assistant_

## Core Mission
---
### bicsubi_core_api

- 초기 재고 Stock
  ```python
  weapons = [
      {"id":1, "name":"Gun", "stock":20},
      {"id":2, "name":"Sword", "stock":45},
    ]
    ```
- 첫 페이지 (/)
  ```python
  # Main
  @app.route('/')
  def root_page():
      return "Week4-Day5 (Mission 1. My New Assistant) Core Mission"
  ```

- github id & name 반환 (/whoami)
  ```python
  # READ(GET) /whoami | 깃헙 ID와 이름을 가지고 온다.
  @app.route('/whoami', methods=['GET'])
  def get_github_id():
      my_name = {
          "id": "junyup2\n",
          "name": "JunYupLee"
      }
      return jsonify(my_name)
  ```
- Query String : string (echo)
  - string 을 반환
  ```python
  # CREATE(GET) /echo |
  # CREATE(GET) /echo |
@app.route('/echo', methods=['GET'])
def get_echo():
    args = request.args.get('string')
    echo = {
        "value": args
    }
    return jsonify(echo)
  ```
---
#### 다음의 요구사항에 맞게 API를 설계하고 작성

- 빅수비는 자원 weapon 을 가짐
- 이 weapon 은 이름(name : str)과 수량(stock : int)을 가짐
- 각각에 대해 Create, Read, Update, Delete 가능
  - Create : 새로운 weapon 을 추가
  - Read : 현재 존재하는 weapon 을 확인
  - Update : 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경
  - Delete : 현재 존재하는 특정 weapon 을 삭제
- 작성한 API에 대한 명세(API Docs)를 bicsubi_core_api.md 에 작성하여 제출합니다.
- 모든 API는 작성자가 설계한대로 원활하게 동작되어야합니다.      
---

- Read : 현재 존재하는 weapon 을 확인 (/weapon)
  ```python
  # READ(GET) /weapon | 자료를 가지고 온다.
  @app.route('/weapon')
  def get_weapons():
      return jsonify({"weapons" : weapons})
  ```  

- Create : 새로운 weapon 을 추가
  ```python
  # CREATE(POST) /weapon | 자료를 자원에 추가한다.
  @app.route('/weapon', methods=['POST'])
  def create_weapon():
      request_data = request.get_json() # {"name" : ..., "stock": ...}
      new_weapon = {
          "id" : len(weapons) + 1,
          "name" : request_data['name'],
          "stock" : request_data['stock'],
      }
      weapons.append(new_weapon)
      return jsonify(new_weapon)
  ```
- Update : 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경
  - 업데이트 하려는 id가 없는 경우 `error : 해당 id가 존재하지 않습니다.` 를 반환
  ```python
  # UPDATE
  @app.route('/weapon/<int:id>',methods=['PUT'])
  def update_weapons(id):
      request_data = request.get_json()
      try:
          weapons[id-1]['name'] = request_data['name']
          weapons[id-1]['stock'] = request_data['stock']
          return jsonify({"weapons" : weapons})
      except Exception as e:
          return  f'해당 id가 존재하지 않습니다.: {e}'
  ```
- Delete : 현재 존재하는 특정 weapon 을 삭제
  - 해당 id의 weapon을 삭제할시 비는 번호가 없게 삭제되는 뒷번호의 id를 정렬
  - 삭제하려는 id가 없는 경우 `error : 해당 id가 존재하지 않습니다.` 를 반환
  ```python
  # DELETE
  @app.route('/weapon/<int:id>',methods=['DELETE'])
  def delete_weapon(id):
      try:
          # id를 확인
          id_l = len(weapons)
          if id_l == id:
              del weapons[id-1]
          else:
              del weapons[id-1]
              for i in range(id_l-id):
                  weapons[id+i-1]['id'] = id+i
          return jsonify({"weapons" : weapons})
      except Exception as e:
          return  f'해당 id가 존재하지 않습니다.: {e}'
  ```
