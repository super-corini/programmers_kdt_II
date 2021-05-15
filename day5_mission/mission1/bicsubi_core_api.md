# Bicsubi core API Docs

## `GET` /
: DB 초기화

## `GET` /whoami
### Request
> None  
### Respon
- 나의 github ID
```JSON
{
    "name": "hook0318"
}
```
## `GET` /echo?string="string"  
### Request
> Query string(URL)
### Respon
```JSON
{
    "value": "string"
}
```
## `GET` /weapon
: 무기 리스트를 보여줍니다.
### Request
> None  
### Respon
- DB에 있는 모든 무기의 리스트(이름, 수량)
```JSON
[
    {
        "name": "Gonbong",
        "stock" : 12
    }
]


```
## `POST` /weapon
: 무기 데이터를 추가합니다. 
### Request
> HTTPRequest의 Body에 갱신할 내용이 json으로 전달됩니다.
```JSON
{
    "name": "Gun",
    "stock" : 5
}
```
### Respon
- DB에 있는 모든 무기의 리스트(이름, 수량)
- JSON 형식
```JSON
[
    {
        "name": "Gonbong",
        "stock" : 12
    },
    {
        "name": "Gun",
        "stock" : 5
    }
]
```

## `PUT` /weapon/<string:name>
: name에 해당하는 무기 속성를 갱신합니다. 
### Request
> 무기 이름(name),  
HTTPRequest의 Body에 갱신할 내용이 json으로 전달됩니다.
```JSON
{
    "name": "Gonbong",
    "stock" : 8
}
```
### Respon
- DB에 있는 모든 무기의 리스트(이름, 수량)
```JSON
[
    {
        "name": "Gonbong",
        "stock" : 8
    },
    {
        "name": "Gun",
        "stock" : 5
    }
]
```

## `DELETE` /weapon/<string:name>
: name에 해당하는 무기 정보를 삭제합니다. 
### Request
> 무기 이름(name)
### Respon
- DB에 있는 모든 무기의 리스트(이름, 수량)
```JSON
[
    {
        "name": "Gonbong",
        "stock" : 8
    }
]
```


