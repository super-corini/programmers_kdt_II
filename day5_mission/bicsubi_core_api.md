# API Docs

## Github ID

- `GET /whoami`

### Response

```
{
"name" : "taehyun-learn"
}
```

## Query String

- `GET /echo?string=string`

### Response

```
{
    "value" : string
}
```

## Create weapon

- `POST /weapon?name=name`

- 해당 name의 weapon이 db에 존재하는 경우 해당 weapon의 stock 하나 추가
- 존재하지 않는 경우 stock을 1로 새로 추가

## Read weapon

- `GET /weapon`

### Response

- 전체 weapons db 조회

```
{
    weapons:[
        {
            id:int,
            name:string,
            stock:int
        },...
    ]
}
```

## Update Weapon

- `PUT /weapon/id?name=string&stock=int`

- 변경한 name이 db에 존재하는 경우 해당 db에 변경된 stock 추가
- 그렇지 않은 경우 입력된 정보로 수정

## Delete weapon

- `DELETE /weapon/id`

- 해당 id의 데이터 삭제
