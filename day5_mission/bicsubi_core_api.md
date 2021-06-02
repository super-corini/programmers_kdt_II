- `GET /`
  - 간단한 자기소개르 합니다.
  - string으 형태로 반환합니다.
  ```josn
  I'm Bicsubi, What do yo want to do?
  ```
  
- `GET /whoami`

    - 나의 github id를 반환합니다.
    - Example:
    ```json
    {
        "name" : "super-corini"
    }
    ```


- `GET /echo?string="string"`
    - Query String : string
    - string 을 반환합니다.
    ```json
    {
        "value" : "string"
    }
    ```


- `GET /weapon`
    - 현재 존재하는 `weapon` 을 확인합니다. 
    ```json
    [
        {
            "name": "Shotgun",
            "stock": 10
        }
    ]
    ```


- `POST /weapon`
    - 새로운 `weapon` 을 추가합니다.
    - 추가하는 `weapon`의 정보는 body에 json의 형태로 담겨 전달됩니다.
    ```json
    {
        "name": "Muchinegun",
        "stock": 4
    }
    ```

    - 추가한 `weapon`을 반환합니다.
    ```json
    {
        "name": "Mushinegun",
        "stock": 4
    }
    ```

    - `Weapons.name`은 기본 키입니다. 그러므로 같은 `name`을 추가하려고 하면 키 제약에 의해 제약이 발생합니다.
    - 따라서 오류 메시지를 string의 형태로 반환합니다.
    ```json
    "중복된 이름이 있습니다. 다른무기를 추가해 주세요."
    ```
    
- `PUT /weapon`
    - 현재 존재하는 `weapon`에서 특정 속성(이름, 수량)을 변경합니다. 
    - 수정하는 `weapon`의 정보는 body에 json의 형태로 담겨 전달됩니다.
    - `Weapon.name`을 통해 삭제할 `weapon`을 정합니다.

    ```json
    {
        "name": "Shotgun",
        "stock": 20
    }
    ```
    
    - 성공시, 수정한 `weapon`을 반환합니다.
    ```json
    {
        "name": "Shotgun",
        "stock": 20
    }
    ```

    - 실패시, 오류 메시지를 string의 형태로 반환합니다.
    ```json
    "찾는 무기가 없습니다. 추가해 주시길 바랍니다."
    ``` 


- `DELETE /weapon`
    - 현재 존재하는 특정 `weapon` 을 삭제합니다. 
    ```json
    - 삭제하는 `weapon`의 정보는 body에 json의 형태로 담겨 전달됩니다.
    - `Weapons.name`을 통해 삭제할 `weapon`을 정합니다.

    ```json
    {
        "name": "Shotgun",
    }
    ```
    
    - 성공시, 삭제한 `weapon`으 이름고 수량을 반환합니다.
    ```json
    {
        "삭제된 Weapon": "Shotgun",
            "수량": 20
        }
    }
    ```

    - 실패시, 오류 메시지를 string의 형태로 반환합니다.
    ```json
    "찾는 무기가 없습니다."
    ``` 
