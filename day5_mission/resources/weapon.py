## RESOURCES

from flask import request
from flask_restplus import Resource, fields, Namespace

# from models.item import ItemModel
# from schemas.item import ItemSchema
from models.weapon import WeaponModel
from schemas.weapon import WeaponSchema
from db import db

WEAPON_NOT_FOUND = "Weapon not found."


weapon_ns = Namespace('weapon', description='Weapon related operations')
weapons_ns = Namespace('weapons', description='Weapons related operations')
whoami_ns =  Namespace('whoami', description='Who am I?')
echo_ns =  Namespace('echo', description='echo')

weapon_schema = WeaponSchema()
# weapon_list_schema = WeaponSchema(many=True)
weapon_list_schema = WeaponSchema(many=True)

#Model required by flask_restplus for expect
weapon = weapons_ns.model('Weapon', {
    'name': fields.String('Name of the Weapon'),
    # 'price': fields.Float(0.00),
    'stock': fields.Integer
})

class Whoami(Resource):
    def get(self):
        return {"name":"marquis08"}

class Echo(Resource):
    # def get(self):
    #     data = request.get_json()
    #     return {"value":data}
    def get(self):
        string = request.args.get('string')
        return {"value":string}

# This is Weapon
class Weapon(Resource):

    def get(self, name):
        # weapon_data = WeaponModel.find_by_id(id)
        weapon_data = WeaponModel.find_by_name(name)
        if weapon_data:
            return weapon_schema.dump(weapon_data)
        return {'message': WEAPON_NOT_FOUND}, 404

    def delete(self,name):
        # weapon_data = WeaponModel.find_by_id(id)
        weapon_data = WeaponModel.find_by_name(name)
        if weapon_data:
            weapon_data.delete_from_db()
            return {'message': "Weapon Deleted successfully"}, 200
        return {'message': WEAPON_NOT_FOUND}, 404

    @weapon_ns.expect(weapon)
    def put(self, name):
        # weapon_data = WeaponModel.find_by_id(id)
        weapon_data = WeaponModel.find_by_name(name)
        weapon_json = request.get_json();

        if weapon_data:
            weapon_data.stock = weapon_json['stock']
            weapon_data.name = weapon_json['name']
        else:
            weapon_data = weapon_schema.load(weapon_json, session=db.session)

        weapon_data.save_to_db()
        return weapon_schema.dump(weapon_data), 200

## This is Weapons
class WeaponList(Resource):
    @weapons_ns.doc('Get all the Weapons')
    def get(self):
        return weapon_list_schema.dump(WeaponModel.find_all()), 200

    @weapons_ns.expect(weapon)
    @weapons_ns.doc('Create an Weapon')
    def post(self):
        weapon_json = request.get_json()
        weapon_data = weapon_schema.load(weapon_json, session=db.session)
        weapon_data.save_to_db()

        return weapon_schema.dump(weapon_data), 201