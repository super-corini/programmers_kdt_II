# **Bicsubi core API 명세서**

------

## 1. main

| 메서드 | URL      | 출력 형태 |
| ------ | -------- | --------- |
| GET    | /        | string    |
| GET    | /whoami  | json      |
| GET    | /:string | json      |

### **1.1  /**

- **Method**

  `GET`

- **URL params**

  없음

- **Data Params**

  없음

- **Success Response:**

  - **Code: 200**

    **Contents**: `Hello, World`

- **Error Response:**

  없음

### **1.2  /whoami**

- **Method**

  `GET`

- **URL params**

  없음

- **Data Params**

  없음

- **Success Response:**

  - **Code: 200**

    **Contents**: json, `{"name": "Bing-su"}`

- **Error Response:**

  없음

### **1.3 /:string**

- **Method**

  `GET`

- **URL params**

  - **필수**

    string = [string]

    단, string = "weapon"이면 다음에 올 weapon으로 연결됨

- **Data Params**

  없음

- **Success Response:**

  - **Code: 200**

    **Contents**: json, `{"value": string}`

- **Error Response:**

  없음

------

## 2. weapon

| 메서드 | URL             | URL params | Data params | 출력 형태       |
| ------ | --------------- | ---------- | ----------- | --------------- |
| GET    | /weapon         | -          | -           | html 표         |
| POST   | /weapon         | -          | json        | html 표, 문자열 |
| PUT    | /weapon/:string | string     | json        | html 표, 문자열 |
| DELETE | /weapon/:string | string     | -           | 문자열          |

### **2.1  /weapon**

- **Method**

  `GET`

- **URL params**

  없음

- **Data Params**

  없음

- **Success Response:**

  - **Code: 200**

    **Contents**: html로 된 표

    | id      | name   | stock   |
    | ------- | ------ | ------- |
    | integer | string | integer |

- **Error Response:**

  없음

### **2.2 /weapon**

- **Method**

  `POST`

- **URL params**

  없음

- **Data Params**

  - **필수**

    body : json

    ```
    {
    	"name": [string],
    	"stock": [integer]
    }
    ```

- **Success Response:**

  - **Code: 200**

    **Contents**: html로 된 표

    | id      | name   | stock   |
    | ------- | ------ | ------- |
    | integer | string | integer |

- **Error Response:**

  | Code | Contents                             | 설명                                                         |
  | ---- | ------------------------------------ | ------------------------------------------------------------ |
  | 400  | `잘못된 요청입니다: 'error message'` | 형태가 json이 아니거나, <br/>name 또는 stock이 없거나, <br/>형식이 맞지 않을 경우 |
  | 400  | `같은 이름의 무기가 있습니다.`       | name이 동일한 자료가 이미 있을 경우                          |

### **2.3 /weapon/:string**

- **Method**

  `PUT`

- **URL params**

  - **필수**

    string = [string]

- **Data Params**

  - **필수**

    body : json

    ```
    {
    	"stock": [integer]
    }
    ```

- **Success Response:**

  - **Code: 200**

    **Contents**: html로 된 표

    | id      | name   | stock   |
    | ------- | ------ | ------- |
    | integer | string | integer |

- **Error Response:**

  | Code | Contents                               | 설명                                                         |
  | ---- | -------------------------------------- | ------------------------------------------------------------ |
  | 400  | `잘못된 요청입니다: 'error message'`   | 형태가 json이 아니거나, <br/>stock이 없거나, <br/>형식이 맞지 않을 경우 |
  | 400  | `이름이 {string}인 데이터가 없습니다.` | name이 string인 자료가 없을 경우                             |

- 

  - **Code: 400**

    **Contents**: `잘못된 요청입니다: 'error message'`

    형태가 json이 아니거나, stock이 없거나, 형식이 맞지 않을 경우

  - **Code: 400**

    **Contents**: `이름이 {string}인 데이터가 없습니다.`

    name이 string인 자료가 없을 경우

### **2.4 /weapon/:string**

- **Method**

  `DELETE`

- **URL params**

  - **필수**

    string = [string]

- **Data Params**

  없음

- **Success Response:**

  - **Code: 200**

    **Contents**: `{string} 데이터가 삭제되었습니다.`

- **Error Response:**

  | Code | Contents                               | 설명                               |
  | ---- | -------------------------------------- | ---------------------------------- |
  | 400  | `이름이 {string}인 데이터가 없습니다.` | name이 string인 데이터가 없을 경우 |