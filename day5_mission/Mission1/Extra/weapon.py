from flask import request, abort, jsonify
from flask_restx import Resource, Namespace, fields

from models import *


Weapons = Namespace('weapons', 'Bicsubi Weapons Management System')

weapon_fields = Weapons.model(
    'Weapon', 
        {
            'name' : fields.String(required = True),
            'stock' : fields.Integer(required = True)
        })

weapon_fields_in_db = Weapons.model(
    'Weapon_in_DB', 
        {
            '_id' : fields.Integer(required = True),
            'name' : fields.String(required = True),
            'stock' : fields.Integer(required = True)
        })


@Weapons.route('')
class WeaponsCR(Resource) :
    def get(self) :
        '''Read All Weapons in DB'''
        weapons = []

        for weapon in query_all() :
            weapons.append({'id':weapon._id, 'name':weapon.name, 'stock':weapon.stock})

        return jsonify({'weapons' : weapons})

    @Weapons.expect(weapon_fields)
    @Weapons.response(200, 'OK', weapon_fields_in_db)
    def post(self) :
        '''Create Weapon'''
        request_data = request.get_json()

        new_weapon = Weapon(request_data['name'], request_data['stock'])

        db.session.add(new_weapon)
        db.session.commit()

        return jsonify(new_weapon.to_dict())

@Weapons.route('/<int:_id>')
@Weapons.doc(param = {'_id': 'Weapon ID'})
class WeaponRUD(Resource) :
    @Weapons.response(200, 'OK', weapon_fields_in_db)
    def get(self, _id) :
        '''Read One Weapon by ID ''' 
        try :
            weapon = search_by_id(_id)
        except MissingIdException :
            abort(400, 'ID does not exist in DB')

        return jsonify(weapon.to_dict())

    @Weapons.expect(weapon_fields)
    @Weapons.response(200, 'OK', weapon_fields_in_db)
    def put(self, _id) :
        '''Update Weapon Name, Stock by ID'''
        request_data = request.get_json()

        try :
            update_weapon = search_by_id(_id)
            update_weapon.name = request_data['name']
            update_weapon.stock = request_data['stock']

        except MissingIdException :
            abort(400, 'ID does not exist in DB')

        return jsonify(update_weapon.to_dict())

    def delete(self, _id) :
        '''Delete Weapon by ID'''
        try :
            del_weapon = search_by_id(_id)
            db.session.delete(del_weapon)
        except MissingIdException :
            abort(400, 'ID does not exist in DB')

        db.session.commit()

        weapons = []

        for weapon in query_all() :
            weapons.append({'id':weapon._id, 'name':weapon.name, 'stock':weapon.stock})

        return jsonify({'weapons' : weapons})
