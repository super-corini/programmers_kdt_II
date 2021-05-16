from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus

import xmltodict
import json

from ip2loc import ip_to_location


BUS_API_KEY = 'osC7MLox9zrATkUmZ3lyxZt0CAhh5j%2FuX3mWnUfKuf4QOOYLCZVXeSP0dLPNJTE7llNnFYvuPtEWGK0QqrawKg%3D%3D'
base_url = 'http://openapi.tago.go.kr/openapi/service/BusSttnInfoInqireService/getCrdntPrxmtSttnList'


def get_bus_stop(ip_addr) :
    lat = 35.5444
    lon = 129.2561

    #lat, lon = ip_to_location(ip_addr)

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : BUS_API_KEY, quote_plus('gpsLati') : str(lat), quote_plus('gpsLong') : str(lon) })

    query_url = base_url + queryParams

    response = urlopen(query_url).read().decode("utf-8")

    res_dict = xmltodict.parse(response)
    res_json = json.loads(json.dumps(res_dict))

    return res_json

