from flask import jsonify, request
from flask_restx import Resource, Namespace, reqparse


Bicsubi = Namespace(name='')


@Bicsubi.route('/whoami')
class BicsubiWhoami(Resource):
    def get(self):
        return jsonify({"name": "lymchgmk"})


@Bicsubi.route('/echo')
@Bicsubi.doc(params={'string': 'Echo할 query string'})
class BicsubiEcho(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('string', required=True, type=str)
        arg = parser.parse_args()
        query_string = arg['string']
        return jsonify({"value": query_string})
