from flask_restx import Namespace, Resource, reqparse, abort
from .db_core import BicsubiDb
from sqlite3 import Error, IntegrityError

api = Namespace('core', description='Core Methods', path='/')
db = BicsubiDb()


@api.route('/whoami')
class JsonWhoami(Resource):
    @api.doc('get github account name')
    def get(self):
        return db.get_info('github')


parser_echo = reqparse.RequestParser()
parser_echo.add_argument('string', type=str,
                         required=True, help="String to be echoed.")


@api.route('/echo')
class EchoString(Resource):
    @api.doc('get')
    @api.expect(parser_echo)
    def get(self):
        args = parser_echo.parse_args(strict=True)
        return {"value": args['string']}


weapon_create_parser = reqparse.RequestParser()
weapon_create_parser.add_argument('name', type=str, required=True, help="Name of the weapon.")
weapon_create_parser.add_argument('stock', type=int, required=False, help="Amount of weapon available.")

weapon_update_parser = reqparse.RequestParser()
weapon_update_parser.add_argument('name', type=str, required=True, help="Name of the weapon.")
weapon_update_parser.add_argument('stock', type=int, required=False, help="Amount of weapon available.")
weapon_update_parser.add_argument('new_name', type=str, required=False, help="New name of weapon.")

weapon_delete_parser = reqparse.RequestParser()
weapon_delete_parser.add_argument('name', type=str, required=True, help="Name of the weapon.")

ok = {'status': 'ok'}

@api.route('/weapon')
@api.response(200, description="Successful.")
@api.response(400, description="Bad request or malformed data.")
@api.response(500, description="Server error.")
class WeaponInventory(Resource):
    @api.doc('post')
    @api.expect(weapon_create_parser)
    def post(self):
        ret = ok
        args = weapon_create_parser.parse_args(strict=True)
        weapon_name = args['name']
        weapon_stock = 0 if not args['stock'] else args['stock']
        if weapon_stock < 0:
            return abort(400, "Stock cannot be less than 0.")
        try:
            db.weapon_create(weapon_name, weapon_stock)
        except IntegrityError as e:
            ret = abort(400, "Weapon name already exists.")
        except Error as e:
            ret = abort(500)
        return ret

    @api.doc('get')
    def get(self):
        try:
            ret = db.weapon_list_weapons()
        except Error:
            ret = abort(500)
        return ret

    @api.doc('put')
    @api.expect(weapon_update_parser)
    def put(self):
        args = weapon_update_parser.parse_args(strict=True)
        name, stock, new_name = args['name'], args['stock'], args['new_name']
        if not stock and not new_name:
            return abort(400, "At least 1 element has to be changed")
        if stock and stock < 0:
            return abort(400, "Stock cannot be less than 0,")
        try:
            res = db.weapon_update(name=name, stock=stock, new_name=new_name)
            if not res:
                ret = abort(400, "Weapon not found.")
            else:
                ret = ok
        except IntegrityError:
            ret = abort(400, "Weapon name must be unique.")
        except Error:
            ret = abort(500)
        return ret

    @api.doc('delete')
    @api.expect(weapon_delete_parser)
    def delete(self):
        args = weapon_delete_parser.parse_args(strict=True)
        try:
            res = db.weapon_delete(args['name'])
            if not res:
                ret = abort(400, "Weapon doesn't exists.")
            else:
                ret = ok
        except Error:
            ret = abort(500)
        return ret
