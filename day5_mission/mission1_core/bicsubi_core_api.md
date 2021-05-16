### Bicsubi API Docs

- 구현한 api는 ec2-3-34-44-222.ap-northeast-2.compute.amazonaws.com:5000/에서 

- `GET /`
    - 간단한 자기 소개를 합니다.
    - string의 형태로 반환합니다.
    ```json
    hello flask:)
    my name is MinHyeok Lee!
    I will stand tall!
    ```

- `GET /whoami`

    - 여러분의 github id를 반환합니다.
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
            "name": "Knife",
            "stock": 2302
        },
        {
            "name": "javis",
            "stock": 1
        },
        {
            "name": "javisu",
            "stock": 12
        }
    ]
    ```


- `POST /weapon`
    - 새로운 `weapon` 을 추가합니다.
    - 추가하는 `weapon`의 정보는 body에 json의 형태로 담겨 전달됩니다.
    ```json
    {
        "name": "fist",
        "stock": 2
    }
    ```

    - 추가한 `weapon`을 반환합니다.
    ```json
    {
        "name": "fist",
        "stock": 2
    }
    ```

    - `weapon.name`은 기본 키입니다. 그러므로 같은 `name`을 추가하려고 하면 키 제약에 의해 오류가 납니다.
    - 따라서 오류 메시지를 string의 형태로 반환합니다.
    ```json
    "중복된 이름이 있습니다. 값을 수정하려면 update를 이용해주세요."
    ```
    
    - `DB table`의 허용량을 100개의 row로 한정했습니다.
    - 따라서, DB의 length가 100이 넘는다면 데이터를 추가하지 못하게 오류메시지를 string의 형태로 반환합니다.
    ```json
    "데이터베이스의 허용량을 초과했습니다. 데이터를 삭제해주세요."
    ```
    
- `PUT /weapon`
    - 현재 존재하는 `weapon`에서 특정 속성(이름, 수량)을 변경합니다. 
    - 수정하는 `weapon`의 정보는 body에 json의 형태로 담겨 전달됩니다.
    - `weapon.name`을 통해 삭제할 `weapon`을 정합니다.

    ```json
    {
        "name": "Gun",
        "stock": 2
    }
    ```
    
    - 성공시, 수정한 `weapon`을 반환합니다.
    ```json
    {
        "name": "Gun",
        "stock": 2
    }
    ```

    - 실패시, 오류 메시지를 string의 형태로 반환합니다.
    ```json
    "찾으시는 name의 무기가 없습니다."
    ``` 


- `DELETE /weapon`
    - 현재 존재하는 특정 `weapon` 을 삭제합니다. 
    ```json
    - 삭제하는 `weapon`의 정보는 body에 json의 형태로 담겨 전달됩니다.
    - `weapon.name`을 통해 삭제할 `weapon`을 정합니다.

    ```json
    {
        "name": "Gun",
    }
    ```
    
    - 성공시, 삭제한 `weapon`을 반환합니다.
    ```json
    {
        "삭제된 Weapon": {
            "name": "Gun",
            "stock": 1233
        }
    }
    ```

    - 실패시, 오류 메시지를 string의 형태로 반환합니다.
    ```json
    "찾으시는 name의 무기가 없습니다."
    ``` 