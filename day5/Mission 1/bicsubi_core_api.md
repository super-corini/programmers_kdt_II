## Bicsubi CORE API Docs

### Bicsubi Basic API

### `` GET / whoami`` 

- 본인의 github id를 반환합니다.

- result:

  ![1](./image/1.png)

  

### ``GET / echo?string="string"``

- Query String : String

- string을 반환합니다

- result :

  ![2](./image/2.png)

### Bicsubi Weapon API(CRUD)

### ``GET / weapon``

- READ: 현재 데이터베이스에 존재하는 모든 **weapon**을 확인

- url = http://127.0.0.1:5000/weapon

- result 

  ![3](./image/3.png)

### ``POST / weapon``

- CREATE : 새로운 **weapon**의 정보 (name, stock)를 데이터베이스에 추가

- url : http://127.0.0.1:5000/weapon

- body에 포함시켜야 하는 데이터 : name, stock

- result

  ![4](./image/4.png)

### ``PUT / weapon``

- UPDATE : 데이터베이스에 존재하는 **weapon**에서 정보(name, stock)를 수정

- url : http://127.0.0.1:5000/weapon

- body에 포함 시켜야 하는 데이터 : name, modify_name, stock

- result 

  ![5](./image/5.png)

### ``DELETE / weapon``

- DELETE : 데이터베이스에 존재하는 **weapon** 데이터를 삭제
- url : http://127.0.0.1:5000/weapon
- body에 포함시켜야 하는 데이터 : name, stock

- result

  ![6](./image/6.png)

  

