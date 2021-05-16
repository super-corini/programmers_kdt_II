# bicsubi_core API Docs

## resource 구성요소
    1. 이름(name : string)
    2. 수량(stock : int)

## API 요약 

Method | URI | Description
--- | --- | ---
 - | / | home directory 인삿말 반
GET | /whoami | github id를 반환
GET | echo?string="string" | 입력된 string 반환
GET | /weapons | 현재 존재하는 weapon db 반환
POST | /create_weapons | 새로운 weapon 을 추가
PUT | /update_weapons | 특정 weapon의 속성 변경
DELETE | / delete_weapons | 특정 weapon 을 삭제


