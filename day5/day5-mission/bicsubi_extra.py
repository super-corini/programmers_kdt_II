import os
import time
import requests
from flask import Flask, jsonify, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'bicsubi_extra'

@app.route('/weather')
def get_weather():
    my_location = requests.get('http://ipinfo.io').json()   # country, city, region
    weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                params={'q':'Seoul', 'appid':'fe86ee103eda94f53ca121a256337587'}).json()

    country = my_location['country']
    region = my_location['region']
    city = my_location['city']

    coord = weather_data['coord']
    dt = weather_data['dt']
    weathers = weather_data['weather']

    rain = weather_data.get('rain')
    snow = weather_data.get('snow')
    cloud = weather_data.get('clouds')
    wind = weather_data['wind']

    zeroKelvin = -273.15
    temp = weather_data['main'].get('temp') + zeroKelvin
    temp_feels_lick = weather_data['main'].get('feels_like') + zeroKelvin
    temp_max = weather_data['main'].get('temp_max') + zeroKelvin
    temp_min = weather_data['main'].get('temp_min') + zeroKelvin

    pressure = weather_data['main'].get('pressure')
    hum = weather_data['main'].get('humidity')
    vis = weather_data.get('visibility')

    sunrise = weather_data['sys'].get('sunrise')
    sunset = weather_data['sys'].get('sunset')

    try:
        weather_info_text = f"""
        현재 위치는 {country}, {region}, {city} 입니다. (위도: {coord['lat']}, 경도: {coord['lon']})\n
        현재 시각:{time.ctime(dt)}, {city}시의 날씨는 {' 이며 '.join([w['description'] for w in weathers])} 입니다.\n
        -----------------\n
        날씨 : {', '.join([w['main'] for w in weathers])}\n
        온도 : {round(temp, 2)}({round(temp_min,2)}/{round(temp_max,2)})\n
        체감온도 : {round(temp_feels_lick,2)}\n"""

        if cloud:
            weather_info_text += f"구름양 : {cloud['all']}%\n"
        if rain:
            weather_info_text += f"시간당 강수량: {rain['1h']}mm\n"
        if snow is not None:
            weather_info_text += f"시간당 적설량: {snow['1h']}mm\n"

        weather_info_text += f"""
        바람 : {wind['speed']}m/s, {'→↗↑↖←↙↓↘'[int((wind['deg']+22.5)//45)%8]}\n
        습도 : {hum}%\n
        기압 : {pressure}hPa\n
        일출 : {time.ctime(sunrise)}\n
        일몰 : {time.ctime(sunset)}\n
        가시거리 : {vis}m\n
        """
    except Exception as e:
        print(e)
        raise e

    return weather_info_text.replace('\n', '<br/>')

@app.route('/busstop')
def redirect_busstop():
    return redirect("https://map.kakao.com/?q=%EB%B2%84%EC%8A%A4%EC%A0%95%EB%A5%98%EC%9E%A5&service=opensearch")

if __name__ == '__main__':
    app.run(debug=True)
