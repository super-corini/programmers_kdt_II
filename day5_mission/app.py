from flask import Flask, jsonify, request
#from urllib3 import Request, urlopen
#from urllib import urlencode, quote_plus
from urllib.request import urlopen, Request
from urllib.parse import urlencode, unquote, quote_plus
import xmltodict
import json

# Use in Extra Mission
url_forecast = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
url_bus = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos'
url_busstop = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid'

app = Flask(__name__)

weapons = []

@app.route('/whoami')
def whoami_flask():
    return jsonify({"name":"Druwa-git"})

@app.route('/echo')
def string_flask():
    return jsonify({"value": request.args.get("string", "empty_string")})

@app.route('/weapon')
def get_weapon():
    return jsonify({"weapons": weapons})

@app.route('/weapon', methods=['POST'])
def post_weapon():
    request_data = request.get_json()
    id = 1 if len(weapons) == 0 else weapons[-1]["id"]+1
    weapon = dict(id=id, name=request_data["name"], stock=request_data["stock"])
    weapons.append(weapon)
    return jsonify({"weapon": weapon})

@app.route('/weapon/<int:id>', methods=['PUT'])
def update_weapon(id):
    request_data = request.get_json()
    for weapon in weapons:
        if weapon["id"] == id:
            break
    weapon["name"] = request_data["name"]
    weapon["stock"] = request_data["stock"]
    return jsonify({"weapon": weapon})

@app.route('/weapon/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    for weapon in weapons:
        if weapon["id"] == id:
            weapons.remove(weapon)
            return "Success"
    else:
        return "Fail"

# Extra Mission
import math

#한국 공공데이터 좌표계 변환
def grid(v1, v2) :

    RE = 6371.00877 # 지구 반경(km)
    GRID = 5.0      # 격자 간격(km)
    SLAT1 = 30.0    # 투영 위도1(degree)
    SLAT2 = 60.0    # 투영 위도2(degree)
    OLON = 126.0    # 기준점 경도(degree)
    OLAT = 38.0     # 기준점 위도(degree)
    XO = 43         # 기준점 X좌표(GRID)
    YO = 136        # 기1준점 Y좌표(GRID)

    DEGRAD = math.pi / 180.0
    RADDEG = 180.0 / math.pi

    re = RE / GRID;
    slat1 = SLAT1 * DEGRAD
    slat2 = SLAT2 * DEGRAD
    olon = OLON * DEGRAD
    olat = OLAT * DEGRAD

    sn = math.tan(math.pi * 0.25 + slat2 * 0.5) / math.tan(math.pi * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(math.pi * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(math.pi * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn);
    rs = {};

    ra = math.tan(math.pi * 0.25 + float(v1) * DEGRAD * 0.5)
    ra = re * sf / math.pow(ra, sn)

    theta = float(v2) * DEGRAD - olon
    if theta > math.pi :
        theta -= 2.0 * math.pi
    if theta < -math.pi :
        theta += 2.0 * math.pi
    theta *= sn
    rs['x'] = math.floor(ra * math.sin(theta) + XO + 0.5)
    rs['y'] = math.floor(ro - ra * math.cos(theta) + YO + 0.5)

    return rs

@app.route('/weather')
def weather_info():
    base_date = "20210516"
    base_time = "0500"
    latitude = request.args.get("latitude")
    longtitude = request.args.get("longtitude")
    rs = grid(latitude, longtitude)
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): 'GAOmTl%2Fz%2Br81Ybctz7tbHfSrtja1gjSQxTdZy2z7A%2B9duDGcvIzAouW3ThDH0eXfFfEg%2FMsLyu54gV%2FB0ZzDQw%3D%3D',
         quote_plus('pageNo'): '1', quote_plus('numOfRows'): '10',
         quote_plus('dataType'): 'XML', quote_plus('base_date'): base_date, quote_plus('base_time'): base_time,
         quote_plus('nx'): rs['x'], quote_plus('ny'): rs['y']})
    request_val = Request(url_forecast + unquote(queryParams))
    #request_val.get_method = lambda: 'GET'
    response_body = urlopen(request_val).read()
    decode_data = response_body.decode('utf-8')
    xml_parse = xmltodict.parse(decode_data)
    xml_dict = json.loads(json.dumps(xml_parse))
    first_item = xml_dict["response"]["body"]["items"]["item"][0]
    category = first_item["category"]
    # category 마다 value를 해석하는 값이 달라서 나중에 추가할 예정
    if category == "POP":
        forcast_value = first_item["fcstValue"]
        weather_name = "Rain(Value:%)"
    return jsonify({"weather": weather_name, "weather_value": forcast_value})

@app.route('/busstop')
def busstop_info():
    # 실수함 : x, y 반대로 값 집어넣음 (위 좌표와 반대로 넣어야 됌.. 삽질)
    latitude = float(request.args.get("latitude"))
    longtitude = float(request.args.get("longtitude"))
    radius = float(request.args.get("radius")) # 0~2000
    # 가까운 정류장 알아내기
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): 'GAOmTl%2Fz%2Br81Ybctz7tbHfSrtja1gjSQxTdZy2z7A%2B9duDGcvIzAouW3ThDH0eXfFfEg%2FMsLyu54gV%2FB0ZzDQw%3D%3D',
         quote_plus('tmX'): longtitude, quote_plus('tmY'): latitude, quote_plus('radius'): radius})
    request_val = Request(url_bus + unquote(queryParams))
    # request_val.get_method = lambda: 'GET'
    response_body = urlopen(request_val).read()
    decode_data = response_body.decode('utf-8')
    xml_parse = xmltodict.parse(decode_data)
    xml_dict = json.loads(json.dumps(xml_parse))
    first_item = xml_dict["ServiceResult"]["msgBody"]["itemList"][0]
    station_id = first_item["arsId"]

    # 도착정보 알아내기
    queryParams = '?' + urlencode({quote_plus('ServiceKey'): 'GAOmTl%2Fz%2Br81Ybctz7tbHfSrtja1gjSQxTdZy2z7A%2B9duDGcvIzAouW3ThDH0eXfFfEg%2FMsLyu54gV%2FB0ZzDQw%3D%3D',
                                   quote_plus('arsId'): station_id})
    request_val = Request(url_busstop + unquote(queryParams))
    response_body = urlopen(request_val).read()
    decode_data = response_body.decode('utf-8')
    xml_parse = xmltodict.parse(decode_data)
    xml_dict = json.loads(json.dumps(xml_parse))
    first_item = xml_dict["ServiceResult"]["msgBody"]["itemList"][0]
    arrived_info = first_item["arrmsg1"]
    return jsonify({"arrived_info": arrived_info})

if __name__ == '__main__':
    app.run()