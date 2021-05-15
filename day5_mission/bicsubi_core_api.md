# 빅수비 API 명세
- 자신의 github id 반환
- Query String 반환
### `GET /whoami`  
github id를 반환합니다
```
{
    "name": "spongebob03"
}
```
### `GET /echo?string="string"`  
- Query String: `string`
- string을 반환합니다
```
{
   "value" : "string"
}
```
### Create
`POST /weapon`
- 새로운 `weapon` 추가
- input
```
{
    "name": "arrow",
    "stock": 50
}
```
- output: `weapon` 목록 출력
```
{
    "weapons": [
        {
            "stock": 50,
            "weapon": "arrow"
        }
    ]
}
```
### Read
`GET /weapon`
- `weapon` 목록 출력
### Update
`PUT /weapon/<string:name>`
- name이 `name`인 weapon의 이름과 수량 수정
- input
```
{
    "name": "wand",
    "stock": 3
}
```
- output
```
{
    "weapons": [
        {
            "stock": 3,
            "weapon": "wand"
        }
    ]
}
```
### Delete
`DELETE /weapon/<string:name>`
- name이 `name`인 weapon을 삭제