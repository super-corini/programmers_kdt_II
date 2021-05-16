#bicsubi_core_api.md
빅수비는 자원 weapon 을 가집니다.    
이 weapon 은 이름(name : str)과 수량(stock : int)을 가지며  
각각에 대해 Create, Read, Update, Delete를 진행할 수 있습니다.  
  
##GET /whoami
설명: 여러분의 github id를 반환합니다.  
GET http://127.0.0.1:5000/whoami
  
##GET /echo?string="string" 
설명: Query String : string. string 을 반환합니다.  
GET http://127.0.0.1:5000/echo?string="<~string>"
결과: { "string": <~string> }
참고: wings2pc.tistory.com/entry/웹-앱프로그래밍-파이썬-플라스크Python-Flask-Request-get-parameterHTTP-method-GET-POST
  
  
##Create : 새로운 weapon 을 추가  
설명: <weapon_name>에 추가하고 싶은 weapon 이름을 작성하고,  
Body에 { "name": "weapon_name", "stock": num_of_weapon} 작성  
POST http://127.0.0.1:5000/weapon/<weapon_name>
결과: 추가한 새 weapon이 나옵니다.

##Read : 현재 존재하는 weapon 을 확인  
GET http://127.0.0.1:5000/weapon
결과: 존재하는 weapon들이 나옵니다
  
##Update : 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경  
설명: <weapon_name>에 수정하고 싶은 weapon 이름을 작성하고,  
Body에 { "name": "weapon_name", "stock": num_of_weapon} 작성  
PUT http://127.0.0.1:5000/weapon/weaponD
결과: 변경한 결과를 반영한 weapon들이 나옵니다  
  
##Delete : 현재 존재하는 특정 weapon 을 삭제  
설명: <weapon_name>에 삭제하고 싶은 weapon 이름을 작성하고,  
Body에 { "name": "weapon_name", "stock": num_of_weapon} 작성  
DELETE http://127.0.0.1:5000/weapon/weaponD
결과: 삭제 결과를 반영한 결과가 나옵니다  
