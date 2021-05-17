# bicsubi_extra /API

# API

1. **GET** /weather

    **Description:**  
    현재 접속중인 ip의 위치를 기반으로 한 날씨를 프린트합니다.
    ip는 [http://ipinfo.io](http://ipinfo.io)에서, 
    날씨는 
    
    [Weather API](http://api.openweathermap.org)
    
    에서 가져옵니다. 스타일은 적용하지 않았습니다.

2. **GET** /busstop

    **Description:**  
    카카오맵에 "버스정류장" 이라고 검색한 결과 페이지로 리다이렉트 합니다. 카카오맵에서 접속한 사용자의 WIFI 및 IP 기반으로 한 정확한 위치정보를 토대로 근거리의 버스 정류장을 검색해 줍니다.