# Core Mission

- 빅수비는 자원 weapon 을 가집니다. 이 weapon 은 이름(name : str)과 수량(stock : int)을 가지며 각각에 대해 Create, Read, Update, Delete를 진행할 수 있습니다.
    1. Create : 새로운 weapon 을 추가
    2. Read : 현재 존재하는 weapon 을 확인
    3. Update : 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경
    4. Delete : 현재 존재하는 특정 weapon 을 삭제

## API Docs

1. `GET /weapon?name=str`: 현재 존재하는 weapon 을 확인 (Read)
    - out: `{"name" : "str", "stock" : int}` : 파라미터가 있으면 해당요소만 출력
    - out: `{"weapons": [{"name" : "str", "stock" : int}, ...]}` : 파라미터가 없으면 전체 출력

2. `POST /weapon`: 새로운 weapon을 추가 (Create)
    - inp: `{"name" : "str", "stock" : int}`
    - out: `{"name" : "str", "stock" : int}`

3. `PUT /weapon?name=str&stock=int&new_name=str`: 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경 (Update)
    - out: `{"name" : "str", "stock" : int}`

4. `DELETE /weapon?name=str`: 현재 존재하는 특정 weapon 을 삭제 (Delete)
    - out: `{"weapons": [{"name" : "str", "stock" : int}, ...]}` : 전체 weapon 출력