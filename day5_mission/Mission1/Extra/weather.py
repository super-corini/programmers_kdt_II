from urllib.request import urlopen
import json

from ip2loc import ip_to_location


openweather_API_KEY = '0e23eeaccd77ce455fc608099d967c62'
openweather_url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric'


def get_weather(ip_addr) :
    lat = 35.5444
    lon = 129.2561

    #lat, lon = ip_to_location(ip_addr)

    query_url = openweather_url.format(lat, lon, openweather_API_KEY)

    response = urlopen(query_url).read().decode("utf-8")
    response = json.loads(response)

    return response
