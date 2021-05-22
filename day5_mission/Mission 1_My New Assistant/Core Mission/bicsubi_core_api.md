# Bicsubi Core API Documentation


### `GET /whoami`

- 본인의 github id 반환
- example. `localhost:5000/whoami`
  ```
  {
	  "name": "dltnwls9623"
  }
  ```
   
<br>
  
### `GET /echo?string="string"`
- Query String: `string`
- `string`을 그대로 반환
- example. `localhost:5000/echo?string=hello!!!`
  ```
  {
	  "value": "hello!!!"
  }
  ```
   
<br>

## weapon management (CRUD)

### `POST /weapon`
- Create : 새로운 `weapon` 정보(`name`, `stock`)추가
- `JSON` 형태로 요청
- 추가한 `weapon`정보를 `JSON` 형태로 반환
- example. `localhost:5000/weapon`
	- request 
	   ```
	    {
		    "name": "K2",
		    "stock": 10
		}
	  ```
	- response
	   ```
	    {
		    "name": "K2",
		    "stock": 10
		}
	  ```
   
<br>

### `GET /weapon`
- Read: 현재 존재하는 `weapon`을 확인
- 존재하는 `weapon`의 리스트를 `JSON` 형태로 반환
- example. `localhost:5000/weapon`
	- response
	   ```
      {
		  "weapons": [
		  	{
				"name": "AK-47",
				"stock": 2
			},
			{
				"name": "TRG",
				"stock": 5
			},
			{
				"name": "FAMAS",
				"stock": 1
			}
		]
       }
       ```
   
<br>


### `PUT /weapon?name="weapon_name"`
- Update: 현재 존재하는 `weapon` 에서 특정 속성(이름, 수량)을 변경
-  수정 정보를 `JSON` 형태로 요청
- 수정한`weapon`정보를 `JSON` 형태로 반환
- example. `localhost:5000/weapon?name=AK-47`
	- request 
	   ```
	    {
		    "name": "AK-47",
		    "stock": 3
		}
	  ```
	- response
	   ```
	    {
		    "name": "AK-47",
		    "stock": 3
		}
	  ```
   
<br>

### `DELETE /weapon?name="weapon_name"`
-   Delete : 현재 존재하는 특정  `weapon`  을 삭제
- 삭제한 `weapon`의 리스트를 `JSON` 형태로 반환
- example. `localhost:5000/weapon?name=K2`
	- response
	   ```
	  {
		  "deleted weapon": [
			  {
				  "name": "K2",
				  "stock": 10
			  }
	       ]
	  }
	  ```
   
<br>


