- `GET /weapons`

  - Read : 현재 존재하는 `weapon` 을 확인

    ```json
    {
      "weapons" : {
        [
        {"id":id, "name":name, "stock":stock},
        ...
        ]
      }
    }
    ```

- `POST /weapons`

  - Create : 새로운 `weapon` 을 추가

    ```json
    {
      "id" : id,
      "name" : name,
      "stock" : stock
    }
    ```

- `PUT /weapons/<string:name>` 

  - Update : 현재 존재하는 `weapon`에서 특정 속성(이름, 수량)을 변경

    ```json
    {
      "weapons" : {
        [
        {"id":id, "name":name, "stock":stock},
        ...
        ]
      }
    }
    ```

- `DELETE /weapons/<string:name>`

  - Delete : 현재 존재하는 특정 `weapon` 을 삭제

    ```json
    {
      "weapons" : {
        [
        {"id":id, "name":name, "stock":stock},
        ...
        ]
      }
    }
    ```

    