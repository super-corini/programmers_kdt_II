# Bicsubi Core API

* `GET /whoami`
    * GitHub ID를 `string`으로 반환합니다.
        ```
        {
            "name": "devmei"
        }
        ```

* `GET echo?string="string"`
    * 전달받은 `string`을 반환합니다.
        ```
        {
            "value": "string"
        }
        ```

## Bicsubi `weapon` CRUD

* `weapon`
    ```
    weapon {
        name	string
        stock	integer
    }
    ```

* `GET /weapon`
    * 현재 존재하는 `weapon`을 확인한다.
        ```
        # OUTPUT
        {
            "weapon": [
                {
                    "name": "weapon01",
                    "stock": 100
                },
                {
                    "name": "weapon02",
                    "stock": 500
                },
                {
                    "name": "weapon03",
                    "stock": 300
                }
            ]
        }
        ```

* `POST /weapon`
    * 새로운 `weapon`을 추가한다.
    * `JSON` 형식으로 아래와 같이 데이터를 전달해야 한다.
        ```
        # INPUT
        {
            "name": "weaponTEST",
            "stock": 50
        }
        # OUTPUT
        {
            "name": "weaponTEST",
            "stock": 50
        }
        ```

* `PUT /weapon/<string:name>`
    * 현재 존재하는 `weapon`에서 특정 속성(`name`, `stock`)을 변경한다.
    * `name` 값으로 검색하기 때문에 중복되는 `name`의 사용은 지양해야 하며, `name` 또는 `stock` 하나만 변경할 수 있다.
        ```
        # URL : http://127.0.0.1:5000/weapon/weaponTEST
        # INPUT
        {
            "name": "weapon77",
            "stock": 777
        }
        # OUTPUT
        {
            "name": "weapon77",
            "stock": 777
        }
        ```

* `DELETE /weapon/<string:name>`
    * 현재 존재하는 특정 `weapon`을 `name`으로 검색하여 삭제한다.
        ```
        # URL : http://127.0.0.1:5000/weapon/weapon77
        # OUTPUT
        {
            "weapon": [
                {
                    "name": "weapon01",
                    "stock": 100
                },
                {
                    "name": "weapon02",
                    "stock": 500
                },
                {
                    "name": "weapon03",
                    "stock": 300
                }
            ]
        }
        ```
