# API Docs for Bicsubi

## GET /whoami
`http://127.0.0.1:5000/whoami`
Github ID를 반환합니다.

```
# curl
curl --location --request GET 'http://127.0.0.1:5000/whoami'

# output
{
    "name": "dhelee"
}
```

## GET /echo
`http://127.0.0.1:5000/echo?string=hello`

전달된 string을 반환합니다.

```
# curl
curl --location --request GET 'http://127.0.0.1:5000/echo?string=hello'

# output
{
    "value": "hello"
}
```

## POST /weapons
`http://127.0.0.1:5000/weapons`

새로운 weapon을 추가합니다.
{'name': 'weapon 이름', 'stock': 'weapon 수량'} 형태로 데이터를 전달해야 합니다.

```
# raw(json)
{
    "name": "Sword",
    "stock": 2
}

# curl
{
    "name": "Sword",
    "stock": 2
}

# output
{
    "id": 2,
    "name": "Sword",
    "stock": 2
}

```


## GET /weapons
`http://127.0.0.1:5000/weapons`

현재 존재하는 weapon을 확인합니다.

```
# curl
curl --location --request GET 'http://127.0.0.1:5000/weapons'

# output
{
    "weapons": [
        {
            "id": 1,
            "name": "Gun",
            "stock": 2
        },
        {
            "id": 2,
            "name": "Sword",
            "stock": 2
        }
    ]
}
```

## PUT  /weapons
`http://127.0.0.1:5000/weapons/1`

현재 존재하는 weapon 중 특정 속성(이름, 수량)을 변경합니다.
변경하려는 weapon의 id를 url에 입력하고 {'name': 'weapon 이름', 'stock': 'weapon 수량'} 형태로 데이터를 전달해야 합니다.

```
# raw
{
    "name": "Super Gun",
    "stock": 5
}

# curl
curl --location --request PUT 'http://127.0.0.1:5000/weapons/1' \
--data-raw '{
    "name": "Super Gun",
    "stock": 5
}'

# output
{
    "weapons": [
        {
            "id": 1,
            "name": "Super Gun",
            "stock": 5
        }
    ]
}
```

## DEL /weapons
`http://127.0.0.1:5000/weapons/2`

현재 존재하는 특정 weapon을 삭제합니다.
삭제하려는 weapon의 id를 url에 입력합니다.

```
# curl
curl --location --request DELETE 'http://127.0.0.1:5000/weapons/2'

# output
{
    "weapons": [
        {
            "id": 1,
            "name": "Super Gun",
            "stock": 5
        }
    ]
}
```