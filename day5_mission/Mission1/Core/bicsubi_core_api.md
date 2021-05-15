
## Whoami
API 제작자의 Github username을 Return

__URL__  

    /whoami  
__Method__  
    
    GET  
- __Success Response:__  
    - __Code__ 200  
    - __Content__(Json) {"name" : "JJ-HH"}
---
## Echo
Query String을 받은 후 내용을 Json으로 Return

__URL__  
    
    /echo?query_1=string_1&query_2=string_2&...  
__Method__  
    
    GET

- __Success Response:__  
    - __Code__ 200  
    - __Content__(Json) {"query_1": "string_1", "query_2": "string_2", ...}
---
## Weapon CREATE and READ
- __GET:__  
weapons.db의 weapons 테이블을 읽어온 후 Json으로 Return
- __POST:__  
입력 받은 Json Data Param으로 Weapon CREATE > DB commit > Json으로 Weapon Return

__URL__

    /weapons/<int:id>
__Method__

    GET | POST
__Data Params__  

    POST
    name=<string>
    stock=<integer>

__Success Response:__  
- __GET__
    - __Code__ 200  
    - __Content__(Json) {"Weapons": db.weapons}

- __POST__
    - __Code__ 200  
    - __Content__(Json) model.weapon{id:int, name:str, stock:int}

- __Error Response:__
    - Not yet specified
---
## Weapon UPDATE and DELETE
- __PUT:__   
id로 weapons 테이블 쿼리 > Weapon UPDATE(Json Data Param) > DB commit > Return Weapon
- __DELETE:__  
id로 weapons 테이블 쿼리 > Weapon DELETE > DB commit > Json으로 weapons 테이블 Return

__URL__

    /weapons
__Method__

    PUT | DELETE
__Data Params__  

    PUT
    name=<string>
    stock=<integer>

__Success Response:__  
- __GET__
    - __Code__ 200  
    - __Content__(Json) model.weapon{id:int, name:str, stock:int}

- __POST__
    - __Code__ 200  
    - __Content__(Json) {"Weapons": db.weapons}

- __Error Response:__
    - Not yet specified
---