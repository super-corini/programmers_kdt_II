from flask_restx import Namespace, Resource, fields

api = Namespace('whoami', description='Do you know who am I?')

whoami = api.model('WhoAmI', {
    'name': fields.String()
})


@api.route('')
class WhoAmI(Resource):
    @api.marshal_with(whoami)
    def get(self):
        """Display who I am"""
        return {'name': 'YummyCocopalm'}