from flask import request
from flask_restx import Namespace, Resource, fields

api = Namespace('echo', description='Test query string')

echo = api.model('Echo', {
    'string': fields.String()
})


@api.route('')
class Echo(Resource):
    @api.doc(params={'string': 'any string'})
    @api.marshal_with(echo)
    def get(self):
        """Display what I wrote"""
        request_str = request.args.get('string', type=str)
        return {'string': request_str}