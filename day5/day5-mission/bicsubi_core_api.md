# bicsubi_core /API

# **Models**

- **Weapon**

    `id: Integer`

    `name: String`

    `stock: Integer`
---
# API

1. **GET** /whoami

    - **Description:**  
    제 github 아이디를 프린트합니다.
   


2. **GET** /echo

    - **Description:**  
    `var: string`을 받아 프린트합니다.

    - **Example:**  
    request >>>`GET /echo?string=test`  
    result >>>
    ```json
    {
        "value": "test"
    }
    ```

3. **GET** /weapon

    - **Description:**  
    존재하는 weapon 목록을 읽습니다.


4.  **POST** /weapon

- **Description:**  
  weapon를 추가합니다.

- **Example:**  
  request >>>`POST /weapon`  
  request body >>>

```json
{
    "name": "FN SCAR-H",
		"stock" : 125000
}
```
result >>>

```json
{
    "name": "FN SCAR-H",
		"stock" : 125000
}
```

5.  **PUT** /weapon\<int:id>

- **Description:**  
id에 해당하는 weapon의 정보를 업데이트합니다.

- **Example:**  
request >>>`POST /weapon3`  
request body >>>

```json
{
    "name": "FN SCAR-H",
		"stock" : 125000
}
```

result >>>

```json
{
		"id": 3,
    "name": "FN SCAR-H",
		"stock" : 125000
}
```

6.  **DELETE** /weapon

- **Description:**  
id에 해당하는 weapon의 레코드를 drop합니다. 그리고 빠진 레코드 뒤의 모든 레코드의 id를 하나씩 줄인다.

- **Description:**  
id에 해당하는 weapon의 레코드를 drop합니다. 그리고 빠진 레코드 뒤의 모든 레코드의 id를 하나씩 줄인다.

- **Example:**  
request >>>`POST /weapon1`  
result >>>

```json
[
	{
		"id": 1,
    "name": "AK-47",
		"stock" : 500000
	},
	{
		"id": 2,
    "name": "FN SCAR-H",
		"stock" : 125000
]
```