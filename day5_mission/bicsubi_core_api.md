# **Bicsubi_core_api**
----
Mission 1. My New Assistant

### main
  
* **URL**

  /

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `Hello, World!`

* **Error Response:**

  없음

----

* **URL**

  /whoami

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"name": "Bing-su"}`

* **Error Response:**

  없음
----

* **URL**

  /:string

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   string=[string]  
   단, string = "weapon"이면 아래 weapon으로 연결됨

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"value": "string"}`

* **Error Response:**

  없음

----
### Weapon
  
* **URL**

  /weapon

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   None

* **Data Params**

   None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `html 표로 된 데이터`

* **Error Response:**

  없음

----
  
* **URL**

  /weapon

* **Method:**

  `POST`

*  **URL Params**

   **Required:**

   None

* **Data Params**

   body = `JSON`<br />
   {
       "name": [string],
       "stock": [integer]
   }


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `html 표로 된 데이터`

* **Error Response:**

  * **Code:** 400 <br />
    **Content:** `잘못된 요청입니다: 'error message'`<br />
    형태가 JSON이 아니거나, name 또는 stock이 없을 경우

    또는
  * **Code:** 400 <br />
    **Content:** `같은 이름의 무기가 있습니다.`<br />
    name이 동일한 자료가 이미 있을 경우
----

* **URL**

  /weapon/:string

* **Method:**

  `PUT`

*  **URL Params**

   **Required:**

   string = [string]

* **Data Params**

   body = `JSON`<br />
   {
       "stock": [integer]
   }


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `html 표로 된 데이터`

* **Error Response:**

  * **Code:** 400 <br />
    **Content:** `잘못된 요청입니다: 'error message'`<br />
    형태가 JSON이 아니거나, stock이 없을 경우

    또는
  * **Code:** 400 <br />
    **Content:** `이름이 {string}인 데이터가 없습니다.`<br />
    name이 string인 자료가 없을 경우
----
* **URL**

  /weapon/:string

* **Method:**

  `DELETE`

*  **URL Params**

   **Required:**

   string = [string]

* **Data Params**

   None


* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{string} 데이터가 삭제되었습니다.`

* **Error Response:**

  * **Code:** 400 <br />
    **Content:** `이름이 {string}인 데이터가 없습니다.`<br />
    name이 string인 데이터가 없을 경우
