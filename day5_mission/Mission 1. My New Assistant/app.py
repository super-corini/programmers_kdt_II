import os, requests
from models import db
from flask import Flask, jsonify, request, render_template
from geopy.geocoders import Nominatim
from pprint import pprint
from urllib.request import urlopen, Request
import urllib
import bs4

app = Flask(__name__)

weapons = [
    {"name" : "Steel", "stock" : 30},
    {"name" : "Gold", "stock" : 50},
    {"name" : "Aluminum", "stock" : 10},
]

# READ
@app.route('/weapons')
def get_weapons():
    return jsonify(weapons)

# CREATE
@app.route('/weapons', methods=['POST'])
def create_weapon():
    request_data = request.get_json()
    new_weapon = {
        "name" : request_data['name'],
        "stock" : request_data['stock'],
    }
    weapons.append(new_weapon)
    return jsonify(weapons)

# Update
@app.route('/weapons/<string:name>', methods=['PUT'])
def update_weapon(name):
    update_data = request.get_json()
    for weapon in weapons:
        if weapon['name'] == name:
            weapon['name'] = update_data['name']
            weapon['stock'] = update_data['stock']
            break
    return jsonify(weapon)

# DELETE
@app.route('/weapons/<string:name>', methods=['DELETE'])
def delete_weapon(name):
    for weapon in weapons:
        if weapon['name'] == name:
            weapons.remove(weapon)
            break
    return jsonify(weapon)

# GET 1
@app.route('/whoami', methods=['GET'])
def get_name():
    my_name = [
        {"name" : "ulillilu"},
    ]
    return jsonify(my_name)

# GET 2
@app.route('/<string:string>', methods=['GET'])
def get_string(string):
    my_value = [
        {"value" : string},
    ]
    return jsonify(my_value)

# BONUS : 지역명을 입력하면 날씨 반환
@app.route('/weather/<string:string>', methods=['GET'])
def get_weather(string):
    location = string
    enc_location = urllib.parse.quote(location + '+날씨')
    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')
    return jsonify([string + '의 현재 날씨는 ' + soup.select('div.main_info > div > ul > li:nth-child(1) > p')[0].text])

basdir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basdir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run()