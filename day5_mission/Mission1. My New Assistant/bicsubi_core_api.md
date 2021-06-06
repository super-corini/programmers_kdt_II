# Mission 1. My New Assistant

## GET /whoami
Root url에 '/whoami'를 추가하면 저의 github id를 JSON 형식으로 반환합니다.
* url 입력 방법
```
http://127.0.0.0:5000/whoami
```
* 리턴 값 예시 
```
{
    "name" : "yuseon27"
}
```

## GET /echo?string="string"
Root url에 '/echo' 뒤에 '?string="{원하는 문자열}"'를 입력하면 원하는 문자열을 JSON 형식으로 반환합니다.
* url 입력 예시
```
http://127.0.0.0:5000/echo?string="IwantPizza"
```
* 리턴 값 예시 
```
{
    "value" : "IwantPizza"
}
```

## Weapon CRUD
### Create
새로운 weapon을 추가할 수 있습니다. POST 방식으로 Request를 보내며, JSON 형식으로 값을 전달합니다. 
* url 입력
```
http://127.0.0.1:5000/weapons/create
```
* 요청 메세지 예시 형식
```
{
    "name"  : "weapon1",
    "stock" : 1000
}
```

### Read
GET 방식으로 Request를 보내며, 현존하는 weapon을 확인합니다. JSON 형식으로 리턴합니다.
* url 입력
```
http://127.0.0.1:5000/weapons
또는
http://127.0.0.1:5000/weapons/read
```

* 리턴 값 예시
```
{
    "weapons": [
        {
            "name": "weapon1",
            "stock": 1000
        },
        {
            "name": "weapon2",
            "stock": 20
        }
        {
            "name": "weapon3",
            "stock": 300
        }
    ]
}
```

### Update
기존의 weapon을 변경할 수 있습니다. PUT 방식으로 Request를 보내며, JSON 형식으로 값을 전달합니다. 
* url 입력
```
http://127.0.0.1:5000/weapons/update/weapon1
```
* 요청 메세지 예시 형식
```
{
    "stock" : 2000
}
```
* 결과
```
{
    "weapons": [
        {
            "name": "weapon1",
            "stock": 2000
        },
        {
            "name": "weapon2",
            "stock": 20
        },
        {
            "name": "weapon3",
            "stock": 300
        }
    ]
}
```

### Delete
기존의 weapon을 삭제할 수 있습니다. DELETE 방식으로 진행합니다.
* url 입력
```
http://127.0.0.1:5000/weapons/delete/weapon2
```
* 결과
```
{
    "weapons": [
        {
            "name": "weapon1",
            "stock": 2000
        },
        {
            "name": "weapon3",
            "stock": 300
        }
    ]
}
```