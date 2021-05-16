
## Mission 1. My New Assistant


서울에 사는 호주니는 영화 <브론즈 맨>을 보고 감동을 받았다. 특히 브론즈 맨 슈트를 장착했을 때 나오는 어시스턴트 빅수비의 성능에 금치 못했다. 이를 통해 우리의 매일매일의 생활을 윤택하게 만들어 줄 나만의 빅수비를 만들어보면 좋겠다는 생각을 했다. 호주니를 도와 한국형 자비스, 빅수비를 만들어보자.

### Core Mission
제출할 파일 : bicsubi_core_api.md , API 구축에 사용되는 파일들  

다음의 명세에 맞게 API를 작성합니다.  

GET /whoami  

여러분의 github id를 반환합니다.  

Example:  
{  
    "name" : "super-corini"  
}  

GET /echo?string="string"    

Query String : string  
string 을 반환합니다.   
{  
   "value" : "string"  
}  
다음의 요구사항에 맞게 API를 설계하고 작성합니다.  

빅수비는 자원 weapon 을 가집니다. 이 weapon 은 이름(name : str)과 수량(stock : int)을 가지며 각각에 대해 Create, Read, Update, Delete를 진행할 수 있습니다. 

Create : 새로운 weapon 을 추가  
Read : 현재 존재하는 weapon 을 확인  
Update : 현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경  
Delete : 현재 존재하는 특정 weapon 을 삭제  

작성한 API에 대한 명세(API Docs)를 bicsubi_core_api.md 에 작성하여 제출합니다.

모든 API는 작성자가 설계한대로 원활하게 동작되어야합니다.  

### Extra Mission
제출할 파일 : bicsubi_extra_api.md , API 구축에 사용되는 파일들

다음의 명세서에 맞게 API를 설계하고 작성합니다.  
현재 위치의 위도와 경도 값을 이용해 현재 위치의 날씨(온도, 바람세기 등)을 알 수 있는 API  
현재 위치의 위도와 경도 값을 이용해 현재 위치에서 가장 가까운 버스 정류장의 도착정보를 알 수 있는 API  
이외에 빅수비에 추가하고 싶은 API가 있다면 추가하셔도 좋습니다.  
Swagger를 이용해 API docs를 만듭니다.  
작성한 API에 대한 명세(API Docs)를 bicsubi_extra_api.md 에 작성하여 제출합니다.  
모든 API는 작성자가 설계한대로 원활하게 동작되어야합니다.  
이 과제는 필수 과제 이후에 진행되어야합니다.  
💡 API의 목적을 파악하고, 이를 바탕으로 어떻게 REST하게 작성할 수 있을지 고민해봅시다.  

💡 Swagger를 활용하면 더욱 편리하게 API를 관리할 수 있습니다.  
[swagger](https://swagger.io/)  
