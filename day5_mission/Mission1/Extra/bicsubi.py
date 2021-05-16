import json
from flask import request, jsonify
from flask_restx import Resource, Namespace

from weather import get_weather
from bus import get_bus_stop

Bicsubi = Namespace(
    name='',
    description= 'Bicsubi API'
    )

# Who Am I
@Bicsubi.route('/whoami')
class WhoAmI(Resource) : 
    def get(self) :
        ''' Github ID 출력'''
        return {'name' : 'nsms556'}

# echo String
@Bicsubi.route('/echo')
class Echo(Resource) :
    def get(self) :
        '''Query String 출력'''
        request_param = request.args.to_dict()

        return {'value' : request_param['string']}

# Weather
@Bicsubi.route('/weather')
class Weather(Resource) :
    def get(self) :
        '''위치 기반 현재 날씨 출력'''
        client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        
        weather_info = get_weather(client_ip)

        return jsonify(weather_info)

# Bus Stop
@Bicsubi.route('/bus')
class BusStop(Resource) :
    def get(self) :
        '''현재 위치에서 근접한 버스 정류장 출력'''
        client_ip = request.environ.get('HTTPS_X_REAL_IP', request.remote_addr)

        bus_stop_info = get_bus_stop(client_ip)

        return jsonify(bus_stop_info)