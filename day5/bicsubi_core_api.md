### GET  http://127.0.0.1:5000/
  
  - bicsubi(String type) 반환
  
### GET /whoami
  
  - github id 반환
  
  - 실행결과
    /whoami
    {
      "name" : "mioow"
    }
    
### GET /echo?string={string}
   
   - 전달받은 <"string">반환
   
   - 입력예시
    `/echo?string=meow`
   
   - 실행결과
   {
       "value" : "meow"
   }
    
### GET /weapons

   - weapons의 정보를 반환
   
   - 실행결과
   /weapons
   [
       {
           "id": 1,
           "name": "meow_punch",
           "stock": 2
       }
   ]
   
### POST /weapons

  - 새로운 무기를 추가
  - JSON request
  - request_data
    1. name(string)
    2. stock(int)
  
  - 입력 예시
    {
        "name": "chooru",
        "stock": 100
    }
    
  - 실행 결과
    [
        {
            "id": 1,
            "name": "meow_punch",
            "stock": 2
        },
        {
            "id": 2,
            "name": "chooru",
            "stock": 100
        }
    ]
    
### PUT /weapons/{id}

  - weapons의 해당id(int)를 가진 데이터를 업데이트
  - request_data
    1. name(string)
    2. stock(int)
    
    - 입력 예시
    /weapons/2
    {
        "name": "chooru",
        "stock": 150
    }
    
    - 실행 결과
    [
        {
            "id": 1,
            "name": "meow_punch",
            "stock": 2
        },
        {
            "id": 2,
            "name": "chooru",
            "stock": 150
        }
    ]
    
### DELETE /weapons{id}

  - weapons의 해당id(int)를 가진 데이터를 삭제
  - 해당 id의 데이터를 삭제해도 다음 데이터의 아이디가 해당 id로 변경되진 않음
  
  - 입력 예시
    /weapons/2
    
  - 실행 결과
    [
        {
            "id": 1,
            "name": "meow_punch",
            "stock": 2
        }
    ]