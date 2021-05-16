from flask_restx import Namespace, Resource, reqparse
import requests
from .db_core import BicsubiDb

api = Namespace('extended', description='Extended Methods', path='/')
db = BicsubiDb()

parser_location = reqparse.RequestParser()
parser_location.add_argument('lat', type=str, required=True, help="Latitude of the position of interest.")
parser_location.add_argument('lon', type=str, required=True, help="Longitude of the position of interest.")


@api.route('/weather')
class WeatherInfo(Resource):
    @api.doc('get weather info from openweathermap')
    @api.expect(parser_location)
    def get(self):
        key = db.get_info('weather')
        base = 'https://api.openweathermap.org/data/2.5/onecall'
        args = parser_location.parse_args(strict=True)
        r_params = {'appid': key,
                    'units': 'metric',
                    'lat': args['lat'],
                    'lon': args['lon']}
        res = requests.get(base, params=r_params)
        return res.json()


@api.route('/bus-stop')
class BusStopInfo(Resource):
    @api.doc('get bus stop info from google api')
    @api.expect(parser_location)
    def get(self):
        key = db.get_info('google_places')
        base = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        args = parser_location.parse_args(strict=True)
        r_params = {'location': f"{args['lat']},{args['lon']}",
                    'sensor': 'true',
                    'key': key,
                    'rankby': 'distance',
                    'types': 'bus_station'}
        res = requests.get(base, params=r_params)
        return res.json()


@api.route('/elon')
class ElonMuskLatestTweet(Resource):
    def get(self):
        k = db.get_info('twitter_key')
        ks = db.get_info('twitter_keys')
        session = requests.Session()
        session.auth = (k, ks)
        r_params = {'grant_type': 'client_credentials'}
        res = session.post('https://api.twitter.com/oauth2/token', params=r_params)
        bearer = res.json()['access_token']
        r_params = {'screen_name': 'elonmusk',
                    'count': 1}
        r_headers = {'Authorization': "Bearer " + bearer}
        res = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json',
                           params=r_params, headers=r_headers)
        return res.json()


parser_cocktail = reqparse.RequestParser()
parser_cocktail.add_argument('cocktail', type=str, required=True,
                             help="Name of cocktail")


@api.route('/cocktail')
class CocktailRecipe(Resource):
    @api.doc('search recipe by name')
    @api.expect(parser_cocktail)
    def get(self):
        base = 'https://www.thecocktaildb.com/api/json/v1/1/search.php'
        args = parser_cocktail.parse_args(strict=True)
        res = requests.get(base, params={'s': args['cocktail']})
        return res.json()


@api.route('/fox')
class Fox(Resource):
    @api.doc('get random fox image')
    def get(self):
        return requests.get('https://randomfox.ca/floof/').json()
