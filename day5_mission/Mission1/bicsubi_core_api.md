# Bicsubi-Core-API
  - pip install -r requirements.txt
  
## GET /whoami
  - Do : Github ID 출력
  - return : Github ID
    - type : JSON
    - example
      ``` JSON
      {
          "name" : "nsms556"
      }
      ```

## GET /echo?string="string"
  - Do : 에코
  - Query String
    - "string" : 문자열 
  - return : "string"
    - type : JSON
    - example
      ``` JSON
      {
          "value" : "string"
      }
      ```


## POST /weapons
  - Do : weapons DB에 무기 이름과 수량을 추가
  - Request Body
    - type : JSON
    - example
      ``` JSON
      {
          "name" : "Pulse Gun"
          "stock" : 2
      }
      ```
  - return : new_weapon
    - type : JSON
    - example
      ``` JSON
      {
          "name" : "Pulse Gun",
          "stock" : 2
      }
      ```

## GET /weapons
  - Do : 현재 DB에 있는 무기를 모두 조회
  - return : weapons
    - type : JSON
    - example
      ``` JSON
      {
          "weapons" :
          [
              {
                  "id" : 0,
                  "name" : "Pulse Gun",
                  "stock" : 2 
              },
              {
                  "id" : 1,
                  "name" : "Shield",
                  "stock" : 1
              },
              {
                  "id" : 2, 
                  "name" : "Hammer",
                  "stock" : 1
              }
          ]
      }
      ```

## GET /weapons/\<int:id>
  - Do : 해당 \<id>를 가진 무기 조회
  - URI Input
    - \<int:id> : 무기 ID 번호
    - example : GET /weapon/1
  - return : weapon
    - type : JSON
    - example
      ``` JSON
      {
          "id" : 1,
          "name" : "Shield",
          "stock" : 1
      }
      ```

## PUT /weapons/\<int:id>
  - Do : 해당 \<id>의 무기를 수정
  - URI Input
    - \<int:id> : 무기 ID 번호
    - example : PUT /weapon/0
  - Request Body
    - type : JSON
    - example 
      ``` JSON
      {
          "name" : "Pulse Gun + Beam"
          "stock" : 4
      }
      ```
  - return : update_weapon
    - type : JSON
    - example
      ``` JSON
      {
          "id" : 0
          "name" : "Pulse Gun + Beam"
          "stock" : 4
      }
      ```

## DELETE /weapons/\<int:id>
  - Do : 해당 \<id>의 무기를 삭제
  - URI Input
    - \<int:id> : 무기 ID 번호
  - return : GET /weapons
