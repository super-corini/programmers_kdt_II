from urllib.request import urlopen
import json


geolocate_url = 'http://ip-api.com/json/{}?fields=country,regionName,lat,lon'

def ip_to_location(ip_addr) :
    query_url = geolocate_url.format(ip_addr)

    response = urlopen(query_url).read().decode("euc-kr")
    response = json.loads(response)

    client_lat = response['lat']
    client_lon = response['lon']

    return client_lat, client_lon
