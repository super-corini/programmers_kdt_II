# bicsubi_core API 명세서

## 1. API 기본 정보

| 메서드                      | 요청 URL                                                     | 출력 포맷 |
| --------------------------- | ------------------------------------------------------------ | --------- |
| -                           | http://127.0.0.1:5000/                                       | string    |
| GET                         | http://127.0.0.1:5000/whoami                                 | json      |
| GET                         | http://127.0.0.1:5000/echo/string                            | json      |
| GET, POST,<br />PUT, DELETE | http://127.0.0.1:5000/weapons<br />http://127.0.0.1:5000/weapons/<weapone name> | json      |



## 2. route

가장 최초 실행시 보여지는 화면입니다.

- "I'm not a Sirii, I'm just bicsubi. This is Mission 1." 를 출력합니다.

  

## 3. whoami

링크로 접속하면 API 제작자의 github id가 표시됩니다.

- ```python
   return jsonify({'name': 'SeongwonTak' })
  ```

  

## 4. echo

링크로 접속하면 해당하는 json이 출력 됩니다.

다른 링크로 우회할 경우, "Not matched echo"가 출력됩니다.

- ```python
  if string == 'string':
      return jsonify({'value': 'String'})
  ```

  

## 5. weapons

### 5.1 Class  : Weapons

| Object Name | Type       | Primary Key 여부 | Example | Restriction |
| :---------- | ---------- | ---------------- | ------- | ----------- |
| name        | String(60) | O                | "gun"   |             |
| stock       | Integer    |                  | 35      | 자연수 범위 |



### 5.2 출력결과

#### 5.2.1 GET Method

GET Method 요청시, 현재 Weapons에 있는 DB내역을 모두 출력합니다.



#### 5.2.2 POST Method

POST Method 요청시, Weapons DB에 추가할 Weapons을 입력합니다.

| 요청변수명 | 타입   | 필수 여부 | 설명             |
| ---------- | ------ | --------- | ---------------- |
| name       | string | Y         | 무기에 대한 이름 |
| stock      | int    | Y         | 무기의 재고      |

POST Method를 성공적으로 수행시, json 형태로 현재 입력한 새로운 Weapon의 name과 stock이 출력됩니다.

##### Error Message

| No.  | Message                                              | 사유                                                         |
| ---- | ---------------------------------------------------- | ------------------------------------------------------------ |
| 01   | Error Code 01 : duplicated name exists in Weapons    | 이미 기존 DB에 입력된 무기 이름과 중복된 이름이 존재하는 경우 |
| 02   | Error Code 02 : Stock value must be positive integer | 재고 개수에 0이나 음수값, 혹은 자연수가 아닌 실수 값을 입력 시도하려는 경우 |



#### 5.2.3 PUT Method

PUT Method 요청시, 변경을 원하는 Weapon Name에 따라, http://127.0.0.1:5000/weapons/<weapone name> 을 통해 변경 요청을 합니다.

| 요청변수명 | 타입   | 필수 여부 | 설명                    |
| ---------- | ------ | --------- | ----------------------- |
| name       | string | Y         | 무기에 대한 변경할 이름 |
| stock      | int    | Y         | 무기의 변경할 재고      |

PUT Method를 성공적으로 수행시, json 형태로 현재 입력한 새로운 Weapon의 name과 stock이 출력됩니다.

##### Error Message

| No.  | Message                                              | 사유                                                         |
| ---- | ---------------------------------------------------- | ------------------------------------------------------------ |
| 01   | Error Code 01 : duplicated name exists in Weapons    | 이미 기존 DB에 입력된 무기 이름과 중복된 이름이 존재하는 경우 |
| 02   | Error Code 02 : Stock value must be positive integer | 재고 개수에 0이나 음수값, 혹은 자연수가 아닌 실수 값을 입력 시도하려는 경우 |



#### 5.2.4 DELETE Method

DELETE Method 요청시, 삭제를 원하는 Weapon Name에 따라, http://127.0.0.1:5000/weapons/<weapone name> 을 통해 삭제 요청을 합니다.

DELETE Method를 성공적으로 수행시, 삭제를 원하는 Weapon이 제거된 채로, 남은 DB내역을 확인할 수 있습니다.