from flask import request, jsonify
from flask_restx import Resource, Namespace, fields, reqparse


weapons_dict = {}
weapons_count = 1


Weapon = Namespace(name='Weapon')

weapon_fields = Weapon.model(
    'Weapon',
    {
        'name': fields.String(required=True),
        'stock': fields.Integer(required=True)
    }
)

weapon_fields_with_id = Weapon.inherit(
    'Weapon With ID', weapon_fields,
    {
        'weapon_id': fields.Integer(required=True)
    }
)


@Weapon.route('')
class WeaponCreate(Resource):
    @Weapon.expect(weapon_fields)
    @Weapon.response(201, 'Success', weapon_fields_with_id)
    def post(self):
        global weapons_dict, weapons_count
        
        idx = weapons_count
        weapons_dict[idx] = {
            'name': request.json.get('name'),
            'stock': request.json.get('stock')
        }
        weapons_count += 1
        
        return jsonify({
            'weapon_id': idx,
            'weapon_data': weapons_dict[idx]
        })


@Weapon.route('/<int:weapon_id>')
@Weapon.doc(params={'weapon_id': 'An ID'})
class WeaponRUD(Resource):
    @Weapon.response(200, 'Success', weapon_fields_with_id)
    @Weapon.response(500, 'Failed')
    def get(self, weapon_id):
        try:
            return jsonify({
                'weapon_id': weapon_id,
                'weapon_data': weapons_dict[weapon_id]
            })
        except KeyError:
            return f'존재하지 않는 weapon 입니다.'
    
    @Weapon.response(200, 'Success', weapon_fields_with_id)
    @Weapon.response(500, 'Failed')
    @Weapon.doc(params={'name': 'update할 name', 'stock': 'update할 stock'})
    def put(self, weapon_id):
        global weapons_dict
        
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('stock', required=True, type=int)
        arg = parser.parse_args()
        update_name, update_stock = arg['name'], arg['stock']
        weapons_dict[weapon_id] = {
            'name': update_name,
            'stock': update_stock
        }
        
        return jsonify({
            'weapon_id': weapon_id,
            'weapon_data': weapons_dict[weapon_id]
        })
    
    @Weapon.response(200, 'Success', weapon_fields_with_id)
    @Weapon.response(500, 'Failed')
    def delete(self, weapon_id):
        try:
            del weapons_dict[weapon_id]
            return jsonify({
                "delete": "success"
            })
        except KeyError:
            return f'존재하지 않는 weapon 입니다.'
