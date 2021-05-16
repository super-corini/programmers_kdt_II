# bicsubi_core API Docs

## resource 구성요소
    1. 이름(name : string)
    2. 수량(stock : int)

## API 요약 

Method | URI | Description
--- | --- | ---
 - | / | home directory 인삿말 반환
GET | /whoami | github id를 반환
GET | echo?string="string" | 입력된 string 반환
GET | /weapons | 현재 존재하는 weapon db 반환
POST | /weapons | 새로운 weapon 을 추가
PUT | /weapons | 특정 weapon의 속성 변경
DELETE | / weapons | 특정 weapon 을 삭제


## 상세

### home directory
http://127.0.0.1:5000/ 로 접속하면 
"Welcome! I'm Bicsubi." 를 출력합니다.

### whoami
http://127.0.0.1:5000/whoami 로 접속하면 
API 제작자의 github ID를 출력합니다.

### echo

http://127.0.0.1:5000/echo?string=<"입력문자열"> 으로 접속하면, 
{"value": "입력문자열"} 형태의 json이 출력됩니다.

### weapons

1. CREATE
   
   입력 변수 | 타입 | 필수 여부 | description|
   --- | --- | --- | --- |
   name | string | Y | weapon name
   stock | int | Y | stock of the weapon
   
   데이터를 입력하고, POST method로 요청시, 
   Weapons DB에 새로운 weapon이 등록되고, 
   "The addition has successfully completed."이 출력됩니다.
   

2. READ
   GET method로 요청시, 
   현재 DB에 있는 Weapons의 내역이 모두 출력됩니다.
   

3. UPDATE
   
   입력 변수 | 타입 | 필수 여부 | description|
   --- | --- | --- | --- |
   name | string | Y | weapon name
   stock | int | Y | stock of the weapon
 
   데이터를 입력하고, PUT method로 요청시, 
   Weapons DB에서 요청한 weapon의 기록이 새로운 입력으로 변경되고, 
  "The update has successfully completed."이 출력됩니다.

4. DELETE
   
   입력 변수 | 타입 | 필수 여부 | description|
   --- | --- | --- | --- |
   name | string | Y | weapon name
   stock | int | N | stock of the weapon

   데이터를 입력하고, DELETE method로 요청시, 
   Weapons DB에서 요청한 weapon의 기록이 삭제되고, 
  "The deletion has successfully completed."이 출력됩니다.