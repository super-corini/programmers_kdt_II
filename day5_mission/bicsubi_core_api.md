# API Docs

| Method   | Usage |
| -------- | ----- |
| `GET`    | 조회  |
| `POST`   | 등록  |
| `PUT`    | 수정  |
| `DELETE` | 삭제  |

## GET

- `GET /whoami`

  - github id를 반환합니다.
  - Example:

  ```json
  {
    "name": "LeeSeongYeob"
  }
  ```

- `GET /echo?string="string"`

  - Query String : `string`
  - `string` 을 반환합니다.

  ```json
  {
    "value": "hello"
  }
  ```

- `GET /weapon`

  - 저장된 weapon의 정보를 가져옵니다.
  - `Json` 타입의 weapon을 반환합니다.

  ```json
  {
    "weapons": [
      {
        "name": "gun",
        "stock": 1
      }
    ]
  }
  ```

## POST

- `POST /weapon`

  - 새로운 `weapon` 을 추가
  - 성공시 새로운 `weapon` 정보 반환
  - Body 예시

  ```json
  {
    "name": "gun",
    "stock": 1
  }
  ```

## PUT

- `PUT /weapon/<string:name>`

  - 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경
  - `<string:name>` 을 인자로 값 변경
  - `weapons` 의 값 JSON 형식으로 반환
  - Body 예시

  ```json
  {
    "name": "Machine Gun",
    "stock": 10
  }
  ```

  - 반환 성공시

  ```json
  {
    "weapons": [
      {
        "name": "Machine Gun",
        "stock": 10
      }
    ]
  }
  ```

  - 반환 실패시
    - `<string:name>` 값이 존재하지 않는 경우

  ```json
  Not Found weapon
  ```

## DELETE

- `DELETE /weapon/<string:name>`

  - 현재 존재하는 특정 `weapon` 을 삭제
  - `<string:name>` 을 인자로 값 삭제
  - `weapons` 의 값 JSON 형식으로 반환
  - 삭제 성공시

  ```json
  {
    "weapons": [
      {
        "name": "Machine Gun",
        "stock": 10
      }
    ]
  }
  ```

  - 반환 실패시
    - `<string:name>` 값이 존재하지 않는 경우

  ```json
  Not Found weapon
  ```
