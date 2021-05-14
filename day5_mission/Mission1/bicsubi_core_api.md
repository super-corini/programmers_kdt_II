# API Docs

#### GET /whoami

- 아이디 반환



#### GET /echo/"string"

- string 반환



### Weapon API

#### POST /weapon/create

```json
{
    "name": "무기 이름",
    "stock": "수량"
}
```

입력 시 무기 리스트에 추가



#### GET /weapon/read

- 무기 리스트 반환



#### POST /weapon/update/"무기ID"

```json
{
    "name": "무기 이름",
    "stock": "수량"
}
```

입력 시 무기 정보 수정

#### 

#### POST /weapon/delete/"무기ID"

- 해당 아이디를 가진 무기를 무기 리스트에서 삭제