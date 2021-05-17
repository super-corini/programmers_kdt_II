# [Week4 - Day5] Bicsubi Extra API
  - pip install -r requirements.txt
  
## GET /weather
  - Do : IP 주소에 기반한 현재 위치의 날씨를 출력
  - return : weather_info
    - type : JSON
    - example
      ``` JSON
      {
        "coord": {
          "lon": 129.2561, 
          "lat": 35.5444
        }, 
        "weather": [
          {
            "id": 501, 
            "main": "Rain", 
            "description": "moderate rain", 
            "icon": "10d"
          }, 
          {
            "id": 701, 
            "main": "Mist", 
            "description": "mist", 
            "icon": "50d"
          }
        ], 
        "base": "stations", 
        "main": {
          "temp": 21.56, 
          "feels_like": 22.23, 
          "temp_min": 21, 
          "temp_max": 23, 
          "pressure": 1000, 
          "humidity": 94
        }, 
        "visibility": 4000, 
        "wind": {
          "speed": 3.09, 
          "deg": 160
        }, 
        "rain": {
          "1h": 0.15
        }, 
        "clouds": {
          "all": 90
        }, 
        "dt": 1621154510, 
        "sys": {
          "type": 1, 
          "id": 8086, 
          "country": "KR", 
          "sunrise": 1621109867, 
          "sunset": 1621160465
        }, 
        "timezone": 32400, 
        "id": 1833742, 
        "name": "Ulsan", 
        "cod": 200
      }
      ```

## GET /bus
  - Do : IP주소에 기반한 현재 위치에서 근접한 버스 정류장 출력
  - return : bus_stop_info
    - type : JSON
    - example
      ``` JSON
      {
        "response": {
          "header": {
            "resultCode": "99", 
            "resultMsg": "SERVICE KEY IS NOT REGISTERED ERROR."
          }
        }
      }
      ```