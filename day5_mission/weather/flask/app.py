
# Mission 1. Extra Mission
'''
-제출할 파일 :bicsubi_extra_api.md ,API 구축에 사용되는 파일들
-다음의 명세서에 맞게 API를 설계하고 작성합니다
    현재 위치의 위도와 경도 값을 이용해 현재 위치의 날씨 (온도, 바람세기 등)을 알 수 있는 API - 끝
    현재 위치의 위도와 경도 값을 이용해 현재 위치에서 가장 가까운 버스정류장의 도착정보를 알수 있는 API
-Swagger를 이용해 API Docs를 만듭니다.
-작성한 API에 대한 명세(API Docs)를 bicsubi_extra_api.md에 작성하여 제출합니다.
-모든 API 작성자가 설계한대로 원활하게 동작 되어야 합ㄴ다
-이 과제는 필수 과제 이후에 진행되어야합니다
'''

#날씨 api
#api.openweathermap.org/data/2.5/weather?lat={위도}&lon={경도}&appid={키}


from flask import Flask, render_template, Response, url_for, request, redirect
from urllib.request import urlopen
import json

app =Flask(__name__)

@app.route('/')
def home():
    lat = 37.45 # 세로 위도
    lon = 127.21 # 가로 경도
    url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b6861e4d083404510399e50ac2f9f268".format(lat,lon)
    respondata = urlopen(url).read().decode('utf-8')
    jsonArray = json.loads(respondata)
    pick=jsonArray.get("main")
    pick2=jsonArray.get("wind")
    return render_template('index.html',lat_h=lat,lon_h=lon,temp_h=round(pick['temp']- 273.15,2),wind_h=pick2['speed'])

@app.route('/map', methods=["GET"])
def map():
    lat = request.args.get('lat_pt')
    lon = request.args.get('lon_pt')
    url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=b6861e4d083404510399e50ac2f9f268".format(lat,lon)
    respondata = urlopen(url).read().decode('utf-8')
    jsonArray = json.loads(respondata)
    pick=jsonArray.get("main")
    pick2=jsonArray.get("wind")
    print(pick['temp'])
    print(pick2['speed'])
    return render_template('index.html',lat_h=lat,lon_h=lon,temp_h=round(pick['temp']- 273.15,2),wind_h=pick2['speed'])


if __name__ == "__main__":
    app.run(debug=True)
