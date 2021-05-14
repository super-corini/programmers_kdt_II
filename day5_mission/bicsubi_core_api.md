# bicsubi_core_api

## GET /weapon

현재 존재하는 모든 weapon 을 반환합니다.

```json
{
    "name": "k2",
    "stock": 100
}
```

## GET /weapon?name="k2"

Query String: `name`

`k2`에 해당하는 weapon을 반환합니다.

```json
{
    "name": "k2",
    "stock": 100
}
```

## POST /weapon?name="k2"&stock=100

Query String: `name`, `stock`

새로운 weapon 을 추가합니다.

## PUT /weapon/{seq}?name="k5"

Query String: `name`

현재 `weapon`의 `name` 속성을 변경합니다.

## PUT /weapon/{seq}?stock="200"

Query String: `stock`

현재 `weapon`의 `stock` 속성을 변경합니다.

## DEL /weapon/{seq}

현재 `weapon`의 정보를 삭제합니다.
